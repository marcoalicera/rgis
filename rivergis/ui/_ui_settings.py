# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_settings.ui'
#
# Created: Sun Dec 06 22:49:39 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from ..resources import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName(_fromUtf8("Settings"))
        Settings.resize(494, 418)
        Settings.setSizeGripEnabled(False)
        Settings.setModal(True)
        self.verticalLayout_4 = QtGui.QVBoxLayout(Settings)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.mOptionsSplitter = QtGui.QSplitter(Settings)
        self.mOptionsSplitter.setEnabled(True)
        self.mOptionsSplitter.setOrientation(QtCore.Qt.Horizontal)
        self.mOptionsSplitter.setOpaqueResize(True)
        self.mOptionsSplitter.setChildrenCollapsible(False)
        self.mOptionsSplitter.setObjectName(_fromUtf8("mOptionsSplitter"))
        self.optionsListFrame = QtGui.QFrame(self.mOptionsSplitter)
        self.optionsListFrame.setFrameShape(QtGui.QFrame.NoFrame)
        self.optionsListFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.optionsListFrame.setObjectName(_fromUtf8("optionsListFrame"))
        self.verticalLayout_15 = QtGui.QVBoxLayout(self.optionsListFrame)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setMargin(0)
        self.verticalLayout_15.setObjectName(_fromUtf8("verticalLayout_15"))
        self.optionsList = QtGui.QListWidget(self.optionsListFrame)
        self.optionsList.setMinimumSize(QtCore.QSize(58, 0))
        self.optionsList.setMaximumSize(QtCore.QSize(150, 16777215))
        self.optionsList.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.optionsList.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.optionsList.setIconSize(QtCore.QSize(32, 32))
        self.optionsList.setTextElideMode(QtCore.Qt.ElideNone)
        self.optionsList.setResizeMode(QtGui.QListView.Adjust)
        self.optionsList.setWordWrap(True)
        self.optionsList.setObjectName(_fromUtf8("optionsList"))
        item = QtGui.QListWidgetItem()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/rivergis/icons/rivergis_big.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon)
        self.optionsList.addItem(item)
        item = QtGui.QListWidgetItem()
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/rivergis/icons/rdb.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon1)
        self.optionsList.addItem(item)
        item = QtGui.QListWidgetItem()
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/rivergis/icons/dtmSetup.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon2)
        self.optionsList.addItem(item)
        self.verticalLayout_15.addWidget(self.optionsList)
        self.optionsFrame = QtGui.QFrame(self.mOptionsSplitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.optionsFrame.sizePolicy().hasHeightForWidth())
        self.optionsFrame.setSizePolicy(sizePolicy)
        self.optionsFrame.setFrameShape(QtGui.QFrame.NoFrame)
        self.optionsFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.optionsFrame.setObjectName(_fromUtf8("optionsFrame"))
        self.verticalLayout = QtGui.QVBoxLayout(self.optionsFrame)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.optionsStackedWidget = QtGui.QStackedWidget(self.optionsFrame)
        self.optionsStackedWidget.setObjectName(_fromUtf8("optionsStackedWidget"))
        self.optionsPageGeneral = QtGui.QWidget()
        self.optionsPageGeneral.setObjectName(_fromUtf8("optionsPageGeneral"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.optionsPageGeneral)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.mOptionsScrollArea_01 = QtGui.QScrollArea(self.optionsPageGeneral)
        self.mOptionsScrollArea_01.setFrameShape(QtGui.QFrame.NoFrame)
        self.mOptionsScrollArea_01.setWidgetResizable(True)
        self.mOptionsScrollArea_01.setObjectName(_fromUtf8("mOptionsScrollArea_01"))
        self.mOptionsScrollAreaContents_01 = QtGui.QWidget()
        self.mOptionsScrollAreaContents_01.setGeometry(QtCore.QRect(0, 0, 322, 369))
        self.mOptionsScrollAreaContents_01.setObjectName(_fromUtf8("mOptionsScrollAreaContents_01"))
        self.verticalLayout_28 = QtGui.QVBoxLayout(self.mOptionsScrollAreaContents_01)
        self.verticalLayout_28.setObjectName(_fromUtf8("verticalLayout_28"))
        self.groupBox_3 = QtGui.QGroupBox(self.mOptionsScrollAreaContents_01)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.open_lastChbox = QtGui.QCheckBox(self.groupBox_3)
        self.open_lastChbox.setChecked(True)
        self.open_lastChbox.setObjectName(_fromUtf8("open_lastChbox"))
        self.verticalLayout_7.addWidget(self.open_lastChbox)
        self.debugModeChbox = QtGui.QCheckBox(self.groupBox_3)
        self.debugModeChbox.setObjectName(_fromUtf8("debugModeChbox"))
        self.verticalLayout_7.addWidget(self.debugModeChbox)
        self.rgisAlwaysOnTopChbox = QtGui.QCheckBox(self.groupBox_3)
        self.rgisAlwaysOnTopChbox.setObjectName(_fromUtf8("rgisAlwaysOnTopChbox"))
        self.verticalLayout_7.addWidget(self.rgisAlwaysOnTopChbox)
        self.verticalLayout_28.addWidget(self.groupBox_3)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_28.addItem(spacerItem)
        self.mOptionsScrollArea_01.setWidget(self.mOptionsScrollAreaContents_01)
        self.verticalLayout_3.addWidget(self.mOptionsScrollArea_01)
        self.optionsStackedWidget.addWidget(self.optionsPageGeneral)
        self.optionsPageRdb = QtGui.QWidget()
        self.optionsPageRdb.setObjectName(_fromUtf8("optionsPageRdb"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.optionsPageRdb)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.scrollArea = QtGui.QScrollArea(self.optionsPageRdb)
        self.scrollArea.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 322, 369))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.groupBox_2 = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.db_loadAllChbox = QtGui.QCheckBox(self.groupBox_2)
        self.db_loadAllChbox.setChecked(True)
        self.db_loadAllChbox.setObjectName(_fromUtf8("db_loadAllChbox"))
        self.verticalLayout_9.addWidget(self.db_loadAllChbox)
        self.verticalLayout_6.addWidget(self.groupBox_2)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_5.addWidget(self.scrollArea)
        self.optionsStackedWidget.addWidget(self.optionsPageRdb)
        self.optionsPageDtm = QtGui.QWidget()
        self.optionsPageDtm.setObjectName(_fromUtf8("optionsPageDtm"))
        self.verticalLayout_12 = QtGui.QVBoxLayout(self.optionsPageDtm)
        self.verticalLayout_12.setMargin(0)
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.mOptionsScrollArea_04 = QtGui.QScrollArea(self.optionsPageDtm)
        self.mOptionsScrollArea_04.setFrameShape(QtGui.QFrame.NoFrame)
        self.mOptionsScrollArea_04.setWidgetResizable(True)
        self.mOptionsScrollArea_04.setObjectName(_fromUtf8("mOptionsScrollArea_04"))
        self.mOptionsScrollAreaContents_04 = QtGui.QWidget()
        self.mOptionsScrollAreaContents_04.setGeometry(QtCore.QRect(0, 0, 119, 189))
        self.mOptionsScrollAreaContents_04.setObjectName(_fromUtf8("mOptionsScrollAreaContents_04"))
        self.verticalLayout_29 = QtGui.QVBoxLayout(self.mOptionsScrollAreaContents_04)
        self.verticalLayout_29.setObjectName(_fromUtf8("verticalLayout_29"))
        self.groupBox = QtGui.QGroupBox(self.mOptionsScrollAreaContents_04)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.dtm_selectAllChbox = QtGui.QCheckBox(self.groupBox)
        self.dtm_selectAllChbox.setObjectName(_fromUtf8("dtm_selectAllChbox"))
        self.verticalLayout_2.addWidget(self.dtm_selectAllChbox)
        self.dtm_listView = QtGui.QListView(self.groupBox)
        self.dtm_listView.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.dtm_listView.setSelectionBehavior(QtGui.QAbstractItemView.SelectItems)
        self.dtm_listView.setObjectName(_fromUtf8("dtm_listView"))
        self.verticalLayout_2.addWidget(self.dtm_listView)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.dtm_chunksize = QtGui.QSpinBox(self.groupBox)
        self.dtm_chunksize.setMaximum(999999999)
        self.dtm_chunksize.setSingleStep(1000)
        self.dtm_chunksize.setObjectName(_fromUtf8("dtm_chunksize"))
        self.verticalLayout_2.addWidget(self.dtm_chunksize)
        self.verticalLayout_29.addWidget(self.groupBox)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_29.addItem(spacerItem2)
        self.mOptionsScrollArea_04.setWidget(self.mOptionsScrollAreaContents_04)
        self.verticalLayout_12.addWidget(self.mOptionsScrollArea_04)
        self.optionsStackedWidget.addWidget(self.optionsPageDtm)
        self.verticalLayout.addWidget(self.optionsStackedWidget)
        self.verticalLayout_4.addWidget(self.mOptionsSplitter)
        self.buttonBox = QtGui.QDialogButtonBox(Settings)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_4.addWidget(self.buttonBox)

        self.retranslateUi(Settings)
        self.optionsStackedWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Settings.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Settings.reject)
        QtCore.QObject.connect(self.optionsList, QtCore.SIGNAL(_fromUtf8("currentRowChanged(int)")), self.optionsStackedWidget.setCurrentIndex)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(_translate("Settings", "RiverGIS Options", None))
        __sortingEnabled = self.optionsList.isSortingEnabled()
        self.optionsList.setSortingEnabled(False)
        item = self.optionsList.item(0)
        item.setText(_translate("Settings", "General", None))
        item.setToolTip(_translate("Settings", "General", None))
        item = self.optionsList.item(1)
        item.setText(_translate("Settings", "River Database", None))
        item = self.optionsList.item(2)
        item.setText(_translate("Settings", "DTM", None))
        item.setToolTip(_translate("Settings", "System", None))
        self.optionsList.setSortingEnabled(__sortingEnabled)
        self.groupBox_3.setTitle(_translate("Settings", "Application", None))
        self.open_lastChbox.setText(_translate("Settings", "Load last river database when starting", None))
        self.debugModeChbox.setText(_translate("Settings", "Debugging mode", None))
        self.rgisAlwaysOnTopChbox.setText(_translate("Settings", "Plugin window always on top", None))
        self.groupBox_2.setTitle(_translate("Settings", "Database", None))
        self.db_loadAllChbox.setText(_translate("Settings", "Load all tables in preview", None))
        self.groupBox.setTitle(_translate("Settings", "Rasters selection", None))
        self.dtm_selectAllChbox.setText(_translate("Settings", "Select all", None))
        self.label_2.setToolTip(_translate("Settings", "<html><head/><body><p>Maximum number of raster cell values fetched at once by a database query. </p><p>If the number of raster cells exceeds the chunk size they are fetched successively.</p></body></html>", None))
        self.label_2.setText(_translate("Settings", "Chunk size:", None))
        self.dtm_chunksize.setToolTip(_translate("Settings", "<html><head/><body><p>Maximum number of raster cell values fetched at once by a database query. </p><p>If the number of raster cells exceeds the chunk size they are fetched successively.</p></body></html>", None))

