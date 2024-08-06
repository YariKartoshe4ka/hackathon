from .auth.dialogs import auth_dialog
from .main.dialogs import main_dialog


def register_dialogs():
    auth_dialog()
    main_dialog()
