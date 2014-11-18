import sys

from PyQt4.QtGui import QApplication

from dip.ui import Form
from dip.ui.toolkits.qt import QtToolkit


# Every PyQt GUI application needs a QApplication.
app = QApplication(sys.argv)

# We need a toolkit to create the widgets.
toolkit = QtToolkit()

# Create the model.
model = dict(name='')

# Define the view.
view = Form()

# Create an instance of the view for the model.
ui = view(model, toolkit, widget=True)

# Make the instance of the view visible.
ui.show()

# Enter the event loop.
# app.exec()

# Show the value of the model.
#print("Name:", model['name'])
