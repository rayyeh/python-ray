# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\study\python\pyqttest\GoogleMaps.ui'
#
# Created: Mon Aug 10 20:12:22 2009
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_DialogGoogleMaps(object):
    def setupUi(self, DialogGoogleMaps):
        DialogGoogleMaps.setObjectName("DialogGoogleMaps")
        DialogGoogleMaps.resize(773, 588)
        self.inputAddress = QtGui.QLineEdit(DialogGoogleMaps)
        self.inputAddress.setGeometry(QtCore.QRect(40, 30, 371, 20))
        self.inputAddress.setObjectName("inputAddress")
        self.labelAddress = QtGui.QLabel(DialogGoogleMaps)
        self.labelAddress.setGeometry(QtCore.QRect(10, 30, 31, 16))
        self.labelAddress.setObjectName("labelAddress")
        self.groupBoxMapCtrl = QtGui.QGroupBox(DialogGoogleMaps)
        self.groupBoxMapCtrl.setGeometry(QtCore.QRect(530, 40, 211, 121))
        self.groupBoxMapCtrl.setObjectName("groupBoxMapCtrl")
        self.ButtonUp = QtGui.QPushButton(self.groupBoxMapCtrl)
        self.ButtonUp.setGeometry(QtCore.QRect(90, 10, 31, 31))
        self.ButtonUp.setObjectName("ButtonUp")
        self.ButtonDown = QtGui.QPushButton(self.groupBoxMapCtrl)
        self.ButtonDown.setGeometry(QtCore.QRect(90, 90, 31, 31))
        self.ButtonDown.setObjectName("ButtonDown")
        self.ButtonLeft = QtGui.QPushButton(self.groupBoxMapCtrl)
        self.ButtonLeft.setGeometry(QtCore.QRect(30, 50, 31, 31))
        self.ButtonLeft.setObjectName("ButtonLeft")
        self.ButtonRight = QtGui.QPushButton(self.groupBoxMapCtrl)
        self.ButtonRight.setGeometry(QtCore.QRect(150, 50, 31, 31))
        self.ButtonRight.setObjectName("ButtonRight")
        self.ButtonZoom = QtGui.QPushButton(self.groupBoxMapCtrl)
        self.ButtonZoom.setGeometry(QtCore.QRect(70, 50, 31, 31))
        self.ButtonZoom.setObjectName("ButtonZoom")
        self.ButtonNarrow = QtGui.QPushButton(self.groupBoxMapCtrl)
        self.ButtonNarrow.setGeometry(QtCore.QRect(110, 50, 31, 31))
        self.ButtonNarrow.setObjectName("ButtonNarrow")
        self.MapView = QtWebKit.QWebView(DialogGoogleMaps)
        self.MapView.setGeometry(QtCore.QRect(10, 60, 512, 512))
        self.MapView.setUrl(QtCore.QUrl("http://maps.google.com/staticmap?center=32.0583650,118.7964680&zoom=14&size=512x512&maptype=mobile&markers=32.0583650,118.7964680&key=ABQIAAAApIB1Ubv-TkAKBJ37W0Hh2RS1AC4DxUbsxJ-9A5H8anlW8PhTrBQW71UJo3SK1Lm1LK_DZxfeCJessA&sensor=false"))
        self.MapView.setObjectName("MapView")
        self.BtnSearch = QtGui.QPushButton(DialogGoogleMaps)
        self.BtnSearch.setGeometry(QtCore.QRect(440, 30, 75, 23))
        self.BtnSearch.setObjectName("BtnSearch")
        self.ListAddress = QtGui.QListWidget(DialogGoogleMaps)
        self.ListAddress.setGeometry(QtCore.QRect(530, 200, 211, 371))
        self.ListAddress.setFrameShape(QtGui.QFrame.StyledPanel)
        self.ListAddress.setObjectName("ListAddress")
        QtGui.QListWidgetItem(self.ListAddress)
        QtGui.QListWidgetItem(self.ListAddress)
        self.label = QtGui.QLabel(DialogGoogleMaps)
        self.label.setGeometry(QtCore.QRect(530, 180, 54, 14))
        self.label.setObjectName("label")

        self.retranslateUi(DialogGoogleMaps)
        QtCore.QMetaObject.connectSlotsByName(DialogGoogleMaps)

    def retranslateUi(self, DialogGoogleMaps):
        DialogGoogleMaps.setWindowTitle(QtGui.QApplication.translate("DialogGoogleMaps", "Google maps应用程序", None, QtGui.QApplication.UnicodeUTF8))
        self.labelAddress.setText(QtGui.QApplication.translate("DialogGoogleMaps", "地址:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBoxMapCtrl.setTitle(QtGui.QApplication.translate("DialogGoogleMaps", "地图控制", None, QtGui.QApplication.UnicodeUTF8))
        self.ButtonUp.setText(QtGui.QApplication.translate("DialogGoogleMaps", "上", None, QtGui.QApplication.UnicodeUTF8))
        self.ButtonDown.setText(QtGui.QApplication.translate("DialogGoogleMaps", "下", None, QtGui.QApplication.UnicodeUTF8))
        self.ButtonLeft.setText(QtGui.QApplication.translate("DialogGoogleMaps", "左", None, QtGui.QApplication.UnicodeUTF8))
        self.ButtonRight.setText(QtGui.QApplication.translate("DialogGoogleMaps", "右", None, QtGui.QApplication.UnicodeUTF8))
        self.ButtonZoom.setText(QtGui.QApplication.translate("DialogGoogleMaps", "大", None, QtGui.QApplication.UnicodeUTF8))
        self.ButtonNarrow.setText(QtGui.QApplication.translate("DialogGoogleMaps", "小", None, QtGui.QApplication.UnicodeUTF8))
        self.BtnSearch.setText(QtGui.QApplication.translate("DialogGoogleMaps", "搜索", None, QtGui.QApplication.UnicodeUTF8))
        self.ListAddress.setSortingEnabled(False)
        __sortingEnabled = self.ListAddress.isSortingEnabled()
        self.ListAddress.setSortingEnabled(False)
        self.ListAddress.item(0).setText(QtGui.QApplication.translate("DialogGoogleMaps", "结果1", None, QtGui.QApplication.UnicodeUTF8))
        self.ListAddress.item(1).setText(QtGui.QApplication.translate("DialogGoogleMaps", "新建项目", None, QtGui.QApplication.UnicodeUTF8))
        self.ListAddress.setSortingEnabled(__sortingEnabled)
        self.label.setText(QtGui.QApplication.translate("DialogGoogleMaps", "搜索结果:", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import QtWebKit

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DialogGoogleMaps = QtGui.QDialog()
    ui = Ui_DialogGoogleMaps()
    ui.setupUi(DialogGoogleMaps)
    DialogGoogleMaps.show()
    sys.exit(app.exec_())

