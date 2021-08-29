# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/29 16:15

import csv
from datetime import datetime
"""在缺失代码处，为了偷懒，所以将缺失的数据置为0，从图中可明显看出"""


class Getinfo:
    """获取数据集当中的日期、最高温度及最低温度的数据"""
    def __init__(self, filename):
        self.dates = []
        self.highs = []
        self.lows = []
        self.filename = filename

    def get_dates(self):
        with open(self.filename) as f:
            reader = csv.reader(f)
            header_row = next(reader)
            for row in reader:
                try:
                    current_date = datetime.strptime(row[0], '%Y-%m-%d')
                except ValueError:
                    print('missing data')
                else:
                    self.dates.append(current_date)

    def get_highs(self):
        with open(self.filename) as f:
            reader = csv.reader(f)
            header_row = next(reader)
            for row in reader:
                try:
                    high = int(row[1])
                except ValueError:
                    self.highs.append(0)
                else:
                    self.highs.append(high)

    def get_lows(self):
        with open(self.filename) as f:
            reader = csv.reader(f)
            header_row = next(reader)
            for row in reader:
                try:
                    low = int(row[3])
                except ValueError:
                    self.lows.append(0)
                else:
                    self.lows.append(low)

    def get_info(self):
        self.get_dates()
        self.get_highs()
        self.get_lows()


