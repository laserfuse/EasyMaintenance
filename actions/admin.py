import os
import sys
import ctypes

def ensure_admin():
    # Si déjà admin → OK
    if ctypes.windll.shell32.IsUserAnAdmin():
        return

    # Chemin complet du script/exe
    script = os.path.abspath(sys.argv[0])

    # Arguments
    params = " ".join([script] + sys.argv[1:])

    # Dossier d’origine
    cwd = os.path.dirname(script)

    # Relance en admin dans le BON dossier
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", script, params, cwd, 1
    )

    sys.exit()
