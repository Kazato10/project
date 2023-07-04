from tkinter import *
import os

class main_page():
    def __init__(self,window):
        self.window = window
        #屏幕位置
        sw = self.window.winfo_screenwidth()
        sh = self.window.winfo_screenheight()
        #脚本屏幕大小
        ww = 400
        wh = 200
        #脚本x,y
        x = (sw-ww)/2
        y = (sh-wh)/2
        self.window.title('文件脚本')
        self.window.geometry("%dx%d+%d+%d" % (ww,wh,x,y))
        self.createPage()

    def createPage(self):
        self.btn01 = Button(self.window,text="文件删除",command=self.change_one)
        self.btn01.pack()

    def change_one(self):
        self.btn01.destroy()
        Applicationone(screen)
        
class Applicationone():
    def __init__(self,window):
        self.window = window
        #屏幕位置
        sw = self.window.winfo_screenwidth()
        sh = self.window.winfo_screenheight()
        #脚本屏幕大小
        ww = 400
        wh = 200
        #脚本x,y
        x = (sw-ww)/2
        y = (sh-wh)/2
        self.window.title('文件脚本')
        self.window.geometry("%dx%d+%d+%d" % (ww,wh,x,y))
        self.createWidget()

    def createWidget(self):
        # 创建说明组件
        self.label01 = Label(self.window, text="请根据自身需求在下方输入输入文件路径")
        self.label01.pack()

        # 创建路径输入框
        # StringVar 变量绑定到指定的组件
        v1 = StringVar()
        self.Entry01 = Entry(self.window,textvariable=v1)
        self.Entry01.pack()

        # 创建说明组件
        self.label02 = Label(self.window, text="请根据自身需求在下方输入文件词")
        self.label02.pack()
        # 创建时间输入框
        v2 = StringVar()
        self.Entry02 = Entry(self.window,textvariable=v2)
        self.Entry02.pack()

        # 创建说明组件
        self.label03 = Label(self.window, text="请根据自身需求在下方输入文件后缀")
        self.label03.pack()
        # 创建后缀输入框
        v3 = StringVar()
        self.Entry03 = Entry(self.window,textvariable=v3)
        self.Entry03.pack()

        # 创建删除组件
        self.btn02 = Button(self.window,text='确认删除',command=self.delete)
        self.btn02.pack()

        # 创建退出组件
        self.btnQuit = Button(self.window,text='退出',command=screen.destroy)
        self.btnQuit.pack()

    def delete(self):
        # 获取路径和时间
        path = self.Entry01.get()
        word = self.Entry02.get()
        lastword = self.Entry03.get()
        print(path,word,lastword)
        # 文件分割
        files = os.listdir(path)
        for file in files:
            # 找到以...结尾的文件并且删除
            if (file.endswith(lastword)) and (word in file):
                a = "\\"
                new_path = path + a + file
                os.remove(new_path)
                
screen = Tk()
page_one = main_page(screen)

screen.mainloop()


# F:\xunlei\合集\2
# 工作表1
# xlsx
# F:\game-project\My_project\main.py
# pyinstaller -F F:\game-project\My_project\main.py