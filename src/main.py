################################################################################
##
## BY: enigmapr0ject
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
################################################################################
import pyminizip, zipfile, ruamelmod, ntpath, base64, sys, webbrowser, time, requests, os, json
import pandas as pd
from BlurWindow.blurWindow import GlobalBlur
from Cryptodome.Cipher import AES
from ruamelmod import delete_from_zip_file
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent, QFile)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from PySide2.QtUiTools import QUiLoader
## ==> SPLASH SCREEN
from ui_splash_screen import Ui_SplashScreen
from internetfailed import Ui_FailedScreen
from signaturefailed import Ui_FailedScreen2
from mainui import Ui_main
from mainui2 import Ui_main2
from tsar import Ui_Tsar
from createZip import Ui_createArchiveGUI
from modifyZip import Ui_modifyArchiveGUI
from universal import Ui_enterpassword
from addFiles import Ui_addFilesGUI
from removeFiles import Ui_removeFilesGUI
from displayFiles import Ui_displayArchiveGUI
from renameArchive import Ui_renameArchiveGUI
from extractArchive import Ui_extractArchiveGUI
from apikey import Ui_apiwindow
## ==> GLOBALS
counter = 0
exceptionArray = []
passthrough = []
#
#BREADTH FIRST SEARCH#####
def breadthFirstFileScan( root ) :
    dirs = [root]
    # while we has dirs to scan
    while len(dirs) :
        nextDirs = []
        for parent in dirs :
            # scan each dir
            for f in os.listdir( parent ) :
                # if there is a dir, then save for next ittr
                # if it  is a file then yield it (we'll return later)
                ff = os.path.join( parent, f )
                if os.path.isdir( ff ) :
                    nextDirs.append( ff )
                else :
                    yield ff
        # once we've done all the current dirs then
        # we set up the next itter as the child dirs
        # from the current itter.
        dirs = nextDirs
#######################################
def getAPIKey():
    with open("api.key", "r") as apifile:
        api_key = apifile.read().rstrip()
        apifile.close()
    return api_key
# UNIVERSAL
class AddFilesToArchive(QMainWindow):
    def __init__(self, archiveName, archivePW, key, iv):
        QMainWindow.__init__(self)
        self.ui = Ui_addFilesGUI()
        self.ui.setupUi(self)
        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)
        hWnd = self.winId()
        GlobalBlur(hWnd)
        self.ui.importFiles.clicked.connect(self.importFiles)
        self.ui.addAllFiles.clicked.connect(self.addToArchive)
        self.ui.closeButton.clicked.connect(self.fade)
        self.filestobeadded = [] 
        self.filearray = []
        self.archiveName = archiveName
        self.archivePW = bytes(archivePW, encoding="utf-8")
        self.key = key
        self.iv = iv
    def importFiles(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()","", "All Files (*)",options=options)
        if fileName:
            self.filestobeadded.append(fileName)
            self.ui.feedback.setText("Added: " + fileName)
    def addToArchive(self):
        z = zipfile.ZipFile(self.archiveName, 'a')
        z.setpassword(self.archivePW)
        def path_leaf(path):  # Splits path names into tails and heads
            head, tail = ntpath.split(path)
            return tail or ntpath.basename(head)
        try:
            os.mkdir("temp")
            for file in self.filestobeadded:
                with open(file, "rb") as plaintextFile:
                    contents = plaintextFile.read()
                    plaintextFile.close()
                data = base64.b64encode(contents)
                cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
                length = 16 - (len(data) % 16)
                data += bytes([length]) * length
                ciphertext = cipher.encrypt(data)
                newName = path_leaf(file)
                with open(newName, "wb") as newFile:
                    newFile.write(ciphertext)
                    newFile.close()
                self.filearray.append(newName)
            archiveDest = self.archiveName
            status = os.stat(archiveDest)  # Display permissions
            status2 = oct(status.st_mode)[-3:]  # Convert to readable number
            fileSize = int(os.stat(archiveDest).st_size)
            fileSizeInMB = fileSize / (1024 * 1024)
            fileStats = "Inode/Dir size: " + str(fileSizeInMB) + "MB \n  Permissions: " + str(status2) + "\n  Added: " + str(len(self.filearray)) + " file(s)."
            for item in self.filearray:
                z.write(item)
                os.remove(item)
            os.rmdir("temp")
            z.close()
            passthrough.append(fileStats)
        except Exception as e:
            exceptionArray.append(repr(e))
            self.fade()
    def fade(self):
        for i in range(10):
            i = i / 10
            self.setWindowOpacity(1 - i)
            time.sleep(0.05)
        self.close()
# ADD FILES
class RemoveFilesFromArchive(QMainWindow):
    def __init__(self, archiveName, archivePW, key, iv):
        QMainWindow.__init__(self)
        self.ui = Ui_removeFilesGUI()
        self.ui.setupUi(self)
        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)
        hWnd = self.winId()
        GlobalBlur(hWnd)
        self.ui.closeButton.clicked.connect(self.fade)
        self.ui.removeAllFiles.clicked.connect(self.removeAllFiles)
        self.filestoberemoved = []
        self.filearray = []
        self.archiveName = archiveName
        self.archivePW = archivePW
        self.key = key
        self.iv = iv
        self.displayContents()
    def displayContents(self):
        z = zipfile.ZipFile(self.archiveName, 'a')
        z.setpassword(self.archivePW)
        contents = z.namelist()
        z.close()
        jsonFileContents = []
        for item in contents:
            nextJson = dict()
            nextJson["File"] = item
            nextJson["Permissions"] = "666"
            jsonFileContents.append(nextJson)
        jsonFileContents = str(json.dumps(jsonFileContents)).replace("[", " ").replace("]", " ")
        df = pd.read_json(jsonFileContents, lines=True)
        contentstable = df.to_html()
        if len(contents) > 5:
            Tsar.ui.dashlabel.setText(contentstable)
        else:
            self.ui.contentsLabel.setText(contentstable)
    def removeAllFiles(self):
        self.filelist = self.ui.filelist.text().replace(" ", "")
        self.filestoberemoved = self.filelist.split(",")
        try:
            delete_from_zip_file(self.archiveName, file_names=self.filestoberemoved, password=self.archivePW)
            self.ui.feedback.setText("Successfully removed: " + self.filelist + "\n You can safely close\n this window.")
        except Exception as e:
            self.ui.feedback.setText("Something went wrong.\n Refresh dashboard to see\nexception.")
            exceptionArray.append(repr(e))
            return 0
    def fade(self):
        for i in range(10):
            i = i / 10
            self.setWindowOpacity(1 - i)
            time.sleep(0.05)
        self.close()
