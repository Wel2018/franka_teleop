# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPlainTextEdit, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_DemoWindow(object):
    def setupUi(self, DemoWindow):
        if not DemoWindow.objectName():
            DemoWindow.setObjectName(u"DemoWindow")
        DemoWindow.resize(932, 769)
        font = QFont()
        font.setFamilies([u"Microsoft YaHei"])
        font.setPointSize(11)
        DemoWindow.setFont(font)
        self.act_setting = QAction(DemoWindow)
        self.act_setting.setObjectName(u"act_setting")
        self.act_setting.setMenuRole(QAction.MenuRole.PreferencesRole)
        self.act_gripper = QAction(DemoWindow)
        self.act_gripper.setObjectName(u"act_gripper")
        self.act_gripper.setMenuRole(QAction.MenuRole.NoRole)
        self.centralwidget = QWidget(DemoWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.wd_left = QWidget(self.centralwidget)
        self.wd_left.setObjectName(u"wd_left")
        self.wd_left.setMinimumSize(QSize(0, 200))
        self.lb_left = QLabel(self.wd_left)
        self.lb_left.setObjectName(u"lb_left")
        self.lb_left.setGeometry(QRect(0, 0, 100, 100))
        self.lb_left.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_6.addWidget(self.wd_left)

        self.wd_right = QWidget(self.centralwidget)
        self.wd_right.setObjectName(u"wd_right")
        self.lb_right = QLabel(self.wd_right)
        self.lb_right.setObjectName(u"lb_right")
        self.lb_right.setGeometry(QRect(0, 0, 100, 100))
        self.lb_right.setAutoFillBackground(False)
        self.lb_right.setStyleSheet(u"")

        self.horizontalLayout_6.addWidget(self.wd_right)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.msg = QLabel(self.centralwidget)
        self.msg.setObjectName(u"msg")
        self.msg.setFrameShape(QFrame.Shape.StyledPanel)

        self.verticalLayout_3.addWidget(self.msg)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.txt_log = QPlainTextEdit(self.centralwidget)
        self.txt_log.setObjectName(u"txt_log")
        self.txt_log.setReadOnly(True)

        self.verticalLayout.addWidget(self.txt_log)

        self.btn_clear = QPushButton(self.centralwidget)
        self.btn_clear.setObjectName(u"btn_clear")

        self.verticalLayout.addWidget(self.btn_clear)


        self.horizontalLayout_7.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.dataset_dir = QLineEdit(self.centralwidget)
        self.dataset_dir.setObjectName(u"dataset_dir")

        self.horizontalLayout_3.addWidget(self.dataset_dir)

        self.btn_open_dir = QPushButton(self.centralwidget)
        self.btn_open_dir.setObjectName(u"btn_open_dir")

        self.horizontalLayout_3.addWidget(self.btn_open_dir)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_play = QPushButton(self.centralwidget)
        self.btn_play.setObjectName(u"btn_play")

        self.horizontalLayout.addWidget(self.btn_play)

        self.btn_turb = QPushButton(self.centralwidget)
        self.btn_turb.setObjectName(u"btn_turb")

        self.horizontalLayout.addWidget(self.btn_turb)

        self.btn_capture = QPushButton(self.centralwidget)
        self.btn_capture.setObjectName(u"btn_capture")

        self.horizontalLayout.addWidget(self.btn_capture)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_gripper = QPushButton(self.centralwidget)
        self.btn_gripper.setObjectName(u"btn_gripper")

        self.horizontalLayout_2.addWidget(self.btn_gripper)

        self.btn_setting = QPushButton(self.centralwidget)
        self.btn_setting.setObjectName(u"btn_setting")
        self.btn_setting.setCheckable(False)
        self.btn_setting.setAutoDefault(False)
        self.btn_setting.setFlat(False)

        self.horizontalLayout_2.addWidget(self.btn_setting)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei"])
        font1.setPointSize(11)
        font1.setBold(True)
        self.label_2.setFont(font1)

        self.horizontalLayout_10.addWidget(self.label_2)

        self.rb_keyboard = QRadioButton(self.centralwidget)
        self.rb_keyboard.setObjectName(u"rb_keyboard")
        self.rb_keyboard.setChecked(True)

        self.horizontalLayout_10.addWidget(self.rb_keyboard)

        self.rb_spacemouse = QRadioButton(self.centralwidget)
        self.rb_spacemouse.setObjectName(u"rb_spacemouse")

        self.horizontalLayout_10.addWidget(self.rb_spacemouse)

        self.rb_iphone = QRadioButton(self.centralwidget)
        self.rb_iphone.setObjectName(u"rb_iphone")

        self.horizontalLayout_10.addWidget(self.rb_iphone)

        self.rb_io = QRadioButton(self.centralwidget)
        self.rb_io.setObjectName(u"rb_io")

        self.horizontalLayout_10.addWidget(self.rb_io)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.is_keyboard_ctrl = QCheckBox(self.centralwidget)
        self.is_keyboard_ctrl.setObjectName(u"is_keyboard_ctrl")

        self.horizontalLayout_4.addWidget(self.is_keyboard_ctrl)

        self.is_collect_data = QCheckBox(self.centralwidget)
        self.is_collect_data.setObjectName(u"is_collect_data")

        self.horizontalLayout_4.addWidget(self.is_collect_data)

        self.is_mirror = QCheckBox(self.centralwidget)
        self.is_mirror.setObjectName(u"is_mirror")

        self.horizontalLayout_4.addWidget(self.is_mirror)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_5.addWidget(self.label_3)

        self.ctl_state = QLineEdit(self.centralwidget)
        self.ctl_state.setObjectName(u"ctl_state")
        self.ctl_state.setEnabled(False)
        font2 = QFont()
        font2.setFamilies([u"Microsoft YaHei"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.ctl_state.setFont(font2)
        self.ctl_state.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.ctl_state)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)

        self.horizontalLayout_8.addWidget(self.label_4)

        self.step_posi = QDoubleSpinBox(self.centralwidget)
        self.step_posi.setObjectName(u"step_posi")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.step_posi.sizePolicy().hasHeightForWidth())
        self.step_posi.setSizePolicy(sizePolicy1)
        self.step_posi.setDecimals(3)
        self.step_posi.setSingleStep(0.001000000000000)
        self.step_posi.setValue(0.003000000000000)

        self.horizontalLayout_8.addWidget(self.step_posi)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)

        self.horizontalLayout_9.addWidget(self.label_5)

        self.step_angle = QDoubleSpinBox(self.centralwidget)
        self.step_angle.setObjectName(u"step_angle")
        sizePolicy1.setHeightForWidth(self.step_angle.sizePolicy().hasHeightForWidth())
        self.step_angle.setSizePolicy(sizePolicy1)
        self.step_angle.setDecimals(3)
        self.step_angle.setSingleStep(0.001000000000000)
        self.step_angle.setValue(0.003000000000000)

        self.horizontalLayout_9.addWidget(self.step_angle)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_9)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)

        self.horizontalLayout_15.addWidget(self.label_10)

        self.step_posi_vel = QDoubleSpinBox(self.centralwidget)
        self.step_posi_vel.setObjectName(u"step_posi_vel")
        sizePolicy1.setHeightForWidth(self.step_posi_vel.sizePolicy().hasHeightForWidth())
        self.step_posi_vel.setSizePolicy(sizePolicy1)
        self.step_posi_vel.setSingleStep(0.100000000000000)
        self.step_posi_vel.setValue(0.100000000000000)

        self.horizontalLayout_15.addWidget(self.step_posi_vel)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)

        self.horizontalLayout_16.addWidget(self.label_11)

        self.step_angle_vel = QDoubleSpinBox(self.centralwidget)
        self.step_angle_vel.setObjectName(u"step_angle_vel")
        sizePolicy1.setHeightForWidth(self.step_angle_vel.sizePolicy().hasHeightForWidth())
        self.step_angle_vel.setSizePolicy(sizePolicy1)
        self.step_angle_vel.setDecimals(2)
        self.step_angle_vel.setSingleStep(0.010000000000000)
        self.step_angle_vel.setValue(0.200000000000000)

        self.horizontalLayout_16.addWidget(self.step_angle_vel)


        self.horizontalLayout_15.addLayout(self.horizontalLayout_16)


        self.verticalLayout_2.addLayout(self.horizontalLayout_15)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_7.addLayout(self.verticalLayout_2)

        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.verticalLayout_3.setStretch(0, 2)
        self.verticalLayout_3.setStretch(2, 2)

        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        DemoWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(DemoWindow)
        self.statusbar.setObjectName(u"statusbar")
        DemoWindow.setStatusBar(self.statusbar)

        self.retranslateUi(DemoWindow)

        QMetaObject.connectSlotsByName(DemoWindow)
    # setupUi

    def retranslateUi(self, DemoWindow):
        DemoWindow.setWindowTitle(QCoreApplication.translate("DemoWindow", u"\u6f14\u793a", None))
        self.act_setting.setText(QCoreApplication.translate("DemoWindow", u"\u8bbe\u7f6e", None))
