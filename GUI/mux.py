# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Respuesta.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys
from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, Qt)
from PySide6.QtGui import QCursor, QFont, QPixmap, QPalette, QBrush
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, QWidget, QStatusBar, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy)
# from GUI.comprobacion_ui import Ui_Comprobacion

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

        # Crea un layout vertical para organizar los widgets
        self.vertical_layout = QVBoxLayout(self.centralwidget)
        self.vertical_layout.setContentsMargins(0, 0, 0, 0)  # Sin márgenes para llenar la ventana

        # Layout horizontal para centrar el botón "Nueva función"
        self.horizontal_layout = QHBoxLayout()
        self.horizontal_layout.setContentsMargins(0, 0, 0, 0)  # Sin márgenes para el botón

        # Botón "Nueva función" en el layout horizontal
        self.nueva_funcion = QPushButton(self.centralwidget)
        self.nueva_funcion.setObjectName(u"nueva_funcion")
        self.nueva_funcion.setGeometry(QRect(200, 60, 211, 41))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.nueva_funcion.setFont(font)
        self.nueva_funcion.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.nueva_funcion.setStyleSheet(u"QPushButton{\n"
"                                 padding: 7px;\n"
"                                   background-color: #f7dd3b;\n"
"                                   border: 2px solid rgb(182, 182, 182);\n"
"                                   border-radius: 8px;\n"
"}")
        self.nueva_funcion.setMaximumSize(211, 41)  # Mantén el tamaño original
        self.nueva_funcion.clicked.connect(self.back_menu)
        self.horizontal_layout.addWidget(self.nueva_funcion, alignment=Qt.AlignmentFlag.AlignCenter)
        self.regresar = QPushButton(self.centralwidget)
        self.regresar.setObjectName(u"regresar")
        self.regresar.setGeometry(QRect(50, 510, 181, 51))
        self.vertical_layout.addWidget(self.regresar, alignment=Qt.AlignHCenter)
        
        self.regresar.clicked.connect(self.back_window)
        # Añade el layout horizontal al vertical layout
        self.vertical_layout.addLayout(self.horizontal_layout)

        # Espaciador para separar el botón del texto "SOLUCIÓN"
        self.spacer_top = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.vertical_layout.addItem(self.spacer_top)

        # Configura los botones de navegación
        
        
        self.pixmap = QPixmap("src/img/fondo.jpg") 
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(self.pixmap))
        self.setPalette(palette)

        # Redimensionar el fondo al tamaño de la ventana
        self.setAutoFillBackground(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "MainWindow", None))
        self.nueva_funcion.setText(QCoreApplication.translate("MainWindow", "Nueva función", None))
        self.regresar.setText(QCoreApplication.translate("MainWindow", u"Regresar", None))
        

    def resizeEvent(self, event):
        # Redimensionar la imagen de fondo cuando la ventana cambie de tamaño
        # pixmap = QPixmap("ruta/a/tu/imagen.jpg")  # Vuelve a cargar la imagen
        scaled_pixmap = self.pixmap.scaled(self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        palette = self.palette()
        palette.setBrush(QPalette.Window, QBrush(scaled_pixmap))
        self.setPalette(palette)

        # Llamar al evento de redimensionamiento original
        super().resizeEvent(event)
    
    def back_window(self):
        self.hide()
        self.b.show()
        
    def back_menu(self):
        self.hide()
        self.menu.show()
