# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(966, 882)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/ecg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.gainSlider_1 = QtWidgets.QSlider(self.centralwidget)
        self.gainSlider_1.setEnabled(False)
        self.gainSlider_1.setMaximum(50)
        self.gainSlider_1.setSingleStep(1)
        self.gainSlider_1.setProperty("value", 10)
        self.gainSlider_1.setOrientation(QtCore.Qt.Vertical)
        self.gainSlider_1.setObjectName("gainSlider_1")
        self.horizontalLayout_5.addWidget(self.gainSlider_1)
        spacerItem = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.gainSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.gainSlider_2.setEnabled(False)
        self.gainSlider_2.setMaximum(50)
        self.gainSlider_2.setProperty("value", 10)
        self.gainSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.gainSlider_2.setObjectName("gainSlider_2")
        self.horizontalLayout_5.addWidget(self.gainSlider_2)
        spacerItem1 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.gainSlider_3 = QtWidgets.QSlider(self.centralwidget)
        self.gainSlider_3.setEnabled(False)
        self.gainSlider_3.setMaximum(50)
        self.gainSlider_3.setProperty("value", 10)
        self.gainSlider_3.setOrientation(QtCore.Qt.Vertical)
        self.gainSlider_3.setObjectName("gainSlider_3")
        self.horizontalLayout_5.addWidget(self.gainSlider_3)
        spacerItem2 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.gainSlider_4 = QtWidgets.QSlider(self.centralwidget)
        self.gainSlider_4.setEnabled(False)
        self.gainSlider_4.setMaximum(50)
        self.gainSlider_4.setProperty("value", 10)
        self.gainSlider_4.setOrientation(QtCore.Qt.Vertical)
        self.gainSlider_4.setObjectName("gainSlider_4")
        self.horizontalLayout_5.addWidget(self.gainSlider_4)
        spacerItem3 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.gainSlider_5 = QtWidgets.QSlider(self.centralwidget)
        self.gainSlider_5.setEnabled(False)
        self.gainSlider_5.setMaximum(50)
        self.gainSlider_5.setProperty("value", 10)
        self.gainSlider_5.setOrientation(QtCore.Qt.Vertical)
        self.gainSlider_5.setObjectName("gainSlider_5")
        self.horizontalLayout_5.addWidget(self.gainSlider_5)
        spacerItem4 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.gainSlider_6 = QtWidgets.QSlider(self.centralwidget)
        self.gainSlider_6.setEnabled(False)
        self.gainSlider_6.setMaximum(50)
        self.gainSlider_6.setProperty("value", 10)
        self.gainSlider_6.setOrientation(QtCore.Qt.Vertical)
        self.gainSlider_6.setObjectName("gainSlider_6")
        self.horizontalLayout_5.addWidget(self.gainSlider_6)
        spacerItem5 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.gainSlider_7 = QtWidgets.QSlider(self.centralwidget)
        self.gainSlider_7.setEnabled(False)
        self.gainSlider_7.setMaximum(50)
        self.gainSlider_7.setProperty("value", 10)
        self.gainSlider_7.setOrientation(QtCore.Qt.Vertical)
        self.gainSlider_7.setObjectName("gainSlider_7")
        self.horizontalLayout_5.addWidget(self.gainSlider_7)
        spacerItem6 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.gainSlider_8 = QtWidgets.QSlider(self.centralwidget)
        self.gainSlider_8.setEnabled(False)
        self.gainSlider_8.setMaximum(50)
        self.gainSlider_8.setProperty("value", 10)
        self.gainSlider_8.setOrientation(QtCore.Qt.Vertical)
        self.gainSlider_8.setObjectName("gainSlider_8")
        self.horizontalLayout_5.addWidget(self.gainSlider_8)
        spacerItem7 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.gainSlider_9 = QtWidgets.QSlider(self.centralwidget)
        self.gainSlider_9.setEnabled(False)
        self.gainSlider_9.setMaximum(50)
        self.gainSlider_9.setProperty("value", 10)
        self.gainSlider_9.setOrientation(QtCore.Qt.Vertical)
        self.gainSlider_9.setObjectName("gainSlider_9")
        self.horizontalLayout_5.addWidget(self.gainSlider_9)
        spacerItem8 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem8)
        self.gainSlider_10 = QtWidgets.QSlider(self.centralwidget)
        self.gainSlider_10.setEnabled(False)
        self.gainSlider_10.setMaximum(50)
        self.gainSlider_10.setProperty("value", 10)
        self.gainSlider_10.setOrientation(QtCore.Qt.Vertical)
        self.gainSlider_10.setObjectName("gainSlider_10")
        self.horizontalLayout_5.addWidget(self.gainSlider_10)
        spacerItem9 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem9)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.spectro_maximum_slider = QtWidgets.QSlider(self.centralwidget)
        self.spectro_maximum_slider.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spectro_maximum_slider.sizePolicy().hasHeightForWidth())
        self.spectro_maximum_slider.setSizePolicy(sizePolicy)
        self.spectro_maximum_slider.setMaximum(100)
        self.spectro_maximum_slider.setProperty("value", 100)
        self.spectro_maximum_slider.setOrientation(QtCore.Qt.Horizontal)
        self.spectro_maximum_slider.setObjectName("spectro_maximum_slider")
        self.verticalLayout_3.addWidget(self.spectro_maximum_slider)
        self.spectro_minimum_slider = QtWidgets.QSlider(self.centralwidget)
        self.spectro_minimum_slider.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spectro_minimum_slider.sizePolicy().hasHeightForWidth())
        self.spectro_minimum_slider.setSizePolicy(sizePolicy)
        self.spectro_minimum_slider.setMaximum(100)
        self.spectro_minimum_slider.setOrientation(QtCore.Qt.Horizontal)
        self.spectro_minimum_slider.setObjectName("spectro_minimum_slider")
        self.verticalLayout_3.addWidget(self.spectro_minimum_slider)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.gridLayout.addLayout(self.verticalLayout_6, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setEnabled(True)
        self.tab.setObjectName("tab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_before1 = PlotWidget(self.tab)
        self.widget_before1.setObjectName("widget_before1")
        self.verticalLayout.addWidget(self.widget_before1)
        self.widget_after1 = PlotWidget(self.tab)
        self.widget_after1.setObjectName("widget_after1")
        self.verticalLayout.addWidget(self.widget_after1)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_1s = PlotWidget(self.tab)
        self.widget_1s.setObjectName("widget_1s")
        self.verticalLayout_2.addWidget(self.widget_1s)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.gridLayout_4.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        spacerItem10 = QtWidgets.QSpacerItem(1, 600, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.horizontalLayout.addItem(spacerItem10)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 966, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuColor_palette = QtWidgets.QMenu(self.menubar)
        self.menuColor_palette.setObjectName("menuColor_palette")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon1)
        self.actionOpen.setObjectName("actionOpen")
        self.actionToolbar = QtWidgets.QAction(MainWindow)
        self.actionToolbar.setCheckable(True)
        self.actionToolbar.setChecked(True)
        self.actionToolbar.setObjectName("actionToolbar")
        self.actionStatus_bar = QtWidgets.QAction(MainWindow)
        self.actionStatus_bar.setCheckable(True)
        self.actionStatus_bar.setChecked(True)
        self.actionStatus_bar.setObjectName("actionStatus_bar")
        self.actionZoom_in = QtWidgets.QAction(MainWindow)
        self.actionZoom_in.setEnabled(False)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/zoom-in.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoom_in.setIcon(icon2)
        self.actionZoom_in.setObjectName("actionZoom_in")
        self.actionZoom_out = QtWidgets.QAction(MainWindow)
        self.actionZoom_out.setEnabled(False)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/magnifying-glass.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoom_out.setIcon(icon3)
        self.actionZoom_out.setObjectName("actionZoom_out")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setEnabled(False)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/rejected.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClose.setIcon(icon4)
        self.actionClose.setObjectName("actionClose")
        self.actionPlay = QtWidgets.QAction(MainWindow)
        self.actionPlay.setEnabled(False)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPlay.setIcon(icon5)
        self.actionPlay.setObjectName("actionPlay")
        self.actionPause = QtWidgets.QAction(MainWindow)
        self.actionPause.setEnabled(False)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/pause(1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPause.setIcon(icon6)
        self.actionPause.setObjectName("actionPause")
        self.actionStop = QtWidgets.QAction(MainWindow)
        self.actionStop.setEnabled(False)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/iconfinder_Stop_85391.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStop.setIcon(icon7)
        self.actionStop.setObjectName("actionStop")
        self.action1_Signal = QtWidgets.QAction(MainWindow)
        self.action1_Signal.setCheckable(True)
        self.action1_Signal.setChecked(True)
        self.action1_Signal.setObjectName("action1_Signal")
        self.action2_Signals = QtWidgets.QAction(MainWindow)
        self.action2_Signals.setCheckable(True)
        self.action2_Signals.setObjectName("action2_Signals")
        self.action3_Signals = QtWidgets.QAction(MainWindow)
        self.action3_Signals.setCheckable(True)
        self.action3_Signals.setObjectName("action3_Signals")
        self.actionSpectrogram = QtWidgets.QAction(MainWindow)
        self.actionSpectrogram.setEnabled(False)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/color-circle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSpectrogram.setIcon(icon8)
        self.actionSpectrogram.setObjectName("actionSpectrogram")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionSignal_graph = QtWidgets.QAction(MainWindow)
        self.actionSignal_graph.setEnabled(True)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icons/ecg-lines.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSignal_graph.setIcon(icon9)
        self.actionSignal_graph.setObjectName("actionSignal_graph")
        self.actionSave_as_PDF = QtWidgets.QAction(MainWindow)
        self.actionSave_as_PDF.setEnabled(False)
        self.actionSave_as_PDF.setObjectName("actionSave_as_PDF")
        self.actionFaster = QtWidgets.QAction(MainWindow)
        self.actionFaster.setEnabled(False)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("icons/fast-forward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFaster.setIcon(icon10)
        self.actionFaster.setObjectName("actionFaster")
        self.actionSlower = QtWidgets.QAction(MainWindow)
        self.actionSlower.setEnabled(False)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("icons/fast-forward(1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSlower.setIcon(icon11)
        self.actionSlower.setObjectName("actionSlower")
        self.actionColor_1 = QtWidgets.QAction(MainWindow)
        self.actionColor_1.setEnabled(False)
        self.actionColor_1.setObjectName("actionColor_1")
        self.actionColor_2 = QtWidgets.QAction(MainWindow)
        self.actionColor_2.setEnabled(False)
        self.actionColor_2.setObjectName("actionColor_2")
        self.actionColor_3 = QtWidgets.QAction(MainWindow)
        self.actionColor_3.setEnabled(False)
        self.actionColor_3.setObjectName("actionColor_3")
        self.actionColor_4 = QtWidgets.QAction(MainWindow)
        self.actionColor_4.setEnabled(False)
        self.actionColor_4.setObjectName("actionColor_4")
        self.actionColor_5 = QtWidgets.QAction(MainWindow)
        self.actionColor_5.setEnabled(False)
        self.actionColor_5.setObjectName("actionColor_5")
        self.actionScroll_up = QtWidgets.QAction(MainWindow)
        self.actionScroll_up.setEnabled(False)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("icons/up-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionScroll_up.setIcon(icon12)
        self.actionScroll_up.setObjectName("actionScroll_up")
        self.actionScroll_down = QtWidgets.QAction(MainWindow)
        self.actionScroll_down.setEnabled(False)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("icons/arrow-down-sign-to-navigate.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionScroll_down.setIcon(icon13)
        self.actionScroll_down.setObjectName("actionScroll_down")
        self.actionScroll_left = QtWidgets.QAction(MainWindow)
        self.actionScroll_left.setEnabled(False)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("icons/left-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionScroll_left.setIcon(icon14)
        self.actionScroll_left.setObjectName("actionScroll_left")
        self.actionScroll_right = QtWidgets.QAction(MainWindow)
        self.actionScroll_right.setEnabled(False)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("icons/right-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionScroll_right.setIcon(icon15)
        self.actionScroll_right.setWhatsThis("")
        self.actionScroll_right.setObjectName("actionScroll_right")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setEnabled(False)
        self.actionSave.setObjectName("actionSave")
        self.actionNew_tab = QtWidgets.QAction(MainWindow)
        self.actionNew_tab.setObjectName("actionNew_tab")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionNew_tab)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave_as_PDF)
        self.menuFile.addAction(self.actionExit)
        self.menuView.addAction(self.actionToolbar)
        self.menuView.addAction(self.actionStatus_bar)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionPlay)
        self.menuView.addAction(self.actionPause)
        self.menuView.addAction(self.actionStop)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionFaster)
        self.menuView.addAction(self.actionSlower)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionSpectrogram)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionZoom_in)
        self.menuView.addAction(self.actionZoom_out)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionScroll_up)
        self.menuView.addAction(self.actionScroll_down)
        self.menuView.addAction(self.actionScroll_left)
        self.menuView.addAction(self.actionScroll_right)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionClose)
        self.menuHelp.addAction(self.actionAbout)
        self.menuColor_palette.addAction(self.actionColor_1)
        self.menuColor_palette.addAction(self.actionColor_2)
        self.menuColor_palette.addAction(self.actionColor_3)
        self.menuColor_palette.addAction(self.actionColor_4)
        self.menuColor_palette.addAction(self.actionColor_5)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuColor_palette.menuAction())
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionPlay)
        self.toolBar.addAction(self.actionPause)
        self.toolBar.addAction(self.actionStop)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSpectrogram)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionZoom_out)
        self.toolBar.addAction(self.actionZoom_in)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionClose)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Signal viewer"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Signal 1"))
        self.pushButton.setText(_translate("MainWindow", "Play sound"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuColor_palette.setTitle(_translate("MainWindow", "Color palette"))
        self.statusbar.setStatusTip(_translate("MainWindow", "Ready"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar_2"))
        self.actionOpen.setText(_translate("MainWindow", "Open..."))
        self.actionOpen.setStatusTip(_translate("MainWindow", "Open an existing document"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionToolbar.setText(_translate("MainWindow", "Toolbar"))
        self.actionToolbar.setStatusTip(_translate("MainWindow", "Show or hide the toolbar"))
        self.actionStatus_bar.setText(_translate("MainWindow", "Status bar"))
        self.actionStatus_bar.setStatusTip(_translate("MainWindow", "Show or hide the status bar"))
        self.actionZoom_in.setText(_translate("MainWindow", "Zoom in"))
        self.actionZoom_in.setStatusTip(_translate("MainWindow", "Zoom in"))
        self.actionZoom_in.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.actionZoom_out.setText(_translate("MainWindow", "Zoom out"))
        self.actionZoom_out.setStatusTip(_translate("MainWindow", "Zoom out"))
        self.actionZoom_out.setShortcut(_translate("MainWindow", "Ctrl+D"))
        self.actionAbout.setText(_translate("MainWindow", "About..."))
        self.actionAbout.setStatusTip(_translate("MainWindow", "Show Information, version number and copy rights "))
        self.actionAbout.setShortcut(_translate("MainWindow", "Ctrl+H"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionClose.setStatusTip(_translate("MainWindow", "Close the selected signal"))
        self.actionClose.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionPlay.setText(_translate("MainWindow", "Play"))
        self.actionPlay.setStatusTip(_translate("MainWindow", "Play the signal"))
        self.actionPlay.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.actionPause.setText(_translate("MainWindow", "Pause"))
        self.actionPause.setStatusTip(_translate("MainWindow", "Pause the signal"))
        self.actionPause.setShortcut(_translate("MainWindow", "Space"))
        self.actionStop.setText(_translate("MainWindow", "Stop"))
        self.actionStop.setStatusTip(_translate("MainWindow", "Stop signal flow"))
        self.actionStop.setShortcut(_translate("MainWindow", "Return"))
        self.action1_Signal.setText(_translate("MainWindow", "Signal 1"))
        self.action1_Signal.setStatusTip(_translate("MainWindow", "View the first signal"))
        self.action1_Signal.setShortcut(_translate("MainWindow", "F1"))
        self.action2_Signals.setText(_translate("MainWindow", "Signal 2"))
        self.action2_Signals.setStatusTip(_translate("MainWindow", "View the second signal"))
        self.action2_Signals.setShortcut(_translate("MainWindow", "F2"))
        self.action3_Signals.setText(_translate("MainWindow", "Signal 3"))
        self.action3_Signals.setStatusTip(_translate("MainWindow", "View the third signal"))
        self.action3_Signals.setShortcut(_translate("MainWindow", "F3"))
        self.actionSpectrogram.setText(_translate("MainWindow", "Spectrogram"))
        self.actionSpectrogram.setStatusTip(_translate("MainWindow", "Create a spectrogram of the selected signal"))
        self.actionSpectrogram.setShortcut(_translate("MainWindow", "Ctrl+T"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setStatusTip(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Esc"))
        self.actionSignal_graph.setText(_translate("MainWindow", "Signal graph"))
        self.actionSignal_graph.setStatusTip(_translate("MainWindow", "Show the signal ghraph"))
        self.actionSignal_graph.setShortcut(_translate("MainWindow", "Ctrl+G"))
        self.actionSave_as_PDF.setText(_translate("MainWindow", "Save as PDF"))
        self.actionSave_as_PDF.setStatusTip(_translate("MainWindow", "Save signals as pdf"))
        self.actionSave_as_PDF.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionFaster.setText(_translate("MainWindow", "Faster"))
        self.actionFaster.setStatusTip(_translate("MainWindow", "Make the playback faster"))
        self.actionFaster.setShortcut(_translate("MainWindow", "Ctrl++"))
        self.actionSlower.setText(_translate("MainWindow", "Slower"))
        self.actionSlower.setStatusTip(_translate("MainWindow", "Make the playback slower"))
        self.actionSlower.setShortcut(_translate("MainWindow", "Ctrl+-"))
        self.actionColor_1.setText(_translate("MainWindow", "Color 1"))
        self.actionColor_1.setShortcut(_translate("MainWindow", "Ctrl+1"))
        self.actionColor_2.setText(_translate("MainWindow", "Color 2"))
        self.actionColor_2.setShortcut(_translate("MainWindow", "Ctrl+2"))
        self.actionColor_3.setText(_translate("MainWindow", "Color 3"))
        self.actionColor_3.setShortcut(_translate("MainWindow", "Ctrl+3"))
        self.actionColor_4.setText(_translate("MainWindow", "Color 4"))
        self.actionColor_4.setShortcut(_translate("MainWindow", "Ctrl+4"))
        self.actionColor_5.setText(_translate("MainWindow", "Color 5"))
        self.actionColor_5.setShortcut(_translate("MainWindow", "Ctrl+5"))
        self.actionScroll_up.setText(_translate("MainWindow", "Scroll up"))
        self.actionScroll_up.setStatusTip(_translate("MainWindow", "Scroll the graph up"))
        self.actionScroll_up.setShortcut(_translate("MainWindow", "Up"))
        self.actionScroll_down.setText(_translate("MainWindow", "Scroll down"))
        self.actionScroll_down.setStatusTip(_translate("MainWindow", "Scroll the graph down"))
        self.actionScroll_down.setShortcut(_translate("MainWindow", "Down"))
        self.actionScroll_left.setText(_translate("MainWindow", "Scroll left"))
        self.actionScroll_left.setStatusTip(_translate("MainWindow", "Scroll the graph left"))
        self.actionScroll_left.setShortcut(_translate("MainWindow", "Left"))
        self.actionScroll_right.setText(_translate("MainWindow", "Scroll right"))
        self.actionScroll_right.setStatusTip(_translate("MainWindow", "Scroll the graph right"))
        self.actionScroll_right.setShortcut(_translate("MainWindow", "Right"))
        self.actionSave.setText(_translate("MainWindow", "Save the sound"))
        self.actionNew_tab.setText(_translate("MainWindow", "New tab"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
