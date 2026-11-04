from actions.admin import ensure_admin
from ui import start_ui


if __name__ == "__main__":
    ensure_admin()
    start_ui()
