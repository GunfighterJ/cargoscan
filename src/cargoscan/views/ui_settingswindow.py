# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources\ui\settingswindow.ui'
#
# Created: Sat Jul 15 12:57:35 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        SettingsWindow.setObjectName("SettingsWindow")
        SettingsWindow.resize(462, 443)
        SettingsWindow.setWindowTitle("")
        self.gridLayout = QtGui.QGridLayout(SettingsWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.settings_ok_button = QtGui.QPushButton(SettingsWindow)
        self.settings_ok_button.setObjectName("settings_ok_button")
        self.horizontalLayout.addWidget(self.settings_ok_button)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 2, 1, 1)
        self.tabWidget = QtGui.QTabWidget(SettingsWindow)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.colors_tab = QtGui.QWidget()
        self.colors_tab.setObjectName("colors_tab")
        self.gridLayout_3 = QtGui.QGridLayout(self.colors_tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtGui.QLabel(self.colors_tab)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.btn_value_add = QtGui.QPushButton(self.colors_tab)
        self.btn_value_add.setMinimumSize(QtCore.QSize(24, 0))
        self.btn_value_add.setMaximumSize(QtCore.QSize(24, 16777215))
        self.btn_value_add.setText("")
        self.btn_value_add.setObjectName("btn_value_add")
        self.horizontalLayout_4.addWidget(self.btn_value_add)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        self.volumeTableWidget = QtGui.QTableWidget(self.colors_tab)
        self.volumeTableWidget.setFrameShape(QtGui.QFrame.StyledPanel)
        self.volumeTableWidget.setFrameShadow(QtGui.QFrame.Plain)
        self.volumeTableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.volumeTableWidget.setShowGrid(False)
        self.volumeTableWidget.setWordWrap(False)
        self.volumeTableWidget.setRowCount(1)
        self.volumeTableWidget.setObjectName("volumeTableWidget")
        self.volumeTableWidget.setColumnCount(0)
        self.volumeTableWidget.setRowCount(1)
        self.volumeTableWidget.horizontalHeader().setVisible(False)
        self.volumeTableWidget.verticalHeader().setVisible(False)
        self.gridLayout_3.addWidget(self.volumeTableWidget, 2, 1, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtGui.QLabel(self.colors_tab)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.btn_volume_add = QtGui.QPushButton(self.colors_tab)
        self.btn_volume_add.setMinimumSize(QtCore.QSize(24, 0))
        self.btn_volume_add.setMaximumSize(QtCore.QSize(24, 16777215))
        self.btn_volume_add.setText("")
        self.btn_volume_add.setObjectName("btn_volume_add")
        self.horizontalLayout_5.addWidget(self.btn_volume_add)
        self.gridLayout_3.addLayout(self.horizontalLayout_5, 1, 1, 1, 1)
        self.valueTableWidget = QtGui.QTableWidget(self.colors_tab)
        self.valueTableWidget.setFrameShape(QtGui.QFrame.StyledPanel)
        self.valueTableWidget.setFrameShadow(QtGui.QFrame.Plain)
        self.valueTableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.valueTableWidget.setShowGrid(False)
        self.valueTableWidget.setWordWrap(False)
        self.valueTableWidget.setRowCount(1)
        self.valueTableWidget.setObjectName("valueTableWidget")
        self.valueTableWidget.setColumnCount(0)
        self.valueTableWidget.setRowCount(1)
        self.valueTableWidget.horizontalHeader().setVisible(False)
        self.valueTableWidget.verticalHeader().setVisible(False)
        self.gridLayout_3.addWidget(self.valueTableWidget, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtGui.QLabel(self.colors_tab)
        self.label_3.setTextFormat(QtCore.Qt.RichText)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 3, 0, 1, 2)
        self.tabWidget.addTab(self.colors_tab, "")
        self.other_tab = QtGui.QWidget()
        self.other_tab.setObjectName("other_tab")
        self.formLayout_2 = QtGui.QFormLayout(self.other_tab)
        self.formLayout_2.setObjectName("formLayout_2")
        self.checkbox_items_table = QtGui.QCheckBox(self.other_tab)
        self.checkbox_items_table.setChecked(True)
        self.checkbox_items_table.setObjectName("checkbox_items_table")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.checkbox_items_table)
        self.checkbox_abbreviate_value = QtGui.QCheckBox(self.other_tab)
        self.checkbox_abbreviate_value.setChecked(True)
        self.checkbox_abbreviate_value.setObjectName("checkbox_abbreviate_value")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.checkbox_abbreviate_value)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtGui.QLabel(self.other_tab)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.slider_opacity = QtGui.QSlider(self.other_tab)
        self.slider_opacity.setMaximum(100)
        self.slider_opacity.setProperty("value", 20)
        self.slider_opacity.setOrientation(QtCore.Qt.Horizontal)
        self.slider_opacity.setObjectName("slider_opacity")
        self.horizontalLayout_3.addWidget(self.slider_opacity)
        self.spinbox_opacity = QtGui.QSpinBox(self.other_tab)
        self.spinbox_opacity.setMaximum(100)
        self.spinbox_opacity.setProperty("value", 20)
        self.spinbox_opacity.setObjectName("spinbox_opacity")
        self.horizontalLayout_3.addWidget(self.spinbox_opacity)
        self.formLayout_2.setLayout(2, QtGui.QFormLayout.LabelRole, self.horizontalLayout_3)
        self.tabWidget.addTab(self.other_tab, "")
        self.gridLayout.addWidget(self.tabWidget, 1, 2, 1, 1)

        self.retranslateUi(SettingsWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.slider_opacity, QtCore.SIGNAL("valueChanged(int)"), self.spinbox_opacity.setValue)
        QtCore.QObject.connect(self.spinbox_opacity, QtCore.SIGNAL("valueChanged(int)"), self.slider_opacity.setValue)
        QtCore.QMetaObject.connectSlotsByName(SettingsWindow)

    def retranslateUi(self, SettingsWindow):
        self.settings_ok_button.setText(QtGui.QApplication.translate("SettingsWindow", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("SettingsWindow", "Value Color Overrides", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("SettingsWindow", "Volume Color Overrides", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("SettingsWindow", "<html><head/><body><p>Add color alerts to each table to override the value/volume colors of the main window. Colors will change at each step if it is greater or equal to that value. To change the color, click the space between the text box and close box.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.colors_tab), QtGui.QApplication.translate("SettingsWindow", "Colors", None, QtGui.QApplication.UnicodeUTF8))
        self.checkbox_items_table.setText(QtGui.QApplication.translate("SettingsWindow", "Show items table", None, QtGui.QApplication.UnicodeUTF8))
        self.checkbox_abbreviate_value.setText(QtGui.QApplication.translate("SettingsWindow", "Abbreviate values (thousand, million, billion)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("SettingsWindow", "Overlay Transparency", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.other_tab), QtGui.QApplication.translate("SettingsWindow", "Other", None, QtGui.QApplication.UnicodeUTF8))