class RenameZIP(QMainWindow):
    def __init__(self, filePath):
        QMainWindow.__init__(self)
        self.ui = Ui_renameArchiveGUI()
        self.ui.setupUi(self)
        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)
        hWnd = self.winId()
        GlobalBlur(hWnd)
        self.filePath = filePath
        self.ui.closeButton.clicked.connect(self.fade)
        self.ui.renameButton.clicked.connect(self.renameArchive)
    def renameArchive(self):
        self.newName = self.ui.zipName.text()
        if len(self.newName) < 1:
            self.ui.feedback.setText("Field empty.")
        else:
            def path_leaf(path):  # Splits path names into tails and heads
                head, tail = ntpath.split(path)
                return head
            newPath = path_leaf(self.filePath) + "/" + self.newName
            os.rename(self.filePath, newPath)
            self.ui.feedback.setText("Archive renamed.")
    def fade(self):
        for i in range(10):
            i = i / 10
            self.setWindowOpacity(1 - i)
            time.sleep(0.05)
        self.close()
class ExtractZipGUI(QMainWindow):
    def __init__(self, key, iv):
        QMainWindow.__init__(self)
        self.ui = Ui_extractArchiveGUI()
        self.ui.setupUi(self)
        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)
        hWnd = self.winId()
        GlobalBlur(hWnd)
        self.ui.closeButton.clicked.connect(self.fade)
        self.ui.selectArchiveButton.clicked.connect(self.selectArchive)
        self.ui.extractArchiveButton.clicked.connect(self.extractAndDecrypt)
        self.key = bytes(key, encoding="utf-8")
        self.iv = bytes(iv, encoding="utf-8")
    def selectArchive(self):
        options = QFileDialog.Options()
        self.fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "Zip Files (*.zip)", options=options)
        if self.fileName:
            self.ui.feedback.setText("Selected: " + self.fileName)
            time.sleep(0.3) #Prevents the blurring bug from happening
            self.passwordentry = EnterPassword4(self.fileName)
            self.passwordentry.show()
        else:
            self.ui.feedback.setText("No archive selected.")
            return 0
    def extractAndDecrypt(self):
        try:
            z = zipfile.ZipFile(self.fileName, 'a')
            z.setpassword(self.archivePassword)
            contents = z.namelist()
            tempdir = self.fileName.replace(".zip", "")
            tempdircontents = []
            os.mkdir(tempdir)
            z.extractall(tempdir)
            for item in contents:
                newitem = tempdir + "/" + item
                tempdircontents.append(newitem)
            for file in tempdircontents:
                with open(file, "rb") as encryptedfile:
                    encryptedcontents = encryptedfile.read()
                    encryptedfile.close()
                cipher2 = AES.new(self.key, AES.MODE_CBC, self.iv)  # New cipher object
                plaintext = cipher2.decrypt(encryptedcontents)  # plaintext = decrypted file contents
                data = plaintext[:-plaintext[-1]]  # Remove padding
                plaintext = data.decode('utf-8')  # Decode it
                plaintext = base64.b64decode(plaintext)  # Decode it again
                with open(file, "wb") as decryptfile:  # Open new file
                    decryptfile.write(plaintext)  # Write original data
                    decryptfile.close()  # Close it
            self.ui.feedback.setText("Archive extracted\n and decrypted.")
        except Exception as e:
            exceptionArray.append(repr(e))
            self.ui.feedback.setText("Something went wrong.\n Refresh dashboard to see\n error message.")
    def fade(self):
        for i in range(10):
            i = i / 10
            self.setWindowOpacity(1 - i)
            time.sleep(0.05)
        self.close()
