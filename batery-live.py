from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QSystemTrayIcon, QMenu,\
    QDialog
import MainWindow_GUI, Dialog_Settings
import sys, psutil


class DialogSettings(QDialog, Dialog_Settings.Ui_Dialog):
    def __init__(self, parent=None):
        super(DialogSettings, self).__init__(parent)
        self.setupUi(self)


class MainWindow(QMainWindow, MainWindow_GUI.Ui_MainWindow):
    def __init__(self, app, parent=None):
        super(MainWindow, self).__init__(parent)

        self.app = app
        self.battery_threshold1 = False
        self.batter_warning = 20

        # System Tray creation
        self.icon_tray = QSystemTrayIcon(QIcon(
            QPixmap(":/icons8-spade-64.png")))
        self.icon_tray.setToolTip("Battery Live!")
        self.icon_tray.show()
        self.create_menu()
        self.icon_tray.setContextMenu(self.menu)
        self.icon_tray.activated.connect(self.show_configs)

        # Window GUI attributes
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setupUi(self)

        # Grab desktop size
        print(app.desktop().screen().rect().width())
        width = app.desktop().screen().rect().width()
        height = app.desktop().screen().rect().height()
        # self.resize(width, height/3)
        # self.move(width, height/3)

        # Timer to get battery info periodically
        timer = QTimer(self)
        timer.timeout.connect(self.update_battery_info)
        timer.start(3000)

        self.pushButton.clicked.connect(self.hide)

    def create_menu(self):
        self.menu = QMenu()
        settings_action = self.menu.addAction("Settings")
        quit_action = self.menu.addAction("Quit")

        settings_action.triggered.connect(self.open_settings)
        quit_action.triggered.connect(self.close)

    def open_settings(self):
        dialog_settings = DialogSettings()
        dialog_settings.exec_()

    def show_configs(self, reason):
        # Si nuestro click al icono fue un click derecho no manejamos el evento
        if reason == QSystemTrayIcon.Context:
            return False
        else:
            self.open_settings()

    # Get Battery Info
    def update_battery_info(self):
        battery_info = psutil.sensors_battery()
        if battery_info is not None:
            print(battery_info.percent)
            if not battery_info.power_plugged and battery_info.percent <= 25 and not self.battery_threshold1:
                self.battery_threshold1 = True
                self.showFullScreen()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MainWindow(app)
    app.exec_()