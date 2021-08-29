# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/29 16:13

from matplotlib import pyplot as plt
from get_info import Getinfo


"""创建两个实例对象，使用plot绘制图形"""
filename1 = 'sitka_weather_2014.csv'
filename2 = 'death_valley_2014.csv'
files1 = Getinfo(filename1)
files2 = Getinfo(filename2)
files1.get_info()
files2.get_info()

# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(files1.dates, files1.highs, c='red', alpha=0.5)
plt.plot(files1.dates, files1.lows, c='blue', alpha=0.5)
plt.plot(files2.dates, files2.highs, c='green', alpha=0.3)
plt.plot(files2.dates, files2.lows, c='yellow', alpha=0.3)
plt.fill_between(files2.dates, files2.highs, files2.lows, facecolor='blue', alpha=0.1)
plt.fill_between(files1.dates, files1.highs, files1.lows, facecolor='blue', alpha=0.1)
plt.title("Daily high and low temperatures-2014")
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)")


plt.show()