class EnterPassword(QMainWindow):
    def __init__(self, zipPath):
        QMainWindow.__init__(self)
        self.ui = Ui_enterpassword()
        self.ui.setupUi(self)
        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)
        self.zipPath = zipPath
        hWnd = self.winId()
        GlobalBlur(hWnd)
        self.ui.enterButton.clicked.connect(self.returnPassword)
        self.ui.archivePassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui.closeButton.clicked.connect(self.fade)
    def returnPassword(self):
        archivePassword = bytes(self.ui.archivePassword.text(), encoding="utf-8")
        if len(archivePassword) < 1:
            self.ui.feedback.setText("Field empty.")
        else:
            z = zipfile.ZipFile(self.zipPath, 'a')
            contents = z.namelist()
            testfile = contents[0]
            try:
                z.extract(testfile, pwd=archivePassword)
                os.remove(testfile)
                z.close()
                ModifyZipGUI.archivePassword = archivePassword
                self.ui.feedback.setText("Archive password set.")
                self.fade()
            except Exception as e:
                exceptionArray.append(repr(e))
                self.ui.feedback.setText("Something went wrong.\n Refresh dashboard to see\nexception.")
                return 0
    def fade(self):
        for i in range(10):
            i = i / 10
            self.setWindowOpacity(1 - i)
            time.sleep(0.05)
        self.close()
class EnterPassword2(QMainWindow):
    def __init__(self, zipPath):
        QMainWindow.__init__(self)
        self.ui = Ui_enterpassword()
        self.ui.setupUi(self)
        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)
        self.zipPath = zipPath
        hWnd = self.winId()
        GlobalBlur(hWnd)
        self.ui.enterButton.clicked.connect(self.returnPassword)
        self.ui.archivePassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui.closeButton.clicked.connect(self.fade)
    def returnPassword(self):
        archivePassword = bytes(self.ui.archivePassword.text(), encoding="utf-8")
        if len(archivePassword) < 1:
            self.ui.feedback.setText("Field empty.")
        else:
            z = zipfile.ZipFile(self.zipPath, 'a')
            contents = z.namelist()
            testfile = contents[0]
            try:
                z.extract(testfile, pwd=archivePassword)
                os.remove(testfile)
                self.ui.feedback.setText("Archive password set.")
                z.close()
                self.fade()
                self.zipcontents = DisplayZipGUI(self.zipPath, archivePassword)
                self.zipcontents.show()
            except Exception as e:
                exceptionArray.append(repr(e))
                self.ui.feedback.setText("Something went wrong.\n Refresh dashboard to see\nexception.")
                return 0
    def fade(self):
        for i in range(10):
            i = i / 10
            self.setWindowOpacity(1 - i)
            time.sleep(0.05)
        self.close()
