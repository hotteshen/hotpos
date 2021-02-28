from PyQt5.QtWidgets import QVBoxLayout, QLabel, QGroupBox


class GroupBox(QGroupBox):

    def __init__(self, title=None):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)
        if title:
            titleLabel = QLabel(title)
            titleLabel.setStyleSheet('margin-bottom: 0;')
            layout.addWidget(titleLabel, 0)
        self.root = QVBoxLayout()
        layout.addLayout(self.root, 1)
        self.setStyleSheet('padding: 0')

    def getRootLayout(self):
        return self.root
