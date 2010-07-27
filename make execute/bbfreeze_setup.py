#This script is for bbfreeze 
#It generate execute file.
#Usage : python setup.py

from bbfreeze import Freezer
f = Freezer("Base64gui-1.0")
f.addScript("base64gui.py",gui_only=True)
f()    # starts the freezing process