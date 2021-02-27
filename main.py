import sys

from hotpos.application import Application


if __name__ == "__main__":
    app = Application(sys.argv)
    app.start()
    sys.exit(app.exec_())
