__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = ""

# REQUIREMENT - add import statements
from user_interface.client_lookup_window import ClientLookupWindow

# GIVEN:
from PySide6.QtWidgets import QApplication

# GIVEN:
if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    mainWindow = ClientLookupWindow()
    mainWindow.show()
    sys.exit(app.exec())