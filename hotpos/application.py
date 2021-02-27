from PyQt5.QtWidgets import QApplication

from .widgets.main_window import MainWindow


class Application(QApplication):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.main_window = MainWindow()

    def start(self):
        self.main_window.show()
