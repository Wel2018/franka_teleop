# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setting.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)

class Ui_SettingWindow(object):
    def setupUi(self, SettingWindow):
        if not SettingWindow.objectName():
            SettingWindow.setObjectName(u"SettingWindow")
        SettingWindow.resize(635, 760)
        font = QFont()
        font.setFamilies([u"Microsoft YaHei"])
        font.setPointSize(11)
        SettingWindow.setFont(font)
        self.centralwidget = QWidget(SettingWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 20, 261, 612))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.sub_y = QLineEdit(self.layoutWidget)
        self.sub_y.setObjectName(u"sub_y")
        self.sub_y.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.sub_y, 4, 1, 1, 1)

        self.add_Y = QLineEdit(self.layoutWidget)
        self.add_Y.setObjectName(u"add_Y")
        self.add_Y.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.add_Y, 12, 1, 1, 1)

        self.add_y = QLineEdit(self.layoutWidget)
        self.add_y.setObjectName(u"add_y")
        self.add_y.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.add_y, 3, 1, 1, 1)

        self.sub_R = QLineEdit(self.layoutWidget)
        self.sub_R.setObjectName(u"sub_R")
        self.sub_R.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.sub_R, 9, 1, 1, 1)

        self.label_13 = QLabel(self.layoutWidget)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 12, 0, 1, 1)

        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 6, 0, 1, 1)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei"])
        font1.setPointSize(11)
        font1.setBold(True)
        self.label.setFont(font1)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.sub_z = QLineEdit(self.layoutWidget)
        self.sub_z.setObjectName(u"sub_z")
        self.sub_z.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.sub_z, 6, 1, 1, 1)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)

        self.sub_P = QLineEdit(self.layoutWidget)
        self.sub_P.setObjectName(u"sub_P")
        self.sub_P.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.sub_P.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.sub_P, 11, 1, 1, 1)

        self.label_14 = QLabel(self.layoutWidget)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout.addWidget(self.label_14, 13, 0, 1, 1)

        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.add_R = QLineEdit(self.layoutWidget)
        self.add_R.setObjectName(u"add_R")
        self.add_R.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.add_R, 8, 1, 1, 1)

        self.label_10 = QLabel(self.layoutWidget)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 9, 0, 1, 1)

        self.sub_x = QLineEdit(self.layoutWidget)
        self.sub_x.setObjectName(u"sub_x")
        self.sub_x.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.sub_x, 2, 1, 1, 1)

        self.label_12 = QLabel(self.layoutWidget)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 11, 0, 1, 1)

        self.sub_Y = QLineEdit(self.layoutWidget)
        self.sub_Y.setObjectName(u"sub_Y")
        self.sub_Y.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.sub_Y, 13, 1, 1, 1)

        self.add_x = QLineEdit(self.layoutWidget)
        self.add_x.setObjectName(u"add_x")
        self.add_x.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.add_x, 1, 1, 1, 1)

        self.add_z = QLineEdit(self.layoutWidget)
        self.add_z.setObjectName(u"add_z")
        self.add_z.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.add_z, 5, 1, 1, 1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.gridLayout.addWidget(self.label_2, 7, 0, 1, 1)

        self.label_30 = QLabel(self.layoutWidget)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout.addWidget(self.label_30, 15, 0, 1, 1)

        self.label_15 = QLabel(self.layoutWidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font1)

        self.gridLayout.addWidget(self.label_15, 14, 0, 1, 1)

        self.label_11 = QLabel(self.layoutWidget)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 10, 0, 1, 1)

        self.gripper = QLineEdit(self.layoutWidget)
        self.gripper.setObjectName(u"gripper")
        self.gripper.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.gripper, 15, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 18, 1, 1, 1)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.btn_apply = QPushButton(self.layoutWidget)
        self.btn_apply.setObjectName(u"btn_apply")
        self.btn_apply.setFont(font1)

        self.gridLayout.addWidget(self.btn_apply, 19, 0, 1, 2)

        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 8, 0, 1, 1)

        self.add_P = QLineEdit(self.layoutWidget)
        self.add_P.setObjectName(u"add_P")
        self.add_P.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.add_P, 10, 1, 1, 1)

        self.collect = QLineEdit(self.layoutWidget)
        self.collect.setObjectName(u"collect")
        self.collect.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.collect, 17, 1, 1, 1)

        self.label_31 = QLabel(self.layoutWidget)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout.addWidget(self.label_31, 17, 0, 1, 1)

        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(320, 20, 291, 676))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_28 = QLabel(self.layoutWidget1)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_28)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_16 = QLabel(self.layoutWidget1)
        self.label_16.setObjectName(u"label_16")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.label_16, 0, 0, 1, 1)

        self.j1 = QDoubleSpinBox(self.layoutWidget1)
        self.j1.setObjectName(u"j1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.j1.sizePolicy().hasHeightForWidth())
        self.j1.setSizePolicy(sizePolicy1)
        self.j1.setDecimals(4)
        self.j1.setMinimum(-9999.000000000000000)
        self.j1.setMaximum(9999.000000000000000)

        self.gridLayout_4.addWidget(self.j1, 0, 1, 1, 1)

        self.label_17 = QLabel(self.layoutWidget1)
        self.label_17.setObjectName(u"label_17")
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.label_17, 1, 0, 1, 1)

        self.j2 = QDoubleSpinBox(self.layoutWidget1)
        self.j2.setObjectName(u"j2")
        sizePolicy1.setHeightForWidth(self.j2.sizePolicy().hasHeightForWidth())
        self.j2.setSizePolicy(sizePolicy1)
        self.j2.setDecimals(4)
        self.j2.setMinimum(-9999.000000000000000)
        self.j2.setMaximum(9999.000000000000000)

        self.gridLayout_4.addWidget(self.j2, 1, 1, 1, 1)

        self.label_18 = QLabel(self.layoutWidget1)
        self.label_18.setObjectName(u"label_18")
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.label_18, 2, 0, 1, 1)

        self.j3 = QDoubleSpinBox(self.layoutWidget1)
        self.j3.setObjectName(u"j3")
        sizePolicy1.setHeightForWidth(self.j3.sizePolicy().hasHeightForWidth())
        self.j3.setSizePolicy(sizePolicy1)
        self.j3.setDecimals(4)
        self.j3.setMinimum(-9999.000000000000000)
        self.j3.setMaximum(9999.000000000000000)

        self.gridLayout_4.addWidget(self.j3, 2, 1, 1, 1)

        self.label_19 = QLabel(self.layoutWidget1)
        self.label_19.setObjectName(u"label_19")
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.label_19, 3, 0, 1, 1)

        self.j4 = QDoubleSpinBox(self.layoutWidget1)
        self.j4.setObjectName(u"j4")
        sizePolicy1.setHeightForWidth(self.j4.sizePolicy().hasHeightForWidth())
        self.j4.setSizePolicy(sizePolicy1)
        self.j4.setDecimals(4)
        self.j4.setMinimum(-9999.000000000000000)
        self.j4.setMaximum(9999.000000000000000)

        self.gridLayout_4.addWidget(self.j4, 3, 1, 1, 1)

        self.label_20 = QLabel(self.layoutWidget1)
        self.label_20.setObjectName(u"label_20")
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.label_20, 4, 0, 1, 1)

        self.j5 = QDoubleSpinBox(self.layoutWidget1)
        self.j5.setObjectName(u"j5")
        sizePolicy1.setHeightForWidth(self.j5.sizePolicy().hasHeightForWidth())
        self.j5.setSizePolicy(sizePolicy1)
        self.j5.setDecimals(4)
        self.j5.setMinimum(-9999.000000000000000)
        self.j5.setMaximum(9999.000000000000000)

        self.gridLayout_4.addWidget(self.j5, 4, 1, 1, 1)

        self.label_21 = QLabel(self.layoutWidget1)
        self.label_21.setObjectName(u"label_21")
        sizePolicy.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.label_21, 5, 0, 1, 1)

        self.j6 = QDoubleSpinBox(self.layoutWidget1)
        self.j6.setObjectName(u"j6")
        sizePolicy1.setHeightForWidth(self.j6.sizePolicy().hasHeightForWidth())
        self.j6.setSizePolicy(sizePolicy1)
        self.j6.setDecimals(4)
        self.j6.setMinimum(-9999.000000000000000)
        self.j6.setMaximum(9999.000000000000000)

        self.gridLayout_4.addWidget(self.j6, 5, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_4)

        self.label_29 = QLabel(self.layoutWidget1)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_29)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_22 = QLabel(self.layoutWidget1)
        self.label_22.setObjectName(u"label_22")
        sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)

        self.gridLayout_5.addWidget(self.label_22, 0, 0, 1, 1)

        self.x = QDoubleSpinBox(self.layoutWidget1)
        self.x.setObjectName(u"x")
        sizePolicy1.setHeightForWidth(self.x.sizePolicy().hasHeightForWidth())
        self.x.setSizePolicy(sizePolicy1)
        self.x.setDecimals(4)
        self.x.setMinimum(-9999.000000000000000)
        self.x.setMaximum(9999.000000000000000)

        self.gridLayout_5.addWidget(self.x, 0, 1, 1, 1)

        self.label_23 = QLabel(self.layoutWidget1)
        self.label_23.setObjectName(u"label_23")
        sizePolicy.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy)

        self.gridLayout_5.addWidget(self.label_23, 1, 0, 1, 1)

        self.y = QDoubleSpinBox(self.layoutWidget1)
        self.y.setObjectName(u"y")
        sizePolicy1.setHeightForWidth(self.y.sizePolicy().hasHeightForWidth())
        self.y.setSizePolicy(sizePolicy1)
        self.y.setDecimals(4)
        self.y.setMinimum(-9999.000000000000000)
        self.y.setMaximum(9999.000000000000000)

        self.gridLayout_5.addWidget(self.y, 1, 1, 1, 1)

        self.label_24 = QLabel(self.layoutWidget1)
        self.label_24.setObjectName(u"label_24")
        sizePolicy.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy)

        self.gridLayout_5.addWidget(self.label_24, 2, 0, 1, 1)

        self.z = QDoubleSpinBox(self.layoutWidget1)
        self.z.setObjectName(u"z")
        sizePolicy1.setHeightForWidth(self.z.sizePolicy().hasHeightForWidth())
        self.z.setSizePolicy(sizePolicy1)
        self.z.setDecimals(4)
        self.z.setMinimum(-9999.000000000000000)
        self.z.setMaximum(9999.000000000000000)

        self.gridLayout_5.addWidget(self.z, 2, 1, 1, 1)

        self.label_25 = QLabel(self.layoutWidget1)
        self.label_25.setObjectName(u"label_25")
        sizePolicy.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy)

        self.gridLayout_5.addWidget(self.label_25, 3, 0, 1, 1)

        self.R = QDoubleSpinBox(self.layoutWidget1)
        self.R.setObjectName(u"R")
        sizePolicy1.setHeightForWidth(self.R.sizePolicy().hasHeightForWidth())
        self.R.setSizePolicy(sizePolicy1)
        self.R.setDecimals(4)
        self.R.setMinimum(-9999.000000000000000)
        self.R.setMaximum(9999.000000000000000)

        self.gridLayout_5.addWidget(self.R, 3, 1, 1, 1)

        self.label_26 = QLabel(self.layoutWidget1)
        self.label_26.setObjectName(u"label_26")
        sizePolicy.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy)

        self.gridLayout_5.addWidget(self.label_26, 4, 0, 1, 1)

        self.P = QDoubleSpinBox(self.layoutWidget1)
        self.P.setObjectName(u"P")
        sizePolicy1.setHeightForWidth(self.P.sizePolicy().hasHeightForWidth())
        self.P.setSizePolicy(sizePolicy1)
        self.P.setDecimals(4)
        self.P.setMinimum(-9999.000000000000000)
        self.P.setMaximum(9999.000000000000000)

        self.gridLayout_5.addWidget(self.P, 4, 1, 1, 1)

        self.label_27 = QLabel(self.layoutWidget1)
        self.label_27.setObjectName(u"label_27")
        sizePolicy.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy)

        self.gridLayout_5.addWidget(self.label_27, 5, 0, 1, 1)

        self.Y = QDoubleSpinBox(self.layoutWidget1)
        self.Y.setObjectName(u"Y")
        sizePolicy1.setHeightForWidth(self.Y.sizePolicy().hasHeightForWidth())
        self.Y.setSizePolicy(sizePolicy1)
        self.Y.setDecimals(4)
        self.Y.setMinimum(-9999.000000000000000)
        self.Y.setMaximum(9999.000000000000000)

        self.gridLayout_5.addWidget(self.Y, 5, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_5)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_get_real = QPushButton(self.layoutWidget1)
        self.btn_get_real.setObjectName(u"btn_get_real")
        self.btn_get_real.setEnabled(False)

        self.verticalLayout.addWidget(self.btn_get_real)

        self.btn_sync_sim = QPushButton(self.layoutWidget1)
        self.btn_sync_sim.setObjectName(u"btn_sync_sim")
        self.btn_sync_sim.setEnabled(False)

        self.verticalLayout.addWidget(self.btn_sync_sim)

        self.btn_sync_real = QPushButton(self.layoutWidget1)
        self.btn_sync_real.setObjectName(u"btn_sync_real")
        self.btn_sync_real.setEnabled(False)

        self.verticalLayout.addWidget(self.btn_sync_real)

        self.btn_set_default = QPushButton(self.layoutWidget1)
        self.btn_set_default.setObjectName(u"btn_set_default")
        self.btn_set_default.setEnabled(False)

        self.verticalLayout.addWidget(self.btn_set_default)

        self.btn_save_default = QPushButton(self.layoutWidget1)
        self.btn_save_default.setObjectName(u"btn_save_default")
        self.btn_save_default.setEnabled(False)

        self.verticalLayout.addWidget(self.btn_save_default)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        SettingWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(SettingWindow)
        self.statusbar.setObjectName(u"statusbar")
        SettingWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SettingWindow)

        QMetaObject.connectSlotsByName(SettingWindow)
    # setupUi

    def retranslateUi(self, SettingWindow):
        SettingWindow.setWindowTitle(QCoreApplication.translate("SettingWindow", u"\u8bbe\u7f6e", None))
        self.sub_y.setInputMask("")
        self.sub_y.setText(QCoreApplication.translate("SettingWindow", u"D", None))
        self.sub_y.setPlaceholderText(QCoreApplication.translate("SettingWindow", u"\u8bf7\u8f93\u5165\u5feb\u6377\u952e", None))
        self.add_Y.setInputMask("")
        self.add_Y.setText(QCoreApplication.translate("SettingWindow", u"O", None))
        self.add_Y.setPlaceholderText(QCoreApplication.translate("SettingWindow", u"\u8bf7\u8f93\u5165\u5feb\u6377\u952e", None))
        self.add_y.setInputMask("")
        self.add_y.setText(QCoreApplication.translate("SettingWindow", u"A", None))
        self.add_y.setPlaceholderText(QCoreApplication.translate("SettingWindow", u"\u8bf7\u8f93\u5165\u5feb\u6377\u952e", None))
        self.sub_R.setInputMask("")
        self.sub_R.setText(QCoreApplication.translate("SettingWindow", u"J", None))
        self.sub_R.setPlaceholderText(QCoreApplication.translate("SettingWindow", u"\u8bf7\u8f93\u5165\u5feb\u6377\u952e", None))
        self.label_13.setText(QCoreApplication.translate("SettingWindow", u"+Y", None))
        self.label_8.setText(QCoreApplication.translate("SettingWindow", u"-z", None))
        self.label_4.setText(QCoreApplication.translate("SettingWindow", u"-x", None))
        self.label.setText(QCoreApplication.translate("SettingWindow", u"\u4f4d\u7f6e\u63a7\u5236", None))
        self.sub_z.setInputMask("")
        self.sub_z.setText(QCoreApplication.translate("SettingWindow", u"Z", None))
        self.sub_z.setPlaceholderText(QCoreApplication.translate("SettingWindow", u"\u8bf7\u8f93\u5165\u5feb\u6377\u952e", None))
        self.label_6.setText(QCoreApplication.translate("SettingWindow", u"-y", None))
        self.sub_P.setInputMask("")
        self.sub_P.setText(QCoreApplication.translate("SettingWindow", u"K", None))
        self.sub_P.setPlaceholderText(QCoreApplication.translate("SettingWindow", u"\u8bf7\u8f93\u5165\u5feb\u6377\u952e", None))
        self.label_14.setText(QCoreApplication.translate("SettingWindow", u"-Y", None))
        self.label_7.setText(QCoreApplication.translate("SettingWindow", u"+z", None))
        self.label_3.setText(QCoreApplication.translate("SettingWindow", u"+x", None))
        self.add_R.setInputMask("")
        self.add_R.setText(QCoreApplication.translate("SettingWindow", u"U", None))
        self.add_R.setPlaceholderText(QCoreApplication.translate("SettingWindow", u"\u8bf7\u8f93\u5165\u5feb\u6377\u952e", None))
        self.label_10.setText(QCoreApplication.translate("SettingWindow", u"-R", None))
        self.sub_x.setInputMask("")
        self.sub_x.setText(QCoreApplication.translate("SettingWindow", u"S", None))
        self.sub_x.setPlaceholderText(QCoreApplication.translate("SettingWindow", u"\u8bf7\u8f93\u5165\u5feb\u6377\u952e", None))
        self.label_12.setText(QCoreApplication.translate("SettingWindow", u"-P", None))
        self.sub_Y.setInputMask("")
        self.sub_Y.setText(QCoreApplication.translate("SettingWindow", u"L", None))
        self.sub_Y.setPlaceholderText(QCoreApplication.translate("SettingWindow", u"\u8bf7\u8f93\u5165\u5feb\u6377\u952e", None))
        self.add_x.setInputMask("")
        self.add_x.setText(QCoreApplication.translate("SettingWindow", u"W", None))
        self.add_x.setPlaceholderText(QCoreApplication.translate("SettingWindow", u"\u8bf7\u8f93\u5165\u5feb\u6377\u952e", None))
        self.add_z.setInputMask("")
        self.add_z.setText(QCoreApplication.translate("SettingWindow", u"Q", None))
        self.add_z.setPlaceholderText(QCoreApplication.translate("SettingWindow", u"\u8bf7\u8f93\u5165\u5feb\u6377\u952e", None))
        self.label_2.setText(QCoreApplication.translate("SettingWindow", u"\u59ff\u52bf\u63a7\u5236", None))
        self.label_30.setText(QCoreApplication.translate("SettingWindow", u"\u5939\u722a", None))
        self.label_15.setText(QCoreApplication.translate("SettingWindow", u"\u5176\u4ed6", None))
        self.label_11.setText(QCoreApplication.translate("SettingWindow", u"+P", None))
        self.gripper.setInputMask("")
        self.gripper.setText(QCoreApplication.translate("SettingWindow", u"P", None))
        self.gripper.setPlaceholderText(QCoreApplication.translate("SettingWindow", u"\u8bf7\u8f93\u5165\u5feb\u6377\u952e", None))
        self.label_5.setText(QCoreApplication.translate("SettingWindow", u"+y", None))
        self.btn_apply.setText(QCoreApplication.translate("SettingWindow", u"\u5e94\u7528", None))
        self.label_9.setText(QCoreApplication.translate("SettingWindow", u"+R", None))
        self.add_P.setInputMask("")
        self.add_P.setText(QCoreApplication.translate("SettingWindow", u"I", None))
        self.add_P.setPlaceholderText(QCoreApplication.translate("SettingWindow", u"\u8bf7\u8f93\u5165\u5feb\u6377\u952e", None))
        self.collect.setText(QCoreApplication.translate("SettingWindow", u"B", None))
        self.label_31.setText(QCoreApplication.translate("SettingWindow", u"\u6536\u96c6", None))
        self.label_28.setText(QCoreApplication.translate("SettingWindow", u"\u5173\u8282\u7a7a\u95f4", None))
        self.label_16.setText(QCoreApplication.translate("SettingWindow", u"\u5173\u82821", None))
        self.label_17.setText(QCoreApplication.translate("SettingWindow", u"\u5173\u82822", None))
        self.label_18.setText(QCoreApplication.translate("SettingWindow", u"\u5173\u82823", None))
        self.label_19.setText(QCoreApplication.translate("SettingWindow", u"\u5173\u82824", None))
        self.label_20.setText(QCoreApplication.translate("SettingWindow", u"\u5173\u82825", None))
        self.label_21.setText(QCoreApplication.translate("SettingWindow", u"\u5173\u82826", None))
        self.label_29.setText(QCoreApplication.translate("SettingWindow", u"\u5750\u6807\u7a7a\u95f4", None))
        self.label_22.setText(QCoreApplication.translate("SettingWindow", u"x", None))
        self.label_23.setText(QCoreApplication.translate("SettingWindow", u"y", None))
        self.label_24.setText(QCoreApplication.translate("SettingWindow", u"z", None))
        self.label_25.setText(QCoreApplication.translate("SettingWindow", u"R", None))
        self.label_26.setText(QCoreApplication.translate("SettingWindow", u"P", None))
        self.label_27.setText(QCoreApplication.translate("SettingWindow", u"Y", None))
        self.btn_get_real.setText(QCoreApplication.translate("SettingWindow", u"\u83b7\u53d6\u7269\u7406\u673a\u72b6\u6001", None))
        self.btn_sync_sim.setText(QCoreApplication.translate("SettingWindow", u"\u540c\u6b65\u5230\u865a\u62df\u73af\u5883", None))
        self.btn_sync_real.setText(QCoreApplication.translate("SettingWindow", u"\u540c\u6b65\u5230\u771f\u5b9e\u73af\u5883", None))
        self.btn_set_default.setText(QCoreApplication.translate("SettingWindow", u"\u83b7\u53d6\u9ed8\u8ba4\u72b6\u6001", None))
        self.btn_save_default.setText(QCoreApplication.translate("SettingWindow", u"\u8bbe\u7f6e\u5f53\u524d\u4e3a\u9ed8\u8ba4\u72b6\u6001", None))
    # retranslateUi

