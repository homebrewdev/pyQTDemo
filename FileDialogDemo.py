#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication, QFileDialog
# from PyQt5.Qt import QColor


class FileDialogWindow(QMainWindow):
    def __init__(self):
        super(FileDialogWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)
        self.statusBar()

        open_file = QAction("open", self)
        open_file.setShortcut("Ctrl+O")
        open_file.setStatusTip("Open new File")
        open_file.triggered.connect(self.showFileDialog)

        menubar = self.menuBar()
        file_menu = menubar.addMenu("&File")
        file_menu.addAction(open_file)

        self.setGeometry(200, 200, 640, 480)
        self.setWindowTitle("File dialog")
        self.show()

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
    ex = FileDialogWindow()
    sys.exit(app.exec_())