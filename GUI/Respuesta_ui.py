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
from GUI.mux import Mux
import DATA

class SalidaMenu2(QMainWindow):
    def __init__(self, Main, Back):
        super().__init__()
        self.b = Back
        self.menu = Main
        self.setupUi(self)
        # self.load_resultado_final()  # Carga y muestra el resultado final al iniciar

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
        
        self.boton_mux = QPushButton(self.centralwidget)
        self.boton_mux.setObjectName(u"reduccion")
        self.boton_mux.setGeometry(QRect(510, 60, 211, 41))
        self.boton_mux.setFont(font)
        self.boton_mux.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.boton_mux.setStyleSheet(u"")
        self.boton_mux.clicked.connect(self.mostrar_mux)
        self.nueva_funcion.setMaximumSize(211, 41)  # Mantén el tamaño original
        self.nueva_funcion.clicked.connect(self.back_menu)
        self.horizontal_layout.addWidget(self.nueva_funcion, alignment=Qt.AlignmentFlag.AlignCenter)
        self.horizontal_layout.addWidget(self.boton_mux, alignment=Qt.AlignmentFlag.AlignCenter)

        # Añade el layout horizontal al vertical layout
        self.vertical_layout.addLayout(self.horizontal_layout)

        # Espaciador para separar el botón del texto "SOLUCIÓN"
        self.spacer_top = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.vertical_layout.addItem(self.spacer_top)

        # Texto "SOLUCIÓN"
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName("label")
        font1 = self.label.font()
        font1.setFamilies(["Arial Black"])
        font1.setPointSize(15)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Centra el texto
        self.vertical_layout.addWidget(self.label)

        # Espaciador para separar el texto "SOLUCIÓN" del resultado final
        self.spacer_middle = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.vertical_layout.addItem(self.spacer_middle)

        # Texto del resultado final
        self.ecuacion = QLabel(self.centralwidget)
        self.ecuacion.setObjectName("ecuacion")
        self.ecuacion.setStyleSheet("QLabel { font-family: \"STIX Two Text\"; font-style: italic; font-size: 24px; color: #ffffff; padding: 15px; }")  # Cambiado a blanco
        self.ecuacion.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Centra el texto
        self.vertical_layout.addWidget(self.ecuacion)
        
        # Espaciador para ajustar la posición del resultado final
        self.spacer_bottom = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.vertical_layout.addItem(self.spacer_bottom)

        # Configura los botones de navegación
        self.regresar = QPushButton(self.centralwidget)
        self.regresar.setObjectName(u"regresar")
        self.regresar.setGeometry(QRect(50, 510, 181, 51))
        self.vertical_layout.addWidget(self.regresar, alignment=Qt.AlignHCenter)
        
        self.regresar.clicked.connect(self.back_window)
        
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
        self.ecuacion.setText("")
        self.nueva_funcion.setText(QCoreApplication.translate("MainWindow", "Nueva función", None))
        self.label.setText(QCoreApplication.translate("MainWindow", "SOLUCIÓN", None))
        self.regresar.setText(QCoreApplication.translate("MainWindow", u"Regresar", None))
        self.boton_mux.setText(QCoreApplication.translate("MainWindow", u"Ver Mux", None))
        
        # self.comprobacion.setText(QCoreApplication.translate("MainWindow", u"Ver comprobaci\u00f3n", None))
        
    def crear_html_respuesta(self):
        # Obtener el texto como una cadena
        if len(DATA.ResultadoFinal) == 1 and DATA.ResultadoFinal[0] == "":
            return "1"
        text = ', '.join(map(str, DATA.ResultadoFinal)).replace(', ', ' + ')
        
        # Generar el HTML con las líneas superiores
        html_text = ''
        i = 0
        while i < len(text):
            char = text[i]
            if char == "'":
                # Salta las comillas simples
                i += 1
                continue
            
            # Verifica si el carácter siguiente es una comilla simple
            if i + 1 < len(text) and text[i + 1] == "'":
                html_text += f'<span style="text-decoration:overline">{char}</span>'
                i += 1  # Saltar el carácter de la comilla simple
            else:
                html_text += char
            
            i += 1
        
        return html_text

    def resizeEvent(self, event):
        # Redimensionar la imagen de fondo cuando la ventana cambie de tamaño
        # pixmap = QPixmap("ruta/a/tu/imagen.jpg")  # Vuelve a cargar la imagen
        scaled_pixmap = self.pixmap.scaled(self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        palette = self.palette()
        palette.setBrush(QPalette.Window, QBrush(scaled_pixmap))
        self.setPalette(palette)

        # Llamar al evento de redimensionamiento original
        super().resizeEvent(event)


    # def load_resultado_final(self):
    #     # Asumiendo que 'DATA.ResultadoFinal' es una lista o un vector de valores
    #     resultado_final = DATA.ResultadoFinal  # Obtén el vector
    #     # Convierte el vector en una cadena y reemplaza las comas por signos más
    #     resultado_final_str = self.crear_html_respuesta()
    #     # print(resultado_final_str)
    #     # Muestra el vector en la QLabel 'ecuacion'
    #     self.ecuacion.setText(f"Resultado Final: {resultado_final_str}")

    #     # Estiliza el texto de la QLabel
    #     font = QFont("Arial", 18, QFont.Bold)
    #     self.ecuacion.setFont(font)
    #     self.ecuacion.setStyleSheet("color: #ffffff;")  # Cambia el color del texto a blanco
    #     self.ecuacion.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Centra el texto
    #     self.ecuacion.setWordWrap(True)  # Permite el ajuste de línea si el texto es largo
    
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
