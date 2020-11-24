
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QTextEdit, QDialog, QLineEdit
from PyQt5 import QtGui
from PyQt5.QtCore import Qt

from dao.db import db


class LoginPage(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

        self.show()

    def initUI(self):
        self.setGeometry(300, 300, 500, 500)
        # self.setGeometry(shape)
        self.setWindowTitle('登录')

        # 显示logo
        self.icon=QLabel(self)
        # self.icon.move(200,60)
        self.icon.setGeometry(200,60,100,100)
        # self.icon.size(100,100)
        self.icon.setScaledContents(True)  # 设置图片随QLabel大小缩放
        png=QtGui.QPixmap("../images/icon.png")
        self.icon.setPixmap(png)

        # 显示文字
        self.headline=QLabel("信息管理系统",self)
        self.headline.setGeometry(200,170,100,20)
        self.headline.setAlignment(Qt.AlignCenter)# 文字居中

        # username框
        self.username_edit=QTextEdit(self)
        self.username_edit.setGeometry(200,250,100,30)
        self.username_edit.setPlaceholderText("请输入用户名")

        # password框
        self.password_edit = QTextEdit(self)
        self.password_edit.setGeometry(200, 300, 100, 30)
        self.password_edit.setPlaceholderText("请输入密码")

        # 登录按钮
        self.bt_login=QPushButton("登录",self)
        self.bt_login.setGeometry(220,350,60,40)
        self.bt_login.clicked.connect(self.check_login)


        # self.username_edit.setText("请输入用户名") # 设置文本
        # self.btn = QPushButton("Button", self)
        # self.btn.move(30, 50)
        # self.btn.clicked.connect(self.bt_click)

    # def set_mainpage(self,mainpage):
    #     self.mainpage=mainpage

    def check_login(self):
        # 验证登录
        user_name = self.username_edit.toPlainText()
        password = self.password_edit.toPlainText()
        row = db.get_user(user_name)
        print(row)
        if row == None or len(row) == 0 or row['password'] != password:
            print("用户名或密码错误",user_name,password)
            dialog = QDialog()
            dialog.adjustSize()  # 随内容自动改变大小
            text = QLineEdit("用户名或密码错误", dialog)  # 添加空间显示提示文字
            text.adjustSize()
            # 设置窗口的属性为ApplicationModal模态，用户只有关闭弹窗后，才能关闭主界面
            dialog.setWindowModality(Qt.ApplicationModal)
            dialog.exec_()  # 阻塞执行，只调用show执行后立马销毁
            return
        level = row['level']
        print("level:",level)
        print("跳转")
        from pages import home
        if level == 1:
            self.homepage=home.HomePage1()
            self.homepage.show()
            # return render_template('index_3.html', content=content)
        elif level == 2:
            # return render_template('index_2.html', content=content)
            self.homepage = home.HomePage2()
            self.homepage.show()
        else:
            self.homepage = home.HomePage3()
            self.homepage.show()
        # self.homepage.show()
        self.close()

        pass



