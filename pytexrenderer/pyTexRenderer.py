# -*- coding: utf-8 -*- 

"""
A simple Desktop UI for rendering TeX

Author: Hajime Mihara (hajimemihara1108@gmail.com)
"""

import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets

from gui import Ui_MainWindow

class RunGUI(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(RunGUI, self).__init__(parent)
        # initialize UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = RunGUI()
    window.show()
    sys.exit(app.exec_())
