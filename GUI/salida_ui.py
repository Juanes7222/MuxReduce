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
from GUI.Respuesta_ui import SalidaMenu2
BASE_DIR = Path(__file__).resolve().parent.parent
import sys 
sys.path.append(fr"{BASE_DIR}")
import DATA as DT
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
        
        self.boton_reduccion = QPushButton(self.centralwidget)
        self.boton_reduccion.setObjectName(u"reduccion")
        self.boton_reduccion.setGeometry(QRect(510, 60, 211, 41))
        self.boton_reduccion.setFont(font)
        self.boton_reduccion.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.boton_reduccion.setStyleSheet(u"")
        
        self.boton_reduccion.clicked.connect(self.reduccion)
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

         
        self.current_index = 0
        self.load_dict(DT.lista_binarios)
        

    def resizeEvent(self, event):
        
        scaled_pixmap = self.pixmap.scaled(self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        palette = self.palette()
        palette.setBrush(QPalette.Window, QBrush(scaled_pixmap))
        self.setPalette(palette)

        
        super().resizeEvent(event)

    #################################Style TAble
    def style_table(self):
    # Ajustar el estilo de las cabeceras
        self.Tabla_minterminos.horizontalHeader().setStyleSheet(
            "QHeaderView::section { "
            "background-color: #f7dd3b; "
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

    def load_dict(self, data_dict):
        self.Tabla_minterminos.setRowCount(0)  # Limpia la tabla
        
        # Obtén el número de bits (el valor máximo en el diccionario determina el número de bits)
        max_bits = len(bin(max(data_dict.keys()))[2:])
        
        # Establece las cabeceras de la tabla
        self.Tabla_minterminos.setColumnCount(2)
        self.Tabla_minterminos.setHorizontalHeaderLabels(['Número Decimal', 'Número Binario'])
        
        for row, (decimal_number, binary_vector) in enumerate(data_dict.items()):
            # Crea un nuevo ítem para la columna del número decimal
            decimal_item = QTableWidgetItem(str(decimal_number))
            
            # Asegúrate de que el valor binario tenga el número correcto de bits (rellenar con ceros a la izquierda)
            binary_item = QTableWidgetItem(format(decimal_number, f'0{max_bits}b'))  # Rellenar con ceros a la izquierda
            
            # Añadir los ítems a la tabla
            self.Tabla_minterminos.insertRow(row)
            self.Tabla_minterminos.setItem(row, 0, decimal_item)
            self.Tabla_minterminos.setItem(row, 1, binary_item)



    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.ecuacion.setText("")
        self.nueva_funcion.setText(QCoreApplication.translate("MainWindow", u"Nueva funci\u00f3n", None))
        self.boton_reduccion.setText(QCoreApplication.translate("MainWindow", u"Reducci\u00f3n", None))
        # self.back.setText("")
        # self.next.setText("")
    
    def reduccion(self):
        self.hide()
        self.respuesta = SalidaMenu2(self.menu, self) 
        self.respuesta.show()

    def back_menu(self):
        self.hide()
        self.menu.show()

if __name__ == "__main__":

    app = QApplication(sys.argv)
    ui = SalidaMenu()

    ui.show()
    sys.exit(app.exec())