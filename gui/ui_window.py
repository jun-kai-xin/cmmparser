# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created: Mon Dec 28 22:30:03 2015
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from gui.editor import CodeEditor


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(930, 650)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setEnabled(True)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.splitterOutter = QtWidgets.QSplitter(self.centralWidget)
        self.splitterOutter.setOrientation(QtCore.Qt.Vertical)
        self.splitterOutter.setObjectName("splitterOutter")
        self.splitterInner = QtWidgets.QSplitter(self.splitterOutter)
        self.splitterInner.setOrientation(QtCore.Qt.Horizontal)
        self.splitterInner.setObjectName("splitterInner")
        self.tabWidgetBrowser = QtWidgets.QTabWidget(self.splitterInner)
        self.tabWidgetBrowser.setTabsClosable(True)
        self.tabWidgetBrowser.setObjectName("tabWidgetBrowser")
        self.tabFile = QtWidgets.QWidget()
        self.tabFile.setObjectName("tabFile")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tabFile)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.treeViewFile = QtWidgets.QTreeView(self.tabFile)
        self.treeViewFile.setObjectName("treeViewFile")
        self.verticalLayout.addWidget(self.treeViewFile)
        self.tabWidgetBrowser.addTab(self.tabFile, "")
        self.tabToken = QtWidgets.QWidget()
        self.tabToken.setObjectName("tabToken")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tabToken)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.treeViewToken = QtWidgets.QTreeView(self.tabToken)
        self.treeViewToken.setObjectName("treeViewToken")
        self.verticalLayout_3.addWidget(self.treeViewToken)
        self.tabWidgetBrowser.addTab(self.tabToken, "")
        self.tabSyntax = QtWidgets.QWidget()
        self.tabSyntax.setObjectName("tabSyntax")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tabSyntax)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.treeViewSyntax = QtWidgets.QTreeView(self.tabSyntax)
        self.treeViewSyntax.setObjectName("treeViewSyntax")
        self.verticalLayout_4.addWidget(self.treeViewSyntax)
        self.tabWidgetBrowser.addTab(self.tabSyntax, "")
        self.tabWidgetEditor = QtWidgets.QTabWidget(self.splitterInner)
        self.tabWidgetEditor.setTabsClosable(False)
        self.tabWidgetEditor.setObjectName("tabWidgetEditor")
        self.tabEditor = QtWidgets.QWidget()
        self.tabEditor.setObjectName("tabEditor")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tabEditor)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.codeEditor = CodeEditor(self.tabEditor)
        self.codeEditor.setObjectName("codeEditor")
        self.horizontalLayout.addWidget(self.codeEditor)
        self.tabWidgetEditor.addTab(self.tabEditor, "")
        self.tabWidgetOutput = QtWidgets.QTabWidget(self.splitterOutter)
        self.tabWidgetOutput.setTabsClosable(True)
        self.tabWidgetOutput.setObjectName("tabWidgetOutput")
        self.tabConsole = QtWidgets.QWidget()
        self.tabConsole.setObjectName("tabConsole")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tabConsole)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.tabConsole)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_2.addWidget(self.textBrowser)
        self.tabWidgetOutput.addTab(self.tabConsole, "")
        self.gridLayout.addWidget(self.splitterOutter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 930, 25))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuEditor = QtWidgets.QMenu(self.menuBar)
        self.menuEditor.setObjectName("menuEditor")
        self.menuRun = QtWidgets.QMenu(self.menuBar)
        self.menuRun.setObjectName("menuRun")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuView = QtWidgets.QMenu(self.menuBar)
        self.menuView.setObjectName("menuView")
        self.menuTest = QtWidgets.QMenu(self.menuBar)
        self.menuTest.setObjectName("menuTest")
        MainWindow.setMenuBar(self.menuBar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setMovable(False)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew.setIcon(icon)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon1)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon2)
        self.actionSave.setObjectName("actionSave")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCopy.setIcon(icon3)
        self.actionCopy.setObjectName("actionCopy")
        self.actionCut = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/cut.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCut.setIcon(icon4)
        self.actionCut.setObjectName("actionCut")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/paste.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPaste.setIcon(icon5)
        self.actionPaste.setObjectName("actionPaste")
        self.actionRun = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images/start.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRun.setIcon(icon6)
        self.actionRun.setObjectName("actionRun")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAboutQt = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/images/qtcreator.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAboutQt.setIcon(icon7)
        self.actionAboutQt.setObjectName("actionAboutQt")
        self.actionViewFiles = QtWidgets.QAction(MainWindow)
        self.actionViewFiles.setCheckable(True)
        self.actionViewFiles.setChecked(True)
        self.actionViewFiles.setObjectName("actionViewFiles")
        self.actionViewTokenTree = QtWidgets.QAction(MainWindow)
        self.actionViewTokenTree.setCheckable(True)
        self.actionViewTokenTree.setChecked(False)
        self.actionViewTokenTree.setObjectName("actionViewTokenTree")
        self.actionViewSystaxTree = QtWidgets.QAction(MainWindow)
        self.actionViewSystaxTree.setCheckable(True)
        self.actionViewSystaxTree.setChecked(False)
        self.actionViewSystaxTree.setObjectName("actionViewSystaxTree")
        self.actionBuild = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/images/build.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBuild.setIcon(icon8)
        self.actionBuild.setObjectName("actionBuild")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/images/undo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUndo.setIcon(icon9)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/images/redo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRedo.setIcon(icon10)
        self.actionRedo.setObjectName("actionRedo")
        self.actionSelectAll = QtWidgets.QAction(MainWindow)
        self.actionSelectAll.setObjectName("actionSelectAll")
        self.actionRunLexer = QtWidgets.QAction(MainWindow)
        self.actionRunLexer.setObjectName("actionRunLexer")
        self.actionRunParser = QtWidgets.QAction(MainWindow)
        self.actionRunParser.setObjectName("actionRunParser")
        self.actionSaveAs = QtWidgets.QAction(MainWindow)
        self.actionSaveAs.setObjectName("actionSaveAs")
        self.actionViewToolbar = QtWidgets.QAction(MainWindow)
        self.actionViewToolbar.setCheckable(True)
        self.actionViewToolbar.setChecked(True)
        self.actionViewToolbar.setObjectName("actionViewToolbar")
        self.actionTestLexer = QtWidgets.QAction(MainWindow)
        self.actionTestLexer.setObjectName("actionTestLexer")
        self.actionTestParser = QtWidgets.QAction(MainWindow)
        self.actionTestParser.setObjectName("actionTestParser")
        self.actionTestRuntime = QtWidgets.QAction(MainWindow)
        self.actionTestRuntime.setObjectName("actionTestRuntime")
        self.actionViewConsole = QtWidgets.QAction(MainWindow)
        self.actionViewConsole.setCheckable(True)
        self.actionViewConsole.setChecked(False)
        self.actionViewConsole.setObjectName("actionViewConsole")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.actionQuit.setObjectName("actionQuit")
        self.actionTestCompiler = QtWidgets.QAction(MainWindow)
        self.actionTestCompiler.setObjectName("actionTestCompiler")
        self.actionTestSemantic = QtWidgets.QAction(MainWindow)
        self.actionTestSemantic.setObjectName("actionTestSemantic")
        self.actionShowStable = QtWidgets.QAction(MainWindow)
        self.actionShowStable.setObjectName("actionShowStable")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSaveAs)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuEditor.addAction(self.actionUndo)
        self.menuEditor.addAction(self.actionRedo)
        self.menuEditor.addSeparator()
        self.menuEditor.addAction(self.actionCopy)
        self.menuEditor.addAction(self.actionCut)
        self.menuEditor.addAction(self.actionPaste)
        self.menuEditor.addSeparator()
        self.menuEditor.addAction(self.actionSelectAll)
        self.menuRun.addAction(self.actionRun)
        self.menuRun.addAction(self.actionBuild)
        self.menuRun.addSeparator()
        self.menuRun.addAction(self.actionRunLexer)
        self.menuRun.addAction(self.actionRunParser)
        self.menuRun.addAction(self.actionShowStable)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAboutQt)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionViewToolbar)
        self.menuView.addAction(self.actionViewConsole)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionViewFiles)
        self.menuView.addAction(self.actionViewTokenTree)
        self.menuView.addAction(self.actionViewSystaxTree)
        self.menuTest.addAction(self.actionTestLexer)
        self.menuTest.addAction(self.actionTestParser)
        self.menuTest.addAction(self.actionTestSemantic)
        self.menuTest.addAction(self.actionTestCompiler)
        self.menuTest.addAction(self.actionTestRuntime)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuEditor.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())
        self.menuBar.addAction(self.menuRun.menuAction())
        self.menuBar.addAction(self.menuTest.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionNew)
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addAction(self.actionUndo)
        self.toolBar.addAction(self.actionRedo)
        self.toolBar.addAction(self.actionCopy)
        self.toolBar.addAction(self.actionCut)
        self.toolBar.addAction(self.actionPaste)
        self.toolBar.addAction(self.actionBuild)
        self.toolBar.addAction(self.actionRun)

        self.retranslateUi(MainWindow)
        self.tabWidgetBrowser.setCurrentIndex(2)
        self.tabWidgetEditor.setCurrentIndex(0)
        self.tabWidgetOutput.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cinter"))
        self.tabWidgetBrowser.setTabText(self.tabWidgetBrowser.indexOf(self.tabFile), _translate("MainWindow", "File"))
        self.tabWidgetBrowser.setTabText(self.tabWidgetBrowser.indexOf(self.tabToken),
                                         _translate("MainWindow", "Token"))
        self.tabWidgetBrowser.setTabText(self.tabWidgetBrowser.indexOf(self.tabSyntax),
                                         _translate("MainWindow", "Syntax"))
        self.tabWidgetEditor.setTabText(self.tabWidgetEditor.indexOf(self.tabEditor),
                                        _translate("MainWindow", "New File"))
        self.tabWidgetOutput.setTabText(self.tabWidgetOutput.indexOf(self.tabConsole), _translate("MainWindow", "Page"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEditor.setTitle(_translate("MainWindow", "Edit"))
        self.menuRun.setTitle(_translate("MainWindow", "Run"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuTest.setTitle(_translate("MainWindow", "Test"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionCut.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionRun.setText(_translate("MainWindow", "Run"))
        self.actionRun.setShortcut(_translate("MainWindow", "F5"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionAboutQt.setText(_translate("MainWindow", "AboutQt"))
        self.actionViewFiles.setText(_translate("MainWindow", "File Tree"))
        self.actionViewTokenTree.setText(_translate("MainWindow", "Token Tree"))
        self.actionViewSystaxTree.setText(_translate("MainWindow", "Systax Tree"))
        self.actionBuild.setText(_translate("MainWindow", "Build"))
        self.actionBuild.setShortcut(_translate("MainWindow", "Shift+F5"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionUndo.setToolTip(_translate("MainWindow", "Undo"))
        self.actionUndo.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionRedo.setToolTip(_translate("MainWindow", "Redo"))
        self.actionRedo.setShortcut(_translate("MainWindow", "Ctrl+Y"))
        self.actionSelectAll.setText(_translate("MainWindow", "Select All"))
        self.actionSelectAll.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.actionRunLexer.setText(_translate("MainWindow", "Run Lexer"))
        self.actionRunParser.setText(_translate("MainWindow", "Run Parser"))
        self.actionSaveAs.setText(_translate("MainWindow", "Save As..."))
        self.actionSaveAs.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.actionViewToolbar.setText(_translate("MainWindow", "Toolbar"))
        self.actionTestLexer.setText(_translate("MainWindow", "Lexer"))
        self.actionTestParser.setText(_translate("MainWindow", "Parser"))
        self.actionTestRuntime.setText(_translate("MainWindow", "Runtime"))
        self.actionViewConsole.setText(_translate("MainWindow", "Console"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionTestCompiler.setText(_translate("MainWindow", "Compile"))
        self.actionTestSemantic.setText(_translate("MainWindow", "Semantic"))
        self.actionShowStable.setText(_translate("MainWindow", "Show Stable"))


import cinter_rc
