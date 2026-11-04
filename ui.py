import customtkinter as ctk
from tkinter import TclError, messagebox
import threading
from actions.infos_systeme import infos_systeme
from actions.espace_disque import espace_disque
from actions.maintenance import run_cmd

_root = None
_console_output = None
_active_process = None

def start_ui():
    global _root

    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    _root = root
    root.title("Easy Maintenance")
    root.geometry("700x500")
    root.protocol("WM_DELETE_WINDOW", fermer_application)

    # Titre
    title = ctk.CTkLabel(root, text="Easy Maintenance", font=("Arial", 24, "bold"))
    title.pack(pady=10)

    # Frame principale
    frame = ctk.CTkFrame(root)
    frame.pack(fill="both", expand=True, padx=20, pady=10)

    # Colonne boutons
    btn_frame = ctk.CTkFrame(frame)
    btn_frame.pack(side="left", fill="y", padx=10, pady=10)

    # Zone d'affichage
    global output_frame
    output_frame = ctk.CTkScrollableFrame(frame, width=450, height=400)
    output_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

    # Boutons
    ctk.CTkButton(btn_frame, text="Infos système",
                  command=afficher_infos_systeme).pack(pady=10)

    ctk.CTkButton(btn_frame, text="Espace disque",
                  command=afficher_espace_disque).pack(pady=10)

    ctk.CTkButton(btn_frame, text="Maintenance",
                  command=afficher_dashboard_maintenance).pack(pady=10)

    root.mainloop()

## Ajustement de la hauteur des textbox

def ajuster_hauteur(textbox: ctk.CTkTextbox):
    contenu = textbox.get("1.0", "end-1c")
    nb_lignes = contenu.count("\n") + 1
    textbox.configure(height=nb_lignes * 20)

## Infos systeme

def afficher_infos_systeme():
    data = infos_systeme()

    for widget in output_frame.winfo_children():
        widget.destroy()

    for categorie, infos in data.items():
        titre = ctk.CTkLabel(output_frame, text=categorie, font=("Arial", 18, "bold"))
        titre.pack(anchor="w", pady=(10, 0))

        cadre = ctk.CTkFrame(output_frame)
        cadre.pack(fill="x", pady=5, padx=5)

        textbox = ctk.CTkTextbox(
            cadre,
            wrap="word",
            font=("Arial", 12),
            activate_scrollbars=False
        )
        textbox.pack(fill="x", padx=10, pady=5)

        for k, v in infos.items():
            textbox.insert("end", f"{k} : {v}\n")

        textbox.configure(state="disabled")
        ajuster_hauteur(textbox)

## Espace disque

def afficher_espace_disque():
    data = espace_disque()

    for widget in output_frame.winfo_children():
        widget.destroy()

    for disque, infos in data.items():
        titre_disque = ctk.CTkLabel(output_frame, text=disque, font=("Arial", 16, "bold"))
        titre_disque.pack(anchor="w", pady=(5, 0))

        cadre = ctk.CTkFrame(output_frame)
        cadre.pack(fill="x", pady=5, padx=5)

        textbox = ctk.CTkTextbox(
            cadre,
            wrap="word",
            font=("Arial", 12),
            activate_scrollbars=False
        )
        textbox.pack(fill="x", padx=10, pady=5)

        for k, v in infos.items():
            textbox.insert("end", f"{k} : {v}\n")

        textbox.configure(state="disabled")
        ajuster_hauteur(textbox)

##  Dashboard maintenance

