# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/26 22:11
def get_city_country(city, country, population=''):
    if population:
        city_country = city.title() + ', ' + country.title() + ' - population ' + str(population)
    else:
        city_country = city.title() + ', ' + country.title()
    return city_country
