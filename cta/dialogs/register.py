from .auth.dialogs import auth_dialog
from .user.register import user_dialogs


def register_dialogs():
    auth_dialog()
    user_dialogs()
