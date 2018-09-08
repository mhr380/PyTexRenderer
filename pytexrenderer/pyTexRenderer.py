# -*- coding: utf-8 -*- 

"""
A simple Desktop UI for rendering TeX

Author: Hajime Mihara (hajimemihara1108@gmail.com)
"""

import sys
import os

import urllib.parse
import urllib.request

from PyQt5 import QtCore, QtGui, QtWidgets

from gui import Ui_MainWindow

class RunGUI(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(RunGUI, self).__init__(parent)

        # initialize member variables
        self.input_string = r'f(t) = A e^{j2\pi ft}'
        self.q_pixmap = None
        # self.fontsize = 20
        self.output_name = 'out'
        self.output_type = 'png'
        self.tmp_file_name = None

        # initialize UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.textEdit.setText(self.input_string)
        self.getAndShowEquationImage()

        self.ui.renderButton.pressed.connect(self.getAndShowEquationImage)

    def getAndShowEquationImage(self):
        self.input_string = self.ui.textEdit.toPlainText()
        self.tmp_file_name = self.getEqImageFromCodecogs()
        self.q_pixmap = QtGui.QPixmap(self.tmp_file_name)
        self.ui.renderingArea.setPixmap(self.q_pixmap)

    def getEqImageFromCodecogs(self):
        ''' 
        get image from online api : http://latex.codecogs.com/
        reference: http://shogo82148.github.io/homepage/memo/soft/tex/web.html
        '''
        s = urllib.parse.quote(self.input_string)
        url = r'http://latex.codecogs.com/' + self.output_type + r'.latex?' + s
        #url = r'http://chart.apis.google.com/chart?cht=tx&chs=3460&chl=' + s

        tmp_file_name = '{}.{}'.format(self.output_name, self.output_type)
        urllib.request.urlretrieve(url, tmp_file_name)
        return tmp_file_name

    def setEqImageToQPixmap(self):
        if os.path.exists(self.save_name):
            self.q_pixmap = QtGui.Qpixmap(self.save_name)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = RunGUI()
    window.show()
    sys.exit(app.exec_())
