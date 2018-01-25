import urllib.request
import re

class Crawl:

    def get_fans_str(self):
        '''刷新网页，返还str类型的访问数, i.e. '57' '''
        request = urllib.request.Request(r'https://www.panda.tv/ajax_search?roomid='+self.room_id)
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')      # read from html
        reg_fan = r'"fans":[0-9]+'
        fan_num = re.findall(reg_fan,html,re.S)
        return fan_num[0][7:]


    def get_fans_int(self):
        '''刷新网页，返还int类型的访问数, i.e., 57 '''
        return int(self.get_fans_str())


    def get_starting_fans(self):
        '''返还昨日粉丝人数'''
        return self.starting_fans


    def get_remaining_goals(self):
        '''返还距离目标还剩下多少人，可为负数'''
        return self.goal-(self.get_fans_int()-self.starting_fans)

    def get_incresed_fans(self):
        '''返还增加了多少订阅'''
        return self.get_fans_int()-self.starting_fans

    def set_follower_goal_callback(self,goal):
        '''设置人数增长目标，i.e. 今日70人，预计达到90人，增加目标为90-70 = 20'''
        self.goal = goal


    def reset(self,start_from=-1):
        '''重设开始人数
        start_from = 从什么人数开始，如果不提供，则默认从当前关注数开始'''
        if start_from <0:
            self.starting_fans = self.get_fans_int()
        else:
            self.starting_fans = start_from

    def __init__(self, goal,room_id):
        '''goal = 今日目标增长量
            roomdI-d = 直播间ID
        '''
        self.goal = goal
        self.room_id = room_id
        self.starting_fans = self.get_fans_int()


    # def start_count(self):
    #     while True:
    #         request = urllib.request.Request(r'https://www.panda.tv/ajax_search?roomid=1778649')
    #         response = urllib.request.urlopen(request)
    #         html = response.read().decode('utf-8')      # read from html
    #         print(html)
    #
    #         # finding data using regular expression
    #         reg_fan = r'"fans":[0-9]+'
    #         reg_watch = r'"person_num":[0-9]+'
    #         fan_num = re.findall(reg_fan,html,re.S)
    #         watch_num = re.findall(reg_watch,html,re.S)
    #         print('当前订阅数:',fan_num[0][7:])
    #         print('当前观看数:',watch_num[0][13:])
    #         time.sleep(self.refresh_time)