class EnterPassword3(QMainWindow):
    def __init__(self, zipPath):
        QMainWindow.__init__(self)
        self.ui = Ui_enterpassword()
        self.ui.setupUi(self)
        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)
        self.fileName = zipPath
        hWnd = self.winId()
        GlobalBlur(hWnd)
        self.ui.enterButton.clicked.connect(self.returnPassword)
        self.ui.archivePassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui.closeButton.clicked.connect(self.fade)
    def returnPassword(self):
        archivePassword = bytes(self.ui.archivePassword.text(), encoding="utf-8")
        self.archivePW = archivePassword
        if len(archivePassword) < 1:
            self.ui.feedback.setText("Field empty.")
        else:
            z = zipfile.ZipFile(self.fileName, 'a')
            contents = z.namelist()
            testfile = contents[0]
            try:
                z.extract(testfile, pwd=archivePassword)
                os.remove(testfile)
                self.ui.feedback.setText("Archive password set.")
                z.close()
                self.relock()
            except Exception as e:
                exceptionArray.append(repr(e))
                self.ui.feedback.setText("Something went wrong.\n Refresh dashboard to see\nexception.")
                return 0
    def relock(self):
        def path_leaf2(path):
            head, tail = ntpath.split(path)
            return head
        currentDir = path_leaf2(self.fileName)
        temporary = currentDir + "/relock"
        os.mkdir(temporary)
        z = zipfile.ZipFile(self.fileName, 'a')  # Set zipfile object
        z.setpassword(self.archivePW)  # Set password
        z.extractall(temporary)
        z.close()
        import random
        archiveNumbers = random.randint(0, 999999)
        self.oldName = self.fileName
        self.fileName = self.fileName.replace(".zip", "") + str(archiveNumbers) + ".zip"
        self.filelist = os.listdir(temporary)
        self.filelist2 = []
        for item in self.filelist:
            newitem = temporary + "/" + item
            self.filelist2.append(newitem)
        pyminizip.compress_multiple(self.filelist2, [], self.fileName, self.archivePW, 5)
        for item in self.filelist2:
            os.remove(item)
        os.rmdir(temporary)
        os.remove(self.oldName)
        archiveDest = self.fileName
        status = os.stat(archiveDest)  # Display permissions
        status2 = oct(status.st_mode)[-3:]  # Convert to readable number
        fileSize = int(os.stat(archiveDest).st_size)
        fileSizeInMB = fileSize / (1024 * 1024)
        fileStats = "  Inode/Dir size: " + str(fileSizeInMB) + "MB \n  Permissions: " + str(
            status2) + "\n  Contents: " + str(len(self.filelist)) + " file(s)."
        justMade = "Archive Made: " + archiveDest + "\n" + fileStats
        passthrough.append(justMade)
        self.ui.feedback.setText("Archive relocked. Refresh\n the dashboard to see stats.")
    def fade(self):
        for i in range(10):
            i = i / 10
            self.setWindowOpacity(1 - i)
            time.sleep(0.05)
        self.close()
class EnterPassword4(QMainWindow):
    def __init__(self, zipPath):
        QMainWindow.__init__(self)
        self.ui = Ui_enterpassword()
        self.ui.setupUi(self)
        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)
        self.zipPath = zipPath
        hWnd = self.winId()
        GlobalBlur(hWnd)
        self.ui.enterButton.clicked.connect(self.returnPassword)
        self.ui.archivePassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui.closeButton.clicked.connect(self.fade)
    def returnPassword(self):
        archivePassword = bytes(self.ui.archivePassword.text(), encoding="utf-8")
        if len(archivePassword) < 1:
            self.ui.feedback.setText("Field empty.")
        else:
            z = zipfile.ZipFile(self.zipPath, 'a')
            contents = z.namelist()
            testfile = contents[0]
            try:
                z.extract(testfile, pwd=archivePassword)
                os.remove(testfile)
                z.close()
                ExtractZipGUI.archivePassword = archivePassword
                self.ui.feedback.setText("Archive password set.")
                self.fade()
            except Exception as e:
                exceptionArray.append(repr(e))
                self.ui.feedback.setText("Something went wrong.\n Refresh dashboard to see\nexception.")
                return 0
    def fade(self):
        for i in range(10):
            i = i / 10
            self.setWindowOpacity(1 - i)
            time.sleep(0.05)
        self.close()
