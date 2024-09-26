from PySide6.QtWidgets import QTableWidget, QTableWidgetItem
from PySide6.QtGui import QColor, QPainter, QPen
from PySide6.QtCore import Qt
import DATA as DT

class TablaReduccion(QTableWidget):
    def __init__(self, parent=None):
        super().__init__(3, max(len(values) for values in DT.Agrupados.values()), parent=parent)
        
    def paintEvent(self, event):
        super().paintEvent(event)
        
        painter = QPainter(self.viewport())
        pen = QPen(QColor(255, 15, 0 ), 4)         
        pen.setCapStyle(Qt.RoundCap)
        pen.setJoinStyle(Qt.RoundJoin)
        painter.setPen(pen)
        
        self.load_dict_data(painter)
        painter.end()
        
    def load_dict_data(self, painter: QPainter):
        data = DT.Agrupados  # Diccionario
        minterms = DT.minterms  # Vector de números en formato entero
        respuesta_final = DT.Respuesta_final  # Vector que se mostrará en la tercera fila

        # print("Datos del diccionario:", data)
        # print("Minterms:", minterms)

        rows = len(data) + 1  # Añadir una fila extra para la Respuesta_final
        cols = max(len(values) for values in data.values())

        self.setRowCount(rows)  # Aumentar el número de filas
        self.setColumnCount(cols)
        self.horizontalHeader().setVisible(False)
        # Rellenar la tabla con el diccionario Agrupados
        for row, (key, values) in enumerate(data.items()):
            for col, value in enumerate(values):
                # Crear el QTableWidgetItem con el valor
                item = QTableWidgetItem(str(value))
                item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
                self.setItem(row, col, item) 
                if value in minterms:
                    painter.drawRect(self.visualRect(self.model().index(row, col)).adjusted(-1, -1, 1, 1))
                    
        # Rellenar la tercera fila (índice 2) con el vector Respuesta_final
        for col, value in enumerate(respuesta_final):
            item = QTableWidgetItem(str(value))
            item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
            
            # print(f"Valor en Respuesta_final (col {col}): {value}")
            
            # Establecer el item en la fila 2 (tercera fila) de la tabla
            self.setItem(2, col, item)

        # Actualizar las etiquetas del encabezado vertical
        self.setVerticalHeaderLabels(list(data.keys()) + ["Respuesta Final"])