
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QTextEdit, QWidget,QDialog, QListView , QVBoxLayout, QLineEdit,QTableView
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QStringListModel
from PyQt5.QtGui import QStandardItemModel,QStandardItem

from dao.db import db

# 学生主页
class CoursePage(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

        self.show()

    def initUI(self):
        self.setGeometry(300, 300, 500, 500)

        # 左上角标语
        self.headline = QLabel("选课情况", self)
        self.headline.setGeometry(10, 10, 100, 20)
        self.headline.setAlignment(Qt.AlignCenter)  # 文字居中

        # 显示课程列表
        # self.mg_labels=QLabel("暂无资讯", self)
        self.mg_lv = QListView(self)
        self.mg_lv.setGeometry(50, 150, 200, 200)
        slm = QStringListModel();  # 创建mode
        rows = db.get_courses()

        self.tb = QTableView(self)
        self.tb.setGeometry(20, 50, 400, 300)
        model = QStandardItemModel(len(rows), 4)  # 存储任意结构数据
        model.setHorizontalHeaderLabels(['序号', '课程', '教师', '学分'])
        for index,row in enumerate(rows):
            model.setItem(index,0,QStandardItem(str(row['id'])))
            model.setItem(index,1,QStandardItem(row['name']))
            model.setItem(index,2,QStandardItem(row['teacher']))
            model.setItem(index,3,QStandardItem(str(row['score'])))
        self.tb.setModel(model)


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    a = CoursePage()
    a.show()

    sys.exit(app.exec_())