# YOUR APPLICATION
class Tsar(QMainWindow):
    def __init__(self, user, passwd):
        QMainWindow.__init__(self)
        self.ui = Ui_Tsar()
        self.ui.setupUi(self)
        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)
        hWnd = self.winId()
        GlobalBlur(hWnd)
        self.ui.exitButton.clicked.connect(self.exitApp)
        self.user = user
        self.ui.keylabel.setText("*******************************")
        self.ui.ivlabel.setText("****************")
        self.ui.userlabel.setText(self.user)
        self.getKeys(passwd)
        self.ui.keyreveal.stateChanged.connect(self.revealKey)
        self.ui.ivreveal.stateChanged.connect(self.revealIV)
        self.ui.refreshButton.clicked.connect(self.refreshDashboard)
        self.ui.createArchiveButton.clicked.connect(self.createArchive)
        self.ui.modifyArchiveButton.clicked.connect(self.modifyArchive)
        self.ui.displayArchiveButton.clicked.connect(self.displayArchive)
        self.ui.deleteArchiveButton.clicked.connect(self.deleteArchive)
        self.ui.relockArchiveButton.clicked.connect(self.relockArchive)
        self.ui.extractArchiveButton.clicked.connect(self.extractArchive)
    def refreshDashboard(self):
        if len(passthrough) > 0:
            dashlabeltext = passthrough[0]
            passthrough.pop(0)
            self.ui.dashlabel.setText(dashlabeltext)
        elif len(exceptionArray) > 0:
            dashlabeltext = exceptionArray[0]
            exceptionArray.pop(0)
            self.ui.dashlabel.setText(dashlabeltext)
        else:
            return 0
    def extractArchive(self):
        self.extractZipArchive = ExtractZipGUI(self.key, self.iv)
        self.extractZipArchive.show()
    def createArchive(self):
        self.createZipArchive = CreateZipGUI(self.key, self.iv)
        self.createZipArchive.show()
    def modifyArchive(self):
        self.modifyZipArchive = ModifyZipGUI(self.key, self.iv)
        self.modifyZipArchive.show()
    def displayArchive(self):
        options = QFileDialog.Options()
        self.fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "","Zip Files (*.zip)", options=options)
        if self.fileName:
            self.displayZipArchive = EnterPassword2(self.fileName)
            self.displayZipArchive.show()
        else:
            return 0
    def deleteArchive(self):
        options = QFileDialog.Options()
        self.fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "Zip Files (*.zip)",options=options)
        if self.fileName:
            os.remove(self.fileName)
            self.ui.dashlabel.setText("Deleted archive: " + self.fileName)
        else:
            return 0
    def relockArchive(self):
        options = QFileDialog.Options()
        self.fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "Zip Files (*.zip)",options=options)
        if self.fileName:
            self.relock = EnterPassword3(self.fileName)
            self.relock.show()
        else:
            return 0
    def getKeys(self, passwd):
        api_key = getAPIKey()
        jsonString = {"key": api_key, "Email": self.user, "Password": passwd}  # Create JSON object
        url = "https://enigmapr0ject.live/api/tsar/queryKeys.php/"  # URL
        headers = {}  # Blank headers
        r = requests.post(url, data=jsonString, headers=headers)  # set this to True when you set up
        # a valid SSL, this part relies on SSL/TLS encryption.
        response = r.content  # Get server response
        keyarray = response.decode('utf-8').split('\n')  # Decode it
        self.key = keyarray[0]
        self.iv = keyarray[1]
        keyarray = None
    def revealKey(self, state):
        if state == Qt.Checked:
            self.ui.keylabel.setText(self.key)
        else:
            self.ui.keylabel.setText("*******************************")
    def revealIV(self, state):
        if state == Qt.Checked:
            self.ui.ivlabel.setText(self.iv)
        else:
            self.ui.ivlabel.setText("****************")
    def exitApp(self):
        sys.exit(app.exec_())
# DISPLAY ARCHIVE WINDOW
class DisplayZipGUI(QMainWindow):
    def __init__(self, zipPath, archivePW):
        QMainWindow.__init__(self)
        self.ui = Ui_displayArchiveGUI()
        self.ui.setupUi(self)
        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)
        hWnd = self.winId()
        GlobalBlur(hWnd)
        self.archivePassword = archivePW
        self.zipPath = zipPath
        self.ui.closeButton.clicked.connect(self.fade)
        self.displayZIPContents()
    def displayZIPContents(self):
        if not hasattr(self, 'zipPath'):
            self.ui.feedback.setText("No archive selected.")
            return 0
        elif not hasattr(self, 'archivePassword'):
            self.ui.feedback.setText("No archive password set. Continuing anyway...")
        z = zipfile.ZipFile(self.zipPath, 'a')
        z.setpassword(self.archivePassword)
        contents = z.namelist()
        z.close()
        jsonFileContents = []
        for item in contents:
            nextJson = dict()
            nextJson["File"] = item
            nextJson["Permissions"] = "666"
            jsonFileContents.append(nextJson)
        jsonFileContents = str(json.dumps(jsonFileContents)).replace("[", " ").replace("]", " ")
        df = pd.read_json(jsonFileContents, lines=True)
        contentstable = df.to_html()
        if len(contents) > 15:
            Tsar.ui.dashlabel.setText(contentstable)
        else:
            self.ui.contentsLabel.setText(contentstable)
    def fade(self):
        for i in range(10):
            i = i / 10
            self.setWindowOpacity(1 - i)
            time.sleep(0.05)
        self.close()
