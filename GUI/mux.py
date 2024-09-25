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
from PySide6.QtCore import Qt, QRect, QCoreApplication
from PySide6.QtGui import QCursor, QFont, QPixmap, QPalette, QBrush
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QScrollArea)
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
        
        # Crear un widget central
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Crear un área de scroll
        self.scroll_area = QScrollArea(self.centralwidget)
        self.scroll_area.setWidgetResizable(True)  # Hacer que el área se ajuste automáticamente al contenido
        
        # Crear un contenedor dentro del área de scroll
        self.scroll_content = QWidget()
        self.scroll_content.setObjectName("scroll_content")

        # Crear un layout vertical para el contenido dentro del scroll
        self.vertical_layout = QVBoxLayout(self.scroll_content)
        self.vertical_layout.setContentsMargins(0, 0, 0, 10)
        self.vertical_layout.setSpacing(3)
        
        # Agregar un título principal
        self.Titulo_principal = QLabel(self.scroll_content)
        self.Titulo_principal.setObjectName(u"Titulo_principal")
        self.vertical_layout.addWidget(self.Titulo_principal, alignment=Qt.AlignmentFlag.AlignCenter)
        
        font = QFont()
        font.setFamilies([u"CountryBlueprint"])
        font.setPointSize(40)
        font.setWeight(QFont.Black)
        font.setItalic(False)
        self.Titulo_principal.setFont(font)
        self.Titulo_principal.setStyleSheet(u"Qlabel{font-weight: 8000;}")
        self.Titulo_principal.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Agregar un widget personalizado
        self.trapezoid_widget = TrapezoidWidget(self.scroll_content)
        self.vertical_layout.addWidget(self.trapezoid_widget, alignment=Qt.AlignmentFlag.AlignCenter)

        # Botones
        self.horizontal_layout = QHBoxLayout()
        
        self.nueva_funcion = QPushButton(self.scroll_content)
        self.nueva_funcion.setObjectName(u"nueva_funcion")
        font.setPointSize(14)
        font.setBold(True)
        self.nueva_funcion.setFont(font)
        self.nueva_funcion.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.nueva_funcion.setStyleSheet(u"QPushButton{\n"
                                         " padding: 7px;\n"
                                         " background-color: #f7dd3b;\n"
                                         " border: 2px solid rgb(182, 182, 182);\n"
                                         " border-radius: 8px;\n"
                                         "}")
        self.nueva_funcion.setMaximumSize(211, 41)
        self.nueva_funcion.clicked.connect(self.back_menu)
        
        self.back = QPushButton(self.scroll_content)
        self.back.setObjectName(u"regresar")
        self.back.setFont(font)
        self.back.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.back.clicked.connect(self.back_window)
        
        self.horizontal_layout.addWidget(self.nueva_funcion, alignment=Qt.AlignmentFlag.AlignCenter)
        self.horizontal_layout.addWidget(self.back, alignment=Qt.AlignmentFlag.AlignCenter)
        
        self.vertical_layout.addLayout(self.horizontal_layout)

        # Establecer el contenido del área de scroll
        self.scroll_area.setWidget(self.scroll_content)

        # Añadir el área de scroll al layout principal
        self.main_layout = QVBoxLayout(self.centralwidget)
        self.main_layout.addWidget(self.scroll_area)

        # Configurar el fondo de la ventana
        self.pixmap = QPixmap("src/img/fondo.jpg")
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(self.pixmap))
        self.setPalette(palette)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        
    def retranslateUi(self, MainWindow: QMainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("Mux", "Mux", None))
        self.Titulo_principal.setText(QCoreApplication.translate("Mux", u"Mux resultante", None))
        self.nueva_funcion.setText(QCoreApplication.translate("Mux", "Nueva función", None))
        self.back.setText(QCoreApplication.translate("Mux", u"Regresar", None))
        
    def resizeEvent(self, event):
        scaled_pixmap = self.pixmap.scaled(self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        palette = self.palette()
        palette.setBrush(QPalette.Window, QBrush(scaled_pixmap))
        self.setPalette(palette)
        super().resizeEvent(event)
                
    def back_window(self):
        self.hide()
        self.b.show()

    def back_menu(self):
        self.hide()
        self.menu.show()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    Back = QMainWindow()
    mux_window = Mux(MainWindow, Back)
    MainWindow.show()
    sys.exit(app.exec())
