# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\python-ray\PyQt4\pyqt\chap07\findandreplacedlg.ui'
#
# Created: Sun Sep 20 22:51:52 2009
# by: PyQt4 UI code generator 4.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui


class Ui_FindAndReplaceDlg(object):
    def setupUi(self, FindAndReplaceDlg):
        FindAndReplaceDlg.setObjectName("FindAndReplaceDlg")
        FindAndReplaceDlg.resize(363, 192)
        self.hboxlayout = QtGui.QHBoxLayout(FindAndReplaceDlg)
        self.hboxlayout.setMargin(9)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")
        self.vboxlayout = QtGui.QVBoxLayout()
        self.vboxlayout.setMargin(0)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")
        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setMargin(0)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")
        self.replaceLineEdit = QtGui.QLineEdit(FindAndReplaceDlg)
        self.replaceLineEdit.setObjectName("replaceLineEdit")
        self.gridlayout.addWidget(self.replaceLineEdit, 1, 1, 1, 1)
        self.findLineEdit = QtGui.QLineEdit(FindAndReplaceDlg)
        self.findLineEdit.setObjectName("findLineEdit")
        self.gridlayout.addWidget(self.findLineEdit, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(FindAndReplaceDlg)
        self.label_2.setObjectName("label_2")
        self.gridlayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtGui.QLabel(FindAndReplaceDlg)
        self.label.setObjectName("label")
        self.gridlayout.addWidget(self.label, 0, 0, 1, 1)
        self.vboxlayout.addLayout(self.gridlayout)
        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setMargin(0)
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setObjectName("hboxlayout1")
        self.caseCheckBox = QtGui.QCheckBox(FindAndReplaceDlg)
        self.caseCheckBox.setObjectName("caseCheckBox")
        self.hboxlayout1.addWidget(self.caseCheckBox)
        self.wholeCheckBox = QtGui.QCheckBox(FindAndReplaceDlg)
        self.wholeCheckBox.setChecked(True)
        self.wholeCheckBox.setObjectName("wholeCheckBox")
        self.hboxlayout1.addWidget(self.wholeCheckBox)
        self.vboxlayout.addLayout(self.hboxlayout1)
        self.hboxlayout2 = QtGui.QHBoxLayout()
        self.hboxlayout2.setMargin(0)
        self.hboxlayout2.setSpacing(6)
        self.hboxlayout2.setObjectName("hboxlayout2")
        self.label_3 = QtGui.QLabel(FindAndReplaceDlg)
        self.label_3.setObjectName("label_3")
        self.hboxlayout2.addWidget(self.label_3)
        self.syntaxComboBox = QtGui.QComboBox(FindAndReplaceDlg)
        self.syntaxComboBox.setObjectName("syntaxComboBox")
        self.syntaxComboBox.addItem(QtCore.QString())
        self.syntaxComboBox.addItem(QtCore.QString())
        self.hboxlayout2.addWidget(self.syntaxComboBox)
        self.vboxlayout.addLayout(self.hboxlayout2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem)
        self.hboxlayout.addLayout(self.vboxlayout)
        self.line = QtGui.QFrame(FindAndReplaceDlg)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.hboxlayout.addWidget(self.line)
        self.vboxlayout1 = QtGui.QVBoxLayout()
        self.vboxlayout1.setMargin(0)
        self.vboxlayout1.setSpacing(6)
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.findButton = QtGui.QPushButton(FindAndReplaceDlg)
        self.findButton.setObjectName("findButton")
        self.vboxlayout1.addWidget(self.findButton)
        self.replaceButton = QtGui.QPushButton(FindAndReplaceDlg)
        self.replaceButton.setObjectName("replaceButton")
        self.vboxlayout1.addWidget(self.replaceButton)
        self.replaceAllButton = QtGui.QPushButton(FindAndReplaceDlg)
        self.replaceAllButton.setObjectName("replaceAllButton")
        self.vboxlayout1.addWidget(self.replaceAllButton)
        spacerItem1 = QtGui.QSpacerItem(20, 16, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vboxlayout1.addItem(spacerItem1)
        self.closeButton = QtGui.QPushButton(FindAndReplaceDlg)
        self.closeButton.setObjectName("closeButton")
        self.vboxlayout1.addWidget(self.closeButton)
        self.hboxlayout.addLayout(self.vboxlayout1)
        self.label_2.setBuddy(self.replaceLineEdit)
        self.label.setBuddy(self.findLineEdit)
        self.label_3.setBuddy(self.syntaxComboBox)

        self.retranslateUi(FindAndReplaceDlg)
        QtCore.QObject.connect(self.closeButton, QtCore.SIGNAL("clicked()"), FindAndReplaceDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(FindAndReplaceDlg)
        FindAndReplaceDlg.setTabOrder(self.findLineEdit, self.replaceLineEdit)
        FindAndReplaceDlg.setTabOrder(self.replaceLineEdit, self.caseCheckBox)
        FindAndReplaceDlg.setTabOrder(self.caseCheckBox, self.wholeCheckBox)
        FindAndReplaceDlg.setTabOrder(self.wholeCheckBox, self.syntaxComboBox)
        FindAndReplaceDlg.setTabOrder(self.syntaxComboBox, self.findButton)
        FindAndReplaceDlg.setTabOrder(self.findButton, self.replaceButton)
        FindAndReplaceDlg.setTabOrder(self.replaceButton, self.replaceAllButton)
        FindAndReplaceDlg.setTabOrder(self.replaceAllButton, self.closeButton)

    def retranslateUi(self, FindAndReplaceDlg):
        FindAndReplaceDlg.setWindowTitle(
            QtGui.QApplication.translate("FindAndReplaceDlg", "Find and Replace", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(
            QtGui.QApplication.translate("FindAndReplaceDlg", "Replace w&ith:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(
            QtGui.QApplication.translate("FindAndReplaceDlg", "Find &what:", None, QtGui.QApplication.UnicodeUTF8))
        self.caseCheckBox.setText(
            QtGui.QApplication.translate("FindAndReplaceDlg", "&Case sensitive", None, QtGui.QApplication.UnicodeUTF8))
        self.wholeCheckBox.setText(
            QtGui.QApplication.translate("FindAndReplaceDlg", "Wh&ole words", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(
            QtGui.QApplication.translate("FindAndReplaceDlg", "&Syntax:", None, QtGui.QApplication.UnicodeUTF8))
        self.syntaxComboBox.setItemText(0, QtGui.QApplication.translate("FindAndReplaceDlg", "Literal text", None,
                                                                        QtGui.QApplication.UnicodeUTF8))
        self.syntaxComboBox.setItemText(1, QtGui.QApplication.translate("FindAndReplaceDlg", "Regular expression", None,
                                                                        QtGui.QApplication.UnicodeUTF8))
        self.findButton.setText(
            QtGui.QApplication.translate("FindAndReplaceDlg", "&Find", None, QtGui.QApplication.UnicodeUTF8))
        self.replaceButton.setText(
            QtGui.QApplication.translate("FindAndReplaceDlg", "&Replace", None, QtGui.QApplication.UnicodeUTF8))
        self.replaceAllButton.setText(
            QtGui.QApplication.translate("FindAndReplaceDlg", "Replace &All", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setText(
            QtGui.QApplication.translate("FindAndReplaceDlg", "Close", None, QtGui.QApplication.UnicodeUTF8))

