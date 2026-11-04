import platform
import os
import socket
import time
import ctypes


class _MemoryStatusEx(ctypes.Structure):
    _fields_ = [
        ("dwLength", ctypes.c_ulong),
        ("dwMemoryLoad", ctypes.c_ulong),
        ("ullTotalPhys", ctypes.c_ulonglong),
        ("ullAvailPhys", ctypes.c_ulonglong),
        ("ullTotalPageFile", ctypes.c_ulonglong),
        ("ullAvailPageFile", ctypes.c_ulonglong),
        ("ullTotalVirtual", ctypes.c_ulonglong),
        ("ullAvailVirtual", ctypes.c_ulonglong),
        ("ullAvailExtendedVirtual", ctypes.c_ulonglong),
    ]


def get_ram_windows():
    status = _MemoryStatusEx()
    status.dwLength = ctypes.sizeof(status)
    if not ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(status)):
        return "Non disponible"
    return status.ullTotalPhys // (1024**3)

def get_windows_edition():
    try:
        import winreg

        with winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE,
            r"SOFTWARE\Microsoft\Windows NT\CurrentVersion",
        ) as key:
            return winreg.QueryValueEx(key, "ProductName")[0]
    except (OSError, ImportError):
        return "Non disponible"


def infos_systeme():
    data = {}

    # Infos générales
    data["Informations générales"] = {
        "Nom du PC": platform.node(),
        "Système": platform.system(),
        "Version": platform.version(),
        "Release": platform.release(),
        "Édition Windows": get_windows_edition(),
        "Architecture": platform.machine(),
        "Plateforme": platform.platform(),
    }


    # Processeur
    data["Processeur"] = {
        "Processeur": platform.processor(),
        "Cœurs CPU": os.cpu_count(),
    }

    # RAM
    if platform.system() == "Windows":
        ram = get_ram_windows()
    else:
        ram = "Disponible avec psutil"

    data["Mémoire (RAM)"] = {
        "RAM totale (Go)": ram
    }

    # Reseau
    try:
        ip = socket.gethostbyname(socket.gethostname())
    except (OSError, socket.gaierror):
        ip = "Non disponible"

    data["Réseau"] = {
        "Nom d'hôte": socket.gethostname(),
        "Adresse IP locale": ip,
    }

    # Autres
    data["Autres"] = {
        "Heure locale": time.ctime(),
        "Dossier utilisateur": os.path.expanduser("~"),
    }

    return data
