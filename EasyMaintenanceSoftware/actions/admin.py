import ctypes
import sys
import os

def ensure_admin():
    try:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin()
    except:
        is_admin = False

    if not is_admin:
        # Chemin du python dans le venv
        python_exe = os.path.join(os.getcwd(), "venv", "Scripts", "python.exe")

        # Chemin du script principal
        script = os.path.abspath(sys.argv[0])

        # Arguments
        params = f"\"{script}\""

        # Relance en admin
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", python_exe, params, None, 1
        )

        sys.exit()