# MODIFY ARCHIVE WINDOW
class ModifyZipGUI(QMainWindow):
    def __init__(self, key, iv):
        QMainWindow.__init__(self)
        self.ui = Ui_modifyArchiveGUI()
        self.ui.setupUi(self)
        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)
        hWnd = self.winId()
        GlobalBlur(hWnd)
        self.ui.closeButton.clicked.connect(self.fade)
        self.ui.selectArchiveButton.clicked.connect(self.selectArchive)
        self.ui.addFilesButton.clicked.connect(self.addFiles)
        self.ui.removeFilesButton.clicked.connect(self.removeFiles)
        self.ui.closeArchiveButton.clicked.connect(self.closeArchive)
        self.ui.renameArchiveButton.clicked.connect(self.renameArchive)
        self.key = bytes(key, encoding="utf-8")
        self.iv = bytes(iv, encoding="utf-8")
    def selectArchive(self):
        options = QFileDialog.Options()
        self.fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "Zip Files (*.zip)", options=options)
        if self.fileName:
            self.ui.feedback.setText("Selected: " + self.fileName)
            time.sleep(0.3) #Prevents the blurring bug from happening
            self.passwordentry = EnterPassword(self.fileName)
            self.passwordentry.show()
        else:
            self.ui.feedback.setText("No archive selected.")
            return 0
    def addFiles(self):
        if not hasattr(self, 'fileName'):
            self.ui.feedback.setText("No archive selected.")
            return 0
        elif not hasattr(self, 'archivePassword'):
            self.ui.feedback.setText("No archive password set. Continuing anyway...")
        self.AddFilesToZIP = AddFilesToArchive(self.fileName, self.archivePassword, self.key, self.iv)
        self.AddFilesToZIP.show()
    def removeFiles(self):
        if not hasattr(self, 'fileName'):
            self.ui.feedback.setText("No archive selected.")
            return 0
        elif not hasattr(self, 'archivePassword'):
            self.ui.feedback.setText("No archive password set. Continuing anyway...")
        self.RemoveFilesFromZIP = RemoveFilesFromArchive(self.fileName, self.archivePassword, self.key, self.iv)
        self.RemoveFilesFromZIP.show()
    def renameArchive(self):
        if not hasattr(self, 'fileName'):
            self.ui.feedback.setText("No archive selected.")
            return 0
        else:
            pass
        self.renameZIP = RenameZIP(self.fileName)
        self.renameZIP.show()
    def closeArchive(self):
        self.fileName = None
        options = None
        self.archivePassword = None
        self.ui.feedback.setText("Archive closed.")
    def fade(self):
        for i in range(10):
            i = i / 10
            self.setWindowOpacity(1 - i)
            time.sleep(0.05)
        self.close()
