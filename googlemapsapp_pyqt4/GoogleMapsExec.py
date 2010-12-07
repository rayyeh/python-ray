# -*- coding: utf-8 -*-

"""
Module implementing GoogleMapsExec.
"""
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature

from Ui_GoogleMaps import Ui_DialogGoogleMaps

import GoogleMapsUtil

class GoogleMapsExec(QDialog, Ui_DialogGoogleMaps):
    """
    Class documentation goes here.
    """
    jindu = 32.058365
    weidu = 118.796468
    zoom = 14
    def __init__(self, parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
    
    @pyqtSignature("")
    def on_ButtonUp_clicked(self):
        """
        Slot documentation goes here.
        """
        self.jindu =self.jindu-0.01
        GmapUrl = GoogleMapsUtil.getGMapsStaticUrl(self.jindu, self.weidu, self.zoom)
        self.MapView.setUrl(QtCore.QUrl(GmapUrl))
    
    @pyqtSignature("")
    def on_ButtonDown_clicked(self):
        """
        Slot documentation goes here.
        """
        self.jindu = self.jindu+0.01
        GmapUrl = GoogleMapsUtil.getGMapsStaticUrl(self.jindu, self.weidu, self.zoom)
        self.MapView.setUrl(QtCore.QUrl(GmapUrl))
    
    @pyqtSignature("")
    def on_ButtonLeft_clicked(self):
        """
        Slot documentation goes here.
        """
        self.weidu = self.weidu-0.01
        GmapUrl = GoogleMapsUtil.getGMapsStaticUrl(self.jindu, self.weidu, self.zoom)
        self.MapView.setUrl(QtCore.QUrl(GmapUrl))
    
    @pyqtSignature("")
    def on_ButtonRight_clicked(self):
        """
        Slot documentation goes here.
        """
        self.weidu = self.weidu+0.01
        GmapUrl = GoogleMapsUtil.getGMapsStaticUrl(self.jindu, self.weidu, self.zoom)
        self.MapView.setUrl(QtCore.QUrl(GmapUrl))
    
    @pyqtSignature("")
    def on_ButtonZoom_clicked(self):
        """
        Slot documentation goes here.
        """
        if self.zoom < 18:
             self.zoom = self.zoom+1
        else:
            return 
        GmapUrl = GoogleMapsUtil.getGMapsStaticUrl(self.jindu, self.weidu, self.zoom)
        self.MapView.setUrl(QtCore.QUrl(GmapUrl))
    
    @pyqtSignature("")
    def on_ButtonNarrow_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        if self.zoom > 0:
             self.zoom = self.zoom-1
        else:
            return
        GmapUrl = GoogleMapsUtil.getGMapsStaticUrl(self.jindu, self.weidu, self.zoom)
        self.MapView.setUrl(QtCore.QUrl(GmapUrl))
    
    @pyqtSignature("")
    def on_BtnSearch_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        qaddr = self.inputAddress.text().toUtf8()
        center = GoogleMapsUtil.getGMapsGEO(qaddr)
        self.jindu = float(center[2])
        self.weidu = float(center[3])
        self.zoom = 14
        GmapUrl = GoogleMapsUtil.getGMapsStaticUrl(self.jindu, self.weidu, self.zoom)
        self.MapView.setUrl(QtCore.QUrl(GmapUrl))
        #QtGui.QListWidgetItem(self.ListAddress)
        #self.ListAddress.item(2).setText(QtGui.QApplication.translate("DialogGoogleMaps", "结果3", None, QtGui.QApplication.UnicodeUTF8))
    
    @pyqtSignature("QListWidgetItem*")
    def on_ListAddress_itemClicked(self, item):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        pass
    
    @pyqtSignature("")
    def on_ListAddress_itemSelectionChanged(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        pass


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DialogGoogleMaps = GoogleMapsExec()
    DialogGoogleMaps.show()
    sys.exit(app.exec_())
