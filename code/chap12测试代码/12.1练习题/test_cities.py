# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/26 22:18
import unittest
from city_functions import get_city_country


class CityTestCase(unittest.TestCase):
    def test_city_country(self):
        city_country = get_city_country('santiago', 'chile')
        self.assertEqual(city_country, 'Santiago, Chile')

    def test_city_country_population(self):
        city_country_population = get_city_country('santiago', 'chile', 5000000)
        self.assertEqual(city_country_population, 'Santiago, Chile - population 5000000')


if __name__ == '__main__':
    unittest.main()
