from tkinter import *
from tkinter import messagebox
from main_display import MainDisplay


class SettingDisplay:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)

        ###########################     设置初始windows位置 ##################
        self.master.geometry('285x80+40+560')  # 长 X  宽  + 向右平移 + 向下平移
        #####################################################################

        self.master.title('设置')
        self.today_goal_label = Label(self.frame, text="今日订阅人数目标： ", font=("宋体", 10))
        self.refresh_time_label = Label(self.frame, text="刷新订阅时间(分钟)： ", font=("宋体", 10))

        self.count = 0
        self.refresh_time_entry_var = DoubleVar()
        self.goal_entry_var = StringVar()
        self.goal_entry = Entry(self.frame, textvariable=self.goal_entry_var)
        self.refresh_time_entry = Entry(self.frame, textvariable=self.refresh_time_entry_var)
        self.submit = Button(self.frame, text="保存", width=6, command=self.new_window)\
            .grid(row=3, column=1, sticky=W, pady=4)
        self.quit = Button(self.frame, text="退出", width=6, command=self.master.destroy).grid(row=3, column=0)
        self.today_goal_label.grid(row=1, column=0)
        self.refresh_time_label.grid(row=2, column=0)
        self.goal_entry.grid(row=1, column=1)
        self.refresh_time_entry.grid(row=2, column=1)
        self.frame.pack()

    def check_input(self):
        try:
            if len(self.goal_entry_var.get()) == 0:
                messagebox.showinfo("Warning", "请输入订阅目标！")
                self.count += 1
            elif self.goal_entry_var.get().isdecimal() is False:
                messagebox.showinfo("Warning", "请输入整数！")
                self.count += 1
            if self.refresh_time_entry_var.get() == 0:
                messagebox.showinfo("Warning", "请输入刷新时间！")
                self.count += 1
            elif self.refresh_time_entry_var.get() * 60 < 1:
                messagebox.showinfo("Warning", "小于1秒！")
                self.count += 1
        except Exception as e:
            messagebox.showinfo("Warning", e.args)
            self.count += 1

    def new_window(self):
        self.check_input()
        if 0 < self.count < 3:
            self.count = 0

        else:
            self.master.destroy()
            self.app = MainDisplay(self.goal_entry_var.get(), self.refresh_time_entry_var.get(),1778649)    # 今日目标，刷新间隔，直播间ID


def main():
    root = Tk()
    SettingDisplay(root)
    root.mainloop()


if __name__ == '__main__':
    main()
