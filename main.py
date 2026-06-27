from actions import admin
from actions import espace_disque
from actions import infos_systeme
from actions import maintenance
import ui

from actions.admin import ensure_admin
ensure_admin()

from ui import start_ui
start_ui()

import os
print("Current working directory:", os.getcwd())
input("Press Enter...")
