# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu_principal.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import sys 
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QTextEdit, QWidget, QLineEdit)
from string import ascii_uppercase
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(fr"{BASE_DIR}")
from utils import procesar_variables, to_list, validar_pesos, obtener_cant_vars
from GUI.salida_ui import SalidaMenu
import controller
import src.img.fondo_rc

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        if not self.objectName():
            self.setObjectName(u"MainWindow")
        self.resize(890, 738)
        self.setStyleSheet(u"Qlabel{\n"
"font-weight: 1000;\n"
"}")
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Titulo_principal = QLabel(self.centralwidget)
        self.Titulo_principal.setObjectName(u"Titulo_principal")
        self.Titulo_principal.setGeometry(QRect(240, 10, 451, 101))
        font = QFont()
        font.setFamilies([u"CountryBlueprint"])
        font.setPointSize(40)
        font.setWeight(QFont.Black)
        font.setItalic(False)
        self.Titulo_principal.setFont(font)
        self.Titulo_principal.setStyleSheet(u"Qlabel{font-weight: 8000;}")
        self.Titulo_principal.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_minterminos = QLabel(self.centralwidget)
        self.label_minterminos.setObjectName(u"label_minterminos")
        self.label_minterminos.setGeometry(QRect(30, 180, 181, 61))
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.label_minterminos.setFont(font1)
        self.label_minterminos.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.calcular = QPushButton(self.centralwidget)
        self.calcular.setObjectName(u"calcular")
        self.calcular.setGeometry(QRect(310, 460, 301, 71))
        font2 = QFont()
        font2.setPointSize(17)
        font2.setBold(True)
        self.calcular.setFont(font2)
        self.calcular.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.calcular.setStyleSheet(u"QPushButton{\n"
"                                 padding: 20;\n"
"                                   background-color: #3b8710;\n"
"                                   border: 2px solid rgb(182, 182, 182);\n"
"                                   border-radius: 8px;\n"
"}")
        # self.calcular
        self.calcular.clicked.connect(self.event_calc)
        self.label_cantidad = QLabel(self.centralwidget)
        self.label_cantidad.setObjectName(u"label_cantidad")
        self.label_cantidad.setGeometry(QRect(10, 260, 201, 91))
        self.label_cantidad.setFont(font1)
        self.label_cantidad.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_cantidad.setWordWrap(True)
        self.minterminos = QLineEdit(self.centralwidget)
        self.minterminos.setObjectName(u"minterminos")
        self.minterminos.setGeometry(QRect(220, 190, 541, 51))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(17)
        self.minterminos.setFont(font3)
        self.minterminos.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.minterminos.setCursorMoveStyle(Qt.CursorMoveStyle.VisualMoveStyle)
        self.minterminos.setClearButtonEnabled(True)
        self.cant_variables = QLineEdit(self.centralwidget)
        self.cant_variables.setObjectName(u"cant_variables")
        self.cant_variables.setGeometry(QRect(220, 280, 541, 51))
        self.cant_variables.setFont(font3)
        self.cant_variables.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cant_variables.setCursorMoveStyle(Qt.CursorMoveStyle.VisualMoveStyle)
        self.cant_variables.setClearButtonEnabled(True)
        self.variables = QLineEdit(self.centralwidget)
        self.variables.setObjectName(u"variables")
        self.variables.setGeometry(QRect(220, 370, 541, 51))
        self.variables.setFont(font3)
        self.variables.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.variables.setCursorMoveStyle(Qt.CursorMoveStyle.VisualMoveStyle)
        self.variables.setClearButtonEnabled(True)
        # self.minterminos.setAcceptRichText(True)
        self.label_variabls = QLabel(self.centralwidget)
        self.label_variabls.setObjectName(u"label_variabls")
        self.label_variabls.setGeometry(QRect(20, 350, 201, 91))
        self.label_variabls.setFont(font1)
        self.label_variabls.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_variabls.setWordWrap(True)
        # self.fondo_pantalla = QLabel(self.centralwidget)
        # self.fondo_pantalla.setObjectName(u"fondo_pantalla")
        # self.fondo_pantalla.setGeometry(QRect(-10, 0, 911, 741))
        self.setCentralWidget(self.centralwidget)
        # self.fondo_pantalla.raise_()
        self.Titulo_principal.raise_()
        self.label_minterminos.raise_()
        self.calcular.raise_()
        self.label_cantidad.raise_()
        self.cant_variables.raise_()
        self.minterminos.raise_()
        self.label_variabls.raise_()
        self.variables.raise_()
        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName(u"statusbar")
        self.setStatusBar(self.statusbar)
        
        self.estilo_original = """QLineEdit {
    border: 3px solid #4CAF50;
    border-radius: 8px;
    padding: 8px;
    background-color: #FFFFFF;
    font-size: 16px;
            }"""

        self.pixmap = QPixmap("src/img/fondo.jpg") 
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(self.pixmap))
        self.setPalette(palette)

        # Redimensionar el fondo al tamaño de la ventana
        self.setAutoFillBackground(True)
        
        self.retranslateUi(self)
        # self.fondo_pantalla.setScaledContents(True)
        size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # self.fondo_pantalla.setSizePolicy(size_policy)
        self.cant_variables.textChanged.connect(self.verificar_cant)
        self.minterminos.textChanged.connect(self.cambio_vars)
        self.variables.textChanged.connect(self.cambio_variables)
        # self.minterminos.textEdited.connect(self.cambio_vars)

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Titulo_principal.setText(QCoreApplication.translate("MainWindow", u"Mc. Closkey", None))
        self.label_minterminos.setText(QCoreApplication.translate("MainWindow", u"Minterminos", None))
        self.calcular.setText(QCoreApplication.translate("MainWindow", u"Calcular", None))
        self.label_cantidad.setText(QCoreApplication.translate("MainWindow", u"Cantidad de terminos", None))
        self.label_variabls.setText(QCoreApplication.translate("MainWindow", u"Variables", None))
        # self.fondo_pantalla.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>|<img src=\":/fondo_pantalla/94-948666_m.jpg\"/></p></body></html>", None))
        self.minterminos.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1,2,3,4,5,6,...", None))
        self.cant_variables.setPlaceholderText(QCoreApplication.translate("MainWindow", u"# de variables", None))
        self.variables.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ABCD", None))
    # retranslateUi
    
    def resizeEvent(self, event):
        # Redimensionar la imagen de fondo cuando la ventana cambie de tamaño
        # pixmap = QPixmap("ruta/a/tu/imagen.jpg")  # Vuelve a cargar la imagen
        scaled_pixmap = self.pixmap.scaled(self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        palette = self.palette()
        palette.setBrush(QPalette.Window, QBrush(scaled_pixmap))
        self.setPalette(palette)

        # Llamar al evento de redimensionamiento original
        super().resizeEvent(event)
    
    def cambio_vars(self):
        vars_list = self.minterminos.text()
        variables, _ = procesar_variables(vars_list)
        if not variables:
            self.error_cant("", self.minterminos)
            return
        else:
            self.volver_estilo(self.minterminos)

        if self.cant_variables.text().strip() != "":
            self.verificar_cant()
            return
        
        self.variables.setPlaceholderText("".join(variables))
        self.volver_estilo(self.minterminos)
        
    def verificar_cant(self):
        if self.cant_variables.text().strip() == "":
            self.volver_estilo(self.cant_variables)
            self.cambio_vars()
            return
        try:
            cant = int(self.cant_variables.text())
            minterminos = to_list(self.minterminos.text())
            cant_vars = obtener_cant_vars(minterminos)
            if cant < cant_vars:
                self.error_cant("", self.cant_variables)     
            else:
                self.variables.setPlaceholderText(ascii_uppercase[:cant])
                self.volver_estilo(self.cant_variables)
                
        except ValueError:
            self.error_cant("", self.cant_variables)
        
    def error_cant(self, mensaje, obj):
        nuevo_estilo = self.estilo_original + "QLineEdit { border: 3px solid red; }"
        obj.setStyleSheet(nuevo_estilo)
        
    def volver_estilo(self, obj):
        obj.setStyleSheet(self.estilo_original)
    
    def obtener_valores(self):
        minterminos = self.minterminos.text()
        if minterminos.strip() == "":
            self.error_cant("", self.minterminos)
            return
        elif not validar_pesos(minterminos):
            self.error_cant("", self.minterminos)
            return
        variables = self.variables.text()
        variables = variables.strip()
        if variables == "":
            variables, _ = procesar_variables(minterminos, self.cant_variables.text().strip())
        else:
            variables = list(variables)
            if len(set(variables)) < len(variables):
                self.error_cant("", self.variables)
                return
        cant_terminos = self.cant_variables.text().strip()
        if cant_terminos == "":
            cant_terminos = len(variables)
        else:
            cant_terminos = int(cant_terminos)
        if cant_terminos != len(variables):
            self.error_cant("", self.variables)
        params = locals()
        params.pop("self")
        
        resultado = controller.main(**params)
        return resultado
    
    def cambio_variables(self):
        variables = self.variables.text()
        variables = variables.strip()
        cant = self.cant_variables.text().strip()
        if cant != "":
            length = int(cant)
        else:
            length = len(variables)
        if length != obtener_cant_vars(self.minterminos.text().strip().split(",")):
            self.error_cant("", self.variables)
        else:
            self.volver_estilo(self.variables)
    
    def event_calc(self, event):
        resultado = self.obtener_valores()
        if not resultado:
            return
        self.hide()
        
        self.salida = SalidaMenu(self)
        self.salida.show()

if __name__ == "__main__":
    import sys


    app = QApplication(sys.argv)
    app.setStyleSheet(Path("./src/qss/style.qss").read_text())
    ui = Ui_MainWindow()
    
    ui.show()
   
    sys.exit(app.exec())
    