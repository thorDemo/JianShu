# -*- coding:utf-8 -*-
import datetime


class Spider:
    def __init__(self):
        self.format_day = "%d/%b/%Y"
        self.format_hou = "%d/%b/%Y:%H"

    def seven_day(self):
        date = []
        now = datetime.datetime.today()
        for x in range(7):
            delta = datetime.timedelta(days=x)
            yesterday = now - delta
            date.append(yesterday.strftime(self.format_day))
        return date

    def twenty_four_hours(self):
        hours = []
        now = datetime.datetime.today()
        for x in range(24):
            delta = datetime.timedelta(hours=x)
            before = now - delta
            hours.append(before.strftime(self.format_hou))
        return hours


if __name__ == "__main__":
    spider = Spider()
    print(spider.seven_day())
    print(spider.twenty_four_hours())
