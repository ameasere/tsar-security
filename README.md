<p align="center">
  <a href="https://enigmapr0ject.live" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/RCd6ef2.jpg" alt="Project logo"></a>
</p>

<h3 align="center">tsar-security</h3>

---

<p align="center"> Tsar, Security Vault successor to Solitaire Security.
    <br> 
</p>

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Deployment](#deployment)
- [Usage](#usage)
- [Built Using](#built_using)
- [TODO](../TODO.md)
- [Contributing](../CONTRIBUTING.md)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## About <a name = "about"></a>

Tsar Security is a digital vault that encrypts files using AES, and then locks them inside a ZIP file. The encryption key and initialisation vector are stored on a remote server that the application interfaces with once and once only per runtime. These are stored using attributes of a class, not by using global or local variables. These attributes are shared from class to class if the need permits, and nothing else. Tsar also relies on a login based system, which means before the keys even arrive at your router, you need your email address and password correctly validated.

Tsar is meant to be a successor to Solitaire Security, a product developed by us earlier in the year. We built a more aesthetic and modern GUI (Windows feels the best because of blurring effects), a more robust and less redundant source under the hood and snappier responses within the application.

## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

-First, install Python 3 (we use Python 3.9) and make sure it is added to PATH.
-Open CMD, enter in: `pip3 install pyside2 blurwindow pandas pyminizip ruamel.std.encryptedzip requests PyCryptodomex` and hit enter. For the first time, you will get the error that pyminizip needs Visual C++ Build Tools. Once these are installed (it does provide a link), then try running the above command again.
-Run the EXE or the main.py file

You will need your API key found <a href="https://enigmapr0ject.live/tsar">here</a> from when you registered as a beta tester (once beta testing ends, these become defunct) and place it into the api.key file, or change the API key through the login screen of Tsar.

### Prerequisites

What things you need to install the software and how to install them.

```
Python 3 (preferably 3.9)
Pyminizip
ruamelmod
PySide2
Pandas
BlurWindow
Requests
PyCryptodomex
Optionally: QT Designer
```

### Installing

Step 1: Install Python from <a href="https://python.org">here</a>.
Step 2: Run the Python installer and make sure to tick "Add Python 3 to PATH" on the first screen.
Step 3: Open up Command Prompt with Run or by searchbar.
Step 4: Enter in `pip3 install pyside2 blurwindow pandas pyminizip ruamel.std.encryptedzip requests PyCryptodomex`.
Step 5: If prompted, install C++ Build Tools as required by `pyminizip`.
Step 6: Run Tsar by .exe or by main.py

Your final result should look like this:

<img width=200px height=200px src="https://i.imgur.com/qHJFXa3.png" alt="Tsar Login Screen">

## 🔧 Running the tests <a name = "tests"></a>


```
-Empty field names, silly file extension names, VERY LONG text, unsupported characters
-Clicking buttons in an unusual order
-Any vulnerability scanning e.g key intercepting, keylogging etc.
```

## Usage <a name="usage"></a>

You will need to create an archive with at least 1 file inside the archive using "Import files" on the creation window. Empty archives will break the entire concept. Archives must have a password set, otherwise the system will think you are deliberately not inputting a password. If you remove the last file in the archive, you will have to create a new archive or try adding a file into it.

There is a currently known issue with how Python handles zip files. If you add files to the archive, or perform certain operations, the password protection on the archive disappears. <b>After every edit to the archive, please press "Relock Archive". This enables new password protection using the old password.</b>

## Deployment <a name = "deployment"></a>

Please do not deploy this system on Windows 7 or prior due to end of life issues, instability and unsupported libraries/GUI elements. Some old hardware may also struggle to handle this software.

## Built Using <a name = "built_using"></a>

- [PHPMyAdmin](https://www.phpmyadmin.net/) - Database Management
- [MySQL](https://mysql.com/) - Database
- [Qt5](https://www.qt.io/) - Graphical Engine
- [TEP API](https://enigmapr0ject.live/) - Server API
- [Mailgun](https://www.mailgun.com/) - Email API
- [Twilio](https://www.twilio.com/) - 2 Factor Authentication

## Authors <a name = "authors"></a>

- [@projectintel-anon](https://github.com/projectintel-anon) - Founder, Developer
- [@Viibrant](https://github.com/Viibrant) - Linux Developer, Cross Platform Support and Major Contributor

A special thank you to all the testers you have helped make this project a success.

## Acknowledgements <a name = "acknowledgement"></a>

- Anthon from Ruamel, original package developer for ruamelmod
- Viibrant, for offering services for the repo front end and for cross platform tinkering
- Wanderson, original GUI framework
