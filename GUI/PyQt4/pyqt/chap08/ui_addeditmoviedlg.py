# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\python-ray\PyQt4\pyqt\chap08\addeditmoviedlg.ui'
#
# Created: Wed Sep 30 16:41:00 2009
# by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui


class Ui_AddEditMovieDlg(object):
    def setupUi(self, AddEditMovieDlg):
        AddEditMovieDlg.setObjectName("AddEditMovieDlg")
        AddEditMovieDlg.resize(484, 334)
        self.gridlayout = QtGui.QGridLayout(AddEditMovieDlg)
        self.gridlayout.setMargin(9)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")
        self.buttonBox = QtGui.QDialogButtonBox(AddEditMovieDlg)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QtGui.QDialogButtonBox.Cancel | QtGui.QDialogButtonBox.NoButton | QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridlayout.addWidget(self.buttonBox, 4, 4, 1, 2)
        self.titleLineEdit = QtGui.QLineEdit(AddEditMovieDlg)
        self.titleLineEdit.setObjectName("titleLineEdit")
        self.gridlayout.addWidget(self.titleLineEdit, 0, 1, 1, 5)
        self.label_5 = QtGui.QLabel(AddEditMovieDlg)
        self.label_5.setObjectName("label_5")
        self.gridlayout.addWidget(self.label_5, 2, 0, 1, 2)
        self.notesTextEdit = QtGui.QTextEdit(AddEditMovieDlg)
        self.notesTextEdit.setTabChangesFocus(True)
        self.notesTextEdit.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.notesTextEdit.setAcceptRichText(False)
        self.notesTextEdit.setObjectName("notesTextEdit")
        self.gridlayout.addWidget(self.notesTextEdit, 3, 0, 1, 6)
        self.label_2 = QtGui.QLabel(AddEditMovieDlg)
        self.label_2.setObjectName("label_2")
        self.gridlayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.yearSpinBox = QtGui.QSpinBox(AddEditMovieDlg)
        self.yearSpinBox.setAlignment(QtCore.Qt.AlignRight)
        self.yearSpinBox.setMaximum(2100)
        self.yearSpinBox.setMinimum(1890)
        self.yearSpinBox.setProperty("value", 1890)
        self.yearSpinBox.setObjectName("yearSpinBox")
        self.gridlayout.addWidget(self.yearSpinBox, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(AddEditMovieDlg)
        self.label_3.setObjectName("label_3")
        self.gridlayout.addWidget(self.label_3, 1, 2, 1, 1)
        self.minutesSpinBox = QtGui.QSpinBox(AddEditMovieDlg)
        self.minutesSpinBox.setAlignment(QtCore.Qt.AlignRight)
        self.minutesSpinBox.setMaximum(720)
        self.minutesSpinBox.setObjectName("minutesSpinBox")
        self.gridlayout.addWidget(self.minutesSpinBox, 1, 3, 1, 1)
        self.label_4 = QtGui.QLabel(AddEditMovieDlg)
        self.label_4.setObjectName("label_4")
        self.gridlayout.addWidget(self.label_4, 1, 4, 1, 1)
        self.acquiredDateEdit = QtGui.QDateEdit(AddEditMovieDlg)
        self.acquiredDateEdit.setAlignment(QtCore.Qt.AlignRight)
        self.acquiredDateEdit.setObjectName("acquiredDateEdit")
        self.gridlayout.addWidget(self.acquiredDateEdit, 1, 5, 1, 1)
        self.label = QtGui.QLabel(AddEditMovieDlg)
        self.label.setObjectName("label")
        self.gridlayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_5.setBuddy(self.notesTextEdit)
        self.label_2.setBuddy(self.yearSpinBox)
        self.label_3.setBuddy(self.minutesSpinBox)
        self.label_4.setBuddy(self.acquiredDateEdit)
        self.label.setBuddy(self.titleLineEdit)

        self.retranslateUi(AddEditMovieDlg)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), AddEditMovieDlg.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), AddEditMovieDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(AddEditMovieDlg)
        AddEditMovieDlg.setTabOrder(self.titleLineEdit, self.yearSpinBox)
        AddEditMovieDlg.setTabOrder(self.yearSpinBox, self.minutesSpinBox)
        AddEditMovieDlg.setTabOrder(self.minutesSpinBox, self.acquiredDateEdit)
        AddEditMovieDlg.setTabOrder(self.acquiredDateEdit, self.notesTextEdit)
        AddEditMovieDlg.setTabOrder(self.notesTextEdit, self.buttonBox)

    def retranslateUi(self, AddEditMovieDlg):
        AddEditMovieDlg.setWindowTitle(QtGui.QApplication.translate("AddEditMovieDlg", "My Movies - Add Movie", None,
                                                                    QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(
            QtGui.QApplication.translate("AddEditMovieDlg", "&Notes:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(
            QtGui.QApplication.translate("AddEditMovieDlg", "&Year:", None, QtGui.QApplication.UnicodeUTF8))
        self.yearSpinBox.setSpecialValueText(
            QtGui.QApplication.translate("AddEditMovieDlg", "Unknown", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(
            QtGui.QApplication.translate("AddEditMovieDlg", "&Minutes:", None, QtGui.QApplication.UnicodeUTF8))
        self.minutesSpinBox.setSpecialValueText(
            QtGui.QApplication.translate("AddEditMovieDlg", "Unknown", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(
            QtGui.QApplication.translate("AddEditMovieDlg", "A&cquired:", None, QtGui.QApplication.UnicodeUTF8))
        self.acquiredDateEdit.setDisplayFormat(
            QtGui.QApplication.translate("AddEditMovieDlg", "ddd MMM d, yyyy", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(
            QtGui.QApplication.translate("AddEditMovieDlg", "&Title:", None, QtGui.QApplication.UnicodeUTF8))