# CREATE ARCHIVE WINDOW
class CreateZipGUI(QMainWindow):
    def __init__(self, key, iv):
        QMainWindow.__init__(self)
        self.ui = Ui_createArchiveGUI()
        self.ui.setupUi(self)
        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)
        hWnd = self.winId()
        GlobalBlur(hWnd)
        self.ui.closeButton.clicked.connect(self.fade)
        self.ui.createZip.clicked.connect(self.createZip)
        self.ui.selectFolder.clicked.connect(self.chooseFolder)
        self.ui.importFiles.clicked.connect(self.importFiles)
        self.ui.zipPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.filestobeadded = []
        self.filearray = []
        self.key = bytes(key, encoding="utf-8")
        self.iv = bytes(iv, encoding="utf-8")
    def importFiles(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()","", "All Files (*)",options=options)
        if fileName:
            self.filestobeadded.append(fileName)
            self.ui.feedback.setText("Added: " + fileName)
    def chooseFolder(self):
        directoryName = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.ui.zipDirectory.setText(directoryName)
    def createZip(self):
        def path_leaf(path):
            head, tail = ntpath.split(path)  # Split the path into head and tail
            return tail or ntpath.basename(head)  # Only return the tail or base name of the head
        archiveName = self.ui.zipName.text()
        archiveDirectory = self.ui.zipDirectory.text()
        archivePassword = self.ui.zipPassword.text()
        if archiveName == "" or archivePassword == "" or archiveDirectory == "":
            self.ui.feedback.setText("Field/s empty.")
        elif len(self.filestobeadded) < 1:
            self.ui.feedback.setText("No imported files.")
        else:
            try:
                for f in breadthFirstFileScan(archiveDirectory):
                    if archiveName not in f:
                        continue
                    else:
                        self.ui.feedback.setText("Archive exists already.")
                        break
                os.mkdir("temp")
                for file in self.filestobeadded:
                    with open(file, "rb") as plaintextFile:
                        contents = plaintextFile.read()
                        plaintextFile.close()
                    data = base64.b64encode(contents)
                    cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
                    length = 16 - (len(data) % 16)
                    data += bytes([length]) * length
                    ciphertext = cipher.encrypt(data)
                    newName = path_leaf(file)
                    with open(newName, "wb") as newFile:
                        newFile.write(ciphertext)
                        newFile.close()
                    self.filearray.append(newName)
                pyminizip.compress_multiple(self.filearray, [], archiveDirectory + "/" + archiveName, archivePassword,5)
                for item in self.filearray:
                    os.remove(item)
                os.rmdir("temp")
                archiveDest = archiveDirectory + "/" + archiveName
                status = os.stat(archiveDest)  # Display permissions
                status2 = oct(status.st_mode)[-3:]  # Convert to readable number
                fileSize = int(os.stat(archiveDest).st_size)
                fileSizeInMB = fileSize/(1024*1024)
                fileStats = "  Inode/Dir size: " + str(fileSizeInMB) + "MB \n  Permissions: " + str(status2) + "\n  Contents: " + str(len(self.filearray)) + " file(s)."
                justMade = "Archive Made: " + archiveDest + "\n" + fileStats
                passthrough.append(justMade)
                self.fade()
            except Exception as e:
                self.fade()
                exceptionArray.append(repr(e))
    def fade(self):
        for i in range(10):
            i = i / 10
            self.setWindowOpacity(1 - i)
            time.sleep(0.05)
        self.close()
# KEY WINDOW
class APIKeyWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_apiwindow()
        self.ui.setupUi(self)
        # MAIN WINDOW LABEL
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)
        hWnd = self.winId()
        GlobalBlur(hWnd)
        with open("api.key", "r") as apifile:
            contents = apifile.read()
            apifile.close()
        self.ui.apibox.setText(contents)
        self.ui.writekey.clicked.connect(self.writekey)
        self.ui.exitButton.clicked.connect(self.fade)
    def writekey(self):
        with open("api.key", "w+") as apifile:
            apifile.write(self.ui.apibox.text())
            apifile.close()
        self.ui.apibox.setText(self.ui.apibox.text())
        self.ui.response.setText("Key set!")
    def fade(self):
        for i in range(10):
            i = i / 10
            self.setWindowOpacity(1 - i)
            time.sleep(0.05)
        self.close()
# LOGIN WINDOW
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_main()
        self.ui.setupUi(self)
        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)
        hWnd = self.winId()
        GlobalBlur(hWnd)
        self.ui.passbox.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui.exitButton.clicked.connect(self.exitApp)
        self.ui.registerButton.clicked.connect(self.registerWindow)
        self.ui.github.clicked.connect(self.github)
        self.ui.login.clicked.connect(self.loginUser)
        self.ui.manageKey.clicked.connect(self.manageKey)
    def manageKey(self):
        self.keywindow = APIKeyWindow()
        self.keywindow.show()
    def github(self):
        webbrowser.get().open("https://github.com/projectintel-anon/tsar-security")
    def registerWindow(self):
        for i in range(10):
            i = i / 10
            self.setWindowOpacity(1 - i)
            time.sleep(0.05)
        self.close()
        self.main = MainWindow2()
        self.main.show()
    def fade(self):
        for i in range(10):
            i = i / 10
            self.setWindowOpacity(1 - i)
            time.sleep(0.05)
        self.close()
    def loginUser(self):
        emailaddress = self.ui.userbox.text()
        userpass = self.ui.passbox.text()
        api_key = getAPIKey()
        jsonString = {"key": api_key, "Email": emailaddress, "Password": userpass}  # Create JSON object
        url = "https://enigmapr0ject.live/api/tsar/login.php/"  # URL
        headers = {}  # Blank headers
        r = requests.post(url, data=jsonString, headers=headers)  # set this to True when you set up
        # a valid SSL, this part relies on SSL/TLS encryption.
        response = r.content  # Get server response
        response = response.decode('utf-8')  # Decode it
        if response == "1":
            self.fade()
            self.main = Tsar(emailaddress, userpass)
            self.main.show()
        else:
            self.ui.response.setText(response)
    def exitApp(self):
        sys.exit(app.exec_())
