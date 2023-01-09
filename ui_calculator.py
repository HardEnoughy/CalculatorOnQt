# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculator.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import rc_resource

class Ui_main_window(object):
    def setupUi(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName(u"main_window")
        main_window.resize(300, 500)
        main_window.setMinimumSize(QSize(300, 500))
        icon = QIcon()
        icon.addFile(u":/images/calculate_p.png", QSize(), QIcon.Normal, QIcon.Off)
        main_window.setWindowIcon(icon)
        main_window.setStyleSheet(u"QWidget {\n"
"	color: white;\n"
"	background-color: #121212;\n"
"	font-family: Rubik;\n"
"	font-size: 16pt;\n"
"	font-weight: 600;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: transparent;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #666;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #888;\n"
"}")
        self.main_v_layout = QWidget(main_window)
        self.main_v_layout.setObjectName(u"main_v_layout")
        self.verticalLayout = QVBoxLayout(self.main_v_layout)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.main_display = QLabel(self.main_v_layout)
        self.main_display.setObjectName(u"main_display")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_display.sizePolicy().hasHeightForWidth())
        self.main_display.setSizePolicy(sizePolicy)
        self.main_display.setStyleSheet(u"color: #888;")
        self.main_display.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.main_display)

        self.answer_line = QLineEdit(self.main_v_layout)
        self.answer_line.setObjectName(u"answer_line")
        sizePolicy.setHeightForWidth(self.answer_line.sizePolicy().hasHeightForWidth())
        self.answer_line.setSizePolicy(sizePolicy)
        self.answer_line.setStyleSheet(u"font-size: 40pt;\n"
"border: none;")
        self.answer_line.setMaxLength(16)
        self.answer_line.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.answer_line.setReadOnly(True)

        self.verticalLayout.addWidget(self.answer_line)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.divide_button = QPushButton(self.main_v_layout)
        self.divide_button.setObjectName(u"divide_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.divide_button.sizePolicy().hasHeightForWidth())
        self.divide_button.setSizePolicy(sizePolicy1)
        self.divide_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.divide_button.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.divide_button, 0, 3, 1, 1)

        self.five_button = QPushButton(self.main_v_layout)
        self.five_button.setObjectName(u"five_button")
        sizePolicy1.setHeightForWidth(self.five_button.sizePolicy().hasHeightForWidth())
        self.five_button.setSizePolicy(sizePolicy1)
        self.five_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.five_button.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.five_button, 2, 1, 1, 1)

        self.equal_button = QPushButton(self.main_v_layout)
        self.equal_button.setObjectName(u"equal_button")
        sizePolicy1.setHeightForWidth(self.equal_button.sizePolicy().hasHeightForWidth())
        self.equal_button.setSizePolicy(sizePolicy1)
        self.equal_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.equal_button.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.equal_button, 4, 3, 1, 1)

        self.c_button = QPushButton(self.main_v_layout)
        self.c_button.setObjectName(u"c_button")
        sizePolicy1.setHeightForWidth(self.c_button.sizePolicy().hasHeightForWidth())
        self.c_button.setSizePolicy(sizePolicy1)
        self.c_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.c_button.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.c_button, 0, 0, 1, 1)

        self.one_button = QPushButton(self.main_v_layout)
        self.one_button.setObjectName(u"one_button")
        sizePolicy1.setHeightForWidth(self.one_button.sizePolicy().hasHeightForWidth())
        self.one_button.setSizePolicy(sizePolicy1)
        self.one_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.one_button.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.one_button, 3, 0, 1, 1)

        self.eight_button = QPushButton(self.main_v_layout)
        self.eight_button.setObjectName(u"eight_button")
        sizePolicy1.setHeightForWidth(self.eight_button.sizePolicy().hasHeightForWidth())
        self.eight_button.setSizePolicy(sizePolicy1)
        self.eight_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.eight_button.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.eight_button, 1, 1, 1, 1)

        self.ch_sign_button = QPushButton(self.main_v_layout)
        self.ch_sign_button.setObjectName(u"ch_sign_button")
        sizePolicy1.setHeightForWidth(self.ch_sign_button.sizePolicy().hasHeightForWidth())
        self.ch_sign_button.setSizePolicy(sizePolicy1)
        self.ch_sign_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.ch_sign_button.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.ch_sign_button, 4, 0, 1, 1)

        self.ce_button = QPushButton(self.main_v_layout)
        self.ce_button.setObjectName(u"ce_button")
        sizePolicy1.setHeightForWidth(self.ce_button.sizePolicy().hasHeightForWidth())
        self.ce_button.setSizePolicy(sizePolicy1)
        self.ce_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.ce_button.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.ce_button, 0, 1, 1, 1)

        self.zero_button = QPushButton(self.main_v_layout)
        self.zero_button.setObjectName(u"zero_button")
        sizePolicy1.setHeightForWidth(self.zero_button.sizePolicy().hasHeightForWidth())
        self.zero_button.setSizePolicy(sizePolicy1)
        self.zero_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.zero_button.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.zero_button, 4, 1, 1, 1)

        self.three_button = QPushButton(self.main_v_layout)
        self.three_button.setObjectName(u"three_button")
        sizePolicy1.setHeightForWidth(self.three_button.sizePolicy().hasHeightForWidth())
        self.three_button.setSizePolicy(sizePolicy1)
        self.three_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.three_button.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.three_button, 3, 2, 1, 1)

        self.seven_button = QPushButton(self.main_v_layout)
        self.seven_button.setObjectName(u"seven_button")
        sizePolicy1.setHeightForWidth(self.seven_button.sizePolicy().hasHeightForWidth())
        self.seven_button.setSizePolicy(sizePolicy1)
        self.seven_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.seven_button.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.seven_button, 1, 0, 1, 1)

        self.nine_button = QPushButton(self.main_v_layout)
        self.nine_button.setObjectName(u"nine_button")
        sizePolicy1.setHeightForWidth(self.nine_button.sizePolicy().hasHeightForWidth())
        self.nine_button.setSizePolicy(sizePolicy1)
        self.nine_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.nine_button.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.nine_button, 1, 2, 1, 1)

        self.multip_button = QPushButton(self.main_v_layout)
        self.multip_button.setObjectName(u"multip_button")
        sizePolicy1.setHeightForWidth(self.multip_button.sizePolicy().hasHeightForWidth())
        self.multip_button.setSizePolicy(sizePolicy1)
        self.multip_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.multip_button.setLayoutDirection(Qt.LeftToRight)
        self.multip_button.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.multip_button, 1, 3, 1, 1)

        self.six_button = QPushButton(self.main_v_layout)
        self.six_button.setObjectName(u"six_button")
        sizePolicy1.setHeightForWidth(self.six_button.sizePolicy().hasHeightForWidth())
        self.six_button.setSizePolicy(sizePolicy1)
        self.six_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.six_button.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.six_button, 2, 2, 1, 1)

        self.plus_button = QPushButton(self.main_v_layout)
        self.plus_button.setObjectName(u"plus_button")
        sizePolicy1.setHeightForWidth(self.plus_button.sizePolicy().hasHeightForWidth())
        self.plus_button.setSizePolicy(sizePolicy1)
        self.plus_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.plus_button.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.plus_button, 3, 3, 1, 1)

        self.four_button = QPushButton(self.main_v_layout)
        self.four_button.setObjectName(u"four_button")
        sizePolicy1.setHeightForWidth(self.four_button.sizePolicy().hasHeightForWidth())
        self.four_button.setSizePolicy(sizePolicy1)
        self.four_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.four_button.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.four_button, 2, 0, 1, 1)

        self.esc_button = QPushButton(self.main_v_layout)
        self.esc_button.setObjectName(u"esc_button")
        sizePolicy1.setHeightForWidth(self.esc_button.sizePolicy().hasHeightForWidth())
        self.esc_button.setSizePolicy(sizePolicy1)
        self.esc_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.esc_button.setLayoutDirection(Qt.LeftToRight)
        icon1 = QIcon()
        icon1.addFile(u":/images/backspace_p.png", QSize(), QIcon.Normal, QIcon.Off)
        self.esc_button.setIcon(icon1)
        self.esc_button.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.esc_button, 0, 2, 1, 1)

        self.two_button = QPushButton(self.main_v_layout)
        self.two_button.setObjectName(u"two_button")
        sizePolicy1.setHeightForWidth(self.two_button.sizePolicy().hasHeightForWidth())
        self.two_button.setSizePolicy(sizePolicy1)
        self.two_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.two_button.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.two_button, 3, 1, 1, 1)

        self.minus_button = QPushButton(self.main_v_layout)
        self.minus_button.setObjectName(u"minus_button")
        sizePolicy1.setHeightForWidth(self.minus_button.sizePolicy().hasHeightForWidth())
        self.minus_button.setSizePolicy(sizePolicy1)
        self.minus_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.minus_button.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.minus_button, 2, 3, 1, 1)

        self.dot_button = QPushButton(self.main_v_layout)
        self.dot_button.setObjectName(u"dot_button")
        sizePolicy1.setHeightForWidth(self.dot_button.sizePolicy().hasHeightForWidth())
        self.dot_button.setSizePolicy(sizePolicy1)
        self.dot_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.dot_button.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.dot_button, 4, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        main_window.setCentralWidget(self.main_v_layout)

        self.retranslateUi(main_window)

        QMetaObject.connectSlotsByName(main_window)
    # setupUi

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("main_window", u"Calculator", None))
        self.main_display.setText("")
        self.answer_line.setText(QCoreApplication.translate("main_window", u"0", None))
        self.divide_button.setText(QCoreApplication.translate("main_window", u"/", None))
        self.five_button.setText(QCoreApplication.translate("main_window", u"5", None))
        self.equal_button.setText(QCoreApplication.translate("main_window", u"=", None))
        self.c_button.setText(QCoreApplication.translate("main_window", u"C", None))
        self.one_button.setText(QCoreApplication.translate("main_window", u"1", None))
        self.eight_button.setText(QCoreApplication.translate("main_window", u"8", None))
        self.ch_sign_button.setText(QCoreApplication.translate("main_window", u"+/-", None))
        self.ce_button.setText(QCoreApplication.translate("main_window", u"CE", None))
        self.zero_button.setText(QCoreApplication.translate("main_window", u"0", None))
        self.three_button.setText(QCoreApplication.translate("main_window", u"3", None))
        self.seven_button.setText(QCoreApplication.translate("main_window", u"7", None))
        self.nine_button.setText(QCoreApplication.translate("main_window", u"9", None))
        self.multip_button.setText(QCoreApplication.translate("main_window", u"*", None))
        self.six_button.setText(QCoreApplication.translate("main_window", u"6", None))
        self.plus_button.setText(QCoreApplication.translate("main_window", u"+", None))
        self.four_button.setText(QCoreApplication.translate("main_window", u"4", None))
        self.esc_button.setText("")
        self.two_button.setText(QCoreApplication.translate("main_window", u"2", None))
        self.minus_button.setText(QCoreApplication.translate("main_window", u"-", None))
        self.dot_button.setText(QCoreApplication.translate("main_window", u".", None))
    # retranslateUi

