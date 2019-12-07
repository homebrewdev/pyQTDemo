#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QGridLayout, QApplication
from PyQt5.Qt import QFont, QSizePolicy, QLabel
# from PyQt5.QtCore import QFile, QIODevice


class AboutWindow(QMainWindow):
    def __init__(self):
        super(AboutWindow, self).__init__()
        self.initUI()

    def initUI(self):

        gridlayout = QGridLayout(self)
        title_font = QFont()
        title_font.setPointSize(24)
        policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        label = QLabel("About Screen", self)
        label.setFont(title_font)
        label.setSizePolicy(policy)
        gridlayout.addWidget(label, 0, 0)
        label_copyright = QLabel("\u00a9 2015 Fredrick Brennan <admin@8chan.co>")
        label_copyright.setSizePolicy(policy)
        gridlayout.addWidget(label_copyright, 1, 0)
        labeldesc = (
                "<p>QKeysOnScreen is a simple application intended for "
                + "presentations, video tutorials, and any other case where"
                + " you'd want to display the current state of the keyboard"
                + ' on the screen. For more information see our <a href="'
                + 'https://github.com/ctrlcctrlv/QKeysOnScreen">Github</a>'
                + " project."
        )
        qlabeldesc = QLabel(labeldesc)
        qlabeldesc.setWordWrap(True)
        gridlayout.addWidget(qlabeldesc, 2, 0)

        from PyQt5.QtCore import QT_VERSION_STR
        from PyQt5.Qt import PYQT_VERSION_STR
        import platform

        pyversion = ".".join([str(o) for o in sys.version_info])
        uname_result = platform.uname()
        uname = "{} {}".format(uname_result.system, uname_result.release)
        labelversions = (
                "<strong>Versions:</strong><br>Qt: {0}<br>PyQt: {1}" + "<br>Python: {2}<br>OS: {3}<br>QKeysOnScreen: 0.0.1"
        ).format(QT_VERSION_STR, PYQT_VERSION_STR, platform.python_version(), uname, platform.machine())
        qlabelversions = QLabel(labelversions)
        qlabelversions.setStyleSheet("border: 1px solid green")
        gridlayout.addWidget(qlabelversions, 0, 1)

        # self.kb = self.get_keyboard_path()
        # self.mouse = self.get_mouse_path()
        self.infoqlabel = QLabel(
            "<strong>Devices:</strong><br>" + "Our mouse is {0}<br/>Our keyboard is {1}".format("self.mouse", "self.kb"),
            self,
            )
        self.infoqlabel.setStyleSheet("border: 1px solid green")
        gridlayout.addWidget(self.infoqlabel, 2, 1)

        qte = QTextEdit(self)
        qte.setReadOnly(True)
        """qfile = QFile(":/LICENSE")
        qfile.open(QIODevice.ReadOnly)
        qte.setPlainText(bytes(qfile.readAll()).decode("utf-8"))
        qfile.close()"""


        # self.setLayout(gridlayout)

        # set main geometry
        self.setGeometry(200, 200, 640, 480)
        self.setWindowTitle("About window")
        self.show()
        gridlayout.addWidget(qte, 3, 0, 1, 2)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = AboutWindow()
    sys.exit(app.exec_())