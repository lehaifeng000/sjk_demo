import sys

# 这里我们提供必要的引用。基本控件位于pyqt5.qtwidgets模块中。
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QListView, QMainWindow, QVBoxLayout, QTableView
from PyQt5.QtCore import QStringListModel
from PyQt5.QtGui import QStandardItemModel,QStandardItem

class Page(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.tb=QTableView(self)
        self.tb.setGeometry(10,10,300,300)
        model = QStandardItemModel(4, 4)  # 存储任意结构数据
        model.setHorizontalHeaderLabels(['序号', '课程', '教师', '学分'])
        for i in range(4):
            for j in range(4):
                s=str(i)+","+str(j)
                s=QStandardItem(s)
                model.setItem(i,j,s)
        self.tb.setModel(model)


        #
        # self.lv=QListView(self)
        # slm = QStringListModel();  # 创建mode
        # self.qList = ['Item 1', 'Item 2', 'Item 3', 'Item 4']  # 添加的数组数据
        # slm.setStringList(self.qList)  # 将数据设置到model
        # self.lv.setModel(slm)  ##绑定 listView 和 model
        # self.lv.setGeometry(100,100,100,100)
        # # layout = QVBoxLayout()
        # # layout.addWidget(self.lv)  # 将list view添加到layout
        # # self.setLayout(layout)  # 将lay 添加到窗口

        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Event sender')
        self.show()

        # print("hello")

if __name__ == '__main__':
    # 每一pyqt5应用程序必须创建一个应用程序对象。sys.argv参数是一个列表，从命令行输入参数。
    app = QApplication(sys.argv)
    # QWidget部件是pyqt5所有用户界面对象的基类。他为QWidget提供默认构造函数。默认构造函数没有父类。

    p=Page()
    p.show()


    # 系统exit()方法确保应用程序干净的退出
    # 的exec_()方法有下划线。因为执行是一个Python关键词。因此，exec_()代替
    sys.exit(app.exec_())