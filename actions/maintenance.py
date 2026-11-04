import subprocess
import base64
import ctypes
import locale

def run_cmd(cmd):
    return subprocess.Popen(
        ["cmd.exe", "/d", "/c", cmd],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding=locale.getpreferredencoding(False),
        errors="replace",
        bufsize=1,
        creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0),
    )

def run_cmd_in_cmd(command):
    return run_cmd(command)

def run_ps_admin(cmd):
    encoded_command = base64.b64encode(cmd.encode("utf-16le")).decode("ascii")
    arguments = f"-NoProfile -EncodedCommand {encoded_command}"
    result = ctypes.windll.shell32.ShellExecuteW(
        None,
        "runas",
        "powershell.exe",
        arguments,
        None,
        1,
    )
    if result <= 32:
        raise OSError(f"Impossible de démarrer PowerShell administrateur (code {result}).")