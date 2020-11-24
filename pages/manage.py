

from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QTextEdit, QDialog, QLineEdit, QRadioButton
from PyQt5 import QtGui
from PyQt5.QtCore import Qt

from dao.db import db


class ManagePage(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

        self.show()

    def initUI(self):
        self.setGeometry(300, 300, 500, 500)
        # self.setGeometry(shape)
        self.setWindowTitle('添加用户')

        self.name_edit=QTextEdit(self)
        self.name_edit.setPlaceholderText("请输入新用户名")
        self.name_edit.setGeometry(150,50,200,30)
        # self.name_edit.set

        self.password_edit=QTextEdit(self)
        self.password_edit.setPlaceholderText("请设置登录密码")
        self.password_edit.setGeometry(150,100,200,30)

        self.rb1=QRadioButton(self)
        self.rb1.setText("学生")
        self.rb1.setChecked(True)
        self.rb1.setGeometry(150,150,50,30)

        self.rb2=QRadioButton(self)
        self.rb2.setText("教师")
        self.rb2.setChecked(False)
        self.rb2.setGeometry(220,150,50,30)

        # 确认按钮
        self.bt_submit=QPushButton("确认",self)
        self.bt_submit.setGeometry(200,200,100,40)
        self.bt_submit.clicked.connect(self.bt_click)

    def bt_click(self):
        # 查重
        user_name=self.name_edit.toPlainText()
        row=db.get_user(user_name)
        if row is not None and len(row)!=0:
            # 提示用户名已存在
            dialog = QDialog()
            dialog.setGeometry(400, 400, 150, 150)
            # dialog.adjustSize()  # 随内容自动改变大小
            # dialog.resize(200,200)
            text = QLabel("用户名已存在", dialog)  # 添加空间显示提示文字
            # text.resize(200,200)
            text.setGeometry(20, 20, 100, 100)
            text.setWordWrap(True)  # 文本换行
            # 设置窗口的属性为ApplicationModal模态，用户只有关闭弹窗后，才能关闭主界面
            dialog.setWindowModality(Qt.ApplicationModal)
            dialog.exec_()  # 阻塞执行，只调用show执行后立马销毁
            return

        isStudent=self.rb1.isChecked()
        level= 1 if isStudent else 2
        password=self.password_edit.toPlainText()
        db.add_user(user_name,password,level)
        # 提示添加成功
        dialog = QDialog()
        dialog.setGeometry(400, 400, 150, 150)
        # dialog.adjustSize()  # 随内容自动改变大小
        # dialog.resize(200,200)
        text = QLabel("添加成功", dialog)  # 添加空间显示提示文字
        # text.resize(200,200)
        text.setGeometry(20, 20, 100, 100)
        text.setWordWrap(True)  # 文本换行
        # 设置窗口的属性为ApplicationModal模态，用户只有关闭弹窗后，才能关闭主界面
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.exec_()  # 阻塞执行，只调用show执行后立马销毁

        self.close()






if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    a = ManagePage()
    a.show()

    sys.exit(app.exec_())