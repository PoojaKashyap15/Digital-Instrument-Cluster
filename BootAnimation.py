import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Tube1(QObject):

    def __init__(self):
        super().__init__()
        self.tube_item1 = QGraphicsEllipseItem(285, 305, 60, 60)
        self.tube_item1.setTransformOriginPoint(315, 335)
        self.tube_item1.setPen(QPen(Qt.NoPen))
        self.tube_item1.setBrush(QBrush(QColor(58, 59, 58)))

    def _set_rot(self, rot):
        self.tube_item1.setRotation(rot)

    rot = pyqtProperty(int, fset=_set_rot)


class Tube2(QObject):

    def __init__(self):
        super().__init__()
        self.tube_item2 = QGraphicsEllipseItem(400, 305, 60, 60)
        self.tube_item2.setTransformOriginPoint(430, 335)
        self.tube_item2.setPen(QPen(Qt.NoPen))
        self.tube_item2.setBrush(QBrush(QColor(58, 59, 58)))

    def _set_rot(self, rot):
        self.tube_item2.setRotation(rot)

    rot = pyqtProperty(int, fset=_set_rot)


class Line1(QObject):

    def __init__(self):
        super().__init__()
        self.line1 = QGraphicsLineItem(300, 244, 335, 244)
        self.line1.setPen(QPen(QColor(126, 129, 125), 3, Qt.SolidLine))

    def _set_pos(self, pos):
        self.line1.setPos(pos)

    pos = pyqtProperty(QPointF, fset=_set_pos)


class Line2(QObject):

    def __init__(self):
        super().__init__()
        self.line2 = QGraphicsLineItem(308, 254, 321, 254)
        self.line2.setPen(QPen(QColor(126, 129, 125), 3, Qt.SolidLine))

    def _set_pos(self, pos):
        self.line2.setPos(pos)

    pos = pyqtProperty(QPointF, fset=_set_pos)


class Line3(QObject):

    def __init__(self):
        super().__init__()
        self.line3 = QGraphicsLineItem(266, 264, 311, 264)
        self.line3.setPen(QPen(QColor(126, 129, 125), 3, Qt.SolidLine))

    def _set_pos(self, pos):
        self.line3.setPos(pos)

    pos = pyqtProperty(QPointF, fset=_set_pos)


class Rider(QObject):

    def __init__(self):
        super().__init__()

        self.rider_item = QGraphicsPixmapItem(QPixmap("riderBodyShape.png"))
        self.rider_item.setPos(326, 233)

    def _set_pos(self, pos):
        self.rider_item.setPos(pos)

    pos = pyqtProperty(QPointF, fset=_set_pos)


class Helmet(QObject):

    def __init__(self):
        super().__init__()

        self.helmet_item = QGraphicsPixmapItem(QPixmap("helmetDist2.png"))

    def _set_opacity(self, bvalue):
        self.helmet_item.setOpacity(bvalue)

    bvalue = pyqtProperty(int, fset=_set_opacity)


