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
from PySide6.QtGui import QCursor, QFont, QPixmap, QPalette, QBrush, QColor
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, QWidget, QStatusBar, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy, QTableWidget, QTableWidgetItem, QFrame)
# from GUI.comprobacion_ui import Ui_Comprobacion
from GUI.mux import Mux
import DATA as DT

class SalidaMenu2(QMainWindow):
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

        self.vertical_layout = QVBoxLayout(self.centralwidget)
        self.vertical_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontal_layout = QHBoxLayout()
        self.horizontal_layout.setContentsMargins(0, 0, 0, 0)

        self.nueva_funcion = QPushButton(self.centralwidget)
        self.nueva_funcion.setObjectName(u"nueva_funcion")
        self.nueva_funcion.setGeometry(QRect(200, 60, 211, 41))
        font = QFont()
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

        self.boton_mux = QPushButton(self.centralwidget)
        self.boton_mux.setObjectName(u"reduccion")
        self.boton_mux.setGeometry(QRect(510, 60, 211, 41))
        self.boton_mux.setFont(font)
        self.boton_mux.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.boton_mux.clicked.connect(self.mostrar_mux)

        self.nueva_funcion.setMaximumSize(211, 41)
        self.nueva_funcion.clicked.connect(self.back_menu)
        self.horizontal_layout.addWidget(self.nueva_funcion, alignment=Qt.AlignmentFlag.AlignCenter)
        self.horizontal_layout.addWidget(self.boton_mux, alignment=Qt.AlignmentFlag.AlignCenter)

        self.vertical_layout.addLayout(self.horizontal_layout)

        self.spacer_top = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.vertical_layout.addItem(self.spacer_top)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName("label")
        font1 = self.label.font()
        font1.setFamilies(["Arial Black"])
        font1.setPointSize(15)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.vertical_layout.addWidget(self.label)

        self.spacer_middle = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.vertical_layout.addItem(self.spacer_middle)

        # Añadimos el QTableWidget para mostrar el diccionario como tabla
        self.table = QTableWidget(self.centralwidget)
        self.vertical_layout.addWidget(self.table)
        
        self.spacer_bottom = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.vertical_layout.addItem(self.spacer_bottom)

        self.regresar = QPushButton(self.centralwidget)
        self.regresar.setObjectName(u"regresar")
        self.regresar.setGeometry(QRect(50, 510, 181, 51))
        self.vertical_layout.addWidget(self.regresar, alignment=Qt.AlignHCenter)
        self.regresar.clicked.connect(self.back_window)

        self.pixmap = QPixmap("src/img/fondo.jpg")
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(self.pixmap))
        self.setPalette(palette)
        self.setAutoFillBackground(True)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

        # Cargar datos del diccionario en la tabla
        self.load_dict_data()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "MainWindow", None))
        self.nueva_funcion.setText(QCoreApplication.translate("MainWindow", "Nueva función", None))
        self.label.setText(QCoreApplication.translate("MainWindow", "SOLUCIÓN", None))
        self.regresar.setText(QCoreApplication.translate("MainWindow", u"Regresar", None))
        self.boton_mux.setText(QCoreApplication.translate("MainWindow", u"Ver Mux", None))


    def load_dict_data(self):
        data = DT.Agrupados  # Diccionario
        minterms = DT.minterms  # Vector de números en formato entero
        respuesta_final = DT.Respuesta_final  # Vector que se mostrará en la tercera fila

        print("Datos del diccionario:", data)
        print("Minterms:", minterms)

        rows = len(data) + 1  # Añadir una fila extra para la Respuesta_final
        cols = max(len(values) for values in data.values())

        self.table.setRowCount(rows)  # Aumentar el número de filas
        self.table.setColumnCount(cols)
        self.table.horizontalHeader().setVisible(False)

        # Rellenar la tabla con el diccionario Agrupados
        for row, (key, values) in enumerate(data.items()):
            for col, value in enumerate(values):
                # Crear el QTableWidgetItem con el valor
                item = QTableWidgetItem(str(value))
                item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)

                print(f"Valor en la tabla (fila {row}, col {col}): {value}")
                
                # Establecer el item en la tabla
                self.table.setItem(row, col, item)

        # Rellenar la tercera fila (índice 2) con el vector Respuesta_final
        for col, value in enumerate(respuesta_final):
            item = QTableWidgetItem(str(value))
            item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
            
            print(f"Valor en Respuesta_final (col {col}): {value}")
            
            # Establecer el item en la fila 2 (tercera fila) de la tabla
            self.table.setItem(2, col, item)

        # Actualizar las etiquetas del encabezado vertical
        self.table.setVerticalHeaderLabels(list(data.keys()) + ["Respuesta Final"])


    def mostrar_mux(self):
        self.hide()
        self.ventana_mux = Mux(self.menu, self)
        self.ventana_mux.show()

    def back_window(self):
        self.hide()
        self.b.show()

    def back_menu(self):
        self.hide()
        self.menu.show()
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SalidaMenu2()
    window.show()
    sys.exit(app.exec())