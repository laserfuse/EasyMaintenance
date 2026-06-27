import customtkinter as ctk
from actions.infos_systeme import infos_systeme
from actions.espace_disque import espace_disque
from actions.maintenance import run_cmd, run_cmd_in_cmd
from actions.maintenance import run_ps_admin

def start_ui():
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    root.title("Easy Maintenance")
    root.geometry("700x500")

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
    for widget in output_frame.winfo_children():
        widget.destroy()

    # Nettoyage
    section = ctk.CTkLabel(output_frame, text="Nettoyage", font=("Arial", 18, "bold"))
    section.pack(anchor="w", pady=(10, 5))

    ctk.CTkButton(
        output_frame,
        text="Nettoyer fichiers temporaires",
        command=lambda: run_cmd("del /q/f/s %TEMP%\\*")
    ).pack(fill="x", pady=5)

    # Verification
    section = ctk.CTkLabel(output_frame, text="Vérifications système", font=("Arial", 18, "bold"))
    section.pack(anchor="w", pady=(20, 5))

    ctk.CTkButton(
        output_frame,
        text="SFC /scannow",
        command=lambda: run_cmd_in_cmd("sfc /scannow")
    ).pack(fill="x", pady=5)

    ctk.CTkButton(
        output_frame,
        text="DISM /RestoreHealth",
        command=lambda: run_cmd_in_cmd("DISM /Online /Cleanup-Image /RestoreHealth")
    ).pack(fill="x", pady=5)

    ctk.CTkButton(
        output_frame,
        text="CHKDSK /scan",
        command=lambda: run_cmd_in_cmd("chkdsk /scan")
    ).pack(fill="x", pady=5)

    # Reseau
    section = ctk.CTkLabel(output_frame, text="Réseau", font=("Arial", 18, "bold"))
    section.pack(anchor="w", pady=(20, 5))

    ctk.CTkButton(
        output_frame,
        text="Reset DNS",
        command=lambda: run_cmd_in_cmd("ipconfig /flushdns")
    ).pack(fill="x", pady=5)

    ctk.CTkButton(
        output_frame,
        text="Reset réseau",
        command=lambda: run_cmd_in_cmd("netsh winsock reset")
    ).pack(fill="x", pady=5)

    # Services
    section = ctk.CTkLabel(output_frame, text="Services", font=("Arial", 18, "bold"))
    section.pack(anchor="w", pady=(20, 5))

    ctk.CTkButton(
        output_frame,
        text="Redémarrer Windows Update",
        command=lambda: run_cmd_in_cmd("net stop wuauserv && net start wuauserv")
    ).pack(fill="x", pady=5)
