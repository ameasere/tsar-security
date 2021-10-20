# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'createArchive.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import assets_rc

class Ui_createArchiveGUI(object):
    def setupUi(self, createArchiveGUI):
        if not createArchiveGUI.objectName():
            createArchiveGUI.setObjectName(u"createArchiveGUI")
        createArchiveGUI.resize(590, 354)
        icon = QIcon()
        icon.addFile(u"iconfile.ico", QSize(), QIcon.Normal, QIcon.Off)
        createArchiveGUI.setWindowIcon(icon)
        self.centralwidget = QWidget(createArchiveGUI)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.dropShadowFrame = QFrame(self.centralwidget)
        self.dropShadowFrame.setObjectName(u"dropShadowFrame")
        self.dropShadowFrame.setStyleSheet(u"QFrame {	\n"
"	background-color: rgba(255, 255, 255, .15);\n"
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
        self.closeButton.setGeometry(QRect(490, 310, 75, 23))
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
        self.label_credits_6 = QLabel(self.dropShadowFrame)
        self.label_credits_6.setObjectName(u"label_credits_6")
        self.label_credits_6.setGeometry(QRect(10, 60, 281, 21))
        self.label_credits_6.setFont(font1)
        self.label_credits_6.setStyleSheet(u"color: rgba(239, 0, 156, 255);\n"
"background-color: rgba(255, 255, 255, 0); ")
        self.label_credits_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.zipName = QLineEdit(self.dropShadowFrame)
        self.zipName.setObjectName(u"zipName")
        self.zipName.setGeometry(QRect(10, 90, 261, 20))
        self.label_credits_7 = QLabel(self.dropShadowFrame)
        self.label_credits_7.setObjectName(u"label_credits_7")
        self.label_credits_7.setGeometry(QRect(10, 140, 281, 21))
        self.label_credits_7.setFont(font1)
        self.label_credits_7.setStyleSheet(u"color: rgba(239, 0, 156, 255);\n"
"background-color: rgba(255, 255, 255, 0); ")
        self.label_credits_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.zipDirectory = QLineEdit(self.dropShadowFrame)
        self.zipDirectory.setObjectName(u"zipDirectory")
        self.zipDirectory.setGeometry(QRect(10, 170, 261, 20))
        self.selectFolder = QPushButton(self.dropShadowFrame)
        self.selectFolder.setObjectName(u"selectFolder")
        self.selectFolder.setGeometry(QRect(290, 170, 91, 23))
        self.selectFolder.setFont(font2)
        self.selectFolder.setStyleSheet(u"color: rgba(255, 255, 255, 255);\n"
"background-color: rgba(239, 0, 156, 255);")
        self.label_credits_8 = QLabel(self.dropShadowFrame)
        self.label_credits_8.setObjectName(u"label_credits_8")
        self.label_credits_8.setGeometry(QRect(10, 220, 281, 21))
        self.label_credits_8.setFont(font1)
        self.label_credits_8.setStyleSheet(u"color: rgba(239, 0, 156, 255);\n"
"background-color: rgba(255, 255, 255, 0); ")
        self.label_credits_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.zipPassword = QLineEdit(self.dropShadowFrame)
        self.zipPassword.setObjectName(u"zipPassword")
        self.zipPassword.setGeometry(QRect(10, 260, 261, 20))
        self.createZip = QPushButton(self.dropShadowFrame)
        self.createZip.setObjectName(u"createZip")
        self.createZip.setGeometry(QRect(380, 310, 91, 23))
        self.createZip.setFont(font2)
        self.createZip.setStyleSheet(u"color: rgba(255, 255, 255, 255);\n"
"background-color: rgba(239, 0, 156, 255);")
        self.feedback = QLabel(self.dropShadowFrame)
        self.feedback.setObjectName(u"feedback")
        self.feedback.setGeometry(QRect(320, 50, 231, 91))
        self.feedback.setFont(font1)
        self.feedback.setStyleSheet(u"color: rgb(3, 198, 252);\n"
"background-color: rgba(255, 255, 255, 0); ")
        self.feedback.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.importFiles = QPushButton(self.dropShadowFrame)
        self.importFiles.setObjectName(u"importFiles")
        self.importFiles.setGeometry(QRect(280, 310, 91, 23))
        self.importFiles.setFont(font2)
        self.importFiles.setStyleSheet(u"color: rgba(255, 255, 255, 255);\n"
"background-color: rgba(239, 0, 156, 255);")

        self.verticalLayout.addWidget(self.dropShadowFrame)

        createArchiveGUI.setCentralWidget(self.centralwidget)

        self.retranslateUi(createArchiveGUI)

        QMetaObject.connectSlotsByName(createArchiveGUI)
    # setupUi

    def retranslateUi(self, createArchiveGUI):
        createArchiveGUI.setWindowTitle(QCoreApplication.translate("createArchiveGUI", u"Tsar", None))
        self.label_title.setText(QCoreApplication.translate("createArchiveGUI", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Tsar</span></p></body></html>", None))
        self.label_credits.setText(QCoreApplication.translate("createArchiveGUI", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Created</span><span style=\" font-size:12pt;\">: enigmapr0ject</span></p></body></html>", None))
        self.label_credits_3.setText(QCoreApplication.translate("createArchiveGUI", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; font-style:italic;\">Create Archive</span></p></body></html>", None))
        self.closeButton.setText(QCoreApplication.translate("createArchiveGUI", u"Close", None))
        self.response.setText(QCoreApplication.translate("createArchiveGUI", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_credits_6.setText(QCoreApplication.translate("createArchiveGUI", u"<html><head/><body><p><span style=\" font-weight:600; font-style:italic;\">Name of archive (with .zip at the end)</span></p></body></html>", None))
        self.label_credits_7.setText(QCoreApplication.translate("createArchiveGUI", u"<html><head/><body><p><span style=\" font-weight:600; font-style:italic;\">Directory to create into</span></p></body></html>", None))
        self.selectFolder.setText(QCoreApplication.translate("createArchiveGUI", u"Select Folder", None))
        self.label_credits_8.setText(QCoreApplication.translate("createArchiveGUI", u"<html><head/><body><p><span style=\" font-weight:600; font-style:italic;\">Password to encrypt with</span></p></body></html>", None))
        self.createZip.setText(QCoreApplication.translate("createArchiveGUI", u"Create", None))
        self.feedback.setText(QCoreApplication.translate("createArchiveGUI", u"<html><head/><body><p><br/></p></body></html>", None))
        self.importFiles.setText(QCoreApplication.translate("createArchiveGUI", u"Import Files", None))
    # retranslateUi

