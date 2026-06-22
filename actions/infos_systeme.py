import platform
import os
import shutil
import socket
import time
import subprocess

def get_ram_windows():
    try:
        output = subprocess.check_output("wmic computersystem get TotalPhysicalMemory", shell=True)
        lines = output.decode().splitlines()
        for line in lines:
            if line.strip().isdigit():
                total_bytes = int(line.strip())
                return total_bytes // (1024**3)
    except:
        return "Non disponible"

def get_windows_edition():
    try:
        output = subprocess.check_output(
            'wmic os get Caption', shell=True
        ).decode(errors="ignore").splitlines()

        for line in output:
            if "Windows" in line:
                return line.strip()
    except:
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
    except:
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
