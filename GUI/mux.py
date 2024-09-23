# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Respuesta.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################


import sys
import DATA as DT
from PySide6.QtCore import Qt, QRect, QPoint, QCoreApplication
from PySide6.QtGui import QPainter, QPolygon, QColor, QPen, QCursor, QFont
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy, QFrame)
from trapezoide import TrapezoidWidget


class Mux(QMainWindow):
    def __init__(self, Main, Back):
        super().__init__()
        self.b = Back
        self.menu = Main
        self.setupUi(self)

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(913, 697)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.horizontal_layout = QHBoxLayout(self.centralwidget)
        self.horizontal_layout.setContentsMargins(0, 0, 0, 0)  # Sin márgenes

        self.trapezoid_widget = TrapezoidWidget(self.centralwidget)
        
        self.horizontal_layout.addWidget(self.trapezoid_widget, alignment=Qt.AlignmentFlag.AlignCenter)
        # Añadir el trapecio al layout horizontal
        self.pin_count = len(DT.Respuesta_final)
        

        # self.nueva_funcion = QPushButton(self.centralwidget)
        # self.nueva_funcion.setObjectName(u"nueva_funcion")
        # self.nueva_funcion.setGeometry(QRect(200, 60, 211, 41))
        # font = QFont()
        # font.setPointSize(14)
        # font.setBold(True)
        # self.nueva_funcion.setFont(font)
        # self.nueva_funcion.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        # self.nueva_funcion.setStyleSheet(u"QPushButton{\n"
        #                                  " padding: 7px;\n"
        #                                  " background-color: #f7dd3b;\n"
        #                                  " border: 2px solid rgb(182, 182, 182);\n"
        #                                  " border-radius: 8px;\n"
        #                                  "}")
        
        # self.nueva_funcion.setMaximumSize(211, 41)
        # self.nueva_funcion.clicked.connect(self.back_menu)
        # self.horizontal_layout.addWidget(self.nueva_funcion, alignment=Qt.AlignmentFlag.AlignHCenter)

        MainWindow.setCentralWidget(self.centralwidget)
        
    def retranslateUi(self, MainWindow: QMainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("Mux", "Mux", None))
        # self.nueva_funcion.setText(QCoreApplication.translate("Mux", "Nueva función", None))
                
    def back_window(self):
        self.hide()
        self.b.show()

    def back_menu(self):
        self.hide()
        self.menu.show()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    Back = QMainWindow()  # Un placeholder para el botón de regreso
    mux_window = Mux(MainWindow, Back)
    MainWindow.show()
    sys.exit(app.exec())