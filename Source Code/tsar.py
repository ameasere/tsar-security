# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tsar.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import assets_rc

class Ui_Tsar(object):
    def setupUi(self, Tsar):
        if not Tsar.objectName():
            Tsar.setObjectName(u"Tsar")
        Tsar.resize(1075, 599)
        self.centralwidget = QWidget(Tsar)
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
        self.label_credits.setGeometry(QRect(850, 0, 201, 41))
        self.label_credits.setFont(font)
        self.label_credits.setStyleSheet(u"color: rgba(239, 0, 156, 255);\n"
"background-color: rgba(255, 255, 255, 0); ")
        self.label_credits.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_credits_3 = QLabel(self.dropShadowFrame)
        self.label_credits_3.setObjectName(u"label_credits_3")
        self.label_credits_3.setGeometry(QRect(350, 10, 141, 21))
        font1 = QFont()
        font1.setFamily(u"Consolas")
        font1.setPointSize(10)
        self.label_credits_3.setFont(font1)
        self.label_credits_3.setStyleSheet(u"color: rgba(239, 0, 156, 255);\n"
"background-color: rgba(255, 255, 255, 0); ")
        self.label_credits_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.changelog_3 = QLabel(self.dropShadowFrame)
        self.changelog_3.setObjectName(u"changelog_3")
        self.changelog_3.setGeometry(QRect(810, 0, 241, 231))
        font2 = QFont()
        font2.setFamily(u"Consolas")
        font2.setPointSize(20)
        self.changelog_3.setFont(font2)
        self.changelog_3.setStyleSheet(u"color: rgb(3, 198, 252);\n"
"background-color: rgba(255, 255, 255, 0); ")
        self.changelog_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.exitButton = QPushButton(self.dropShadowFrame)
        self.exitButton.setObjectName(u"exitButton")
        self.exitButton.setGeometry(QRect(970, 550, 75, 23))
        font3 = QFont()
        font3.setFamily(u"Consolas")
        self.exitButton.setFont(font3)
        self.exitButton.setStyleSheet(u"color: rgba(255, 255, 255, 255);\n"
"background-color: rgba(239, 0, 156, 255);")
        self.response = QLabel(self.dropShadowFrame)
        self.response.setObjectName(u"response")
        self.response.setGeometry(QRect(230, 210, 181, 41))
        self.response.setFont(font1)
        self.response.setStyleSheet(u"color: rgba(239, 0, 156, 255);\n"
"background-color: rgba(255, 255, 255, 0); ")
        self.response.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_credits_4 = QLabel(self.dropShadowFrame)
        self.label_credits_4.setObjectName(u"label_credits_4")
        self.label_credits_4.setGeometry(QRect(860, 300, 141, 21))
        self.label_credits_4.setFont(font1)
        self.label_credits_4.setStyleSheet(u"color: rgba(239, 0, 156, 255);\n"
"background-color: rgba(255, 255, 255, 0); ")
        self.label_credits_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.keylabel = QLabel(self.dropShadowFrame)
        self.keylabel.setObjectName(u"keylabel")
        self.keylabel.setGeometry(QRect(780, 330, 261, 31))
        self.keylabel.setFont(font1)
        self.keylabel.setStyleSheet(u"color: rgb(3, 198, 252);\n"
"background-color: rgba(255, 255, 255, 0); ")
        self.keylabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_credits_5 = QLabel(self.dropShadowFrame)
        self.label_credits_5.setObjectName(u"label_credits_5")
        self.label_credits_5.setGeometry(QRect(860, 370, 141, 21))
        self.label_credits_5.setFont(font1)
        self.label_credits_5.setStyleSheet(u"color: rgba(239, 0, 156, 255);\n"
"background-color: rgba(255, 255, 255, 0); ")
        self.label_credits_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.ivlabel = QLabel(self.dropShadowFrame)
        self.ivlabel.setObjectName(u"ivlabel")
        self.ivlabel.setGeometry(QRect(780, 410, 261, 31))
        self.ivlabel.setFont(font1)
        self.ivlabel.setStyleSheet(u"color: rgb(3, 198, 252);\n"
"background-color: rgba(255, 255, 255, 0); ")
        self.ivlabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ivreveal = QCheckBox(self.dropShadowFrame)
        self.ivreveal.setObjectName(u"ivreveal")
        self.ivreveal.setGeometry(QRect(940, 450, 70, 17))
        self.keyreveal = QCheckBox(self.dropShadowFrame)
        self.keyreveal.setObjectName(u"keyreveal")
        self.keyreveal.setGeometry(QRect(850, 450, 81, 17))
        self.label_credits_6 = QLabel(self.dropShadowFrame)
        self.label_credits_6.setObjectName(u"label_credits_6")
        self.label_credits_6.setGeometry(QRect(860, 230, 141, 21))
        self.label_credits_6.setFont(font1)
        self.label_credits_6.setStyleSheet(u"color: rgba(239, 0, 156, 255);\n"
"background-color: rgba(255, 255, 255, 0); ")
        self.label_credits_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.userlabel = QLabel(self.dropShadowFrame)
        self.userlabel.setObjectName(u"userlabel")
        self.userlabel.setGeometry(QRect(780, 260, 261, 31))
        self.userlabel.setFont(font1)
        self.userlabel.setStyleSheet(u"color: rgb(3, 198, 252);\n"
"background-color: rgba(255, 255, 255, 0); ")
        self.userlabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.createArchiveButton = QPushButton(self.dropShadowFrame)
        self.createArchiveButton.setObjectName(u"createArchiveButton")
        self.createArchiveButton.setGeometry(QRect(0, 460, 171, 23))
        self.createArchiveButton.setFont(font3)
        self.createArchiveButton.setStyleSheet(u"color: rgba(255, 255, 255, 255);\n"
"background-color: rgba(239, 0, 156, 255);")
        self.dashlabel = QLabel(self.dropShadowFrame)
        self.dashlabel.setObjectName(u"dashlabel")
        self.dashlabel.setGeometry(QRect(10, 70, 791, 371))
        self.dashlabel.setFont(font1)
        self.dashlabel.setStyleSheet(u"color: rgb(3, 198, 252);\n"
"background-color: rgba(255, 255, 255, 0); ")
        self.dashlabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.modifyArchiveButton = QPushButton(self.dropShadowFrame)
        self.modifyArchiveButton.setObjectName(u"modifyArchiveButton")
        self.modifyArchiveButton.setGeometry(QRect(0, 490, 171, 23))
        self.modifyArchiveButton.setFont(font3)
        self.modifyArchiveButton.setStyleSheet(u"color: rgba(255, 255, 255, 255);\n"
"background-color: rgba(239, 0, 156, 255);")
        self.displayArchiveButton = QPushButton(self.dropShadowFrame)
        self.displayArchiveButton.setObjectName(u"displayArchiveButton")
        self.displayArchiveButton.setGeometry(QRect(0, 520, 171, 23))
        self.displayArchiveButton.setFont(font3)
        self.displayArchiveButton.setStyleSheet(u"color: rgba(255, 255, 255, 255);\n"
"background-color: rgba(239, 0, 156, 255);")
        self.deleteArchiveButton = QPushButton(self.dropShadowFrame)
        self.deleteArchiveButton.setObjectName(u"deleteArchiveButton")
        self.deleteArchiveButton.setGeometry(QRect(180, 460, 171, 23))
        self.deleteArchiveButton.setFont(font3)
        self.deleteArchiveButton.setStyleSheet(u"color: rgba(255, 255, 255, 255);\n"
"background-color: rgba(239, 0, 156, 255);")
        self.refreshButton = QPushButton(self.dropShadowFrame)
        self.refreshButton.setObjectName(u"refreshButton")
        self.refreshButton.setGeometry(QRect(880, 550, 75, 23))
        self.refreshButton.setFont(font3)
        self.refreshButton.setStyleSheet(u"color: rgba(255, 255, 255, 255);\n"
"background-color: rgba(239, 0, 156, 255);")
        self.extractArchiveButton = QPushButton(self.dropShadowFrame)
        self.extractArchiveButton.setObjectName(u"extractArchiveButton")
        self.extractArchiveButton.setGeometry(QRect(0, 550, 171, 23))
        self.extractArchiveButton.setFont(font3)
        self.extractArchiveButton.setStyleSheet(u"color: rgba(255, 255, 255, 255);\n"
"background-color: rgba(239, 0, 156, 255);")
        self.relockArchiveButton = QPushButton(self.dropShadowFrame)
        self.relockArchiveButton.setObjectName(u"relockArchiveButton")
        self.relockArchiveButton.setGeometry(QRect(180, 490, 171, 23))
        self.relockArchiveButton.setFont(font3)
        self.relockArchiveButton.setStyleSheet(u"color: rgba(255, 255, 255, 255);\n"
"background-color: rgba(239, 0, 156, 255);")

        self.verticalLayout.addWidget(self.dropShadowFrame)

        Tsar.setCentralWidget(self.centralwidget)

        self.retranslateUi(Tsar)

        QMetaObject.connectSlotsByName(Tsar)
    # setupUi

    def retranslateUi(self, Tsar):
        Tsar.setWindowTitle(QCoreApplication.translate("Tsar", u"SoarGuide", None))
        self.label_title.setText(QCoreApplication.translate("Tsar", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Tsar</span></p></body></html>", None))
        self.label_credits.setText(QCoreApplication.translate("Tsar", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Created</span><span style=\" font-size:12pt;\">: enigmapr0ject</span></p></body></html>", None))
        self.label_credits_3.setText(QCoreApplication.translate("Tsar", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; font-style:italic;\">Dashboard</span></p></body></html>", None))
        self.changelog_3.setText(QCoreApplication.translate("Tsar", u"<html><head/><body><p><img src=\":/icon/iconfile.ico\"/></p></body></html>", None))
        self.exitButton.setText(QCoreApplication.translate("Tsar", u"Exit", None))
        self.response.setText(QCoreApplication.translate("Tsar", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_credits_4.setText(QCoreApplication.translate("Tsar", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; font-style:italic;\">CBC Key</span></p></body></html>", None))
        self.keylabel.setText(QCoreApplication.translate("Tsar", u"<html><head/><body><p align=\"center\"><span style=\" font-style:italic;\"><br/></span></p></body></html>", None))
        self.label_credits_5.setText(QCoreApplication.translate("Tsar", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; font-style:italic;\">CBC IV</span></p></body></html>", None))
        self.ivlabel.setText(QCoreApplication.translate("Tsar", u"<html><head/><body><p align=\"center\"><span style=\" font-style:italic;\"><br/></span></p></body></html>", None))
        self.ivreveal.setText(QCoreApplication.translate("Tsar", u"Reveal IV", None))
        self.keyreveal.setText(QCoreApplication.translate("Tsar", u"Reveal Key", None))
        self.label_credits_6.setText(QCoreApplication.translate("Tsar", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; font-style:italic;\">User</span></p></body></html>", None))
        self.userlabel.setText(QCoreApplication.translate("Tsar", u"<html><head/><body><p align=\"center\"><span style=\" font-style:italic;\"><br/></span></p></body></html>", None))
        self.createArchiveButton.setText(QCoreApplication.translate("Tsar", u"Create New Archive", None))
        self.dashlabel.setText(QCoreApplication.translate("Tsar", u"<html><head/><body><p><br/></p></body></html>", None))
        self.modifyArchiveButton.setText(QCoreApplication.translate("Tsar", u"Modify Existing Archive", None))
        self.displayArchiveButton.setText(QCoreApplication.translate("Tsar", u"Display Contents of Archive", None))
        self.deleteArchiveButton.setText(QCoreApplication.translate("Tsar", u"Delete Existing Archive", None))
        self.refreshButton.setText(QCoreApplication.translate("Tsar", u"Refresh", None))
        self.extractArchiveButton.setText(QCoreApplication.translate("Tsar", u"Extract Existing Archive", None))
        self.relockArchiveButton.setText(QCoreApplication.translate("Tsar", u"Re-lock Archive", None))
    # retranslateUi

