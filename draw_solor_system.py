#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
key doc -  Kepler's laws of planetary motion
https://ko.wikipedia.org/wiki/%EC%BC%80%ED%94%8C%EB%9F%AC%EC%9D%98_%ED%96%89%EC%84%B1%EC%9A%B4%EB%8F%99%EB%B2%95%EC%B9%99

key doc2 - pyqt4
http://zetcode.com/gui/pyqt4/

How to compute planetary positions
http://www.stjarnhimlen.se/comp/ppcomp.html

Computing planetary positions - a tutorial with worked examples
http://www.stjarnhimlen.se/comp/tutorial.html


단어 너무 어렵다.. 코딩을 하고 싶지만. 알고리즘을 이해하려면 오래 걸리겠지. 한걸음씩 나아가자. 조급해서 지치지 말고 나아가자

raction - 분수, 두 수의 비
equinox - 주야 평균시
nutation - 지축의 진동
aberration - 탈선
Precession - 세차운동
ecliptic - 황도면
perturbations - 당황 (????)
UT - Universal Time
longitude - 경도
perihelion - 근일점
aphelion - 원일점
perigee - 인공위성의 근일점
apogee - 인공위성의 원일점
"""

import sys
import datetime
from PyQt4.QtGui import *
from PyQt4.QtCore import *

import astropy

class SolarWindow(QWidget):
    def __init__(self):
        super(SolarWindow, self).__init__()
        self.pen = QPen(Qt.DashDotLine)
        self.qp = QPainter(self)
        self.initUi()

        timeScale = TimeScale()
        self.sun = Sun(timeScale.d)
        self.mercury = Mercury(timeScale.d)

    def initUi(self):
        self.setWindowTitle('Solar System')
        self.fullScreen()
        self.show()

    def fullScreen(self):
        fg = self.frameGeometry()
        self.rect = rect = QDesktopWidget().availableGeometry()
        center = rect.center()
        fg.moveCenter(center)
        self.move(fg.topLeft())
        self.resize(rect.width(), rect.height())

    def paintEvent(self, e):
        print('paintEvent')
        self.qp.begin(self)
        self.drawSun()
        self.drawMercury()
        self.drawVenus()
        self.qp.end()

    def drawSun(self):
        b = QImage("./solorSystemPlanet/sun.png")
        center = self.rect.center()
        size = 40
        br = QRect(center.x() - size / 2, center.y() - size / 2, size, size)
        self.qp.drawImage(br, b)

    def drawMercury(self):
        self.pen.setColor(QColor.fromRgb(0xffb976))
        self.qp.setPen(self.pen)
        center = self.rect.center()
        # 중심점 찾기.(초점 이해하기)
        # 이심율 구하기 - width, height 만들기
        # drawEllipse 하기.
        self.qp.drawEllipse(center.x() - 100, center.y() - 100, 200, 200)

    def drawVenus(self):
        self.pen.setColor(QColor.fromRgb(0xffffff))
        self.qp.setPen(self.pen)
        center = self.rect.center()
        self.qp.drawEllipse(center.x() - 200, center.y() - 200, 400, 400)

class TimeScale():
    def __init__(self):
        t = datetime.datetime.now()
        self.d = 367 * t.year - 7 * (t.year + (t.month + 9) / 12) / 4 + 275 * t.month / 9 + t.day - 730530

class Sun():
    def __init__(self, d):
        self.N = 0.0
        self.i = 0.0
        self.w = 282.9404 + 4.70935E-5 * d
        self.a = 1.000000
        self.e = 0.016709 - 1.151E-9 * d
        self.M = 356.0470 + 0.9856002585 * d

class Mercury():
    def __init__(self, d):
        self.N = 48.3313 + 3.24587E-5 * d
        self.i = 7.0047 + 5.00E-8 * d
        self.w = 29.1241 + 1.01444E-5 * d
        self.a = 0.387098
        self.e = 0.205635 + 5.59E-10 * d
        self.M = 168.6562 + 4.0923344368 * d

# mercury, venus, earth, mars, jupiter, saturn, uranus, neptune

def main():
    app = QApplication(sys.argv)
    w = SolarWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
