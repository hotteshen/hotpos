from PyQt5.QtWidgets import QVBoxLayout, QLabel, QGroupBox


class GroupBoxWidget(QGroupBox):

    def __init__(self, title=None):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)
        if title:
            self.title_label = QLabel(title)
            self.title_label.setStyleSheet('margin-bottom: 0;')
            layout.addWidget(self.title_label, 0)
        self.root = QVBoxLayout()
        layout.addLayout(self.root, 1)
        self.setStyleSheet('padding: 0')

    def getRootLayout(self):
        return self.root
