<p align="center">
  <a href="https://enigmapr0ject.live" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/RCd6ef2.jpg" alt="Project logo"></a>
 <h2 align="center"><b>tsar-security</b></h3>
</p>
</p>

<p align="center">
  <img width=627px height=372px src="https://i.imgur.com/qHJFXa3.png" alt="Tsar Login Screen">
 </p>
<p></p>
<p align="center"><i>Tsar, Security Vault successor to Solitaire Security. </i>
</p>

## Table of Contents


- [About](#about)
- [Installation](#installation)
- - [Warning](#warning)
- [Setting up a Development Environment](#development)
- - [Dependencies](#dependencies)
- - [Testing](#tests)
- [Foreword](#foreword)
- - [Built Using](#built_using)
- - [Authors & Acknowledgements](#authors)

## About <a name = "about"></a>


Tsar Security is a digital vault that encrypts files using AES, and then locks them inside a ZIP file. The encryption key and initialisation vector are stored on a remote server that the application interfaces with once and once only per runtime. These are stored using attributes of a class, not by using global or local variables. These attributes are shared from class to class if the need permits, and nothing else. Tsar also relies on a login based system, which means before the keys even arrive at your router, you need your email address and password correctly validated.

Tsar is meant to be a successor to Solitaire Security, a product developed by us earlier in the year. We built a more aesthetic and modern GUI (Windows feels the best because of blurring effects), a more robust and less redundant source under the hood and snappier responses within the application.

## **Installing** <a name="installation"></a>

The releases are available <a href=https://github.com/projectintel-anon/tsar-security/releases> here.</a>  

Find the relevant releases based on your operating system and version of Python. If your system is not supported, then please refer to [this](#binary)

### Warning <a name = "warning"></a>

Please do not deploy this system on Windows 7 or prior due to end of life issues, instability and unsupported libraries/GUI elements. Some old hardware may also struggle to handle this software.

There is a currently known issue with how Python handles zip files. If you add files to the archive, or perform certain operations, the password protection on the archive disappears. <b>After every edit to the archive, please press "Relock Archive". This enables new password protection using the old password </b>

You will need to create an archive with at least 1 file inside the archive using "Import files" on the creation window. Empty archives will break the entire concept. Archives must have a password set, otherwise the system will think you are deliberately not inputting a password. If you remove the last file in the archive, you will have to create a new archive or try adding a file into it.
  
## Setting up a Development Environment <a name= "development"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### **Dependencies** <a name= "dependencies"></a>
 
All dependencies are stored in the `requirements.txt` file.

```
Python 3 (preferably 3.9)

Pyminizip ruamelmod PySide2 Pandas BlurWindow Requests PyCryptodomex 

Optionally: QT Designer
```

Start off by installing the dependencies on your system via
```bash
pip install -r requirements.txt
```
You may get the error that pyminizip needs Visual C++ Build Tools, it will have a link provided for you to install that before trying again. 

You will need your API key found <a href="https://enigmapr0ject.live/tsar">here</a> from when you registered as a beta tester. Place it into the api.key file, or change the API key through the login screen of Tsar.
  
### 🔧 Running the tests <a name = "tests"></a>

*Implement automated testing...*
```
-Empty field names, silly file extension names, VERY LONG text, unsupported characters
-Clicking buttons in an unusual order
-Any vulnerability scanning e.g key intercepting, keylogging etc.
```
  
### Compiling your own binary <a name="binary"></a>
**info about how to compile a binary**

## Foreword <a name="foreword"></a>

### Built Using <a name = "built_using"></a>

- [PHPMyAdmin](https://www.phpmyadmin.net/) - Database Management
- [MySQL](https://mysql.com/) - Database
- [Qt5](https://www.qt.io/) - Graphical Engine
- [Qt Designer](https://www.qt.io/product) - UI Designer
- [TEP API](https://enigmapr0ject.live/) - Server API
- [Mailgun](https://www.mailgun.com/) - Email API
- [Twilio](https://www.twilio.com/) - 2 Factor Authentication

### Authors & Acknowledgements <a name = "authors"></a>

- [@projectintel-anon](https://github.com/projectintel-anon) - Founder, Developer
- [@Viibrant](https://github.com/Viibrant) - Linux Developer, Cross Platform Support and Major Contributor

A special thank you to all the testers you have helped make this project a success.

- Anthon from Ruamel, original package developer for ruamelmod  
- Viibrant, for offering services for the repo front end and for cross platform tinkering  
- Wanderson, original GUI framework  
