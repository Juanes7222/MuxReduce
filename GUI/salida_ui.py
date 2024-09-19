# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'salida2.ui'
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
    QPalette, QPixmap, QRadialGradient, QTransform, QMovie)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QMainWindow,
    QPushButton, QScrollBar, QSizePolicy, QStatusBar,
    QTableWidget, QTableWidgetItem, QWidget, QAbstractItemView)
from pathlib import Path
# from GUI.Respuesta_ui import SalidaMenu2
BASE_DIR = Path(__file__).resolve().parent.parent
import sys 
sys.path.append(fr"{BASE_DIR}")

import src.videos.next_rc
import src.videos.back_rc

    

class SalidaMenu(QMainWindow):
    def __init__(self, MainMenu: QMainWindow | None=None):
        super().__init__()

        
        self.menu = MainMenu
        self.original_data = {}
        if not self.objectName():
            self.setObjectName(u"Salida")
        
        self.resize(913, 697)
        self.video_player_next = QMovie("src/videos/avance-rapido-sinfondo.gif")
        self.video_player_back = QMovie("src/videos/retroceso-rapido-sinfondo.gif")
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Tabla_minterminos = QTableWidget(self.centralwidget)
        self.Tabla_minterminos.setObjectName(u"Tabl_minterminos")
        self.Tabla_minterminos.setGeometry(QRect(150, 220, 621, 431))
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
"                                   background-color: #f1eb2c;\n"
"                                   border: 2px solid rgb(182, 182, 182);\n"
"                                   border-radius: 8px;\n"
"}")
        self.back = QLabel(self.centralwidget)
        self.back.setObjectName(u"label")
        self.back.setGeometry(QRect(20, 610, 81, 51))
        self.next = QLabel(self.centralwidget)
        self.next.setObjectName(u"label_2")
        self.next.setGeometry(QRect(820, 600, 81, 51))
        self.video_player_next.setScaledSize(self.next.size())
        self.video_player_back.setScaledSize(self.back.size())
        
        self.back.setMovie(self.video_player_back)
        self.next.setMovie(self.video_player_next)
        self.next.setCursor(QCursor(Qt.PointingHandCursor))
        self.back.setCursor(QCursor(Qt.PointingHandCursor))
        self.video_player_back.start()
        self.video_player_next.start()
        # Asignar las señales de clic de los GIFs
        self.back.mousePressEvent = self.on_gif_click_back
        self.next.mousePressEvent = self.on_gif_click_next
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName(u"statusbar")
        self.setStatusBar(self.statusbar)
        self.nueva_funcion.clicked.connect(self.back_menu)
        self.pixmap = QPixmap("src/img/fondo.jpg") 
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(self.pixmap))
        self.setPalette(palette)

        # Redimensionar el fondo al tamaño de la ventana
        self.setAutoFillBackground(True)
        self.style_table()
        self.retranslateUi()


        QMetaObject.connectSlotsByName(self)

         # Inicializar el índice actual
        self.current_index = 0
        # Suponiendo que DATA.APAREAMIENTOS es la lista de diccionarios
        # self.data_list = DATA.APAREAMIENTOS
        # Cargar el primer diccionario al iniciar
        # self.load_dict(self.data_list[self.current_index])
    # setupUi

    def resizeEvent(self, event):
        # Redimensionar la imagen de fondo cuando la ventana cambie de tamaño
        # pixmap = QPixmap("ruta/a/tu/imagen.jpg")  # Vuelve a cargar la imagen
        scaled_pixmap = self.pixmap.scaled(self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        palette = self.palette()
        palette.setBrush(QPalette.Window, QBrush(scaled_pixmap))
        self.setPalette(palette)

        # Llamar al evento de redimensionamiento original
        super().resizeEvent(event)

    #################################Style TAble
    def style_table(self):
    # Ajustar el estilo de las cabeceras
        self.Tabla_minterminos.horizontalHeader().setStyleSheet(
            "QHeaderView::section { "
            "background-color: #f1eb2c; "
            "border: 1px solid #d0d0d0; "
            "padding: 4px; "
            "font-weight: bold; "
            "}"
        )
        self.Tabla_minterminos.setStyleSheet(
        "QTableWidget { "
        "gridline-color: #d0d0d0; "
        "}"
        "QTableWidget::item { "
        "padding: 5px; "
        "border: 1px solid #e0e0e0; "
        "}"
        "QTableWidget::item:selected { "
        "background-color: #FFD700; "
        "}"
    )
        
        # Ajustar el tamaño de las columnas automáticamente
        self.Tabla_minterminos.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        # Ocultar las cabeceras verticales si no las quieres mostrar
        self.Tabla_minterminos.verticalHeader().setVisible(False)

        # Configurar el modo de ajuste de la tabla
        self.Tabla_minterminos.setShowGrid(True)
        self.Tabla_minterminos.setAlternatingRowColors(True)






    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.ecuacion.setText("")
        self.nueva_funcion.setText(QCoreApplication.translate("MainWindow", u"Nueva funci\u00f3n", None))
        self.back.setText("")
        self.next.setText("")
    # retranslateUi

    # def load_dict(self, data_dict):
    #     # Limpiar la tabla antes de cargar nuevos datos
    #     self.Tabla_minterminos.clearContents()
        
    #     no_apareados = DATA.IMPLICANTES  # Lista de elementos no apareados organizados en sublistas
        
    #     # Configurar las columnas de la tabla
    #     self.Tabla_minterminos.setColumnCount(3)
    #     self.Tabla_minterminos.setRowCount(len(data_dict))
    #     self.Tabla_minterminos.setHorizontalHeaderLabels(["DECIMAL", "BINARIO", "APAREADO"])

    #     # Ocultar los encabezados verticales
    #     self.Tabla_minterminos.verticalHeader().setVisible(False)

    #     # Desactivar edición en la tabla
    #     self.Tabla_minterminos.setEditTriggers(QAbstractItemView.NoEditTriggers)

        

    #     # Iterar por cada elemento del diccionario
    #     for row, (key, value) in enumerate(data_dict.items()):
    #             # Convertir la clave (key) en una cadena de números separados por comas
    #         decimal_string = ' '.join(key)  # Asegúrate de que key sea una lista de cadenas
    #         # Convertir el valor (value) a una cadena si es necesario
    #         binary_string = ''.join(value)  # Asegúrate de que value sea una lista de cadenas

    #         # Agregar los valores a las columnas "DECIMAL" y "BINARIO"
    #         self.Tabla_minterminos.setItem(row, 0, QTableWidgetItem(decimal_string))
    #         self.Tabla_minterminos.setItem(row, 1, QTableWidgetItem(binary_string))

    #         # Verificar si el valor está en alguna sublista de no_apareados
    #         apareado = "✓"  # Por defecto, se marcará como "APAREADO"
    #         value_string = ''.join(value)  # Convertir el valor a una cadena para la comparación
    #         for sublist in no_apareados:
    #             sublist_string = ''.join(sublist)  # Convertir la sublista a una cadena
    #             if value_string == sublist_string:
    #                 apareado = "✗"  # Si el valor se encuentra en la lista de no apareados, marcar como "NO APAREADO"
    #                 break  # No es necesario seguir buscando si ya se encontró

    #         # Agregar el resultado en la columna "APAREADO"
    #         self.Tabla_minterminos.setItem(row, 2, QTableWidgetItem(apareado))





    def on_gif_click_next(self, event):
        ...
        # Asegúrate de que no estás en la última tabla
        # print(f"Current index: {self.current_index}")
        # print(f"Data list length: {len(self.data_list)}")
        
        # if self.current_index < len(self.data_list) - 1:
        #     self.current_index += 1
        #     self.load_dict(self.data_list[self.current_index])
        # else:
        #     # Si estás en la última tabla, abre la nueva ventana
        #     self.hide()
        #     self.Respuesta = SalidaMenu2(self.menu, self)
        #     self.Respuesta.show()

    def on_gif_click_back(self, event):
        """Muestra el diccionario anterior en la lista."""
        if self.current_index > 0:
            self.current_index -= 1
            self.load_dict(self.data_list[self.current_index])
            
    def back_menu(self):
        self.hide()
        self.menu.show()

if __name__ == "__main__":

    app = QApplication(sys.argv)
    # app.setStyleSheet(Path("sources/qss/styles_main.qss").read_text())
    ui = SalidaMenu()

    ui.show()
    sys.exit(app.exec())