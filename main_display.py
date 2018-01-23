from tkinter import *
from crawl import Crawl
import threading
import time

class MainDisplay:

    def __init__(self,goal,time):
        '''goal = 今日订阅目标（增加量
            time = 刷新时间 （分钟）'''
        self.goal = goal
        self.time_in_seconds = time*60
        self.c = Crawl(goal)      # 初始化Crawler
        # 设置GUI界面
        self.root = Tk()

        ###########################     设置初始windows位置 ##################
        self.root.geometry('220x45+40+560')         # 长 X  宽  + 向右平移 + 向下平移
        #####################################################################

        self.root.title('就是要莽')
        top_frame = Frame(self.root)  # 上层frame用于显示信息
        top_frame.pack(fill=BOTH)
        text_label = Label(top_frame, text='今日订阅：  ',font="32")
        text_label.grid(row=0,sticky='w')
        self.cur_num = StringVar()   # 当前订阅数
        num_label = Label(top_frame, textvariable=self.cur_num,fg="red",font="28")
        num_label.grid(row=0, column=1,sticky='w')
        objective_label = Label(top_frame,text='/'+str(self.goal),font="28")
        objective_label.grid(row=0,column=2,sticky='w')
        top_frame.columnconfigure(0,weight=4)     # 调整widget位置
        top_frame.columnconfigure(1,weight=2)
        top_frame.columnconfigure(1,weight=2)

        bottom_frame = Frame(self.root)  # 下层frame用于手动获取最新订阅量
        bottom_frame.pack(fill=X, side=BOTTOM)
        refresh_button = Button(bottom_frame, text='手动刷新',font="25")
        refresh_button.bind('<Button-1>', self.refresh)
        refresh_button.pack(fill=BOTH)
        self.root.rowconfigure(0,weight=3)   # 调整widget位置
        self.root.rowconfigure(1,weight=1)

        t = threading.Thread(target=self.start_crawl)   # 开始运行
        t.daemon = True
        t.start()
        self.root.mainloop()

    def print_fans(self):
        self.cur_num.set(self.c.get_incresed_fans())

    def refresh(self,event):
        t = threading.Thread(target=self.print_fans)
        t.daemon = True
        t.start()

    def start_crawl(self):
        while True:
            self.cur_num.set(self.c.get_incresed_fans())
            time.sleep(self.time_in_seconds)

if __name__ == '__main__':
    MainDisplay(10,1)







