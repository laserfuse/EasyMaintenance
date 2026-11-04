import os
import sys
import ctypes
import subprocess


def _hide_console():
    console_window = ctypes.windll.kernel32.GetConsoleWindow()
    if console_window:
        ctypes.windll.user32.ShowWindow(console_window, 0)


def ensure_admin():
    _hide_console()

    if ctypes.windll.shell32.IsUserAnAdmin():
        return

    if getattr(sys, "frozen", False):
        executable = sys.executable
        arguments = sys.argv[1:]
    else:
        executable = sys.executable
        if executable.lower().endswith("python.exe"):
            windowless_executable = executable[:-len("python.exe")] + "pythonw.exe"
            if os.path.isfile(windowless_executable):
                executable = windowless_executable
        arguments = [os.path.abspath(sys.argv[0]), *sys.argv[1:]]

    result = ctypes.windll.shell32.ShellExecuteW(
        None,
        "runas",
        executable,
        subprocess.list2cmdline(arguments),
        os.getcwd(),
        1,
    )
    if result <= 32:
        raise OSError(f"Impossible de relancer l’application en administrateur (code {result}).")

    sys.exit()
