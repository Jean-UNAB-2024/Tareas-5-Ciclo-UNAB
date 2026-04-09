# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana_suma.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lblNumero1 = QLabel(self.centralwidget)
        self.lblNumero1.setObjectName(u"lblNumero1")
        self.lblNumero1.setGeometry(QRect(148, 110, 71, 20))
        self.lblNumero2 = QLabel(self.centralwidget)
        self.lblNumero2.setObjectName(u"lblNumero2")
        self.lblNumero2.setGeometry(QRect(148, 180, 71, 20))
        self.txtNumero1 = QLineEdit(self.centralwidget)
        self.txtNumero1.setObjectName(u"txtNumero1")
        self.txtNumero1.setGeometry(QRect(260, 110, 113, 26))
        self.txtNumero2 = QLineEdit(self.centralwidget)
        self.txtNumero2.setObjectName(u"txtNumero2")
        self.txtNumero2.setGeometry(QRect(260, 180, 113, 26))
        self.btnSumar = QPushButton(self.centralwidget)
        self.btnSumar.setObjectName(u"btnSumar")
        self.btnSumar.setGeometry(QRect(500, 150, 81, 26))
        self.btnLimpiar = QPushButton(self.centralwidget)
        self.btnLimpiar.setObjectName(u"btnLimpiar")
        self.btnLimpiar.setGeometry(QRect(310, 280, 81, 26))
        self.lblResultado = QLabel(self.centralwidget)
        self.lblResultado.setObjectName(u"lblResultado")
        self.lblResultado.setGeometry(QRect(320, 340, 71, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lblNumero1.setText(QCoreApplication.translate("MainWindow", u"Numero 1:", None))
        self.lblNumero2.setText(QCoreApplication.translate("MainWindow", u"Numero 2:", None))
        self.btnSumar.setText(QCoreApplication.translate("MainWindow", u"Suma", None))
        self.btnLimpiar.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.lblResultado.setText(QCoreApplication.translate("MainWindow", u"Resultado", None))
    # retranslateUi

