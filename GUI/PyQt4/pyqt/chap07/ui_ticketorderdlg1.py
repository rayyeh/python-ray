# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\python-ray\PyQt4\pyqt\chap07\ticketorderdlg1.ui'
#
# Created: Sun Sep 20 22:51:52 2009
# by: PyQt4 UI code generator 4.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui


class Ui_TicketOrderDlg(object):
    def setupUi(self, TicketOrderDlg):
        TicketOrderDlg.setObjectName("TicketOrderDlg")
        TicketOrderDlg.resize(379, 140)
        self.gridlayout = QtGui.QGridLayout(TicketOrderDlg)
        self.gridlayout.setMargin(9)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")
        self.buttonBox = QtGui.QDialogButtonBox(TicketOrderDlg)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QtGui.QDialogButtonBox.Cancel | QtGui.QDialogButtonBox.NoButton | QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridlayout.addWidget(self.buttonBox, 4, 0, 1, 6)
        spacerItem = QtGui.QSpacerItem(361, 16, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridlayout.addItem(spacerItem, 3, 0, 1, 6)
        self.amountLabel = QtGui.QLabel(TicketOrderDlg)
        self.amountLabel.setFrameShape(QtGui.QFrame.StyledPanel)
        self.amountLabel.setFrameShadow(QtGui.QFrame.Sunken)
        self.amountLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.amountLabel.setObjectName("amountLabel")
        self.gridlayout.addWidget(self.amountLabel, 2, 5, 1, 1)
        self.label_4 = QtGui.QLabel(TicketOrderDlg)
        self.label_4.setObjectName("label_4")
        self.gridlayout.addWidget(self.label_4, 2, 2, 1, 1)
        self.label_3 = QtGui.QLabel(TicketOrderDlg)
        self.label_3.setObjectName("label_3")
        self.gridlayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_5 = QtGui.QLabel(TicketOrderDlg)
        self.label_5.setObjectName("label_5")
        self.gridlayout.addWidget(self.label_5, 2, 4, 1, 1)
        self.priceSpinBox = QtGui.QDoubleSpinBox(TicketOrderDlg)
        self.priceSpinBox.setAlignment(QtCore.Qt.AlignRight)
        self.priceSpinBox.setMaximum(5000.0)
        self.priceSpinBox.setObjectName("priceSpinBox")
        self.gridlayout.addWidget(self.priceSpinBox, 2, 1, 1, 1)
        self.quantitySpinBox = QtGui.QSpinBox(TicketOrderDlg)
        self.quantitySpinBox.setAlignment(QtCore.Qt.AlignRight)
        self.quantitySpinBox.setMaximum(50)
        self.quantitySpinBox.setMinimum(1)
        self.quantitySpinBox.setProperty("value", QtCore.QVariant(1))
        self.quantitySpinBox.setObjectName("quantitySpinBox")
        self.gridlayout.addWidget(self.quantitySpinBox, 2, 3, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(81, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem1, 1, 4, 1, 2)
        self.label_2 = QtGui.QLabel(TicketOrderDlg)
        self.label_2.setObjectName("label_2")
        self.gridlayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.whenDateTimeEdit = QtGui.QDateTimeEdit(TicketOrderDlg)
        self.whenDateTimeEdit.setObjectName("whenDateTimeEdit")
        self.gridlayout.addWidget(self.whenDateTimeEdit, 1, 1, 1, 2)
        self.customerLineEdit = QtGui.QLineEdit(TicketOrderDlg)
        self.customerLineEdit.setObjectName("customerLineEdit")
        self.gridlayout.addWidget(self.customerLineEdit, 0, 1, 1, 5)
        self.label = QtGui.QLabel(TicketOrderDlg)
        self.label.setObjectName("label")
        self.gridlayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_4.setBuddy(self.quantitySpinBox)
        self.label_3.setBuddy(self.priceSpinBox)
        self.label_2.setBuddy(self.whenDateTimeEdit)
        self.label.setBuddy(self.customerLineEdit)

        self.retranslateUi(TicketOrderDlg)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), TicketOrderDlg.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), TicketOrderDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(TicketOrderDlg)
        TicketOrderDlg.setTabOrder(self.customerLineEdit, self.whenDateTimeEdit)
        TicketOrderDlg.setTabOrder(self.whenDateTimeEdit, self.priceSpinBox)
        TicketOrderDlg.setTabOrder(self.priceSpinBox, self.quantitySpinBox)
        TicketOrderDlg.setTabOrder(self.quantitySpinBox, self.buttonBox)

    def retranslateUi(self, TicketOrderDlg):
        TicketOrderDlg.setWindowTitle(
            QtGui.QApplication.translate("TicketOrderDlg", "Ticket Order #1", None, QtGui.QApplication.UnicodeUTF8))
        self.amountLabel.setText(
            QtGui.QApplication.translate("TicketOrderDlg", "$", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(
            QtGui.QApplication.translate("TicketOrderDlg", "&Quantity:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(
            QtGui.QApplication.translate("TicketOrderDlg", "&Price:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(
            QtGui.QApplication.translate("TicketOrderDlg", "Amount", None, QtGui.QApplication.UnicodeUTF8))
        self.priceSpinBox.setPrefix(
            QtGui.QApplication.translate("TicketOrderDlg", "$ ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(
            QtGui.QApplication.translate("TicketOrderDlg", "&When:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(
            QtGui.QApplication.translate("TicketOrderDlg", "&Customer:", None, QtGui.QApplication.UnicodeUTF8))

