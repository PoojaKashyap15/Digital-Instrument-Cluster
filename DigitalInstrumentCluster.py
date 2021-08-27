import math
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtWidgets

# animation classes
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


class WorkerThread(QThread):

    Speed = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.num = 0

    def run(self):
        while self.num < 99:
            # Here we get the integer values for the LCD
            self.num += 1
            QThread.msleep(55)
            self.Speed.emit(self.num)

# main GraphicsView class
class MainWindow(QGraphicsView):

    left_line_array = {}
    right_line_array = {}
    Speed = pyqtSignal(int)
    previous_value = 67

    def __init__(self):
        QGraphicsView.__init__(self)
        self.dash_array = {}
        self.scene = QGraphicsScene()
        self.lcd = QLCDNumber()
        self.worker = WorkerThread()
        self.Speed.connect(self.add_acceleration_values)
        # self.setScene(self.scene)
        # self.setSceneRect(0, 0, 800, 480)
        # calling methods to create the required display
        self.battery_percentage_indicator()
        self.heat_percentage_indicator()
        self.create_left_and_right_cover_lines()
        self.create_dash_array()
        self.central_gauge()
        self.display_texts()
        self.display_images()
        self.label = QLabel()
        
        # self.create_worker_thread()
        self.create_lcd_display(0)
        self.scene1 = QGraphicsScene()
        self.setScene(self.scene1)
        self.setSceneRect(0, 0, 800, 480)

        

        
        #timer
        # self.heat.connect(self.add_heat_values)
        # self.heat.connect(self.add_battery_values)
        # self.scene1.setBackgroundBrush(QColor(16, 17, 17))
        # QColor(7, 238, 245 )
        self.letter_counter = 0
        self.create_bike_rider()
        self.count_heat = 1
        self.count_battery = 1
        self.count_speed = 1
        self.negative_speed = 66
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_values)
        self.timer.setInterval(250)

        # font = QFont('Verdana', 13, QFont.Normal) 
        # self.label = QLabel()
        # self.label.setFont(font)
        # self.label.setGeometry(170,81,50,20)
        # self.label.setStyleSheet("color: white ;background-color: #07186900")
        # self.scene.addWidget(self.label)
        # self.setScene(self.scene)  
        # self.timer8 = QTimer(self)
        # self.timer8.timeout.connect(self.display_time)
        # self.timer8.setInterval(300)
        

        self.timer2 = QTimer()
        self.timer2.setInterval(250)
        self.timer2.timeout.connect(self.update_heat_values)
        self.timer3 = QTimer()
        self.timer3.setInterval(350)
        self.timer3.timeout.connect(self.update_battery_values)
        self.timer4 = QTimer()
        self.timer4.setInterval(122)
        self.timer4.timeout.connect(self.update_speed_values)
        self.timer5 = QTimer()
        self.timer5.setInterval(150)
        self.timer5.timeout.connect(self.update_speed_values2)
        self.timer6 = QTimer()
        self.timer6.setInterval(150)
        self.timer6.timeout.connect(self.update_speed_values3)
        self.timer7 = QTimer()
        self.timer7.setInterval(150)
        self.timer7.timeout.connect(self.update_speed_values4) 
        self.display_time()
        self.create_text()
        self.myTimer()
        



    def update_heat_values(self):
        print("aaa ondu")
        if self.count_heat == 1:
            self.scene.addItem(self.right_line_array[1])
        elif self.count_heat == 2:
            self.scene.addItem(self.right_line_array[2])
        elif self.count_heat == 3:
            self.scene.addItem(self.right_line_array[3])
        elif self.count_heat == 4:
            self.scene.addItem(self.right_line_array[4])
        elif self.count_heat == 5:
            self.scene.removeItem(self.right_line_array[4])
        elif self.count_heat == 6:
            self.scene.removeItem(self.right_line_array[3])
        elif self.count_heat == 7:
            self.scene.addItem(self.right_line_array[3])
        elif self.count_heat == 8:
            self.scene.addItem(self.right_line_array[4])
        elif self.count_heat == 9:
            self.scene.addItem(self.right_line_array[5])
        elif self.count_heat == 10:
            self.scene.addItem(self.right_line_array[6])
        elif self.count_heat == 11:
            self.scene.removeItem(self.right_line_array[6])
        elif self.count_heat == 12:
            self.scene.removeItem(self.right_line_array[5])
        elif self.count_heat == 13:
            self.scene.addItem(self.right_line_array[5])
        elif self.count_heat == 14:
            self.scene.addItem(self.right_line_array[6])
        elif self.count_heat == 15:
            self.scene.addItem(self.right_line_array[7])
        elif self.count_heat == 16:
            self.scene.addItem(self.right_line_array[8])
        elif self.count_heat == 17:
            self.scene.addItem(self.right_line_array[9])
        elif self.count_heat == 18:
            self.scene.addItem(self.right_line_array[10])
        elif self.count_heat == 19:
            self.scene.removeItem(self.right_line_array[10])
        elif self.count_heat == 21:
            self.scene.addItem(self.right_line_array[10])
        elif self.count_heat == 22:
            self.scene.addItem(self.right_line_array[11])
        elif self.count_heat == 23:
            self.timer2.stop()

        self.count_heat += 1

    def update_battery_values(self):
        print("aaa eradu")
        if self.count_battery == 1:
            self.scene.addItem(self.left_line_array[1])
        elif self.count_battery == 2:
            self.scene.addItem(self.left_line_array[2])
        elif self.count_battery == 3:
            self.scene.removeItem(self.left_line_array[2])
        elif self.count_battery == 4:
            self.scene.addItem(self.left_line_array[2])
        elif self.count_battery == 5:
            self.scene.addItem(self.left_line_array[3])
        elif self.count_battery == 6:
            self.scene.addItem(self.left_line_array[4])
        elif self.count_battery == 7:
            self.scene.addItem(self.left_line_array[5])
        elif self.count_battery == 8:
            self.scene.removeItem(self.left_line_array[5])
        elif self.count_battery == 9:
            self.scene.removeItem(self.left_line_array[4])
        elif self.count_battery == 10:
            self.scene.removeItem(self.left_line_array[3])
        elif self.count_battery == 11:
            self.scene.addItem(self.left_line_array[3])
        elif self.count_battery == 12:
            self.scene.addItem(self.left_line_array[4])
        elif self.count_battery == 13:
            self.scene.addItem(self.left_line_array[5])
        elif self.count_battery == 14:
            self.scene.addItem(self.left_line_array[6])
        elif self.count_battery == 15:
            self.scene.addItem(self.left_line_array[7])
        elif self.count_battery == 16:
            self.scene.addItem(self.left_line_array[8])
        elif self.count_battery == 17:
            self.scene.addItem(self.left_line_array[9])
        elif self.count_battery == 18:
            self.scene.removeItem(self.left_line_array[9])
        elif self.count_battery == 19:
            self.scene.removeItem(self.left_line_array[8])
        elif self.count_battery == 20:
            self.scene.addItem(self.left_line_array[8])
        elif self.count_battery == 21:
            self.scene.addItem(self.left_line_array[9])
        elif self.count_battery == 22:
            self.scene.addItem(self.left_line_array[10])
        elif self.count_battery == 23:
            self.scene.addItem(self.left_line_array[11])
        elif self.count_heat == 24:
            self.timer3.stop()
        self.count_battery += 1

    def update_speed_values(self):
        self.Speed.emit(self.count_speed)
        if self.count_speed == 35:
            self.timer4.stop()
            self.timer5.start()
            self.negative_speed = self.count_speed
        self.count_speed += 1

    def update_speed_values2(self):
        self.Speed.emit(self.negative_speed)
        if self.negative_speed == 22:
            self.timer5.stop()
            self.count_speed = self.negative_speed
            self.timer6.start()
        self.negative_speed -= 1

    def update_speed_values3(self):
        self.Speed.emit(self.count_speed)
        if self.count_speed == 100:
            self.timer6.stop()
            self.negative_speed = self.count_speed
            self.timer7.start()
        self.count_speed += 1

    def update_speed_values4(self):
        self.Speed.emit(self.negative_speed)
        if self.negative_speed == 33:
            self.timer7.stop()
            self.count_speed = self.negative_speed
        self.negative_speed -= 1

    def create_bike_rider(self):

        tire1 = self.scene1.addEllipse(280, 300, 70, 70, QPen(QColor(132, 135, 131), 6, Qt.SolidLine))
        tire2 = self.scene1.addEllipse(395, 300, 70, 70, QPen(QColor(132, 135, 131), 6, Qt.SolidLine))

        tire1_tube_gradient = QConicalGradient(310, 330, 0)
        tire1_tube_gradient.setColorAt(0, QColor(132, 135, 132))
        tire1_tube_gradient.setColorAt(0.1, QColor(83, 85, 83))
        tire1_tube_gradient.setColorAt(0.38, QColor(16, 17, 17))
        tire1_tube_gradient.setColorAt(1, QColor(16, 17, 17))
        brush_gradient_for_tube1 = QBrush(tire1_tube_gradient)

        tire2_tube_gradient = QConicalGradient(425, 330, 0)
        tire2_tube_gradient.setColorAt(0, QColor(132, 135, 132))
        tire2_tube_gradient.setColorAt(0.1, QColor(83, 85, 83))
        tire2_tube_gradient.setColorAt(0.38, QColor(16, 17, 17))
        tire2_tube_gradient.setColorAt(1, QColor(16, 17, 17))
        brush_gradient_for_tube2 = QBrush(tire2_tube_gradient)

        self.head = self.scene1.addEllipse(402, 207, 38, 38, QPen(Qt.NoPen), QColor(7, 238, 245))
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

        self.scene1.addItem(self.tube1.tube_item1)
        self.scene1.addItem(self.tube2.tube_item2)
        self.scene1.addItem(self.anim_line1.line1)
        self.scene1.addItem(self.anim_line2.line2)
        self.scene1.addItem(self.anim_line3.line3)
        self.scene1.addItem(self.anim_rider.rider_item)

        self.anim_helmet.helmet_item.setPos(385, 190)
        self.scene1.addItem(self.anim_helmet.helmet_item)
        self.anim_helmet.helmet_item.setOpacity(0)

        self.tube1.tube_item1.setBrush(brush_gradient_for_tube1)
        self.tube2.tube_item2.setBrush(brush_gradient_for_tube2)
        self.anim.start()
        self.anim2.start()
        self.anim3.start()
        self.anim4.start()
        self.anim5.start()
        # self.anim7.start()

        tire11 = self.scene1.addEllipse(295, 315, 40, 40, QPen(Qt.NoPen), QBrush(QColor(16, 17, 17)))
        tire22 = self.scene1.addEllipse(410, 315, 40, 40, QPen(Qt.NoPen), QBrush(QColor(16, 17, 17)))

    def update_values(self):
        if self.letter_counter == 4:
            self.scene1.removeItem(self.head)
            self.anim6.start()
        elif self.letter_counter == 5:
            self.scene1.addItem(self.text1)
            self.timer.setInterval(90)
        elif self.letter_counter == 6:
            self.text1.setScale(1.05)
        elif self.letter_counter == 5:
            self.text1.setPos(222, 90)
            self.scene1.removeItem(self.text1)
        elif self.letter_counter == 7:
            self.scene1.addItem(self.text1)
            self.text1.setPos(220, 90)
        elif self.letter_counter == 8:
            self.text1.setScale(1)
        elif self.letter_counter == 9:
            self.scene1.addItem(self.text2)
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
            self.scene1.removeItem(self.text2)
        elif self.letter_counter == 23:
            self.text1.setPos(220, 90)
            self.scene1.addItem(self.text2)
        elif self.letter_counter == 24:
            self.text2.setScale(1.05)
        elif self.letter_counter == 25:
            self.text2.setPos(353, 90)
        elif self.letter_counter == 26:
            self.text2.setPos(350, 90)
        elif self.letter_counter == 27:
            self.timer.stop()
            # self.create_worker_thread()
            self.setScene(self.scene)
            self.timer2.start()
            self.timer3.start()
            self.timer4.start()

        self.letter_counter += 1

    def create_text(self):

        font_for_texts = QFont("TW Cen MT", 40, QFont.Bold)

        self.text1 = QGraphicsTextItem("LET'S")
        self.text1.setPos(220, 90)
        self.text1.setFont(font_for_texts)
        # self.text1.setDefaultTextColor(QColor(176, 179, 176))
        self.text1.setDefaultTextColor(Qt.white)

        self.text2 = QGraphicsTextItem("ZCOOT")
        self.text2.setPos(350, 90)
        self.text2.setFont(font_for_texts)
        # self.text2.setDefaultTextColor(QColor(176, 179, 176))
        self.text2.setDefaultTextColor(Qt.white)

    def create_lcd_display(self, nnn):

        self.lcd = QLCDNumber()
        # self.lcd.setMinimumSize(250, 200)
        self.lcd.setFixedWidth(250)
        self.lcd.setFixedHeight(200)
        self.lcd.setGeometry(200, 150, 100, 100)
        self.lcd.setFrameStyle(QFrame.Plain)
        self.lcd.setStyleSheet("background-color:transparent;color:#73bd3c;border:none;")
        self.lcd.setObjectName("lcd")
        self.lcd.display(nnn)
        self.scene.addWidget(self.lcd)

    def create_lcd_display1(self, nnn):
        vbox = QVBoxLayout()
        vbox.setGeometry(200, 160, 100, 100)
        vbox.addWidget(self.lcd)
        self.lcd.setStyleSheet("font-size:50px;background-color:transparent;color:#0fef00;border:none;")
        self.scene.addWidget(vbox)

    def create_worker_thread(self):
        self.worker.Speed.connect(self.add_acceleration_values)
        self.worker.start()

    def create_dash_array(self):
        '''this method is used to create the dash shaped structure in the gauge(speedometer)'''
        # create ellipses and subtract them from one another to get a curved path
        ellipse1 = QPainterPath()
        ellipse1.addEllipse(270, 120, 287, 266)
        ellipse2 = QPainterPath()
        ellipse2.addEllipse(278, 143, 240, 232)
        acceleration_path = QPainterPath()
        curvePath = ellipse1.subtracted(ellipse2)
        for x in range(66, 135):
            if x % 2 == 0:
                continue
            acceleration_indicator = curvePath.intersected(self.create_stick_shape((x * 3.3), ((x + 1) * 3.3), 158))
            acceleration_path = acceleration_path.united(acceleration_indicator)
            # acceleration_indicator holds the shape of accleration indicator(single)
            # for lesser values it will green in color, red otherwise
            # if x <= 115:
            #     graphics_stick_path = QGraphicsPathItem(acceleration_indicator)
            #     graphics_stick_path.setPen(QPen(Qt.green, 1.5, Qt.SolidLine))
            #     graphics_stick_path.setBrush(Qt.green)
            # else:
            #     graphics_stick_path = QGraphicsPathItem(acceleration_indicator)
            #     graphics_stick_path.setPen(QPen(Qt.red, 1.5, Qt.SolidLine))
            #     graphics_stick_path.setBrush(Qt.red)
            graphics_stick_path = QGraphicsPathItem(acceleration_path)
            graphics_stick_path.setPen(QPen(Qt.green, 1.5, Qt.SolidLine))
            graphics_stick_path.setBrush(Qt.green)
            self.dash_array[x] = graphics_stick_path
            x += 1
        self.scene.addItem(self.dash_array[67])

    @QtCore.pyqtSlot(int)
    def add_acceleration_values(self, value):
        self.lcd.display(value)
        iii = 67 + ((value / 3) * 2)

        if iii in self.dash_array :
          self.scene.removeItem(self.dash_array[self.previous_value])
          self.scene.addItem(self.dash_array[iii])
          self.previous_value = iii

        # if self.previous_value <= value and iii in self.dash_array :
        #     self.scene.addItem(self.dash_array[iii])

    def battery_percentage_indicator(self):
        left_line1 = QGraphicsLineItem(110, 350, 125, 350)
        left_line1.setPen(QPen(QColor(247, 1, 1), 8, Qt.SolidLine))
        # self.scene.addItem(left_line1)
        self.left_line_array[1] = left_line1

        left_line2 = QGraphicsLineItem(110, 335, 128, 335)
        left_line2.setPen(QPen(QColor(237, 46, 46), 8, Qt.SolidLine))
        # self.scene.addItem(left_line2)
        self.left_line_array[2] = left_line2

        left_line3 = QGraphicsLineItem(110, 320, 131, 320)
        left_line3.setPen(QPen(QColor(237, 97, 46), 8, Qt.SolidLine))
        # self.scene.addItem(left_line3)
        self.left_line_array[3] = left_line3

        left_line4 = QGraphicsLineItem(110, 305, 134, 305)
        left_line4.setPen(QPen(QColor(237, 129, 46), 8, Qt.SolidLine))
        # self.scene.addItem(left_line4)
        self.left_line_array[4] = left_line4

        left_line5 = QGraphicsLineItem(110, 290, 137, 290)
        left_line5.setPen(QPen(QColor(237, 129, 46), 8, Qt.SolidLine))
        # self.scene.addItem(left_line5)
        self.left_line_array[5] = left_line5

        left_line6 = QGraphicsLineItem(110, 275, 141, 275)
        left_line6.setPen(QPen(QColor(237, 157, 46), 8, Qt.SolidLine))
        # self.scene.addItem(left_line6)
        self.left_line_array[6] = left_line6

        left_line7 = QGraphicsLineItem(110, 260, 145, 260)
        left_line7.setPen(QPen(QColor(237, 189, 46), 8, Qt.SolidLine))
        # self.scene.addItem(left_line7)
        self.left_line_array[7] = left_line7

        left_line8 = QGraphicsLineItem(110, 245, 149, 245)
        left_line8.setPen(QPen(QColor(237, 230, 46), 8, Qt.SolidLine))
        # self.scene.addItem(left_line8)
        self.left_line_array[8] = left_line8

        left_line9 = QGraphicsLineItem(110, 230, 152, 230)
        left_line9.setPen(QPen(QColor(189, 237, 46), 8, Qt.SolidLine))
        # self.scene.addItem(left_line9)
        self.left_line_array[9] = left_line9

        left_line10 = QGraphicsLineItem(110, 215, 156, 215)
        left_line10.setPen(QPen(QColor(115, 237, 46), 8, Qt.SolidLine))
        # self.scene.addItem(left_line10)
        self.left_line_array[10] = left_line10

        left_line11 = QGraphicsLineItem(110, 200, 160, 200)
        left_line11.setPen(QPen(QColor(46, 237, 104), 8, Qt.SolidLine))
        # self.scene.addItem(left_line11)
        self.left_line_array[11] = left_line11

    def heat_percentage_indicator(self):

        right_line1 = QGraphicsLineItem(690, 350, 675, 350)
        right_line1.setPen(QPen(QColor(74, 247, 1), 8, Qt.SolidLine))
        # self.scene.addItem(right_line1)
        self.right_line_array[1] = right_line1

        right_line2 = QGraphicsLineItem(690, 335, 672, 335)
        right_line2.setPen(QPen(QColor(204, 237, 46), 8, Qt.SolidLine))
        # self.scene.addItem(right_line2)
        self.right_line_array[2] = right_line2

        right_line3 = QGraphicsLineItem(690, 320, 669, 320)
        right_line3.setPen(QPen(QColor(237, 186, 46), 8, Qt.SolidLine))
        # self.scene.addItem(right_line3)
        self.right_line_array[3] = right_line3

        right_line4 = QGraphicsLineItem(690, 305, 666, 305)
        right_line4.setPen(QPen(QColor(237, 144, 46), 8, Qt.SolidLine))
        # self.scene.addItem(right_line4)
        self.right_line_array[4] = right_line4

        right_line5 = QGraphicsLineItem(690, 290, 663, 290)
        right_line5.setPen(QPen(QColor(237, 121, 46), 8, Qt.SolidLine))
        # self.scene.addItem(right_line5)
        self.right_line_array[5] = right_line5

        right_line6 = QGraphicsLineItem(690, 275, 660, 275)
        right_line6.setPen(QPen(QColor(237, 112, 46), 8, Qt.SolidLine))
        # self.scene.addItem(right_line6)
        self.right_line_array[6] = right_line6

        right_line7 = QGraphicsLineItem(690, 260, 656, 260)
        right_line7.setPen(QPen(QColor(237, 93, 46), 8, Qt.SolidLine))
        # self.scene.addItem(right_line7)
        self.right_line_array[7] = right_line7

        right_line8 = QGraphicsLineItem(690, 245, 652, 245)
        right_line8.setPen(QPen(QColor(224, 75, 45), 8, Qt.SolidLine))
        # self.scene.addItem(right_line8)
        self.right_line_array[8] = right_line8

        right_line9 = QGraphicsLineItem(690, 230, 648, 230)
        right_line9.setPen(QPen(QColor(237, 46, 74), 8, Qt.SolidLine))
        # self.scene.addItem(right_line9)
        self.right_line_array[9] = right_line9

        right_line10 = QGraphicsLineItem(690, 215, 644, 215)
        right_line10.setPen(QPen(QColor(237, 46, 52), 8, Qt.SolidLine))
        # self.scene.addItem(right_line10)
        self.right_line_array[10] = right_line10

        right_line11 = QGraphicsLineItem(690, 200, 640, 200)
        right_line11.setPen(QPen(QColor(165, 0, 9), 8, Qt.SolidLine))
        # self.scene.addItem(right_line11)
        self.right_line_array[11] = right_line11

    def create_left_and_right_cover_lines(self):
        self.scene.addLine(100, 380, 100, 170, QPen(Qt.white, 2, Qt.SolidLine))
        self.scene.addLine(100, 170, 150, 170, QPen(Qt.white, 2, Qt.SolidLine))
        self.scene.addLine(100, 380, 150, 380, QPen(Qt.white, 2, Qt.SolidLine))
        self.scene.addLine(700, 380, 700, 170, QPen(Qt.white, 2, Qt.SolidLine))
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

        gradient_for_main_gauge = QLinearGradient(5, 30, 85, 98)
        gradient_for_main_gauge.setStart(403, 105)
        gradient_for_main_gauge.setFinalStop(403, 405)
        gradient_for_main_gauge.setColorAt(0, QColor(2, 99, 235))
        gradient_for_main_gauge.setColorAt(0.35, QColor(2, 99, 235))
        gradient_for_main_gauge.setColorAt(0.55, QColor(1, 24, 62))
        gradient_for_main_gauge.setColorAt(1, QColor(0, 6, 15))
        brush_gradient_for_main_gauge = QBrush(gradient_for_main_gauge)

        gradient2 = QLinearGradient()
        gradient2.setStart(399, 154)
        gradient2.setFinalStop(399, 369)
        gradient2.setColorAt(0, QColor(0, 0, 0))
        gradient2.setColorAt(0.5, QColor(0, 0, 0))
        gradient2.setColorAt(1, QColor(1, 11, 24))
        try3 = QBrush(gradient2)

        gradient_for_mid_circle_border = QLinearGradient()
        gradient_for_mid_circle_border.setStart(399, 145)
        gradient_for_mid_circle_border.setFinalStop(399, 418)
        gradient_for_mid_circle_border.setColorAt(0, QColor(210, 211, 212))
        gradient_for_mid_circle_border.setColorAt(0.5, QColor(210, 211, 212))
        gradient_for_mid_circle_border.setColorAt(0.78, QColor(1, 11, 14))
        gradient_for_mid_circle_border.setColorAt(1, QColor(1, 11, 14))
        brush_gradient_for_mid_circle_border = QBrush(gradient_for_mid_circle_border)

        self.scene.addEllipse(235, 93, 338, 325, QPen(Qt.gray), try1)
        self.scene.addEllipse(242, 99, 325, 313, QPen(Qt.white, 2, Qt.SolidLine))
        self.scene.addEllipse(248, 105, 310, 300, QPen(QColor(0, 17, 39)), brush_gradient_for_main_gauge)
        # border of mid-circle
        self.scene.addEllipse(285, 145, 228, 223, QPen(Qt.NoPen), brush_gradient_for_mid_circle_border)
        # mid circle
        self.scene.addEllipse(288, 147, 222, 219, QPen(Qt.NoPen), try3)

    def display_texts(self):

        text1 = self.scene.addText("KM/H", QFont("Trebuchet MS", 13, QFont.Bold))
        text1.setDefaultTextColor(Qt.white)
        text1.adjustSize()
        text1.setPos(420, 290)

        font_for_text2 = QFont("Trebuchet MS", 13, QFont.Bold)
        text2 = self.scene.addText("RANGE : 75KM", font_for_text2)
        text2.setDefaultTextColor(Qt.white)
        text2.adjustSize()
        text2.setPos(336, 175)

        text3 = self.scene.addText("E", QFont("Trebuchet MS", 13, QFont.Bold))
        text3.setDefaultTextColor(Qt.red)
        text3.adjustSize()
        text3.setPos(105, 350)

        text4 = self.scene.addText("F", QFont("Trebuchet MS", 13, QFont.Bold))
        text4.setDefaultTextColor(Qt.green)
        text4.adjustSize()
        text4.setPos(105, 170)

        text5 = self.scene.addText("C", QFont("Trebuchet MS", 13, QFont.Bold))
        text5.setDefaultTextColor(Qt.green)
        text5.adjustSize()
        text5.setPos(672, 350)

        text6 = self.scene.addText("H", QFont("Trebuchet MS", 13, QFont.Bold))
        text6.setDefaultTextColor(Qt.red)
        text6.adjustSize()
        text6.setPos(672, 170)

        text7 = self.scene.addText("21", QFont("Trebuchet MS", 13, QFont.Bold))
        text7.setDefaultTextColor(Qt.white)
        text7.adjustSize()
        text7.setPos(530, 81)

        text8 = self.scene.addText("0", QFont("Trebuchet MS", 9, QFont.Bold))
        text8.setDefaultTextColor(Qt.white)
        text8.adjustSize()
        text8.setPos(548, 77)

        text9 = self.scene.addText("C", QFont("Trebuchet MS", 13, QFont.Bold))
        text9.setDefaultTextColor(Qt.white)
        text9.adjustSize()
        text9.setPos(555, 81)

        text10 = self.scene.addText("TOT : 88C", QFont("Trebuchet MS", 13, QFont.Bold))
        text10.setDefaultTextColor(Qt.white)
        text10.adjustSize()
        text10.setPos(165, 380)

        text11 = self.scene.addText("TRIP A : 0", QFont("Trebuchet MS", 13, QFont.Bold))
        text11.setDefaultTextColor(Qt.white)
        text11.adjustSize()
        text11.setPos(535, 380)

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
        item7.setPos(375, 350)
        item7.setScale(0.1)
        self.scene.addItem(item7)

        pix7 = QPixmap("emobifyLogo.png")
        item8 = QGraphicsPixmapItem(pix7)
        item8.setPos(319, 290)
        item8.setScale(0.08)
        self.scene.addItem(item8)
    def myTimer(self):
        font = QFont('Verdana', 13, QFont.Normal) 
        self.label = QLabel()
        self.label.setFont(font)
        self.label.setGeometry(170,81,120,20)
        self.label.setStyleSheet("color: white ;background-color: #07186900")
        self.scene.addWidget(self.label)
        # self.setScene(self.scene)  
        self.timer8 = QTimer(self)
        self.timer8.timeout.connect(self.display_time) 
        self.timer8.start()

    def display_time(self):
        time = QTime.currentTime() 
        label = time.toString('hh:mm:ss A')
        self.label.setText(label)
        # self.timer8.start()
        

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
    w.setStyleSheet(
        "* {color: qlineargradient(spread:pad, x1:0 y1:0, x2:0 y2:1, stop:0 rgba(0, 0, 0, 255),/"
        " stop:1 rgba(255, 255, 255, 255));"
        "background: qlineargradient( x1:0 y1:0, x2:0 y2:1, stop:0 blue, stop:0.65 black);}")
    w.timer.start()
    # w.timer8.start()
    w.scale(1.5, 1.5)
    w.show()
    w.showMaximized()
    sys.exit(app.exec_())