#if QT_CONFIG(tooltip)
        self.act_setting.setToolTip(QCoreApplication.translate("DemoWindow", u"\u6253\u5f00\u8bbe\u7f6e\u9875", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.act_setting.setShortcut(QCoreApplication.translate("DemoWindow", u"Ctrl+,", None))
#endif // QT_CONFIG(shortcut)
        self.act_gripper.setText(QCoreApplication.translate("DemoWindow", u"\u5939\u722a\u5f00\u5408", None))
        self.lb_left.setText("")
        self.lb_right.setText("")
        self.msg.setText("")
        self.btn_clear.setText(QCoreApplication.translate("DemoWindow", u"x", None))
        self.label.setText(QCoreApplication.translate("DemoWindow", u"\u6570\u636e\u96c6\u76ee\u5f55", None))
        self.dataset_dir.setText(QCoreApplication.translate("DemoWindow", u"tmp/data", None))
#if QT_CONFIG(tooltip)
        self.btn_open_dir.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_open_dir.setStatusTip(QCoreApplication.translate("DemoWindow", u"\u6253\u5f00\u6570\u636e\u96c6\u76ee\u5f55", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.btn_open_dir.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.btn_open_dir.setText(QCoreApplication.translate("DemoWindow", u"\u6253\u5f00", None))
        self.btn_play.setText(QCoreApplication.translate("DemoWindow", u"\u56de\u5230\u96f6\u4f4d", None))
        self.btn_turb.setText(QCoreApplication.translate("DemoWindow", u"\u968f\u673a\u4f4d\u7f6e", None))
        self.btn_capture.setText(QCoreApplication.translate("DemoWindow", u"\u62cd\u6444", None))
        self.btn_gripper.setText(QCoreApplication.translate("DemoWindow", u"\u5939\u722a\u5f00\u5408", None))
#if QT_CONFIG(tooltip)
        self.btn_setting.setToolTip(QCoreApplication.translate("DemoWindow", u"\u4fee\u6539\u5feb\u6377\u952e\u548c\u521d\u59cb\u5316\u865a\u62df\u73af\u5883\u72b6\u6001", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_setting.setStatusTip(QCoreApplication.translate("DemoWindow", u"\u4fee\u6539\u5feb\u6377\u952e\u548c\u521d\u59cb\u5316\u865a\u62df\u73af\u5883\u72b6\u6001", None))
#endif // QT_CONFIG(statustip)
        self.btn_setting.setText(QCoreApplication.translate("DemoWindow", u"\u8bbe\u7f6e", None))
        self.label_2.setText(QCoreApplication.translate("DemoWindow", u"\u6a21\u5f0f", None))
        self.rb_keyboard.setText(QCoreApplication.translate("DemoWindow", u"\u952e\u76d8", None))
        self.rb_spacemouse.setText(QCoreApplication.translate("DemoWindow", u"SpaceMouse", None))
        self.rb_iphone.setText(QCoreApplication.translate("DemoWindow", u"iPhone", None))
        self.rb_io.setText(QCoreApplication.translate("DemoWindow", u"IO \u52a8\u6355", None))
        self.is_keyboard_ctrl.setText(QCoreApplication.translate("DemoWindow", u"\u9065\u64cd\u4f5c\u4f7f\u80fd", None))
        self.is_collect_data.setText(QCoreApplication.translate("DemoWindow", u"\u91c7\u96c6\u8f68\u8ff9", None))
        self.is_mirror.setText(QCoreApplication.translate("DemoWindow", u"\u955c\u50cf\u64cd\u63a7\u6a21\u5f0f", None))
        self.label_3.setText(QCoreApplication.translate("DemoWindow", u"\u63a7\u5236\u72b6\u6001", None))
#if QT_CONFIG(statustip)
        self.ctl_state.setStatusTip(QCoreApplication.translate("DemoWindow", u"\u52fe\u9009\u9065\u64cd\u4f5c\u540e\u5728\u6b64\u663e\u793a\u63a7\u5236\u547d\u4ee4", None))
#endif // QT_CONFIG(statustip)
        self.ctl_state.setText(QCoreApplication.translate("DemoWindow", u"\u6682\u65e0\u63a7\u5236\u72b6\u6001", None))
        self.label_4.setText(QCoreApplication.translate("DemoWindow", u"\u4f4d\u7f6e\u589e\u91cf\uff08m\uff09", None))
        self.label_5.setText(QCoreApplication.translate("DemoWindow", u"\u89d2\u5ea6\u589e\u91cf\uff08rad\uff09", None))
        self.label_10.setText(QCoreApplication.translate("DemoWindow", u"\u7ebf\u901f\u5ea6", None))
        self.label_11.setText(QCoreApplication.translate("DemoWindow", u"\u89d2\u901f\u5ea6", None))
    # retranslateUi

