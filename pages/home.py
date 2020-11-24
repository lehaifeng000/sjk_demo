
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QTextEdit, QWidget,QDialog, QListView , QVBoxLayout, QLineEdit
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QStringListModel

from dao.db import db

# 学生主页
class HomePage1(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

        self.show()

    def initUI(self):
        self.setGeometry(300, 300, 500, 500)
        # self.setGeometry(shape)
        self.setWindowTitle('主页')

        # 左上角标语
        self.headline=QLabel("信息管理系统",self)
        self.headline.setGeometry(10,10,100,20)
        self.headline.setAlignment(Qt.AlignCenter)# 文字居中

        # # 功能按钮
        # 选课查询
        self.bt1=QPushButton("选课查询",self)
        self.bt1.setGeometry(20,60,100,30)
        self.bt1.clicked.connect(self.course_click)

        # 个人信息
        # self.bt1=QPushButton("个人信息",self)
        # self.bt1.setGeometry(120,60,100,30)

        # 显示资讯
        # self.mg_labels=QLabel("暂无资讯", self)
        self.mg_lv=QListView(self)
        self.mg_lv.setGeometry(50,150,200,200)
        slm = QStringListModel();  # 创建mode
        rows=db.get_news()
        self.news_titles=list()
        self.news_contents=list()
        for row in rows:
            self.news_titles.append(row['title'])
            self.news_contents.append(row['content'])
        slm.setStringList(self.news_titles)  # 将数据设置到model
        self.mg_lv.setModel(slm)
        self.mg_lv.clicked.connect(self.news_lv_click)

    def course_click(self):
        from pages.course import CoursePage
        self.coursepage=CoursePage()
        self.coursepage.show()

    def news_lv_click(self,qModelIndex):
        print(qModelIndex.row())
        dialog = QDialog()
        dialog.setGeometry(400,400,300,300)
        # dialog.adjustSize()  # 随内容自动改变大小
        # dialog.resize(200,200)
        text = QLabel(self.news_contents[qModelIndex.row()], dialog)  # 添加空间显示提示文字
        # text.resize(200,200)
        text.setGeometry(20,20,260,260)
        text.setWordWrap(True) # 文本换行
        # 设置窗口的属性为ApplicationModal模态，用户只有关闭弹窗后，才能关闭主界面
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.exec_()  # 阻塞执行，只调用show执行后立马销毁


# 教师主页
class HomePage2(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

        self.show()

    def initUI(self):
        self.setGeometry(300, 300, 500, 500)
        # self.setGeometry(shape)
        self.setWindowTitle('主页')

        # 左上角标语
        self.headline=QLabel("信息管理系统",self)
        self.headline.setGeometry(10,10,100,20)
        self.headline.setAlignment(Qt.AlignCenter)# 文字居中

        # # 功能按钮
        # 学生查询
        self.bt1=QPushButton("查看学生",self)
        self.bt1.setGeometry(20,60,100,30)
        self.bt1.clicked.connect(self.stu_click)

        # 个人信息
        # self.bt1=QPushButton("个人信息",self)
        # self.bt1.setGeometry(120,60,100,30)

        # 显示资讯
        # self.mg_labels=QLabel("暂无资讯", self)
        self.mg_lv=QListView(self)
        self.mg_lv.setGeometry(50,150,200,200)
        slm = QStringListModel();  # 创建mode
        rows=db.get_news()
        self.news_titles=list()
        self.news_contents=list()
        for row in rows:
            self.news_titles.append(row['title'])
            self.news_contents.append(row['content'])
        slm.setStringList(self.news_titles)  # 将数据设置到model
        self.mg_lv.setModel(slm)
        self.mg_lv.clicked.connect(self.news_lv_click)

    def stu_click(self):
        from pages.stu import StuPage
        self.stuPage=StuPage()
        self.stuPage.show()

    def news_lv_click(self,qModelIndex):
        print(qModelIndex.row())
        dialog = QDialog()
        dialog.setGeometry(400,400,300,300)
        # dialog.adjustSize()  # 随内容自动改变大小
        # dialog.resize(200,200)
        text = QLabel(self.news_contents[qModelIndex.row()], dialog)  # 添加空间显示提示文字
        # text.resize(200,200)
        text.setGeometry(20,20,260,260)
        text.setWordWrap(True) # 文本换行
        # 设置窗口的属性为ApplicationModal模态，用户只有关闭弹窗后，才能关闭主界面
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.exec_()  # 阻塞执行，只调用show执行后立马销毁


# 管理员主页
class HomePage3(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

        self.show()

    def initUI(self):
        self.setGeometry(300, 300, 500, 500)
        # self.setGeometry(shape)
        self.setWindowTitle('主页')

        # 左上角标语
        self.headline=QLabel("信息管理系统",self)
        self.headline.setGeometry(10,10,100,20)
        self.headline.setAlignment(Qt.AlignCenter)# 文字居中

        # # 功能按钮
        # 学生查询
        self.bt1=QPushButton("添加用户",self)
        self.bt1.setGeometry(20,60,100,30)
        self.bt1.clicked.connect(self.manage_click)

        # 个人信息
        # self.bt1=QPushButton("个人信息",self)
        # self.bt1.setGeometry(120,60,100,30)

        # 显示资讯
        # self.mg_labels=QLabel("暂无资讯", self)
        self.mg_lv=QListView(self)
        self.mg_lv.setGeometry(50,150,200,200)
        slm = QStringListModel();  # 创建mode
        rows=db.get_news()
        self.news_titles=list()
        self.news_contents=list()
        for row in rows:
            self.news_titles.append(row['title'])
            self.news_contents.append(row['content'])
        slm.setStringList(self.news_titles)  # 将数据设置到model
        self.mg_lv.setModel(slm)
        self.mg_lv.clicked.connect(self.news_lv_click)

    def manage_click(self):
        from pages.manage import ManagePage
        self.managePage=ManagePage()
        self.managePage.show()

    def news_lv_click(self,qModelIndex):
        print(qModelIndex.row())
        dialog = QDialog()
        dialog.setGeometry(400,400,300,300)
        # dialog.adjustSize()  # 随内容自动改变大小
        # dialog.resize(200,200)
        text = QLabel(self.news_contents[qModelIndex.row()], dialog)  # 添加空间显示提示文字
        # text.resize(200,200)
        text.setGeometry(20,20,260,260)
        text.setWordWrap(True) # 文本换行
        # 设置窗口的属性为ApplicationModal模态，用户只有关闭弹窗后，才能关闭主界面
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.exec_()  # 阻塞执行，只调用show执行后立马销毁





if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    a = HomePage1()
    a.show()

    sys.exit(app.exec_())