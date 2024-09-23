import DATA as DT
from PySide6.QtCore import Qt, QRect, QPoint
from PySide6.QtGui import QPainter, QPolygon, QColor, QPen, QFont
from PySide6.QtWidgets import QWidget

class TrapezoidWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(400, 400)
        self.trapezoid_height = 100
        self.pin_count = len(DT.Respuesta_final)
        self.positions = {}

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        pin_count = len(DT.Respuesta_final)
        top_width = 80
        bottom_width = 160 + (pin_count - 1) * 20
        height = self.trapezoid_height + pin_count * 4

        x_center = self.width() // 2
        y_center = self.height() // 2

        painter.translate(x_center, y_center)
        painter.rotate(90)

        points = [
            (-top_width // 2, -height // 2),
            (top_width // 2, -height // 2),
            (bottom_width // 2, height // 2),
            (-bottom_width // 2, height // 2)
        ]

        polygon = QPolygon([QPoint(*p) for p in points])

        painter.setBrush(Qt.transparent)
        pen = QPen(QColor("#ffffff"), 4)
        painter.setPen(pen)
        painter.drawPolygon(polygon)

        # Dibujar el texto "MUX" y "n a 1" rotado localmente
        self.draw_texts(painter, top_width, height)

        # Dibujar las conexiones sin rotar
        self.draw_conections(painter)
        self.draw_right_connections(painter, points)

        painter.resetTransform()
        painter.end()

    def draw_texts(self, painter: QPainter, top_width: int, height: int):
        # Guardar el estado del pintor antes de cualquier transformación
        painter.save()

        # Rotamos el texto localmente para que no afecte el resto del contexto
        painter.rotate(-90)  # Rotamos el texto 90 grados para que quede horizontal

        # Dibujar el texto "MUX"
        font_mux = QFont("Arial", 20, QFont.Bold)
        painter.setFont(font_mux)
        painter.setPen(QColor("#ffffff"))

        text_rect = QRect(-top_width // 2, -height // 2, top_width, height)
        painter.drawText(text_rect, Qt.AlignCenter, "MUX")

        # Dibujar el subtexto
        font_subtext = QFont("Arial", 14)
        painter.setFont(font_subtext)
        n_value = str(len(DT.Respuesta_final))
        subtext = f"{n_value} a 1"
        painter.drawText(text_rect.adjusted(0, 50, 0, 0), Qt.AlignCenter, subtext)

        painter.restore()  # Restaurar el estado

    def draw_conections(self, painter: QPainter):
        bottom_width = 160 + (self.pin_count - 1) * 20
        pin_spacing = bottom_width / (self.pin_count + 1)
        height = self.trapezoid_height + self.pin_count * 4
        
        for i in range(self.pin_count):
            pin_x = -bottom_width // 2 + (i + 1) * pin_spacing
            line_top = height // 2
            line_bottom = line_top + 100

            # Cambiar el color de la línea según el valor en Respuesta_final
            if DT.Respuesta_final[i] == 0:
                pen = QPen(QColor("#00FF00"), 2)  # Verde para 0V
            elif DT.Respuesta_final[i] == 1:
                pen = QPen(QColor("#0000FF"), 2)  # Azul para 5V
            elif DT.Respuesta_final[i] == "A":
                pen = QPen(QColor("#FF0000"), 2)  # Rojo para A
            else:
                pen = QPen(QColor("#FFFF00"), 2)  # Amarillo para A'
            
            painter.setPen(pen)

            # Dibujar la línea con el color correspondiente
            painter.drawLine(QPoint(pin_x, line_top), QPoint(pin_x, line_bottom))

            # Dibujar el texto rotado localmente
            painter.save()  # Guardar el estado del pintor

            # Rotar el texto en su propio contexto para que esté horizontal
            painter.translate(pin_x, line_bottom + 20)  # Trasladamos al punto del texto
            painter.rotate(-90)  # Rotamos el texto localmente

            # Dibujar el texto ajustado según el valor en Respuesta_final
            if DT.Respuesta_final[i] == 0:
                painter.drawText(QPoint(0, 0), "0V")
            elif DT.Respuesta_final[i] == 1:
                painter.drawText(QPoint(0, 0), "5V")
            elif DT.Respuesta_final[i] == "A":
                painter.drawText(QPoint(0, 0), "A")
            else:
                painter.drawText(QPoint(0, 0), "A'")

            painter.restore()  # Restaurar el estado

    def draw_right_connections(self, painter: QPainter, points):
        variable_count = len(DT.variables_eleccion)
        top_right = QPoint(*points[1])
        bottom_right = QPoint(*points[2])
        slope = (bottom_right.y() - top_right.y()) / (bottom_right.x() - top_right.x())
        pin_spacing = self.trapezoid_height / (variable_count + 1)
        pen = QPen(QColor("#ffffff"), 2)
        painter.setPen(pen)

        for i in range(variable_count):
            pin_y = top_right.y() + (i + 1) * pin_spacing
            pin_x = top_right.x() + (pin_y - top_right.y()) / slope
            line_right = pin_x + 30
            line_left = line_right + 50

            # Dibujar la línea de salida
            painter.drawLine(QPoint(pin_x, pin_y), QPoint(line_right, pin_y))

            # Dibujar el texto rotado localmente
            painter.save()  # Guardar el estado del pintor

            # Trasladamos el contexto del pintor para dibujar el texto en el lugar correcto
            painter.translate(line_left - 40, pin_y)
            painter.rotate(-90)  # Rotamos el texto localmente

            # Dibujar el texto correspondiente
            painter.drawText(QPoint(0, 0), DT.variables_eleccion[i])

            painter.restore()  # Restaurar el estado
