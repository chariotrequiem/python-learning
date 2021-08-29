# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/29 19:59
from pygal_maps_world.i18n import COUNTRIES

for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code])
