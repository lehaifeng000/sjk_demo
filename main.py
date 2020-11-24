
import sys

from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication

from pages import login, home


if __name__ == '__main__':
    app = QApplication(sys.argv)

    a = login.LoginPage()
    a.show()


    sys.exit(app.exec_())