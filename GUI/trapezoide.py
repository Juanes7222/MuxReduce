import DATA as DT
from PySide6.QtCore import Qt, QRect, QPoint, QCoreApplication
from PySide6.QtGui import QPainter, QPolygon, QColor, QPen, QCursor, QFont
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy)

class TrapezoidWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # self.parent_w = parent
        self.setMinimumSize(400, 400)
        # self.setGeometry(QRect(400, 500, 400, 400))
        self.trapezoid_height = 100
        self.pin_count = len(DT.Respuesta_final)
        self.positions = {}

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

        self.draw_conections(painter)

        # Restaurar la transformación
        painter.resetTransform()
        painter.end()
        
        
    def draw_conections(self, painter: QPainter):
        # painter.setRenderHint(QPainter.Antialiasing)
        bottom_width = 160 + (self.pin_count - 1) * 20  # Aumentar el ancho según el número de pines
        pin_spacing = bottom_width / (self.pin_count + 1)  # Espaciado de las líneas
        height = self.trapezoid_height + self.pin_count * 4  # Ajustar la altura según el número de pines
        # large_font = QFont("Arial", 20)  # Tamaño más grande para los símbolos
        # painter.setFont(large_font)
        # painter.setPen(QPen(QColor(0, 0, 0), 1))
        # ground_x = self.ground.width() // 2
        for i in range(self.pin_count):
            pin_x = -bottom_width // 2 + (i + 1) * pin_spacing
            line_top = height // 2
            line_bottom = line_top + 100
            if DT.Respuesta_final[i] == 0:
                painter.drawLine(QPoint(pin_x, line_top), QPoint(pin_x, line_bottom))  # Longitud de la línea
                painter.drawText(QPoint(pin_x, line_bottom + 10), "0V")
            elif DT.Respuesta_final[i] == 1:
                painter.drawText(QPoint(pin_x, line_bottom), "5V")
            elif DT.Respuesta_final[i] == "A":
                painter.drawText(QPoint(pin_x, line_bottom), "A")
            else:
                painter.drawText(QPoint(pin_x, line_bottom), "A'")
                