class AnimationView(QGraphicsView):

    def __init__(self):
        super().__init__()
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        self.setSceneRect(0, 0, 800, 480)
        self.scene.setBackgroundBrush(QColor(16, 17, 17))
        # QColor(7, 238, 245 )
        self.letter_counter = 0
        self.create_bike_rider()
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateValues)
        self.timer.setInterval(250)
        self.create_text()

    def create_bike_rider(self):

        tire1 = self.scene.addEllipse(280, 300, 70, 70, QPen(QColor(132, 135, 131), 6, Qt.SolidLine))
        tire2 = self.scene.addEllipse(395, 300, 70, 70, QPen(QColor(132, 135, 131), 6, Qt.SolidLine))

        tire1_tube_gradient=QConicalGradient(310, 330, 0)
        tire1_tube_gradient.setColorAt(0, QColor(132, 135, 132))
        tire1_tube_gradient.setColorAt(0.1, QColor(83, 85, 83 ))
        tire1_tube_gradient.setColorAt(0.38, QColor(16, 17, 17))
        tire1_tube_gradient.setColorAt(1, QColor(16, 17, 17))
        brush_gradient_for_tube1 = QBrush(tire1_tube_gradient)

        tire2_tube_gradient = QConicalGradient(425, 330, 0)
        tire2_tube_gradient.setColorAt(0, QColor(132, 135, 132))
        tire2_tube_gradient.setColorAt(0.1, QColor(83, 85, 83 ))
        tire2_tube_gradient.setColorAt(0.38, QColor(16, 17, 17))
        tire2_tube_gradient.setColorAt(1, QColor(16, 17, 17))
        brush_gradient_for_tube2 = QBrush(tire2_tube_gradient)

        self.head = self.scene.addEllipse(402, 207, 38, 38, QPen(Qt.NoPen), QColor(7, 238, 245))
        self.tube1 = Tube1()
        self.tube2 = Tube2()
        self.anim_line1 = Line1()
        self.anim_line2 = Line2()
        self.anim_line3 = Line3()
        self.anim_rider = Rider()
        self.anim_helmet = Helmet()

        self.anim = QPropertyAnimation(self.tube1, b'rot')
        self.anim.setDuration(700)
        self.anim.setStartValue(0)
        self.anim.setEndValue(360)
        self.anim.setLoopCount(50)

        self.anim2 = QPropertyAnimation(self.tube2, b'rot')
        self.anim2.setDuration(700)
        self.anim2.setStartValue(0)
        self.anim2.setEndValue(360)
        self.anim2.setLoopCount(50)

        self.anim3 = QPropertyAnimation(self.anim_line1, b'pos')
        self.anim3.setDuration(500)
        self.anim3.setStartValue(QPointF(2, 0))
        self.anim3.setKeyValueAt(0.1, QPointF(-2, 0))
        self.anim3.setKeyValueAt(0.4, QPointF(1, 0))
        self.anim3.setKeyValueAt(0.5, QPointF(-3, 0))
        self.anim3.setKeyValueAt(0.7, QPointF(3, 0))
        self.anim3.setKeyValueAt(0.9, QPointF(-1, 0))
        self.anim3.setEndValue(QPointF(1, 0))
        self.anim3.setLoopCount(50)

        self.anim4 = QPropertyAnimation(self.anim_line2, b'pos')
        self.anim4.setDuration(500)
        self.anim4.setStartValue(QPointF(-2, 0))
        self.anim4.setKeyValueAt(0.3, QPointF(1, 0))
        self.anim4.setKeyValueAt(0.5, QPointF(3, 0))
        self.anim4.setKeyValueAt(0.8, QPointF(-1, 0))
        self.anim4.setEndValue(QPointF(1, 0))
        self.anim4.setLoopCount(50)

        self.anim5 = QPropertyAnimation(self.anim_line3, b'pos')
        self.anim5.setDuration(500)
        self.anim5.setStartValue(QPointF(3, 0))
        self.anim5.setKeyValueAt(0.3, QPointF(-1, 0))
        self.anim5.setKeyValueAt(0.5, QPointF(1, 0))
        self.anim5.setKeyValueAt(0.8, QPointF(3, 0))
        self.anim5.setEndValue(QPointF(1, 0))
        self.anim5.setLoopCount(50)

        self.anim6 = QPropertyAnimation(self.anim_helmet, b'bvalue')
        self.anim6.setDuration(400)
        self.anim6.setStartValue(0)
        self.anim6.setKeyValueAt(0.1, 1)
        self.anim6.setKeyValueAt(0.11, 0)
        self.anim6.setKeyValueAt(0.2, 1)

        self.anim6.setEndValue(1)
        self.anim6.setLoopCount(3)

        self.scene.addItem(self.tube1.tube_item1)
        self.scene.addItem(self.tube2.tube_item2)
        self.scene.addItem(self.anim_line1.line1)
        self.scene.addItem(self.anim_line2.line2)
        self.scene.addItem(self.anim_line3.line3)
        self.scene.addItem(self.anim_rider.rider_item)

        self.anim_helmet.helmet_item.setPos(385, 190)
        self.scene.addItem(self.anim_helmet.helmet_item)
        self.anim_helmet.helmet_item.setOpacity(0)

        self.tube1.tube_item1.setBrush(brush_gradient_for_tube1)
        self.tube2.tube_item2.setBrush(brush_gradient_for_tube2)
        self.anim.start()
        self.anim2.start()
        self.anim3.start()
        self.anim4.start()
        self.anim5.start()
        # self.anim7.start()

        tire11 = self.scene.addEllipse(295, 315, 40, 40, QPen(Qt.NoPen), QBrush(QColor(16, 17, 17)))
        tire22 = self.scene.addEllipse(410, 315, 40, 40, QPen(Qt.NoPen), QBrush(QColor(16, 17, 17)))

    def updateValues(self):
        if self.letter_counter == 4:
            self.scene.removeItem(self.head)
            self.anim6.start()
        elif self.letter_counter == 5:
            self.scene.addItem(self.text1)
            self.timer.setInterval(50)
        elif self.letter_counter == 6:
            self.text1.setScale(1.05)
        elif self.letter_counter == 5:
            self.text1.setPos(222, 90)
            self.scene.removeItem(self.text1)
        elif self.letter_counter == 7:
            self.scene.addItem(self.text1)
            self.text1.setPos(220, 90)
        elif self.letter_counter == 8:
            self.text1.setScale(1)
        elif self.letter_counter == 9:
            self.scene.addItem(self.text2)
        elif self.letter_counter == 10:
            self.text1.setPos(222, 90)
        elif self.letter_counter == 11:
            self.text1.setScale(1.05)
        elif self.letter_counter == 12:
            self.text1.setPos(220, 90)
        elif self.letter_counter == 13:
            self.text2.setPos(350, 90)
        elif self.letter_counter == 14:
            self.text2.setPos(353, 90)
        elif self.letter_counter == 15:
            self.text2.setScale(1.05)
        elif self.letter_counter == 16:
            self.text1.setScale(1.05)
        elif self.letter_counter == 17:
            self.text1.setPos(222, 90)
        elif self.letter_counter == 18:
            self.text1.setPos(220, 90)
        elif self.letter_counter == 19:
            self.text1.setScale(1)
            self.anim.setDuration(550)
            self.anim2.setDuration(550)
        elif self.letter_counter == 20:
            self.text1.setScale(1.03)
        elif self.letter_counter == 21:
            self.text1.setScale(1.05)
        elif self.letter_counter == 22:
            self.text1.setPos(222, 90)
            self.scene.removeItem(self.text2)
        elif self.letter_counter == 23:
            self.text1.setPos(220, 90)
            self.scene.addItem(self.text2)
        elif self.letter_counter == 24:
            self.text2.setScale(1.05)
        elif self.letter_counter == 25:
            self.text2.setPos(353, 90)
        elif self.letter_counter == 26:
            self.text2.setPos(350, 90)
        elif self.letter_counter == 27:
            self.timer.stop()

        self.letter_counter += 1

    def create_text(self):

        font_for_texts = QFont("TW Cen MT", 40, QFont.Bold)

        self.text1 = QGraphicsTextItem("LET'S")
        self.text1.setPos(220, 90)
        self.text1.setFont(font_for_texts)
        self.text1.setDefaultTextColor(QColor(176, 179, 176))

        self.text2 = QGraphicsTextItem("ZCOOT")
        self.text2.setPos(350, 90)
        self.text2.setFont(font_for_texts)
        self.text2.setDefaultTextColor(QColor(176, 179, 176))

        pix4 = QPixmap("emobiRoundLogo.png")
        item5 = QGraphicsPixmapItem(pix4)
        item5.setPos(313, 20)
        # item1.update(QRectF(10,10,40,50))
        item5.setScale(0.08)
        self.scene.addItem(item5)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AnimationView()
    ex.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    ex.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    ex.setWindowFlags(Qt.FramelessWindowHint)
    ex.resize(800, 480)
    ex.timer.start()
    ex.show()
    sys.exit(app.exec_())