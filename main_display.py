from tkinter import *
from crawl import Crawl
import threading
import time
from pygame import mixer

class MainDisplay:

    def __init__(self,goal,time):
        '''goal = 今日订阅目标（增加量
            time = 刷新时间 （分钟）'''
        self.goal = goal
        self.time_in_seconds = time*60
        self.today_maximum = -1 # 今日最高订阅数
        self.c = Crawl(goal)      # 初始化Crawler
        # 设置GUI界面
        self.root = Tk()
        mixer.init()
        mixer.music.load('doorbell.mp3')
        ###########################     设置初始windows位置 ##################
        self.root.geometry('340x37+21+733')         # 长 X  宽  + 向右平移 + 向下平移
        #####################################################################

        self.root.title('就是要莽')
        left_frame = Frame(self.root)  # 左边frame用于显示信息
        left_frame.grid(row=0,column=0)
        self.label_text1 = StringVar()
        self.label_text1.set('今日订阅:')
        text_label = Label(left_frame, textvariable=self.label_text1,font="32")
        text_label.grid(row=0,sticky='w')
        self.cur_num = StringVar()   # 当前订阅数
        num_label = Label(left_frame, textvariable=self.cur_num,fg="red",font="28")
        num_label.grid(row=0, column=1,sticky='e')
        self.label_text2 = StringVar()
        self.label_text2.set('/'+str(self.goal))
        objective_label = Label(left_frame,textvariable=self.label_text2,font="28")
        objective_label.grid(row=0,column=2,sticky='w')
        # left_frame.columnconfigure(0,weight=4)     # 调整widget位置
        # left_frame.columnconfigure(1,weight=2)
        # left_frame.columnconfigure(2,weight=2)

        right_frame = Frame(self.root)  # 右边frame用于手动获取最新订阅量和当前订阅人数
        right_frame.grid(row=0,column=1)
        # bottom_frame.pack(fill=BOTH, side=BOTTOM)
        refresh_button = Button(right_frame, text='手动刷新',font="25")
        refresh_button.bind('<Button-1>', self.refresh)
        refresh_button.grid(row=0,column=0,sticky=("N", "S", "E", "W"),padx=4,pady=4)
        fans_button=Button(right_frame,text='当前订阅',font="25")
        fans_button.bind('<Button-1>', self.refresh_total_fans)
        fans_button.grid(row=0,column=1,sticky=("N", "S", "E", "W"),padx=4,pady=4)
        right_frame.columnconfigure(0,weight=1)
        right_frame.columnconfigure(1,weight=1)
        self.root.columnconfigure(0,minsize=50)
        self.root.columnconfigure(1,weight=1)   # 调整widget位置

        t = threading.Thread(target=self.start_crawl)   # 开始运行
        t.daemon = True
        t.start()
        self.root.mainloop()

    def print_fans(self):
        increased_fans = self.c.get_incresed_fans()
        if increased_fans > self.today_maximum:     # 当订阅人数增加时，播放hello音效
            threading.Thread(target=self.play_sound).start()
            self.today_maximum = increased_fans
        self.cur_num.set(increased_fans)
        self.label_text1.set('今日订阅:')
        self.label_text2.set('/'+str(self.goal))


    def play_sound(self):
        mixer.music.play()

    def refresh(self,event):
        t = threading.Thread(target=self.print_fans)
        t.daemon = True
        t.start()

    def start_crawl(self):
        while True:
            self.cur_num.set(self.c.get_incresed_fans())
            time.sleep(self.time_in_seconds)

    def print_total_fans(self):
        self.cur_num.set(self.c.get_fans_str())
        self.label_text1.set('总订阅:')
        self.label_text2.set('')
        time.sleep(3)
        self.print_fans()

    def refresh_total_fans(self,event):
        t = threading.Thread(target=self.print_total_fans)
        t.daemon = True
        t.start()











