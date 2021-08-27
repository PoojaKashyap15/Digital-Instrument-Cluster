import math
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtWidgets, QtCore


class Widget(QGraphicsView):

    def __init__(self):
        super().__init__()
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        self.display_font_styles()

    def display_font_styles(self):
        # que = QStringListModel()
        # que = QtGui.QFontDatabase().families()
        # y = 10
        # for x in que:
        #     text = self.scene.addText("39 KM/H " + x, QFont(x, 35, QFont.Bold))
        #     text.setPos(10, y)
        #     y += 60
        # eff = QGraphicsDropShadowEffect()
        # eff.setBlurRadius(10)

        # label = QLabel("89 km/h")
        # # label.setText("89 km/h")
        # label.setGeometry(660, 300, 100, 100)
        # self.scene.addWidget(label)
        # label.setGraphicsEffect(eff)
        print(1/3)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Widget()
    ex.show()
    sys.exit(app.exec_())
