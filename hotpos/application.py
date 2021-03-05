from PyQt5.QtWidgets import QApplication

from .backend_facade import BackendFacade
from .main_window import MainWindow


class Application(QApplication):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.backend_facade = BackendFacade()
        self.main_window = MainWindow()

    def start(self):
        self.main_window.show()

    def backend(self) -> BackendFacade:
        return self.backend_facade

    def exit(self):
        self.main_window.close()

    def logOut(self):
        self.backend_facade.logOut()
        self.main_window.showPage('login')
