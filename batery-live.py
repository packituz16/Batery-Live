#!/usr/bin/env python3
"""Draw text in the center of the screen."""
import sys

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow
import MainWindow_GUI
import sys, psutil

class MainWindow(QMainWindow, MainWindow_GUI.Ui_MainWindow):
    def __init__(self, app, parent=None):
        self.battery_threshold1 = False
        super(MainWindow, self).__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setupUi(self)
        self.app = app
        self.pushButton.clicked.connect(self.hide)
        print(app.desktop().screen().rect().width())
        width = app.desktop().screen().rect().width()
        height = app.desktop().screen().rect().height()
        # self.resize(width, height/3)
        # self.move(width, height/3)

        timer = QTimer(self)
        timer.timeout.connect(self.update_battery_info)
        timer.start(3000)

    def update_battery_info(self):
        battery_info = psutil.sensors_battery()
        print(battery_info.percent)
        if battery_info is not None:
            if not battery_info.power_plugged and battery_info.percent <= 25 and not self.battery_threshold1:
                self.showFullScreen()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow(app)
    app.exec_()