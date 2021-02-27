import sys

from hotpos.application import Application
from qt_material import apply_stylesheet


if __name__ == "__main__":
    app = Application(sys.argv)
    apply_stylesheet(app, theme='dark_blue.xml')
    app.start()
    sys.exit(app.exec_())
