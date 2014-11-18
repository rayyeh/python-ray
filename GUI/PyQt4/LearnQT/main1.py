import os
import platform
import sys
from PyQt4.QtCore import (PYQT_VERSION_STR, QFile, QFileInfo, QSettings,
                          QString, QT_VERSION_STR, QTimer, QVariant, Qt, SIGNAL)
from PyQt4.QtGui import (QAction, QActionGroup, QApplication,
                         QDockWidget, QFileDialog, QFrame, QIcon, QImage, QImageReader,
                         QImageWriter, QInputDialog, QKeySequence, QLabel, QListWidget,
                         QMainWindow, QMessageBox, QPainter, QPixmap, QPrintDialog,
                         QPrinter, QSpinBox)


class Main1(QMainWindow):
    def __init__(self, parent=None):
        super(Main1, self).__init__(parent)
        self.image = QImage()
        self.dirty = False
        self.filename = None
        self.mirroredvertically = False
        self.mirroredhorizontally = False

        self.imageLabel = QLabel()
        self.imageLabel.setMinimumSize(200, 200)
        self.imageLabel.setAlignment(Qt.AlignCenter)
        self.imageLabel.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.setCentralWidget(self.imageLabel)

        # Create Status Bar
        self.sizeLabel = QLabel()
        self.sizeLabel.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)
        status = self.statusBar()
        status.setSizeGripEnabled(False)
        status.addPermanentWidget(self.sizeLabel)
        status.showMessage("Ready", 5000)


def main():
    app = QApplication(sys.argv)
    app.setOrganizationName("Qtrac Ltd.")
    app.setOrganizationDomain("qtrac.eu")
    app.setApplicationName("Image Changer")
    form = Main1()
    form.show()
    app.exec_()


main()