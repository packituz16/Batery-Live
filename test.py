#!/usr/bin/env python3
"""Draw text in the center of the screen."""
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QLabel

app = QApplication(sys.argv)
w = QLabel()
w.setWindowFlags(Qt.FramelessWindowHint)
w.setAttribute(Qt.WA_TranslucentBackground)
w.setText("Draw text...")
w.setFont(QFont("Times", 25, QFont.Normal))
# w.move(x, y) or center
w.adjustSize()  # update w.rect() now
w.move(app.desktop().screen().rect().center() - w.rect().center())
w.show()
sys.exit(app.exec_())
