import unittest

def city_country(city, country, population=5000000):
    result = city+", "+country+" -population "+str(population)
    return result.title()

class Test_City_Functions(unittest.TestCase):
    #注意测试函数必须以test开头,否则不会自动执行
    def test_City_Country(self):
        finalresult = city_country('beijing', 'china', 11111111)
        self.assertEqual(finalresult, 'Beijing, China -Population 11111111')

    def test_City_Country2(self):
        finalresult2 = city_country('shijiazhuang', 'china')
        self.assertEqual(finalresult2, 'Shijiazhuang, China -Population 5000000')
unittest.main()
'''
assertEqual(a, b)        核实a=b
assertNotEqual(a, b)     核实a!=b
assertIn(item, list)     核实item在list中
assertNotIn(item, list)  核实item不在在list中
assertTrue(x)            核实x为True
assertFlase(x)           核实x为False
'''