# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addFilesToZIP.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import assets_rc

class Ui_addFilesGUI(object):
    def setupUi(self, addFilesGUI):
        if not addFilesGUI.objectName():
            addFilesGUI.setObjectName(u"addFilesGUI")
        addFilesGUI.resize(590, 168)
        self.centralwidget = QWidget(addFilesGUI)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.dropShadowFrame = QFrame(self.centralwidget)
        self.dropShadowFrame.setObjectName(u"dropShadowFrame")
        self.dropShadowFrame.setStyleSheet(u"QFrame {	\n"
"	background-color: rgba(255, 255, 255, .15);  \n"
"    backdrop-filter: blur(1.5rem);\n"
"}")
        self.dropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QFrame.Raised)
        self.label_title = QLabel(self.dropShadowFrame)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(-10, -10, 91, 61))
        font = QFont()
        font.setFamily(u"Consolas")
        font.setPointSize(40)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"color: rgb(3, 198, 252);\n"
"background-color: rgba(255, 255, 255, 0); ")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_credits = QLabel(self.dropShadowFrame)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setGeometry(QRect(360, 0, 201, 41))
        self.label_credits.setFont(font)
        self.label_credits.setStyleSheet(u"color: rgba(239, 0, 156, 255);\n"
"background-color: rgba(255, 255, 255, 0); ")
        self.label_credits.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_credits_3 = QLabel(self.dropShadowFrame)
        self.label_credits_3.setObjectName(u"label_credits_3")
        self.label_credits_3.setGeometry(QRect(150, 10, 141, 21))
        font1 = QFont()
        font1.setFamily(u"Consolas")
        font1.setPointSize(10)
        self.label_credits_3.setFont(font1)
        self.label_credits_3.setStyleSheet(u"color: rgba(239, 0, 156, 255);\n"
"background-color: rgba(255, 255, 255, 0); ")
        self.label_credits_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.closeButton = QPushButton(self.dropShadowFrame)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setGeometry(QRect(210, 120, 91, 23))
        font2 = QFont()
        font2.setFamily(u"Consolas")
        self.closeButton.setFont(font2)
        self.closeButton.setStyleSheet(u"color: rgba(255, 255, 255, 255);\n"
"background-color: rgba(239, 0, 156, 255);")
        self.response = QLabel(self.dropShadowFrame)
        self.response.setObjectName(u"response")
        self.response.setGeometry(QRect(230, 210, 181, 41))
        self.response.setFont(font1)
        self.response.setStyleSheet(u"color: rgba(239, 0, 156, 255);\n"
"background-color: rgba(255, 255, 255, 0); ")
        self.response.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.feedback = QLabel(self.dropShadowFrame)
        self.feedback.setObjectName(u"feedback")
        self.feedback.setGeometry(QRect(320, 50, 231, 91))
        self.feedback.setFont(font1)
        self.feedback.setStyleSheet(u"color: rgba(3, 198, 252, 255);\n"
"background-color: rgba(255, 255, 255, 0); ")
        self.feedback.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.importFiles = QPushButton(self.dropShadowFrame)
        self.importFiles.setObjectName(u"importFiles")
        self.importFiles.setGeometry(QRect(10, 60, 121, 23))
        self.importFiles.setFont(font2)
        self.importFiles.setStyleSheet(u"color: rgba(255, 255, 255, 255);\n"
"background-color: rgba(239, 0, 156, 255);")
        self.addAllFiles = QPushButton(self.dropShadowFrame)
        self.addAllFiles.setObjectName(u"addAllFiles")
        self.addAllFiles.setGeometry(QRect(10, 90, 121, 23))
        self.addAllFiles.setFont(font2)
        self.addAllFiles.setStyleSheet(u"color: rgba(255, 255, 255, 255);\n"
"background-color: rgba(239, 0, 156, 255);")

        self.verticalLayout.addWidget(self.dropShadowFrame)

        addFilesGUI.setCentralWidget(self.centralwidget)

        self.retranslateUi(addFilesGUI)

        QMetaObject.connectSlotsByName(addFilesGUI)
    # setupUi

    def retranslateUi(self, addFilesGUI):
        addFilesGUI.setWindowTitle(QCoreApplication.translate("addFilesGUI", u"SoarGuide", None))
        self.label_title.setText(QCoreApplication.translate("addFilesGUI", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Tsar</span></p></body></html>", None))
        self.label_credits.setText(QCoreApplication.translate("addFilesGUI", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Created</span><span style=\" font-size:12pt;\">: enigmapr0ject</span></p></body></html>", None))
        self.label_credits_3.setText(QCoreApplication.translate("addFilesGUI", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; font-style:italic;\">Add Files</span></p></body></html>", None))
        self.closeButton.setText(QCoreApplication.translate("addFilesGUI", u"Close", None))
        self.response.setText(QCoreApplication.translate("addFilesGUI", u"<html><head/><body><p><br/></p></body></html>", None))
        self.feedback.setText(QCoreApplication.translate("addFilesGUI", u"<html><head/><body><p><br/></p></body></html>", None))
        self.importFiles.setText(QCoreApplication.translate("addFilesGUI", u"Import Files", None))
        self.addAllFiles.setText(QCoreApplication.translate("addFilesGUI", u"Add Selected Files", None))
    # retranslateUi

