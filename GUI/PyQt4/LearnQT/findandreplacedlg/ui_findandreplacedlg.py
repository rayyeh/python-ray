# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'findandreplacelg.ui'
#
# Created: Thu Sep 24 14:18:30 2009
# by: PyQt4 UI code generator 4.5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui


class Ui_FindAndReplaceDlg(object):
    def setupUi(self, FindAndReplaceDlg):
        FindAndReplaceDlg.setObjectName("FindAndReplaceDlg")
        FindAndReplaceDlg.resize(400, 300)
        self.line = QtGui.QFrame(FindAndReplaceDlg)
        self.line.setGeometry(QtCore.QRect(250, 20, 20, 261))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.widget = QtGui.QWidget(FindAndReplaceDlg)
        self.widget.setGeometry(QtCore.QRect(20, 10, 231, 271))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.findLineEdit = QtGui.QLineEdit(self.widget)
        self.findLineEdit.setObjectName("findLineEdit")
        self.gridLayout.addWidget(self.findLineEdit, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.replaceLineEdit = QtGui.QLineEdit(self.widget)
        self.replaceLineEdit.setObjectName("replaceLineEdit")
        self.gridLayout.addWidget(self.replaceLineEdit, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.caseCheckBox = QtGui.QCheckBox(self.widget)
        self.caseCheckBox.setObjectName("caseCheckBox")
        self.horizontalLayout.addWidget(self.caseCheckBox)
        self.wholeCheckBox = QtGui.QCheckBox(self.widget)
        self.wholeCheckBox.setChecked(True)
        self.wholeCheckBox.setObjectName("wholeCheckBox")
        self.horizontalLayout.addWidget(self.wholeCheckBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Syntax = QtGui.QLabel(self.widget)
        self.Syntax.setObjectName("Syntax")
        self.horizontalLayout_2.addWidget(self.Syntax)
        self.syntaxComboBox = QtGui.QComboBox(self.widget)
        self.syntaxComboBox.setObjectName("syntaxComboBox")
        self.syntaxComboBox.addItem(QtCore.QString())
        self.syntaxComboBox.addItem(QtCore.QString())
        self.horizontalLayout_2.addWidget(self.syntaxComboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem = QtGui.QSpacerItem(20, 38, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.widget1 = QtGui.QWidget(FindAndReplaceDlg)
        self.widget1.setGeometry(QtCore.QRect(291, 11, 91, 261))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.findButton = QtGui.QPushButton(self.widget1)
        self.findButton.setObjectName("findButton")
        self.verticalLayout_2.addWidget(self.findButton)
        self.replaceButton = QtGui.QPushButton(self.widget1)
        self.replaceButton.setObjectName("replaceButton")
        self.verticalLayout_2.addWidget(self.replaceButton)
        self.replaceAllButton = QtGui.QPushButton(self.widget1)
        self.replaceAllButton.setObjectName("replaceAllButton")
        self.verticalLayout_2.addWidget(self.replaceAllButton)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.closeButton = QtGui.QPushButton(self.widget1)
        self.closeButton.setObjectName("closeButton")
        self.verticalLayout_2.addWidget(self.closeButton)
        self.label.setBuddy(self.findLineEdit)
        self.label_2.setBuddy(self.replaceLineEdit)

        self.retranslateUi(FindAndReplaceDlg)
        QtCore.QObject.connect(self.closeButton, QtCore.SIGNAL("clicked()"), FindAndReplaceDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(FindAndReplaceDlg)

    def retranslateUi(self, FindAndReplaceDlg):
        FindAndReplaceDlg.setWindowTitle(
            QtGui.QApplication.translate("FindAndReplaceDlg", "Find And Replace", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(
            QtGui.QApplication.translate("FindAndReplaceDlg", "Find &what:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(
            QtGui.QApplication.translate("FindAndReplaceDlg", "Replace w&ith", None, QtGui.QApplication.UnicodeUTF8))
        self.caseCheckBox.setText(
            QtGui.QApplication.translate("FindAndReplaceDlg", "&Case 中文", None, QtGui.QApplication.UnicodeUTF8))
        self.wholeCheckBox.setText(
            QtGui.QApplication.translate("FindAndReplaceDlg", "Wh&ole words", None, QtGui.QApplication.UnicodeUTF8))
        self.Syntax.setText(
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

