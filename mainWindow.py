from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import sys
class MainWindow(QMainWindow):
     
    def __init__(self):
       QMainWindow.__init__(self)
       QtextEdit = QTextEdit(self)
       self.setCentralWidget(QtextEdit );
       bar = self.menuBar() 
       fileMenu = bar.addMenu("File")
       newAct = QAction(QIcon("new.png"), "New", self )
       newAct.setToolTip(self.tr("New File"))
       newAct.setStatusTip(self.tr("New file"))
       fileMenu.addAction(newAct)
       newAct.triggered.connect( self.newFile )
       openAct = QAction(QIcon("open.png"), "open", self )
       openAct.setToolTip(self.tr("open"))
       openAct.setStatusTip(self.tr("open"))
       fileMenu.addAction(openAct)
       openAct.triggered.connect( self.openFile)
       saveAct = QAction(QIcon("save.png"), "save", self )
       saveAct.setToolTip(self.tr("save"))
       saveAct.setStatusTip(self.tr("save"))
       fileMenu.addAction(saveAct)
       saveAct.triggered.connect( self.saveFile )
       copyAct = QAction(QIcon("copy.png"), "copy", self )
       copyAct.setToolTip(self.tr("copy"))
       copyAct.setStatusTip(self.tr("copy"))
       fileMenu.addAction(copyAct)
       copyAct.triggered.connect( self.copyFile )
       quitAct = QAction(QIcon("quit.png"), "quit", self )
       quitAct.setToolTip(self.tr("quit"))
       quitAct.setStatusTip(self.tr("quit"))
       fileMenu.addAction(quitAct)
       quitAct.triggered.connect( self.quitFile)   
    def newFile():
        print("new")
    def openFile():
        print("open")    
    def saveFile():
        print("save")    
    def copyFile():
        print("copy")
    def quitFile():
        print("quit")
        
    
     
def main(args):
    app = QApplication(args)
    win = MainWindow()
    win.resize(400,500)
    win.show()
    app.exec()
   
    
if __name__ == "__main__":
        main(sys.argv)
        
        
    