# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'notas.ui'
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
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(190, 80, 71, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(190, 140, 81, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(190, 200, 71, 16))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(240, 310, 49, 16))
        self.lblResult = QLabel(self.centralwidget)
        self.lblResult.setObjectName(u"lblResult")
        self.lblResult.setGeometry(QRect(330, 310, 361, 16))
        self.txtActitudinal = QLineEdit(self.centralwidget)
        self.txtActitudinal.setObjectName(u"txtActitudinal")
        self.txtActitudinal.setGeometry(QRect(320, 70, 113, 26))
        self.txtProcedimental = QLineEdit(self.centralwidget)
        self.txtProcedimental.setObjectName(u"txtProcedimental")
        self.txtProcedimental.setGeometry(QRect(320, 140, 113, 26))
        self.txtCognocitivo = QLineEdit(self.centralwidget)
        self.txtCognocitivo.setObjectName(u"txtCognocitivo")
        self.txtCognocitivo.setGeometry(QRect(310, 200, 113, 26))
        self.btnEstado = QPushButton(self.centralwidget)
        self.btnEstado.setObjectName(u"btnEstado")
        self.btnEstado.setGeometry(QRect(270, 250, 81, 26))
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
        self.label.setText(QCoreApplication.translate("MainWindow", u"Actitudinal", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Procedimental", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Cognocitivo", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Estado: ", None))
        self.lblResult.setText(QCoreApplication.translate("MainWindow", u"Resultado", None))
        self.btnEstado.setText(QCoreApplication.translate("MainWindow", u"Estado", None))
    # retranslateUi

