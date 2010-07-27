#This script is for py2exe module 
#It generate execute file.
#Usage : python setup.py py2exe


from distutils.core import setup
import py2exe
setup(windows=[{"script" : "d:/base64gui/py2exe/findandreplacedlg.py"}], options={"py2exe" : {"includes" : ["sip", "PyQt4"]}})