def afficher_dashboard_maintenance():
    global _console_output

    for widget in output_frame.winfo_children():
        widget.destroy()
    _console_output = None

    # Nettoyage
    section = ctk.CTkLabel(output_frame, text="Nettoyage", font=("Arial", 18, "bold"))
    section.pack(anchor="w", pady=(10, 5))

    ctk.CTkButton(
        output_frame,
        text="Nettoyer fichiers temporaires",
        command=lambda: lancer_commande("del /q/f/s %TEMP%\\*")
    ).pack(fill="x", pady=5)

    # Verification
    section = ctk.CTkLabel(output_frame, text="Vérifications système", font=("Arial", 18, "bold"))
    section.pack(anchor="w", pady=(20, 5))

    ctk.CTkButton(
        output_frame,
        text="SFC /scannow",
        command=lambda: lancer_commande("sfc /scannow")
    ).pack(fill="x", pady=5)

    ctk.CTkButton(
        output_frame,
        text="DISM /RestoreHealth",
        command=lambda: lancer_commande("DISM /Online /Cleanup-Image /RestoreHealth")
    ).pack(fill="x", pady=5)

    ctk.CTkButton(
        output_frame,
        text="CHKDSK /scan",
        command=lambda: lancer_commande("chkdsk /scan")
    ).pack(fill="x", pady=5)

    # Reseau
    section = ctk.CTkLabel(output_frame, text="Réseau", font=("Arial", 18, "bold"))
    section.pack(anchor="w", pady=(20, 5))

    ctk.CTkButton(
        output_frame,
        text="Reset DNS",
        command=lambda: lancer_commande("ipconfig /flushdns")
    ).pack(fill="x", pady=5)

    ctk.CTkButton(
        output_frame,
        text="Reset réseau",
        command=lambda: lancer_commande("netsh winsock reset")
    ).pack(fill="x", pady=5)

    # Services
    section = ctk.CTkLabel(output_frame, text="Services", font=("Arial", 18, "bold"))
    section.pack(anchor="w", pady=(20, 5))

    ctk.CTkButton(
        output_frame,
        text="Redémarrer Windows Update",
        command=lambda: lancer_commande("net stop wuauserv && net start wuauserv")
    ).pack(fill="x", pady=5)

    _console_output = ctk.CTkTextbox(
        output_frame,
        height=180,
        wrap="word",
        font=("Consolas", 11),
        activate_scrollbars=True,
    )
    _console_output.pack(fill="both", expand=True, pady=(10, 5))
    _console_output.insert("end", "La sortie des commandes apparaîtra ici.\n")
    _console_output.configure(state="disabled")

def lancer_commande(commande):
    global _active_process

    if _active_process is not None:
        if _active_process.poll() is None:
            messagebox.showinfo("Commande en cours", "Une commande de maintenance est déjà en cours.")
            return
        _active_process = None

    try:
        process = run_cmd(commande)
    except OSError as error:
        messagebox.showerror("Erreur de commande", str(error))
        return

    _active_process = process
    _ajouter_sortie(f"> {commande}\n\n")
    threading.Thread(target=_lire_sortie_commande, args=(process,), daemon=True).start()

def _lire_sortie_commande(process):
    try:
        if process.stdout is not None:
            for ligne in process.stdout:
                _planifier_ajout_sortie(ligne)
        code = process.wait()
        _planifier_ajout_sortie(f"\nCommande terminée (code de sortie : {code}).\n\n")
        _planifier_terminaison(process)
    except OSError as error:
        _planifier_ajout_sortie(f"\nErreur de lecture de la commande : {error}\n")
        _planifier_terminaison(process)

def _planifier_ajout_sortie(texte):
    if _root is None:
        return
    try:
        _root.after(0, _ajouter_sortie, texte)
    except TclError:
        return

def _planifier_terminaison(process):
    if _root is None:
        return
    try:
        _root.after(0, _commande_terminee, process)
    except TclError:
        return

def _ajouter_sortie(texte):
    if _console_output is None:
        return
    try:
        if not _console_output.winfo_exists():
            return
        _console_output.configure(state="normal")
        _console_output.insert("end", texte)
        _console_output.see("end")
        _console_output.configure(state="disabled")
    except TclError:
        return

def _commande_terminee(process):
    global _active_process
    if _active_process is process:
        _active_process = None

def fermer_application():
    if _active_process is not None and _active_process.poll() is None:
        _active_process.terminate()
    if _root is not None:
        _root.destroy()
