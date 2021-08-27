import math
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtWidgets


class MainWindow(QGraphicsView):
    left_line_array = {}
    def __init__(self):
        QGraphicsView.__init__(self)
        self.dash_array = {}
        self.scene = QGraphicsScene()
        # self.create_dash_array()
        self._create_gauge()
        self.battery_percentage_indicator()
        # self.display_texts()
        self.display_images()
        self.myTimer()
        self.display_time_and_date()
        self.setScene(self.scene)
        self.setSceneRect(0, 0, 800, 480)
        self.scene.setBackgroundBrush(QColor(45, 45, 45))
        self.create_lcd_display(39)
        

    def _create_gauge(self):
        pix = QPixmap("GAUGE3.png")
        item1 = QGraphicsPixmapItem(pix)
        item1.setPos(380, 120)
        self.scene.addItem(item1)
        eff = QGraphicsDropShadowEffect()
        eff.setBlurRadius(20)
        eff.setColor(Qt.black)
        item1.setGraphicsEffect(eff)

        needle = QPainterPath()
        needle.addRoundedRect(560, 290, 120, 8, 2, 2, Qt.AbsoluteSize)
        needle_path = QGraphicsPathItem(needle)
        needle_path.setBrush(QColor(0, 255, 240))


        pix2 = QPixmap("logoTransperentBackground.png")
        item2 = QGraphicsPixmapItem(pix2)
        item2.setPos(545, 280)
        # item2.setScale(0.9)
        self.scene.addItem(item2)
        # self.scene.addItem(needle_path)
        transform = QTransform()
        transform.rotate(10)
        transform.translate(0, 0)
        needle_path.setTransform(transform)
        print(transform.m31())
        print(transform.m32())
        eff1 = QGraphicsDropShadowEffect()
        eff1.setBlurRadius(10)
        eff1.setColor(Qt.black)
        item2.setGraphicsEffect(eff1)

    def display_images(self):
        pix1 = QPixmap("CircularLeftIndicator.png")
        item1 = QGraphicsPixmapItem(pix1)
        item1.setPos(475, 50)
        item1.setScale(0.09)
        self.scene.addItem(item1)

        pix2 = QPixmap("CircularRightIndicator.png")
        item2 = QGraphicsPixmapItem(pix2)
        item2.setPos(580, 50)
        item2.setScale(0.09)
        self.scene.addItem(item2)

        pix3 = QPixmap("HeadlightHighBeamON.png")
        item3 = QGraphicsPixmapItem(pix3)
        item3.setPos(40, 420)
        item3.setScale(0.09)
        self.scene.addItem(item3)

        pix4 = QPixmap("HeadlightLowBeamOFF.png")
        item4 = QGraphicsPixmapItem(pix4)
        item4.setPos(100, 420)
        item4.setScale(0.09)
        self.scene.addItem(item4)

    def battery_percentage_indicator(self):

        self.scene.addLine(100, 380, 100, 170, QPen(Qt.white, 2, Qt.SolidLine))
        self.scene.addLine(100, 170, 150, 170, QPen(Qt.white, 2, Qt.SolidLine))
        self.scene.addLine(100, 380, 150, 380, QPen(Qt.white, 2, Qt.SolidLine))

        left_lines_color = QColor(43, 211, 46)
        left_line1 = QGraphicsLineItem(110, 350, 125, 350)
        left_line1.setPen(QPen(left_lines_color, 8, Qt.SolidLine))
        self.scene.addItem(left_line1)
        self.left_line_array[1] = left_line1

        left_line2 = QGraphicsLineItem(110, 335, 128, 335)
        left_line2.setPen(QPen(left_lines_color, 8, Qt.SolidLine))
        self.scene.addItem(left_line2)
        self.left_line_array[2] = left_line2

        left_line3 = QGraphicsLineItem(110, 320, 131, 320)
        left_line3.setPen(QPen(left_lines_color, 8, Qt.SolidLine))
        self.scene.addItem(left_line3)
        self.left_line_array[3] = left_line3

        left_line4 = QGraphicsLineItem(110, 305, 134, 305)
        left_line4.setPen(QPen(left_lines_color, 8, Qt.SolidLine))
        self.scene.addItem(left_line4)
        self.left_line_array[4] = left_line4

        left_line5 = QGraphicsLineItem(110, 290, 137, 290)
        left_line5.setPen(QPen(left_lines_color, 8, Qt.SolidLine))
        self.scene.addItem(left_line5)
        self.left_line_array[5] = left_line5

        left_line6 = QGraphicsLineItem(110, 275, 141, 275)
        left_line6.setPen(QPen(left_lines_color, 8, Qt.SolidLine))
        self.scene.addItem(left_line6)
        self.left_line_array[6] = left_line6

        left_line7 = QGraphicsLineItem(110, 260, 145, 260)
        left_line7.setPen(QPen(left_lines_color, 8, Qt.SolidLine))
        self.scene.addItem(left_line7)
        self.left_line_array[7] = left_line7

        left_line8 = QGraphicsLineItem(110, 245, 149, 245)
        left_line8.setPen(QPen(left_lines_color, 8, Qt.SolidLine))
        self.scene.addItem(left_line8)
        self.left_line_array[8] = left_line8

        left_line9 = QGraphicsLineItem(110, 230, 152, 230)
        left_line9.setPen(QPen(left_lines_color, 8, Qt.SolidLine))
        self.scene.addItem(left_line9)
        self.left_line_array[9] = left_line9

        left_line10 = QGraphicsLineItem(110, 215, 156, 215)
        left_line10.setPen(QPen(left_lines_color, 8, Qt.SolidLine))
        self.scene.addItem(left_line10)
        self.left_line_array[10] = left_line10

        left_line11 = QGraphicsLineItem(110, 200, 160, 200)
        left_line11.setPen(QPen(left_lines_color, 8, Qt.SolidLine))
        self.scene.addItem(left_line11)
        self.left_line_array[11] = left_line11

    def create_lcd_display(self, nnn):

        # # self.lcd = QLCDNumber(self)
        # self.lcd = QLCDNumber()
        # # self.lcd.setMinimumSize(250, 200)
        # self.lcd.setFixedWidth(250)
        # self.lcd.setFixedHeight(180)
        # self.lcd.setGeometry(450, 250, 100, 100)
        # self.lcd.setFrameStyle(QFrame.Plain)
        # self.lcd.setStyleSheet("background-color:transparent;color:#00FF9B;border:none;")
        # self.lcd.setObjectName("lcd")
        # self.lcd.display(nnn)
        # self.lcd.setSegmentStyle(QLCDNumber.Flat)
        # font_for_time = QFont("Century Gothic", 44, QFont.ExtraBold)
        # QApplication.setFont(font_for_time)
        # # self.lcd.setFont(font_for_time)
        # self.lcd.setFrameStyle(QFrame.Panel | QFrame.Raised)
        # self.lcd.setMidLineWidth(3)
        # self.lcd.setLineWidth(3)
        # # self.lcd.resize(300, 80)
        # self.scene.addWidget(self.lcd)
        brush_gradient_for_box = QRadialGradient(670, 380, 70)
        brush_gradient_for_box.setColorAt(0, QColor(0, 0, 0))
        brush_gradient_for_box.setColorAt(1, QColor(45, 45, 45))
        rectangle_around_speed = self.scene.addRect(620, 270, 120, 140, QPen(QColor(66, 140, 139), 4, Qt.SolidLine), QBrush(Qt.NoBrush) )

        text1 = self.scene.addText("KM/H", QFont("Century Gothic", 25, QFont.Bold))
        # text1.setDefaultTextColor(Qt.white)
        text1.setDefaultTextColor(QColor(0, 255, 170))
        text1.setPos(635, 350)

        font_for_time = QFont("Century Gothic", 55, QFont.Bold)
        # font_for_time.setLetterSpacing(QFont.AbsoluteSpacing, -2)
        text2 = self.scene.addText("69", font_for_time)
        # text1.setDefaultTextColor(Qt.white)
        text2.setDefaultTextColor(QColor(0, 255, 170))
        # position without box
        # text2.setPos(595, 290)
        # position with box
        text2.setPos(637, 275)
        eff = QGraphicsDropShadowEffect()
        # eff.setOffset(0)
        eff.setBlurRadius(20)
        eff.setColor(QColor(0, 0, 0))
        text2.setGraphicsEffect(eff)



    def create_dash_array(self):
        '''this method is used to create the dash shaped structure in the gauge(speedometer)'''
        # create ellipses and subtract them from one another to get a curved path
        ellipse1 = QPainterPath()
        ellipse1.addEllipse(270, 120, 287, 266)
        ellipse2 = QPainterPath()
        ellipse2.addEllipse(278, 143, 240, 232)
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
            x += 1

    @QtCore.pyqtSlot(int)
    def add_acceleration_values(self, value):
        self.lcd.display(value)
        iii = 67+((value/3)*2)
        if iii in self.dash_array:
            self.scene.addItem(self.dash_array[iii])

    def myTimer(self):
        font = QFont('Century Gothic', 23, QFont.ExtraBold)
        # font.setLetterSpacing(QFont.AbsoluteSpacing, -1) 
        self.label = QLabel()
        self.label.setFont(font)
        self.label.setGeometry(55, 30,50,20)
        self.label.setStyleSheet("color: white ;background-color: #07186900")
        self.scene.addWidget(self.label) 
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.display_time_and_date) 
        self.timer.start() 

    def display_time_and_date(self):
        time = QTime.currentTime() 
        label = time.toString('hh:mm:ss A')
        self.label.setText(label)
        # font_for_time = QFont("Century Gothic", 23, QFont.ExtraBold)
        # font_for_time.setLetterSpacing(QFont.AbsoluteSpacing, -1)
        # time_text = self.scene.addText(time_label, font_for_time)
        # time_text.setPos(55, 30)
        # time_text.setDefaultTextColor(Qt.white)

        date = QDate.currentDate()
        date_label = date.toString('dddd,MMM dd')
        date_text = self.scene.addText(date_label, QFont("Century Gothic", 13, QFont.Bold))
        date_text.setPos(55, 70)
        date_text.setDefaultTextColor(Qt.white)

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
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    w.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    # w.setWindowFlags(Qt.FramelessWindowHint)
    w.resize(800, 480)
    # w.timer.start()
    # w.scale(2,2)
    w.show()
    sys.exit(app.exec_())
