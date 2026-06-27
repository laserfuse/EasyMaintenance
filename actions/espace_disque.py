import shutil
import string
import os

def espace_disque():
    disques = {}

    # On teste toutes les lettres de A à Z
    for lettre in string.ascii_uppercase:
        chemin = f"{lettre}:\\"

        if os.path.exists(chemin):
            try:
                total, used, free = shutil.disk_usage(chemin)
                disques[f"Disque {lettre}:"] = {
                    "Total (Go)": total // (1024**3),
                    "Utilisé (Go)": used // (1024**3),
                    "Libre (Go)": free // (1024**3)
                }
            except:
                pass

    return disques
