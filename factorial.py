import unittest
def factorial(value):
    #condicion de corte
    if value in (0, 1):
        return 1
    #proceso recursivo
    return value * factorial(value - 1)


#resultado = factorial(9)
#print(resultado)

class TestFactorial(unittest.TestCase):
    def test_con_1(self):
        resultado = factorial(1)
        self.assertEqual(resultado, 1)
    
    def test_con_2(self):
        resultado = factorial(2)
        self.assertEqual(resultado, 2)
    
    def test_con_3(self):
        resultado = factorial(3)
        self.assertEqual(resultado, 6)
    
    def test_con_4(self):
        resultado = factorial(4)
        self.assertEqual(resultado, 24)
    
    def test_con_5(self):
        resultado = factorial(5)
        self.assertEqual(resultado, 120)
    
    def test_con_6(self):
        resultado = factorial(6)
        self.assertEqual(resultado, 720)
    
    def test_con_7(self):
        resultado = factorial(7)
        self.assertEqual(resultado, 5040)

    def test_con_8(self):
        resultado = factorial(8)
        self.assertEqual(resultado, 40320)
        
    def test_con_9(self):
        resultado = factorial(9)
        self.assertEqual(resultado, 36288)            

if __name__ == '__main__':
    unittest.main()