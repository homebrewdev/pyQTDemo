#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QCheckBox, QApplication, QToolBar, QComboBox, QPushButton, QDockWidget


class RainbowWindow(QMainWindow):
    def __init__(self):
        super(RainbowWindow, self).__init__()
        self.initUI()

    def initUI(self):
            self.setStyleSheet(
            "QCheckBox { background: palette(window); border-radius: 4px; padding: 2px; margin-right: 2px; }"
            )

            self.toolBar = QToolBar(self)
            # self.toolBar.setStyleSheet(stylesheet % (create_gradient("pastel"),))
            self.toolBar.setMovable(False)
            # self.toolBar.setContextMenuPolicy(Qt.CustomContextMenu)
            self.addToolBar(self.toolBar)

            self.reverseBox = QCheckBox("&Reverse", self)
            self.reverseBox.clicked.connect(lambda: self.updateGradient())
            self.toolBar.addWidget(self.reverseBox)

            self.byWordBox = QCheckBox("By &word", self)
            self.toolBar.addWidget(self.byWordBox)

            self.bounceBox = QCheckBox("&Bounce", self)
            self.bounceBox.clicked.connect(lambda: self.updateGradient())
            self.toolBar.addWidget(self.bounceBox)

            self.sizeList = QComboBox(self)
            self.sizeList.addItem("None")
            for num in range(1, 8):
                self.sizeList.addItem(str(num))
                self.toolBar.addWidget(self.sizeList)

            self.cycleList = QComboBox(self)
            self.toolBar.addWidget(self.cycleList)
            # self.cycleList.currentIndexChanged.connect(self.updateGradient)
            # self.loadCycles()

            self.convertButton = QPushButton("&Convert", self)
            # self.convertButton.clicked.connect(self.convert)
            self.toolBar.addWidget(self.convertButton)

            self.reloadButton = QPushButton("Reload", self)
            self.reloadButton.setShortcut("Alt+Shift+R")
            # self.reloadButton.clicked.connect(self.loadCycles)
            # self.toolBar.addWidget(self.reloadButton)

            self.inputDock = QDockWidget("Input", self)
            self.inputDock.setFeatures(QDockWidget.NoDockWidgetFeatures)
            # self.inputDock.setContextMenuPolicy(Qt.CustomContextMenu)
            # self.addDockWidget(Qt.LeftDockWidgetArea, self.inputDock)

            self.inputField = QTextEdit(self)
            self.inputField.setAcceptRichText(False)
            self.inputDock.setWidget(self.inputField)

            self.outputField = QTextEdit(self)
            self.outputField.setReadOnly(True)
            self.setCentralWidget(self.outputField)

            # set main window
            self.setGeometry(200, 200, 640, 480)
            self.setWindowTitle('Main window PyQT5 Demo')
            self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = RainbowWindow()
    sys.exit(app.exec_())