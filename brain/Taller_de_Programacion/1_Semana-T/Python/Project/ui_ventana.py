# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana.ui'
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
        MainWindow.resize(1102, 858)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.asdasd = QLabel(self.centralwidget)
        self.asdasd.setObjectName(u"asdasd")
        self.asdasd.setGeometry(QRect(230, 220, 161, 16))
        self.txtNombre = QLineEdit(self.centralwidget)
        self.txtNombre.setObjectName(u"txtNombre")
        self.txtNombre.setGeometry(QRect(380, 220, 211, 26))
        self.btnSaludar = QPushButton(self.centralwidget)
        self.btnSaludar.setObjectName(u"btnSaludar")
        self.btnSaludar.setGeometry(QRect(370, 270, 81, 26))
        self.lblResultado = QLabel(self.centralwidget)
        self.lblResultado.setObjectName(u"lblResultado")
        self.lblResultado.setGeometry(QRect(370, 350, 151, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1102, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.asdasd.setText(QCoreApplication.translate("MainWindow", u"Escribe tu nombre aqui: ", None))
        self.btnSaludar.setText(QCoreApplication.translate("MainWindow", u"Saludar", None))
        self.lblResultado.setText(QCoreApplication.translate("MainWindow", u"Aqui empezar\u00e0 el saludo", None))
    # retranslateUi