# REGISTER WINDOW
class MainWindow2(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_main2()
        self.ui.setupUi(self)
        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)
        hWnd = self.winId()
        GlobalBlur(hWnd)
        self.ui.exitButton.clicked.connect(self.fade)
        self.ui.github.clicked.connect(self.github)
        self.ui.registerButton.clicked.connect(self.register)
        self.ui.loginButton.clicked.connect(self.loginWindow)
    def fade(self):
        for i in range(10):
            i = i / 10
            self.setWindowOpacity(1 - i)
            time.sleep(0.05)
        sys.exit(app.exec_())
    def github(self):
        webbrowser.get().open("https://github.com/projectintel-anon/tsar-security")
    def loginWindow(self):
        for i in range(10):
            i = i / 10
            self.setWindowOpacity(1 - i)
            time.sleep(0.05)
        self.close()
        self.main = MainWindow()
        self.main.show()
    def register(self):
        emailaddress = self.ui.emailbox.text()
        api_key = getAPIKey()
        jsonString = {"key": api_key, "Email": emailaddress}  # Create JSON object
        url = "https://enigmapr0ject.live/api/tsar/register.php/"  # URL
        headers = {}  # Blank headers
        r = requests.post(url, data=jsonString, headers=headers)  # set this to True when you set up
        # a valid SSL, this part relies on SSL/TLS encryption.
        response = r.content  # Get server response
        response = response.decode('utf-8')  # Decode it
        self.ui.response.setText(response)
# INTERNET FAILED SCREEN
class InternetFailed(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_FailedScreen()
        self.ui.setupUi(self)
        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)
        hWnd = self.winId()
        GlobalBlur(hWnd)
        self.ui.exitButton.clicked.connect(self.fade)
    def fade(self):
        for i in range(10):
            i = i / 10
            self.setWindowOpacity(1 - i)
            time.sleep(0.05)
        sys.exit(app.exec_())
# SIGNATURE FAILED SCREEN
class SignatureFailed(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_FailedScreen2()
        self.ui.setupUi(self)
        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)
        hWnd = self.winId()
        GlobalBlur(hWnd)
        self.ui.exitButton.clicked.connect(self.exitApp)
        self.ui.updateButton.clicked.connect(self.update)
        self.ui.continueButton.clicked.connect(self.proceed)
    def fade(self):
        for i in range(10):
            i = i / 10
            self.setWindowOpacity(1 - i)
            time.sleep(0.05)
        self.close()
    def exitApp(self):
        sys.exit(app.exec_())
    def update(self):
        webbrowser.get().open("https://enigmapr0ject.live/#projects")
    def proceed(self):
        self.fade()
        self.main = MainWindow()
        self.main.show()
# SPLASH SCREEN
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)
        ## UI ==> INTERFACE CODES
        ########################################################################

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)
        hWnd = self.winId()
        GlobalBlur(hWnd)
        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(35)

        # CHANGE DESCRIPTION

        # Initial Text
        self.ui.label_description.setText("<strong>WELCOME</strong> TO TSAR")

        # Change Texts
        QtCore.QTimer.singleShot(1500, lambda: self.ui.label_description.setText("<strong>LOCKING</strong> DATABASES"))
        QtCore.QTimer.singleShot(3000, lambda: self.ui.label_description.setText("<strong>SALTING</strong> HASHES"))
        # PREREQUISITE CHECKS
        try:
            internetCheck = requests.get("https://enigmapr0ject.live/files/donate.html").content.decode("utf-8")
        except Exception as e:
            self.internet = 0
        if internetCheck is not None:
            self.internet = 1
        signatureCheck = requests.post("https://enigmapr0ject.live/api/tsar/signature.php", data={"hash": "204907209B1ED469D2A01A9C356D52D6B3BD7061"}).content.decode("utf-8")
        if signatureCheck != "200":
            self.signature = 0
        else:
            self.signature = 1

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ## ==> APP FUNCTIONS
    ########################################################################

    def progress(self):

        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREEN AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            if self.internet == 0:
                self.main = InternetFailed()
                self.main.show()
            elif self.signature == 0:
                self.main = SignatureFailed()
                self.main.show()
            else:
                self.main = MainWindow()
                self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 1




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())
