#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication, QInputDialog, QFileDialog
from PyQt5.QtGui import QIcon


class QtDemo(QMainWindow):

    def __init__(self):
        super(QtDemo, self).__init__()
        self.initUI()

    def initUI(self):

        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)

        # exit icon set action
        exit_action = QAction(QIcon('logout.png'), 'Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit application')
        exit_action.triggered.connect(self.close)

        # enter icon set action
        enter_action = QAction(QIcon("enter.png"), "Enter", self)
        enter_action.setShortcut("Ctrl+E")
        enter_action.setStatusTip("Enter to your account")
        enter_action.triggered.connect(self.show_enter_dlg)

        self.statusBar()

        open_file = QAction("open", self)
        open_file.setShortcut("Ctrl+O")
        open_file.setStatusTip("Open new File")
        open_file.triggered.connect(self.showFileDialog)

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("&File")
        file_menu.addAction(open_file)

        # toolbar actions
        toolbar = self.addToolBar("Enter")
        toolbar.addAction(enter_action)
        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exit_action)

        # set main window
        x_pos = 100
        y_pos = 100
        width = 640
        height = 480

        self.setGeometry(x_pos, y_pos, width, height)
        self.setWindowTitle('Main window PyQT5 Demo')
        self.show()

    def show_enter_dlg(self):
        text, ok = QInputDialog.getText(self, 'Login', 'Enter your login:')

        if ok:
            prev_text = self.text_edit.toPlainText()
            if str(text) != "":
                login = str(text)
                self.text_edit.setText("%s\n%s" % (prev_text, login))

    def showFileDialog(self):
        file_name = QFileDialog.getOpenFileName(self, "Open file", "/")

        if file_name[0]:
            f = open(file_name[0], "r")

            with f:
                data = f.read()
                self.text_edit.setStyleSheet("QTextEdit {color:green}")
                self.text_edit.setText(data)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = QtDemo()
    sys.exit(app.exec_())
