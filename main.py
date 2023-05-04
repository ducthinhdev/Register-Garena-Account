# CODE BY ĐỨC THỊNH OFFICIAL | SHARE NHỚ GHI NGUỒN VÀO NHÉ =))
# BOX ZALO : https://zalo.me/g/tidfru278
from PyQt5.QtWidgets import QTextEdit, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
import requests,time,threading,os,sys
from tkinter import messagebox
import random,string
def generate_random_string(length):
    allowed_chars = string.ascii_lowercase + string.digits
    random_string = ''.join(random.choice(allowed_chars) for i in range(length))
    return random_string
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(603, 283)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/logo.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("background-color:rgb(85, 255, 0)")
        self.fSaveAcc = QtWidgets.QTextEdit(parent=Form)
        self.fSaveAcc.setGeometry(QtCore.QRect(280, 10, 311, 261))
        self.fSaveAcc.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.fSaveAcc.setObjectName("fSaveAcc")
        self.groupBox = QtWidgets.QGroupBox(parent=Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 261, 161))
        self.groupBox.setStyleSheet("background-color:rgb(85, 255, 255)")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 71, 21))
        self.label.setObjectName("label")
        self.fUser = QtWidgets.QLineEdit(parent=self.groupBox)
        self.fUser.setGeometry(QtCore.QRect(90, 20, 151, 20))
        self.fUser.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.fUser.setObjectName("fUser")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 120, 91, 21))
        self.label_2.setObjectName("label_2")
        self.fRandomUser = QtWidgets.QCheckBox(parent=self.groupBox)
        self.fRandomUser.setGeometry(QtCore.QRect(90, 50, 70, 17))
        self.fRandomUser.setObjectName("fRandomUser")
        self.fStartTime = QtWidgets.QSpinBox(parent=self.groupBox)
        self.fStartTime.setGeometry(QtCore.QRect(110, 120, 42, 22))
        self.fStartTime.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.fStartTime.setObjectName("fStartTime")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(160, 120, 41, 21))
        self.label_3.setObjectName("label_3")
        self.fStopTime = QtWidgets.QSpinBox(parent=self.groupBox)
        self.fStopTime.setGeometry(QtCore.QRect(200, 120, 42, 22))
        self.fStopTime.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.fStopTime.setObjectName("fStopTime")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 80, 151, 21))
        self.label_4.setObjectName("label_4")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=Form)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 180, 261, 91))
        self.groupBox_2.setStyleSheet("background-color:rgb(85, 255, 255)")
        self.groupBox_2.setObjectName("groupBox_2")
        self.fButtonStart = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.fButtonStart.setGeometry(QtCore.QRect(30, 30, 75, 31))
        self.fButtonStart.setStyleSheet("background-color:rgb(255, 255, 0)")
        self.fButtonStart.setObjectName("fButtonStart")
        self.fButtonStop = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.fButtonStop.setGeometry(QtCore.QRect(140, 30, 75, 31))
        self.fButtonStop.setStyleSheet("background-color:rgb(255, 0, 0)")
        self.fButtonStop.setObjectName("fButtonStop")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.fButtonStart.clicked.connect(self.fMain)
        self.fButtonStop.clicked.connect(self.fStop)
    def fMain(self):
        threading.Thread(target=self.main).start()
    def fStop(self):
        sys.exit()
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Register Garena Account | Đức Thịnh Official"))
        self.groupBox.setTitle(_translate("Form", "Settings"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; color:#aa0000;\">UserName : </span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; color:#aa0000;\">Username Từ : </span></p></body></html>"))
        self.fRandomUser.setText(_translate("Form", "Random"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; color:#aa0000;\">Tới : </span></p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; color:#aa0000;\">Password : </span><span style=\" font-size:10pt; color:#000000;\">Thinh@2006</span></p></body></html>"))
        self.groupBox_2.setTitle(_translate("Form", "Button"))
        self.fButtonStart.setText(_translate("Form", "Start"))
        self.fButtonStop.setText(_translate("Form", "Stop"))
    def fReg(self,username,email):
        cookies = {
            '_ga': 'GA1.1.910981480.1679139514',
            '_ga_1M7M9L6VPX': 'GS1.1.1679139514.1.1.1679139710.0.0.0',
            'datadome': '11GCr2AARrY5rvpDm~LLjMsvJfIZhGaJogm5bCs7Rh0cThm1tGQm9xBFoL~UAWJT-LvmJMXPE1WedLvWlOIyNtdrCxajSi0w1PtkG4g1Ls5isQsjaWOskc0PXD5If38Y',
        }

        headers = {
            'Accept': 'application/json, text/javascript, /; q=0.01',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'Cookie': '_ga=GA1.1.910981480.1679139514; _ga_1M7M9L6VPX=GS1.1.1679139514.1.1.1679139710.0.0.0; datadome=11GCr2AARrY5rvpDm~LLjMsvJfIZhGaJogm5bCs7Rh0cThm1tGQm9xBFoL~UAWJT-LvmJMXPE1WedLvWlOIyNtdrCxajSi0w1PtkG4g1Ls5isQsjaWOskc0PXD5If38Y',
            'Origin': 'https://sso.garena.com',
            'Referer': 'https://sso.garena.com/ui/register?locale=vi',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'x-datadome-clientid': '11GCr2AARrY5rvpDm~LLjMsvJfIZhGaJogm5bCs7Rh0cThm1tGQm9xBFoL~UAWJT-LvmJMXPE1WedLvWlOIyNtdrCxajSi0w1PtkG4g1Ls5isQsjaWOskc0PXD5If38Y',
        }

        data = {
            'username': username,
            'email': email,
            'password': 'add06aede0fb8bc4a5256582c77fcb92da4db46a0895b03d1c22dfd36ada8b0974dd3af5e251195d050572fb22dee9c74682c7c4d200757e2f33405ea3dd4613cfb2852d296e64333b877283c893cc6ac5f807873e8c271c58eb4bf4cc7a2f6844dbc3ec524d3e7b4eafd0a3058fa4a0c096b6181289679693e8513e33ec8a79',
            'location': 'VI',
            'redirect_uri': '',
            'locale': 'vi',
            'mobile_no': '',
            'otp': '',
            'format': 'json',
            'id': '1679139732819',
        }

        response = requests.post('https://sso.garena.com/api/register', cookies=cookies, headers=headers, data=data).json()
        try:
            if response['username']==username:
                print(f'{username}|Thinh@2006')
                self.fSaveAcc.append(f'{username}|Thinh@2006')
                time.sleep(0.75)
            else:
                print(f'{username}|Error')
                self.fSaveAcc.append(f'{username}|Error')
        except:
            messagebox.showerror("Lỗi","UserName Đã Tồn Tại !")
    def main(self):
        if self.fRandomUser.isChecked():
            luong1 = self.fStartTime.value()
            luong2 = self.fStopTime.value()
            for luong1 in range(luong2):
                username = generate_random_string(8)
                email = generate_random_string(12) +'@gmail.com'
                threading.Thread(target=self.fReg,args=(username,email,)).start()
        else:
            luong1 = self.fStartTime.value()
            luong2 = self.fStopTime.value()
            us = self.fUser.text()
            for luong1 in range(luong2):
                username = us+str(luong1)
                email = username+'@gmail.com'
                threading.Thread(target=self.fReg,args=(username,email,)).start()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
