# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kucoin.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import datetime
import CryptoPrice
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(462, 367)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.calcola = QtWidgets.QPushButton(self.centralwidget)
        self.calcola.setGeometry(QtCore.QRect(20, 270, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.calcola.setFont(font)
        self.calcola.setObjectName("calcola")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 101, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 141, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 140, 71, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 200, 71, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(200, 70, 211, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(180, 170, 291, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.yeacrypto = QtWidgets.QLabel(self.centralwidget)
        self.yeacrypto.setGeometry(QtCore.QRect(260, 100, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.yeacrypto.setFont(font)
        self.yeacrypto.setObjectName("yeacrypto")
        self.yeausdt = QtWidgets.QLabel(self.centralwidget)
        self.yeausdt.setGeometry(QtCore.QRect(260, 200, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.yeausdt.setFont(font)
        self.yeausdt.setObjectName("yeausdt")
        self.cryptoperc = QtWidgets.QLabel(self.centralwidget)
        self.cryptoperc.setGeometry(QtCore.QRect(260, 130, 71, 16))
        self.cryptoperc.setObjectName("cryptoperc")
        self.assetz = QtWidgets.QLineEdit(self.centralwidget)
        self.assetz.setGeometry(QtCore.QRect(20, 40, 51, 21))
        self.assetz.setObjectName("assetz")
        self.icz = QtWidgets.QLineEdit(self.centralwidget)
        self.icz.setGeometry(QtCore.QRect(20, 100, 91, 21))
        self.icz.setObjectName("icz")
        self.apz = QtWidgets.QLineEdit(self.centralwidget)
        self.apz.setGeometry(QtCore.QRect(20, 160, 91, 21))
        self.apz.setObjectName("apz")
        self.upz = QtWidgets.QLineEdit(self.centralwidget)
        self.upz.setGeometry(QtCore.QRect(20, 220, 91, 21))
        self.upz.setObjectName("upz")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 462, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.calcola.setText(_translate("MainWindow", "Do the math"))
        self.label_2.setText(_translate("MainWindow", "Asset (BTC, ETH...)"))
        self.label_3.setText(_translate("MainWindow", "Initial crypto assets quantity"))
        self.label_4.setText(_translate("MainWindow", "Asset positions"))
        self.label_5.setText(_translate("MainWindow", "USDT positions"))
        self.label_6.setText(_translate("MainWindow", "Total crypto assets earned"))
        self.label_7.setText(_translate("MainWindow", "Total USDT earned if you sell now"))
        self.yeacrypto.setText(_translate("MainWindow", "0.000"))
        self.yeausdt.setText(_translate("MainWindow", "0.000"))
        self.cryptoperc.setText(_translate("MainWindow", "or (0.00%)"))

        self.calcola.clicked.connect(self.tengset)

    def tengset(self):
        asset=self.assetz.text()
        retriever = CryptoPrice.BinanceRetriever()
        ref_asset = 'USDT'
        now=datetime.datetime.now()
        timestamp = int(datetime.datetime(int(now.strftime('%Y')),int(now.strftime('%m')),int(now.strftime('%d')),int(now.strftime('%H')),int(now.strftime('%M'))).timestamp())
        pattuale=(retriever.get_closest_price(asset, ref_asset, timestamp).value)

        qiniziale=float(self.icz.text())
        pcrypto=float(self.apz.text())
        pusdt=float(self.upz.text())

        #usdt -> crypto
        usdtcrypto=(pusdt/pattuale)+pcrypto

        profitcrypto=round(usdtcrypto-qiniziale, 5)

        percrypto=round(profitcrypto/qiniziale*100, 2)

        profitusdt=round(profitcrypto*pattuale, 2)

        profitcrypto=str(profitcrypto)+('')+asset
        percrypto=str(percrypto)+('%')
        profitusdt=('$')+str(profitusdt)
        self.yeacrypto.setText(profitcrypto)
        self.yeausdt.setText(profitusdt)
        self.cryptoperc.setText(percrypto)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
