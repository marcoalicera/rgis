# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_importDataIntoRasTables.ui'
#
# Created: Wed Sep 30 10:40:35 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_importDataIntoRasTables(object):
    def setupUi(self, importDataIntoRasTables):
        importDataIntoRasTables.setObjectName(_fromUtf8("importDataIntoRasTables"))
        importDataIntoRasTables.resize(362, 586)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(importDataIntoRasTables.sizePolicy().hasHeightForWidth())
        importDataIntoRasTables.setSizePolicy(sizePolicy)
        self.gridLayout = QtGui.QGridLayout(importDataIntoRasTables)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(importDataIntoRasTables)
        self.tabWidget.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.general = QtGui.QWidget()
        self.general.setObjectName(_fromUtf8("general"))
        self.gridLayout_2 = QtGui.QGridLayout(self.general)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.general)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.cboStreamCenterlines = QtGui.QComboBox(self.general)
        self.cboStreamCenterlines.setObjectName(_fromUtf8("cboStreamCenterlines"))
        self.verticalLayout.addWidget(self.cboStreamCenterlines)
        self.label_2 = QtGui.QLabel(self.general)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.cboXsecs = QtGui.QComboBox(self.general)
        self.cboXsecs.setObjectName(_fromUtf8("cboXsecs"))
        self.verticalLayout.addWidget(self.cboXsecs)
        self.label_4 = QtGui.QLabel(self.general)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.cboBanks = QtGui.QComboBox(self.general)
        self.cboBanks.setObjectName(_fromUtf8("cboBanks"))
        self.verticalLayout.addWidget(self.cboBanks)
        self.label_7 = QtGui.QLabel(self.general)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout.addWidget(self.label_7)
        self.cboFlowPaths = QtGui.QComboBox(self.general)
        self.cboFlowPaths.setObjectName(_fromUtf8("cboFlowPaths"))
        self.verticalLayout.addWidget(self.cboFlowPaths)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_8 = QtGui.QLabel(self.general)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout.addWidget(self.label_8)
        self.cboFlowpathType = QtGui.QComboBox(self.general)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboFlowpathType.sizePolicy().hasHeightForWidth())
        self.cboFlowpathType.setSizePolicy(sizePolicy)
        self.cboFlowpathType.setMinimumSize(QtCore.QSize(0, 0))
        self.cboFlowpathType.setObjectName(_fromUtf8("cboFlowpathType"))
        self.horizontalLayout.addWidget(self.cboFlowpathType)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_3 = QtGui.QLabel(self.general)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.cboLevees = QtGui.QComboBox(self.general)
        self.cboLevees.setObjectName(_fromUtf8("cboLevees"))
        self.verticalLayout.addWidget(self.cboLevees)
        self.label_5 = QtGui.QLabel(self.general)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout.addWidget(self.label_5)
        self.cboIneffective = QtGui.QComboBox(self.general)
        self.cboIneffective.setObjectName(_fromUtf8("cboIneffective"))
        self.verticalLayout.addWidget(self.cboIneffective)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_10 = QtGui.QLabel(self.general)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_3.addWidget(self.label_10)
        self.cboIneffElev = QtGui.QComboBox(self.general)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboIneffElev.sizePolicy().hasHeightForWidth())
        self.cboIneffElev.setSizePolicy(sizePolicy)
        self.cboIneffElev.setObjectName(_fromUtf8("cboIneffElev"))
        self.horizontalLayout_3.addWidget(self.cboIneffElev)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.label_6 = QtGui.QLabel(self.general)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout.addWidget(self.label_6)
        self.cboObstructions = QtGui.QComboBox(self.general)
        self.cboObstructions.setObjectName(_fromUtf8("cboObstructions"))
        self.verticalLayout.addWidget(self.cboObstructions)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_11 = QtGui.QLabel(self.general)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_4.addWidget(self.label_11)
        self.cboObstructionsElev = QtGui.QComboBox(self.general)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboObstructionsElev.sizePolicy().hasHeightForWidth())
        self.cboObstructionsElev.setSizePolicy(sizePolicy)
        self.cboObstructionsElev.setObjectName(_fromUtf8("cboObstructionsElev"))
        self.horizontalLayout_4.addWidget(self.cboObstructionsElev)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.label_12 = QtGui.QLabel(self.general)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.verticalLayout.addWidget(self.label_12)
        self.cboLanduse = QtGui.QComboBox(self.general)
        self.cboLanduse.setObjectName(_fromUtf8("cboLanduse"))
        self.verticalLayout.addWidget(self.cboLanduse)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_13 = QtGui.QLabel(self.general)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_5.addWidget(self.label_13)
        self.cboLandCodeAttr = QtGui.QComboBox(self.general)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboLandCodeAttr.sizePolicy().hasHeightForWidth())
        self.cboLandCodeAttr.setSizePolicy(sizePolicy)
        self.cboLandCodeAttr.setObjectName(_fromUtf8("cboLandCodeAttr"))
        self.horizontalLayout_5.addWidget(self.cboLandCodeAttr)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_14 = QtGui.QLabel(self.general)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.horizontalLayout_6.addWidget(self.label_14)
        self.cboManningAttr = QtGui.QComboBox(self.general)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboManningAttr.sizePolicy().hasHeightForWidth())
        self.cboManningAttr.setSizePolicy(sizePolicy)
        self.cboManningAttr.setObjectName(_fromUtf8("cboManningAttr"))
        self.horizontalLayout_6.addWidget(self.cboManningAttr)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.general, _fromUtf8(""))
        self.flowAreas = QtGui.QWidget()
        self.flowAreas.setObjectName(_fromUtf8("flowAreas"))
        self.gridLayout_7 = QtGui.QGridLayout(self.flowAreas)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.groupBox = QtGui.QGroupBox(self.flowAreas)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_4.setMargin(3)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_7.addWidget(self.label_9)
        self.cbo2dFlowAreas = QtGui.QComboBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbo2dFlowAreas.sizePolicy().hasHeightForWidth())
        self.cbo2dFlowAreas.setSizePolicy(sizePolicy)
        self.cbo2dFlowAreas.setMinimumSize(QtCore.QSize(0, 0))
        self.cbo2dFlowAreas.setAcceptDrops(False)
        self.cbo2dFlowAreas.setMinimumContentsLength(0)
        self.cbo2dFlowAreas.setFrame(True)
        self.cbo2dFlowAreas.setObjectName(_fromUtf8("cbo2dFlowAreas"))
        self.horizontalLayout_7.addWidget(self.cbo2dFlowAreas)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.AreaNameAttributeLabel = QtGui.QLabel(self.groupBox)
        self.AreaNameAttributeLabel.setObjectName(_fromUtf8("AreaNameAttributeLabel"))
        self.horizontalLayout_8.addWidget(self.AreaNameAttributeLabel)
        self.cbo2dAreasNameAttr = QtGui.QComboBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbo2dAreasNameAttr.sizePolicy().hasHeightForWidth())
        self.cbo2dAreasNameAttr.setSizePolicy(sizePolicy)
        self.cbo2dAreasNameAttr.setObjectName(_fromUtf8("cbo2dAreasNameAttr"))
        self.horizontalLayout_8.addWidget(self.cbo2dAreasNameAttr)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(6)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.AreaNameAttributeLabel_2 = QtGui.QLabel(self.groupBox)
        self.AreaNameAttributeLabel_2.setObjectName(_fromUtf8("AreaNameAttributeLabel_2"))
        self.horizontalLayout_9.addWidget(self.AreaNameAttributeLabel_2)
        self.cbo2dAreasMeshSizeAttr = QtGui.QComboBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbo2dAreasMeshSizeAttr.sizePolicy().hasHeightForWidth())
        self.cbo2dAreasMeshSizeAttr.setSizePolicy(sizePolicy)
        self.cbo2dAreasMeshSizeAttr.setObjectName(_fromUtf8("cbo2dAreasMeshSizeAttr"))
        self.horizontalLayout_9.addWidget(self.cbo2dAreasMeshSizeAttr)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.gridLayout_4.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.flowAreas)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_5 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_5.setMargin(3)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.AreaNameAttributeLabel_3 = QtGui.QLabel(self.groupBox_2)
        self.AreaNameAttributeLabel_3.setObjectName(_fromUtf8("AreaNameAttributeLabel_3"))
        self.horizontalLayout_10.addWidget(self.AreaNameAttributeLabel_3)
        self.cboBreaklines = QtGui.QComboBox(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboBreaklines.sizePolicy().hasHeightForWidth())
        self.cboBreaklines.setSizePolicy(sizePolicy)
        self.cboBreaklines.setObjectName(_fromUtf8("cboBreaklines"))
        self.horizontalLayout_10.addWidget(self.cboBreaklines)
        self.verticalLayout_5.addLayout(self.horizontalLayout_10)
        self.label_15 = QtGui.QLabel(self.groupBox_2)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.verticalLayout_5.addWidget(self.label_15)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.AreaNameAttributeLabel_4 = QtGui.QLabel(self.groupBox_2)
        self.AreaNameAttributeLabel_4.setObjectName(_fromUtf8("AreaNameAttributeLabel_4"))
        self.horizontalLayout_11.addWidget(self.AreaNameAttributeLabel_4)
        self.cboBreaklineCellSizeAlongAttr = QtGui.QComboBox(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboBreaklineCellSizeAlongAttr.sizePolicy().hasHeightForWidth())
        self.cboBreaklineCellSizeAlongAttr.setSizePolicy(sizePolicy)
        self.cboBreaklineCellSizeAlongAttr.setObjectName(_fromUtf8("cboBreaklineCellSizeAlongAttr"))
        self.horizontalLayout_11.addWidget(self.cboBreaklineCellSizeAlongAttr)
        self.verticalLayout_5.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.label_16 = QtGui.QLabel(self.groupBox_2)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.horizontalLayout_12.addWidget(self.label_16)
        self.cboBreaklineCellSizeAcrossAttr = QtGui.QComboBox(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboBreaklineCellSizeAcrossAttr.sizePolicy().hasHeightForWidth())
        self.cboBreaklineCellSizeAcrossAttr.setSizePolicy(sizePolicy)
        self.cboBreaklineCellSizeAcrossAttr.setObjectName(_fromUtf8("cboBreaklineCellSizeAcrossAttr"))
        self.horizontalLayout_12.addWidget(self.cboBreaklineCellSizeAcrossAttr)
        self.verticalLayout_5.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.label_17 = QtGui.QLabel(self.groupBox_2)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.horizontalLayout_13.addWidget(self.label_17)
        self.cboBreaklineCellRowsAttr = QtGui.QComboBox(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboBreaklineCellRowsAttr.sizePolicy().hasHeightForWidth())
        self.cboBreaklineCellRowsAttr.setSizePolicy(sizePolicy)
        self.cboBreaklineCellRowsAttr.setObjectName(_fromUtf8("cboBreaklineCellRowsAttr"))
        self.horizontalLayout_13.addWidget(self.cboBreaklineCellRowsAttr)
        self.verticalLayout_5.addLayout(self.horizontalLayout_13)
        self.gridLayout_5.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(self.flowAreas)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_6 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_6.setMargin(3)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.label_18 = QtGui.QLabel(self.groupBox_3)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.horizontalLayout_14.addWidget(self.label_18)
        self.cboBreakpoints = QtGui.QComboBox(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboBreakpoints.sizePolicy().hasHeightForWidth())
        self.cboBreakpoints.setSizePolicy(sizePolicy)
        self.cboBreakpoints.setObjectName(_fromUtf8("cboBreakpoints"))
        self.horizontalLayout_14.addWidget(self.cboBreakpoints)
        self.verticalLayout_6.addLayout(self.horizontalLayout_14)
        self.gridLayout_6.addLayout(self.verticalLayout_6, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.gridLayout_7.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem, 1, 0, 1, 1)
        self.tabWidget.addTab(self.flowAreas, _fromUtf8(""))
        self.structures = QtGui.QWidget()
        self.structures.setObjectName(_fromUtf8("structures"))
        self.gridLayout_3 = QtGui.QGridLayout(self.structures)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.structures, _fromUtf8(""))
        self.storageAreas = QtGui.QWidget()
        self.storageAreas.setObjectName(_fromUtf8("storageAreas"))
        self.tabWidget.addTab(self.storageAreas, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(importDataIntoRasTables)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)
        self.label_9.setBuddy(self.cbo2dFlowAreas)
        self.AreaNameAttributeLabel.setBuddy(self.cbo2dAreasNameAttr)
        self.AreaNameAttributeLabel_2.setBuddy(self.cbo2dAreasMeshSizeAttr)
        self.AreaNameAttributeLabel_3.setBuddy(self.cboBreaklines)
        self.AreaNameAttributeLabel_4.setBuddy(self.cboBreaklineCellSizeAlongAttr)

        self.retranslateUi(importDataIntoRasTables)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(importDataIntoRasTables)

    def retranslateUi(self, importDataIntoRasTables):
        importDataIntoRasTables.setWindowTitle(_translate("importDataIntoRasTables", "Import Data Into RAS PostGIS Tables", None))
        self.label.setText(_translate("importDataIntoRasTables", "Rivers Layer", None))
        self.label_2.setText(_translate("importDataIntoRasTables", "Cross-sections Layer", None))
        self.label_4.setText(_translate("importDataIntoRasTables", "Banks Layer", None))
        self.label_7.setText(_translate("importDataIntoRasTables", "Flow Paths Layer", None))
        self.label_8.setText(_translate("importDataIntoRasTables", "Type attribute", None))
        self.label_3.setText(_translate("importDataIntoRasTables", "Levees Layer", None))
        self.label_5.setText(_translate("importDataIntoRasTables", "Ineffective Flow Areas Layer", None))
        self.label_10.setText(_translate("importDataIntoRasTables", "Elevation attribute", None))
        self.label_6.setText(_translate("importDataIntoRasTables", "Blocked Obstructions Layer", None))
        self.label_11.setText(_translate("importDataIntoRasTables", "Elevation attribute", None))
        self.label_12.setText(_translate("importDataIntoRasTables", "Landuse Areas Layer", None))
        self.label_13.setText(_translate("importDataIntoRasTables", "Land Cover Code attribute", None))
        self.label_14.setText(_translate("importDataIntoRasTables", "Manning\'s n attribute", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.general), _translate("importDataIntoRasTables", "General", None))
        self.groupBox.setTitle(_translate("importDataIntoRasTables", "2D Flow Areas", None))
        self.label_9.setText(_translate("importDataIntoRasTables", "Layer name", None))
        self.AreaNameAttributeLabel.setText(_translate("importDataIntoRasTables", "Area name attribute", None))
        self.AreaNameAttributeLabel_2.setText(_translate("importDataIntoRasTables", "Default cell size attribute", None))
        self.groupBox_2.setTitle(_translate("importDataIntoRasTables", "Breaklines", None))
        self.AreaNameAttributeLabel_3.setText(_translate("importDataIntoRasTables", "Layer name", None))
        self.label_15.setText(_translate("importDataIntoRasTables", "Attributes:", None))
        self.AreaNameAttributeLabel_4.setText(_translate("importDataIntoRasTables", "Cell size along a breakline", None))
        self.label_16.setText(_translate("importDataIntoRasTables", "Cell size across a breakline", None))
        self.label_17.setText(_translate("importDataIntoRasTables", "Number of cells rows to align", None))
        self.groupBox_3.setTitle(_translate("importDataIntoRasTables", "Breakpoints", None))
        self.label_18.setText(_translate("importDataIntoRasTables", "Layer name", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.flowAreas), _translate("importDataIntoRasTables", "2D", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.structures), _translate("importDataIntoRasTables", "Hydraulic Structures", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.storageAreas), _translate("importDataIntoRasTables", "Storage Areas", None))

