# -*- coding: utf-8 -*- 

"""
A simple Desktop UI for rendering TeX

Author: Hajime Mihara (hajimemihara1108@gmail.com)
"""

import sys
import os
import datetime
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
        self.output_type = 'png'
        self.cache_image_name = None
        self.tmp_file_name = None
        self.tmpstring = None
        self.cache_dir = './cache/'
        self.input_tex_string = None

        # initialize UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.textEdit.setText(self.input_string)
        self.ui.renderingArea.setAlignment(QtCore.Qt.AlignCenter)

        # behaviors
        self.ui.renderButton.pressed.connect(self.renderButtonPressed)

    def renderButtonPressed(self):
        self.setTmpstring()

        self.getAndShowEquationImage()
        self.saveTexStringToCache()

    def setTmpstring(self):
        now = datetime.datetime.today()
        y = now.year
        m = now.month
        d = now.day
        h = now.hour
        m = now.minute
        s = now.second
        self.tmpstring = '{}_{}_{}_{}_{}_{}'.format(y, m, d, h, m, s)

    def saveTexStringToCache(self):
        cache_dir = self.cache_dir
        out_text_file_name = os.path.join(cache_dir, '{}.txt'.format(self.tmpstring))
        with open(out_text_file_name, 'w') as f:
            f.write(self.input_tex_string)

    def getAndShowEquationImage(self):
        self.input_tex_string = self.ui.textEdit.toPlainText()
        cache_image_name = self.getEqImageFromCodecogs(self.input_tex_string)
        q_pixmap = QtGui.QPixmap(cache_image_name)
        self.ui.renderingArea.setPixmap(q_pixmap)

    def getEqImageFromCodecogs(self, input_tex_string):
        ''' 
        get image from online api : http://latex.codecogs.com/
        reference: http://shogo82148.github.io/homepage/memo/soft/tex/web.html
        '''
        s = urllib.parse.quote(input_tex_string)
        url = r'http://latex.codecogs.com/' + self.output_type + r'.latex?' + s
        #url = r'http://chart.apis.google.com/chart?cht=tx&chs=3460&chl=' + s

        cache_image_name = os.path.join(self.cache_dir, '{}.{}'.format(self.tmpstring, self.output_type))
        urllib.request.urlretrieve(url, cache_image_name)
        return cache_image_name

    def setEqImageToQPixmap(self):
        if os.path.exists(self.save_name):
            self.q_pixmap = QtGui.Qpixmap(self.save_name)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = RunGUI()
    window.show()
    sys.exit(app.exec_())
