# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(471, 273)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(6, 6, 6, 6)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.RR = QWidget()
        self.RR.setObjectName(u"RR")
        self.verticalLayout_3 = QVBoxLayout(self.RR)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.decimal_input = QTextEdit(self.RR)
        self.decimal_input.setObjectName(u"decimal_input")
        self.decimal_input.setMaximumSize(QSize(16777215, 23))
        self.decimal_input.setInputMethodHints(Qt.ImhDigitsOnly)
        self.decimal_input.setLineWrapMode(QTextEdit.NoWrap)

        self.verticalLayout_3.addWidget(self.decimal_input)

        self.line = QFrame(self.RR)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.output_frame = QFrame(self.RR)
        self.output_frame.setObjectName(u"output_frame")
        self.output_frame.setFrameShape(QFrame.StyledPanel)
        self.output_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.output_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.fraction_display = QFrame(self.output_frame)
        self.fraction_display.setObjectName(u"fraction_display")
        self.fraction_display.setFrameShape(QFrame.StyledPanel)
        self.fraction_display.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.fraction_display)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.fraction_subframe = QFrame(self.fraction_display)
        self.fraction_subframe.setObjectName(u"fraction_subframe")
        self.fraction_subframe.setFrameShape(QFrame.StyledPanel)
        self.fraction_subframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.fraction_subframe)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.numerator = QLabel(self.fraction_subframe)
        self.numerator.setObjectName(u"numerator")
        font = QFont()
        font.setFamily(u"Times New Roman")
        font.setPointSize(22)
        self.numerator.setFont(font)
        self.numerator.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.numerator)

        self.faction_line = QFrame(self.fraction_subframe)
        self.faction_line.setObjectName(u"faction_line")
        self.faction_line.setFrameShape(QFrame.HLine)
        self.faction_line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.faction_line)

        self.denominator = QLabel(self.fraction_subframe)
        self.denominator.setObjectName(u"denominator")
        self.denominator.setFont(font)
        self.denominator.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.denominator)


        self.horizontalLayout_3.addWidget(self.fraction_subframe)

        self.equal_sign = QLabel(self.fraction_display)
        self.equal_sign.setObjectName(u"equal_sign")
        self.equal_sign.setMaximumSize(QSize(37, 16777215))
        self.equal_sign.setFont(font)
        self.equal_sign.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.equal_sign)

        self.eval = QLabel(self.fraction_display)
        self.eval.setObjectName(u"eval")
        palette = QPalette()
        brush = QBrush(QColor(139, 139, 139, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        self.eval.setPalette(palette)
        font1 = QFont()
        font1.setFamily(u"Times New Roman")
        font1.setPointSize(12)
        self.eval.setFont(font1)
        self.eval.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.eval)


        self.verticalLayout_2.addWidget(self.fraction_display)

        self.line_3 = QFrame(self.output_frame)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_3)

        self.fraction_output = QFrame(self.output_frame)
        self.fraction_output.setObjectName(u"fraction_output")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fraction_output.sizePolicy().hasHeightForWidth())
        self.fraction_output.setSizePolicy(sizePolicy)
        self.fraction_output.setFrameShape(QFrame.StyledPanel)
        self.fraction_output.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.fraction_output)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.fraction_text = QTextBrowser(self.fraction_output)
        self.fraction_text.setObjectName(u"fraction_text")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.fraction_text.sizePolicy().hasHeightForWidth())
        self.fraction_text.setSizePolicy(sizePolicy1)
        self.fraction_text.setMaximumSize(QSize(16777215, 31))
        self.fraction_text.setLineWrapMode(QTextEdit.FixedColumnWidth)

        self.horizontalLayout_2.addWidget(self.fraction_text)

        self.latex_checkbox = QCheckBox(self.fraction_output)
        self.latex_checkbox.setObjectName(u"latex_checkbox")

        self.horizontalLayout_2.addWidget(self.latex_checkbox)


        self.verticalLayout_2.addWidget(self.fraction_output)


        self.verticalLayout_3.addWidget(self.output_frame)

        self.tabWidget.addTab(self.RR, "")
        self.Q2RR_ = QWidget()
        self.Q2RR_.setObjectName(u"Q2RR_")
        self.tabWidget.addTab(self.Q2RR_, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.decimal_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter repeating decimal...", None))
        self.numerator.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:26pt;\">N</span><span style=\" font-size:12pt;\">umerator</span></p></body></html>", None))
        self.denominator.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:26pt;\">D</span><span style=\" font-size:12pt;\">enominator</span></p></body></html>", None))
        self.equal_sign.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.eval.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">No repeats so far: keep typing</p></body></html>", None))
        self.latex_checkbox.setText(QCoreApplication.translate("MainWindow", u"Latex Code", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.RR), QCoreApplication.translate("MainWindow", u"Determine Repeats", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Q2RR_), QCoreApplication.translate("MainWindow", u"Repeating Rational to Fraction", None))
    # retranslateUi

