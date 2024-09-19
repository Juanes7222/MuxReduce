# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'salida.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QMainWindow,
    QPushButton, QScrollBar, QSizePolicy, QStatusBar,
    QTableWidget, QTableWidgetItem, QWidget)
import next_rc
import back_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(913, 697)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Tabl_minterminos = QTableWidget(self.centralwidget)
        self.Tabl_minterminos.setObjectName(u"Tabl_minterminos")
        self.Tabl_minterminos.setGeometry(QRect(150, 220, 621, 431))
        self.verticalScrollBar = QScrollBar(self.centralwidget)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setGeometry(QRect(890, -30, 20, 681))
        self.verticalScrollBar.setOrientation(Qt.Orientation.Vertical)
        self.ecuacion = QLabel(self.centralwidget)
        self.ecuacion.setObjectName(u"ecuacion")
        self.ecuacion.setGeometry(QRect(160, 30, 601, 71))
        self.ecuacion.setStyleSheet(u"QLabel {\n"
"                font-family: \"STIX Two Text\";\n"
"				font-style: italic;\n"
"                font-size: 24px;\n"
"                color: black;\n"
"                padding: 15px;\n"
"            }")
        self.nueva_funcion = QPushButton(self.centralwidget)
        self.nueva_funcion.setObjectName(u"nueva_funcion")
        self.nueva_funcion.setGeometry(QRect(330, 110, 211, 41))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.nueva_funcion.setFont(font)
        self.nueva_funcion.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.nueva_funcion.setStyleSheet(u"QPushButton{\n"
"                                 padding: 7px;\n"
"                                   background-color: #fff817;\n"
"                                   border: 2px solid rgb(182, 182, 182);\n"
"                                   border-radius: 8px;\n"
"}")
        self.back = QPushButton(self.centralwidget)
        self.back.setObjectName(u"back")
        self.back.setGeometry(QRect(30, 600, 71, 61))
        self.back.setStyleSheet(u"QPushButton{\n"
"	background-color: transparent;\n"
"	border: none;\n"
"}font-style: italic;")
        self.next = QPushButton(self.centralwidget)
        self.next.setObjectName(u"next")
        self.next.setGeometry(QRect(820, 600, 71, 61))
        self.next.setStyleSheet(u"QPushButton{\n"
"	background-color: transparent;\n"
"	border: none;\n"
"}font-style: italic;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.ecuacion.setText("")
        self.nueva_funcion.setText(QCoreApplication.translate("MainWindow", u"Nueva funci\u00f3n", None))
        self.back.setText("")
        self.next.setText("")
    # retranslateUi

