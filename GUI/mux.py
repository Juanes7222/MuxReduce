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
from PySide6.QtCore import Qt, QRect, QPoint
from PySide6.QtGui import QPainter, QPolygon, QColor, QPen
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy)



class GroundSymbol(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(60, 120)  # Tamaño del widget

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Dibuja el polo a tierra
        ground_x = self.width() // 2  # Centrado horizontalmente en el widget
        ground_y_start = 20  # Ajustar para que esté más arriba

        pen = QPen(QColor("#ffffff"), 2)  # Grosor de la línea
        painter.setPen(pen)

        # Dibujar las tres líneas horizontales (invertir el orden)
        painter.drawLine(QPoint(ground_x - 10, ground_y_start - 5), QPoint(ground_x + 10, ground_y_start - 5))
        painter.drawLine(QPoint(ground_x - 15, ground_y_start), QPoint(ground_x + 15, ground_y_start))  # Línea más larga
        painter.drawLine(QPoint(ground_x - 5, ground_y_start - 10), QPoint(ground_x + 5, ground_y_start - 10))  # Línea mediana

        # Línea vertical (aumentar longitud)
        ground_y_end = ground_y_start + 100  # Aumentar longitud de la línea vertical
        painter.drawLine(QPoint(ground_x, ground_y_start), QPoint(ground_x, ground_y_end))  # Línea vertical

        # Marcar el punto de conexión
        connection_marker_size = 5  # Tamaño del marcador
        painter.setBrush(QColor("#ff0000"))  # Color del marcador
        painter.drawEllipse(QPoint(ground_x, ground_y_start + 100), connection_marker_size, connection_marker_size)  # Punto de conexión

class TrapezoidWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(400, 400)
        self.trapezoid_height = 100

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Obtener el tamaño del vector
        pin_count = len(DT.Respuesta_final)  # Supongamos que DT.Respuesta_final es accesible
        top_width = 80
        bottom_width = 160 + (pin_count - 1) * 20  # Aumentar el ancho según el número de pines
        height = self.trapezoid_height + pin_count * 4  # Ajustar la altura según el número de pines
        
        # Modificar las coordenadas para ajustar la posición del trapecio
        x_center = self.width() // 2
        y_center = self.height() // 2

        # Mover el painter al centro del widget
        painter.translate(x_center, y_center)
        painter.rotate(90)

        # Coordenadas para el trapecio
        points = [
            (-top_width // 2, -height // 2),
            (top_width // 2, -height // 2),
            (bottom_width // 2, height // 2),
            (-bottom_width // 2, height // 2)
        ]

        # Convertir la lista de puntos en un QPolygon
        polygon = QPolygon([QPoint(*p) for p in points])

        # Dibujar el trapecio
        painter.setBrush(Qt.transparent)
        pen = QPen(QColor("#ffffff"), 4)
        painter.setPen(pen)
        painter.drawPolygon(polygon)

        # Dibuja las líneas para los pines
        pin_spacing = bottom_width / (pin_count + 1)  # Espaciado de las líneas

        for i in range(pin_count):
            pin_x = -bottom_width // 2 + (i + 1) * pin_spacing
            line_top = height // 2
            line_bottom = line_top + 20
            painter.drawLine(QPoint(pin_x, line_top), QPoint(pin_x, line_bottom))  # Longitud de la línea

            # Conectar a tierra si el valor es 0
            if DT.Respuesta_final[i] == 0:
                # Dibuja la línea conectando al polo a tierra
                ground_x = self.parent().findChild(GroundSymbol).width() // 2
                ground_y_start = 200  # La misma que en GroundSymbol
                # Ajustar la y para conectar desde el final de la línea del pin
                painter.drawLine(QPoint(pin_x, line_bottom), QPoint(ground_x, ground_y_start + 100))  # Aumentar la altura

        # Restaurar la transformación
        painter.resetTransform()


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

        # Crea un layout horizontal para organizar el trapecio y el polo a tierra
        self.horizontal_layout = QHBoxLayout(self.centralwidget)
        self.horizontal_layout.setContentsMargins(0, 0, 0, 0)  # Sin márgenes

        # Añadir el polo a tierra al layout horizontal
        self.ground_symbol = GroundSymbol(self.centralwidget)
        self.horizontal_layout.addWidget(self.ground_symbol, alignment=Qt.AlignmentFlag.AlignLeft)

        # Añadir el trapecio al layout horizontal
        self.trapezoid_widget = TrapezoidWidget(self.centralwidget)
        self.horizontal_layout.addWidget(self.trapezoid_widget, alignment=Qt.AlignmentFlag.AlignCenter)

        MainWindow.setCentralWidget(self.centralwidget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    Back = QMainWindow()  # Un placeholder para el botón de regreso
    mux_window = Mux(MainWindow, Back)
    MainWindow.show()
    sys.exit(app.exec())