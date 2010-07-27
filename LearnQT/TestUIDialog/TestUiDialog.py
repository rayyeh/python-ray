from PyQt4.QtCore import *
from PyQt4.QtGui import *

from ui_Dialog import Ui_dialog
class TestUiDialog(QDialog,Ui_dialog):
    def __init__(self):
        super(TestUiDialog,self).__init__()
        self.setupUi(self)

    def accept(self):
        QMessageBox.about(self,"Hi","Hello Come to the World")

    
if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    form=TestUiDialog()
    form.show()
    app.exec_()
    
