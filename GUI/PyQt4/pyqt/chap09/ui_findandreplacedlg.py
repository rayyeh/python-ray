# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\python-ray\PyQt4\pyqt\chap09\findandreplacedlg.ui'
#
# Created: Fri Oct 09 09:24:40 2009
# by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui


class Ui_FindAndReplaceDlg(object):
    def setupUi(self, FindAndReplaceDlg):
        FindAndReplaceDlg.setObjectName("FindAndReplaceDlg")
        FindAndReplaceDlg.resize(355, 274)
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
        self.vboxlayout1 = QtGui.QVBoxLayout()
        self.vboxlayout1.setMargin(0)
        self.vboxlayout1.setSpacing(6)
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.caseCheckBox = QtGui.QCheckBox(FindAndReplaceDlg)
        self.caseCheckBox.setObjectName("caseCheckBox")
        self.vboxlayout1.addWidget(self.caseCheckBox)
        self.wholeCheckBox = QtGui.QCheckBox(FindAndReplaceDlg)
        self.wholeCheckBox.setChecked(True)
        self.wholeCheckBox.setObjectName("wholeCheckBox")
        self.vboxlayout1.addWidget(self.wholeCheckBox)
        self.vboxlayout.addLayout(self.vboxlayout1)
        spacerItem = QtGui.QSpacerItem(231, 16, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem)
        self.moreFrame = QtGui.QFrame(FindAndReplaceDlg)
        self.moreFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.moreFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.moreFrame.setObjectName("moreFrame")
        self.vboxlayout2 = QtGui.QVBoxLayout(self.moreFrame)
        self.vboxlayout2.setMargin(9)
        self.vboxlayout2.setSpacing(6)
        self.vboxlayout2.setObjectName("vboxlayout2")
        self.backwardsCheckBox = QtGui.QCheckBox(self.moreFrame)
        self.backwardsCheckBox.setObjectName("backwardsCheckBox")
        self.vboxlayout2.addWidget(self.backwardsCheckBox)
        self.regexCheckBox = QtGui.QCheckBox(self.moreFrame)
        self.regexCheckBox.setObjectName("regexCheckBox")
        self.vboxlayout2.addWidget(self.regexCheckBox)
        self.ignoreNotesCheckBox = QtGui.QCheckBox(self.moreFrame)
        self.ignoreNotesCheckBox.setObjectName("ignoreNotesCheckBox")
        self.vboxlayout2.addWidget(self.ignoreNotesCheckBox)
        self.vboxlayout.addWidget(self.moreFrame)
        self.hboxlayout.addLayout(self.vboxlayout)
        self.line = QtGui.QFrame(FindAndReplaceDlg)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.hboxlayout.addWidget(self.line)
        self.vboxlayout3 = QtGui.QVBoxLayout()
        self.vboxlayout3.setMargin(0)
        self.vboxlayout3.setSpacing(6)
        self.vboxlayout3.setObjectName("vboxlayout3")
        self.findButton = QtGui.QPushButton(FindAndReplaceDlg)
        self.findButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.findButton.setObjectName("findButton")
        self.vboxlayout3.addWidget(self.findButton)
        self.replaceButton = QtGui.QPushButton(FindAndReplaceDlg)
        self.replaceButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.replaceButton.setObjectName("replaceButton")
        self.vboxlayout3.addWidget(self.replaceButton)
        self.closeButton = QtGui.QPushButton(FindAndReplaceDlg)
        self.closeButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.closeButton.setObjectName("closeButton")
        self.vboxlayout3.addWidget(self.closeButton)
        self.moreButton = QtGui.QPushButton(FindAndReplaceDlg)
        self.moreButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.moreButton.setCheckable(True)
        self.moreButton.setObjectName("moreButton")
        self.vboxlayout3.addWidget(self.moreButton)
        spacerItem1 = QtGui.QSpacerItem(21, 16, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vboxlayout3.addItem(spacerItem1)
        self.hboxlayout.addLayout(self.vboxlayout3)
        self.label_2.setBuddy(self.replaceLineEdit)
        self.label.setBuddy(self.findLineEdit)

        self.retranslateUi(FindAndReplaceDlg)
        QtCore.QObject.connect(self.closeButton, QtCore.SIGNAL("clicked()"), FindAndReplaceDlg.reject)
        QtCore.QObject.connect(self.moreButton, QtCore.SIGNAL("toggled(bool)"), self.moreFrame.setVisible)
        QtCore.QMetaObject.connectSlotsByName(FindAndReplaceDlg)
        FindAndReplaceDlg.setTabOrder(self.findLineEdit, self.replaceLineEdit)
        FindAndReplaceDlg.setTabOrder(self.replaceLineEdit, self.caseCheckBox)
        FindAndReplaceDlg.setTabOrder(self.caseCheckBox, self.wholeCheckBox)
        FindAndReplaceDlg.setTabOrder(self.wholeCheckBox, self.backwardsCheckBox)
        FindAndReplaceDlg.setTabOrder(self.backwardsCheckBox, self.regexCheckBox)
        FindAndReplaceDlg.setTabOrder(self.regexCheckBox, self.ignoreNotesCheckBox)

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
        self.backwardsCheckBox.setText(QtGui.QApplication.translate("FindAndReplaceDlg", "Search &Backwards", None,
                                                                    QtGui.QApplication.UnicodeUTF8))
        self.regexCheckBox.setText(QtGui.QApplication.translate("FindAndReplaceDlg", "Regular E&xpression", None,
                                                                QtGui.QApplication.UnicodeUTF8))
        self.ignoreNotesCheckBox.setText(
            QtGui.QApplication.translate("FindAndReplaceDlg", "Ignore foot&notes and endnotes", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.findButton.setText(
            QtGui.QApplication.translate("FindAndReplaceDlg", "&Find", None, QtGui.QApplication.UnicodeUTF8))
        self.replaceButton.setText(
            QtGui.QApplication.translate("FindAndReplaceDlg", "&Replace", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setText(
            QtGui.QApplication.translate("FindAndReplaceDlg", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.moreButton.setText(
            QtGui.QApplication.translate("FindAndReplaceDlg", "&More", None, QtGui.QApplication.UnicodeUTF8))

