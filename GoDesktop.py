
from ui import Ui_MainWindow
from PySide2.QtWidgets import *
from PySide2.QtGui import QIcon
import sys
import json
from tendo import singleton


try:
    me = singleton.SingleInstance()
except:
    print("Already running")
    sys.exit(-1)


class Main(QMainWindow):
    def __init__(self,):
        super(Main, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        with open('settings.json') as f:
            UrlData = json.load(f)
        self.setWindowTitle(UrlData["windowName"])
        appIcon = QIcon(UrlData["windowIcon"])
        self.setWindowIcon(appIcon)
        self.resize(UrlData["windowGeometry"][0], UrlData["windowGeometry"][0])
        self.URL = UrlData["URL"]
        self.ui.webEngine.setUrl(self.URL)

        self.trayIcon = QSystemTrayIcon(
            QIcon(UrlData["windowIcon"]), parent=self)

        self.trayIcon.setToolTip("check out my tray")

        self.menu = QMenu()
        self.exitAction = self.menu.addAction("Exit")
        self.openAction = self.menu.addAction("open")
        self.openAction.triggered.connect(self.re_open)
        self.trayIcon.setContextMenu(self.menu)
        self.trayIcon.show()

        

    def re_open(self):
        self.show()
    def closeEvent(self, event):
        event.ignore()
        self.hide()
        #self.ui.webEngine.page().profile().cookieStore().deleteAllCookies();




if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_app = Main()
    my_app.exitAction.triggered.connect(app.quit)
    
    my_app.show()
    sys.exit(app.exec_())
