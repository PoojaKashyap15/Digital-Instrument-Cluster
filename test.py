import math
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtWidgets, QtCore


class Widget(QGraphicsView):
    left_line_array = {}
    right_line_array = {}
    heat = pyqtSignal(int)
    def __init__(self):
        super().__init__()
        self.dash_array = {}
        self.count = 1
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        self.setSceneRect(0, 0, 800, 480)
        self.battery_percentage_indicator()
        self.heat_percentage_indicator()
        self.heat.connect(self.add_heat_values)
        self.create_left_and_right_cover_lines()
        self.create_dash_array()
        self.central_gauge()
        self.display_texts()
        self.display_images()
        self.display_time()

    def updateValues(self):
        print("agta ide")
        self.heat.emit(self.count)
        self.count += 1


    @QtCore.pyqtSlot(int)
    def add_heat_values(self, value):
        print(value)
        if value in self.left_line_array:
           self.scene.addItem(self.left_line_array[value])
           self.scene.addItem(self.right_line_array[value])

    def battery_percentage_indicator(self):
        left_line1 = QGraphicsLineItem(110, 350, 125, 350)
        left_line1.setPen(QPen(QColor(247, 1, 1), 8, Qt.SolidLine))
        self.left_line_array[1] = left_line1

        left_line2 = QGraphicsLineItem(110, 335, 128, 335)
        left_line2.setPen(QPen(QColor(237, 46, 46), 8, Qt.SolidLine))
        self.left_line_array[2] = left_line2

        left_line3 = QGraphicsLineItem(110, 320, 131, 320)
        left_line3.setPen(QPen(QColor(237, 97, 46), 8, Qt.SolidLine))
        self.left_line_array[3] = left_line3

        left_line4 = QGraphicsLineItem(110, 305, 134, 305)
        left_line4.setPen(QPen(QColor(237, 129, 46), 8, Qt.SolidLine))
        self.left_line_array[4] = left_line4

        left_line5 = QGraphicsLineItem(110, 290, 137, 290)
        left_line5.setPen(QPen(QColor(237, 129, 46), 8, Qt.SolidLine))
        self.left_line_array[5] = left_line5

        left_line6 = QGraphicsLineItem(110, 275, 141, 275)
        left_line6.setPen(QPen(QColor(237, 157, 46), 8, Qt.SolidLine))
        self.left_line_array[6] = left_line6

        left_line7 = QGraphicsLineItem(110, 260, 145, 260)
        left_line7.setPen(QPen(QColor(237, 189, 46), 8, Qt.SolidLine))
        self.left_line_array[7] = left_line7

        left_line8 = QGraphicsLineItem(110, 245, 149, 245)
        left_line8.setPen(QPen(QColor(237, 230, 46), 8, Qt.SolidLine))
        self.left_line_array[8] = left_line8

        left_line9 = QGraphicsLineItem(110, 230, 152, 230)
        left_line9.setPen(QPen(QColor(189, 237, 46), 8, Qt.SolidLine))
        self.left_line_array[9] = left_line9

        left_line10 = QGraphicsLineItem(110, 215, 156, 215)
        left_line10.setPen(QPen(QColor(115, 237, 46), 8, Qt.SolidLine))
        self.left_line_array[10] = left_line10

        left_line11 = QGraphicsLineItem(110, 200, 160, 200)
        left_line11.setPen(QPen(QColor(46, 237, 104), 8, Qt.SolidLine))
        self.left_line_array[11] = left_line11

    def create_dash_array(self):
        '''this method is used to create the dash shaped structure in the gauge(speedometer)'''
        # create ellipses and subtract them from one another to get a curved path
        ellipse1 = QPainterPath()
        ellipse1.addEllipse(265, 120, 287, 266)
        ellipse2 = QPainterPath()
        ellipse2.addEllipse(273, 143, 240, 232)
        curvePath = ellipse1.subtracted(ellipse2)
        for x in range(66, 135):
            if x % 2 == 0:
                continue
            acceleration_indicator = curvePath.intersected(self.create_stick_shape((x * 3.3), ((x + 1) * 3.3), 158))
            # acceleration_indicator holds the shape of accleration indicator(single)
            # for lesser values it will green in color, red otherwise
            if x <= 115:
                graphics_stick_path = QGraphicsPathItem(acceleration_indicator)
                graphics_stick_path.setPen(QPen(Qt.green, 1.5, Qt.SolidLine))
                graphics_stick_path.setBrush(Qt.green)
            else:
                graphics_stick_path = QGraphicsPathItem(acceleration_indicator)
                graphics_stick_path.setPen(QPen(Qt.red, 1.5, Qt.SolidLine))
                graphics_stick_path.setBrush(Qt.red)

            self.dash_array[x] = graphics_stick_path
            self.scene.addItem(graphics_stick_path)
            x += 1

        # we connect speed of worker thread to this method i.e it executes whenever speed value is altered



    def heat_percentage_indicator(self):

        right_line1 = QGraphicsLineItem(690, 350, 675, 350)
        right_line1.setPen(QPen(QColor(74, 247, 1), 8, Qt.SolidLine))
        self.right_line_array[1] = right_line1

        right_line2 = QGraphicsLineItem(690, 335, 672, 335)
        right_line2.setPen(QPen(QColor(204, 237, 46), 8, Qt.SolidLine))
        self.right_line_array[2] = right_line2

        right_line3 = QGraphicsLineItem(690, 320, 669, 320)
        right_line3.setPen(QPen(QColor(237, 186, 46), 8, Qt.SolidLine))
        self.right_line_array[3] = right_line3

        right_line4 = QGraphicsLineItem(690, 305, 666, 305)
        right_line4.setPen(QPen(QColor(237, 144, 46), 8, Qt.SolidLine))
        self.right_line_array[4] = right_line4

        right_line5 = QGraphicsLineItem(690, 290, 663, 290)
        right_line5.setPen(QPen(QColor(237, 121, 46), 8, Qt.SolidLine))
        self.right_line_array[5] = right_line5

        right_line6 = QGraphicsLineItem(690, 275, 660, 275)
        right_line6.setPen(QPen(QColor(237, 112, 46), 8, Qt.SolidLine))
        self.right_line_array[6] = right_line6

        right_line7 = QGraphicsLineItem(690, 260, 656, 260)
        right_line7.setPen(QPen(QColor(237, 93, 46), 8, Qt.SolidLine))
        self.right_line_array[7] = right_line7

        right_line8 = QGraphicsLineItem(690, 245, 652, 245)
        right_line8.setPen(QPen(QColor(224, 75, 45), 8, Qt.SolidLine))
        self.right_line_array[8] = right_line8

        right_line9 = QGraphicsLineItem(690, 230, 648, 230)
        right_line9.setPen(QPen(QColor(237, 46, 74), 8, Qt.SolidLine))
        self.right_line_array[9] = right_line9

        right_line10 = QGraphicsLineItem(690, 215, 644, 215)
        right_line10.setPen(QPen(QColor(237, 46, 52), 8, Qt.SolidLine))
        self.right_line_array[10] = right_line10

        right_line11 = QGraphicsLineItem(690, 200, 640, 200)
        right_line11.setPen(QPen(QColor(165, 0, 9), 8, Qt.SolidLine))
        self.right_line_array[11] = right_line11

    def create_left_and_right_cover_lines(self):
        self.scene.addLine(100, 380, 100, 170, QPen(Qt.white, 2, Qt.SolidLine))
        self.scene.addLine(700, 380, 700, 170, QPen(Qt.white, 2, Qt.SolidLine))
        self.scene.addLine(100, 170, 150, 170, QPen(Qt.white, 2, Qt.SolidLine))
        self.scene.addLine(100, 380, 150, 380, QPen(Qt.white, 2, Qt.SolidLine))
        self.scene.addLine(700, 170, 650, 170, QPen(Qt.white, 2, Qt.SolidLine))
        self.scene.addLine(700, 380, 650, 380, QPen(Qt.white, 2, Qt.SolidLine))

    def central_gauge(self):
        gradient = QLinearGradient(5, 30, 85, 98)
        gradient.setSpread(QGradient.ReflectSpread)
        gradient.setStart(5, 5)
        gradient.setColorAt(0, QColor(50, 50, 50))
        gradient.setColorAt(1, QColor(233, 232, 232))
        gradient.setColorAt(0, QColor(50, 50, 50))
        gradient.setColorAt(1, QColor(233, 232, 232))
        try1 = QBrush(gradient)

        gradient1 = QLinearGradient(5, 30, 85, 98)
        gradient1.setSpread(QGradient.ReflectSpread)
        gradient1.setStart(10, 20)
        gradient1.setColorAt(1, QColor(2, 101, 239))
        gradient1.setColorAt(0, QColor(0, 6, 15))
        gradient1.setColorAt(0, QColor(2, 101, 239))
        gradient1.setColorAt(1, QColor(0, 6, 15))
        try2 = QBrush(gradient1)

        gradient2 = QLinearGradient()
        gradient2.setSpread(QGradient.ReflectSpread)
        gradient2.setStart(0, 150)
        gradient2.setColorAt(0, QColor(2, 101, 239))
        gradient2.setColorAt(1, QColor(0, 0, 0))
        gradient2.setColorAt(0, QColor(2, 49, 121))
        gradient2.setColorAt(1, QColor(0, 0, 0))
        try3 = QBrush(gradient2)

        self.scene.addEllipse(235, 93, 333, 325, QPen(Qt.gray), try1)
        self.scene.addEllipse(242, 100, 320, 310, QPen(Qt.white, 2, Qt.SolidLine))
        self.scene.addEllipse(248, 105, 305, 300, QPen(QColor(0, 17, 39)), try2)

        self.scene.addEllipse(280, 145, 228, 223, QPen(Qt.gray, 3, Qt.SolidLine), try3)
        self.scene.addEllipse(284, 154, 220, 215, QPen(try3, 1, Qt.SolidLine), try3)

    def display_texts(self):

        text1 = self.scene.addText("KM/H")
        text1.setDefaultTextColor(Qt.white)
        text1.adjustSize()
        text1.setPos(420, 300)
        text1.setScale(1.4)

        text2 = self.scene.addText("RANGE : 75KM")
        text2.setDefaultTextColor(Qt.white)
        text2.adjustSize()
        text2.setPos(340, 180)
        text2.setScale(1.4)

        text3 = self.scene.addText("E")
        text3.setDefaultTextColor(Qt.red)
        text3.adjustSize()
        text3.setPos(105, 350)
        text3.setScale(1.5)

        text4 = self.scene.addText("F")
        text4.setDefaultTextColor(Qt.green)
        text4.adjustSize()
        text4.setPos(105, 170)
        text4.setScale(1.5)

        text5 = self.scene.addText("C")
        text5.setDefaultTextColor(Qt.green)
        text5.adjustSize()
        text5.setPos(672, 350)
        text5.setScale(1.5)

        text6 = self.scene.addText("H")
        text6.setDefaultTextColor(Qt.red)
        text6.adjustSize()
        text6.setPos(672, 170)
        text6.setScale(1.5)

        text7 = self.scene.addText("21")
        text7.setDefaultTextColor(Qt.white)
        text7.adjustSize()
        text7.setPos(530, 70)
        text7.setScale(1.5)

        text8 = self.scene.addText("0")
        text8.setDefaultTextColor(Qt.white)
        text8.adjustSize()
        text8.setPos(548, 66)
        text8.setScale(1.2)

        text9 = self.scene.addText("C")
        text9.setDefaultTextColor(Qt.white)
        text9.adjustSize()
        text9.setPos(555, 70)
        text9.setScale(1.5)

        text10 = self.scene.addText("TOT : 88C")
        text10.setDefaultTextColor(Qt.white)
        text10.adjustSize()
        text10.setPos(165, 380)
        text10.setScale(1.5)

        text11 = self.scene.addText("TRIP A : 0")
        text11.setDefaultTextColor(Qt.white)
        text11.adjustSize()
        text11.setPos(535, 380)
        text11.setScale(1.5)

    def display_images(self):
        pix = QPixmap("leftIndicator.png")
        item1 = QGraphicsPixmapItem(pix)
        item1.setPos(95, 70)
        item1.setScale(0.09)
        self.scene.addItem(item1)

        pix1 = QPixmap("rightIndicator.png")
        item2 = QGraphicsPixmapItem(pix1)
        item2.setPos(655, 70)
        # item1.update(QRectF(10,10,40,50))
        item2.setScale(0.09)
        self.scene.addItem(item2)

        pix2 = QPixmap("temperature.png")
        item3 = QGraphicsPixmapItem(pix2)
        item3.setPos(645, 375)
        # item1.update(QRectF(10,10,40,50))
        item3.setScale(0.04)
        self.scene.addItem(item3)

        pix3 = QPixmap("network.png")
        tr = pix3.scaled(QSize(38, 25))
        item4 = QGraphicsPixmapItem(tr)
        item4.setPos(605, 75)
        # item1.update(QRectF(10,10,40,50))
        # item4.setScale(0.18)
        self.scene.addItem(item4)

        pix4 = QPixmap("emobiRoundLogo.png")
        item5 = QGraphicsPixmapItem(pix4)
        item5.setPos(323, 20)
        # item1.update(QRectF(10,10,40,50))
        item5.setScale(0.08)
        self.scene.addItem(item5)

        pix5 = QPixmap("battery.png")
        item6 = QGraphicsPixmapItem(pix5)
        item6.setPos(100, 380)
        # item6.update(QRectF(100,100,1,1))
        item6.setScale(0.07)
        self.scene.addItem(item6)

        pix6 = QPixmap("headlightHIGH.png")
        item7 = QGraphicsPixmapItem(pix6)
        item7.setPos(350, 354)
        item7.setScale(0.05)
        self.scene.addItem(item7)

        pix7 = QPixmap("emobifyLogo.png")
        item8 = QGraphicsPixmapItem(pix7)
        item8.setPos(317, 300)
        item8.setScale(0.08)
        self.scene.addItem(item8)

    def display_time(self):
        time = QTime.currentTime()
        label = time.toString('hh:mm A')

        # showing it to the label
        text = self.scene.addText(label, QFont("Verdana", 12.5, QFont.Normal))
        text.setPos(170, 81)
        text.setTextWidth(100)
        text.setDefaultTextColor(Qt.white)

    def create_stick_shape(self, degree_start, degree_end, outer_radius):
        "this method is used to create a stick shaped structure"
        angle_alpha = degree_start * (math.pi / 180)
        angle_alphaNext = degree_end * (math.pi / 180)

        pointX1 = 400
        pointY1 = 266

        pointX2 = 400 + outer_radius * math.sin(angle_alpha)
        pointY2 = 266 - outer_radius * math.cos(angle_alpha)

        pointX3 = 400 + outer_radius * math.sin(angle_alphaNext)
        pointY3 = 266 - outer_radius * math.cos(angle_alphaNext)

        stick_path = QPainterPath()
        stick_path.moveTo(pointX1, pointY1)
        stick_path.lineTo(pointX2, pointY2)
        stick_path.lineTo(pointX3, pointY3)
        stick_path.lineTo(pointX1, pointY1)
        return stick_path


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Widget()
    # ex.resize(800, 480)
    ex.setStyleSheet(
        "* {color: qlineargradient(spread:pad, x1:0 y1:0, x2:0 y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));"
        "background: qlineargradient( x1:0 y1:0, x2:0 y2:1, stop:0 blue, stop:1 black);}")
    timer = QTimer()
    timer.timeout.connect(ex.updateValues)

    timer.setInterval(200)
    ex.show()
    timer.start()
    sys.exit(app.exec_())
