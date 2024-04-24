import unittest
def fibonacci(value):
    #condicion de corte
    if value in (0, 1):
        return value
    return fibonacci(value - 1) + fibonacci(value - 2)


#resultado = fibonacci(9)
#print(resultado)

class Testfibonacci(unittest.TestCase):
    def test_con_1(self):
        resultado = fibonacci(1)
        self.assertEqual(resultado, 1)
    
    def test_con_2(self):
        resultado = fibonacci(2)
        self.assertEqual(resultado, 1)
    
    def test_con_3(self):
        resultado = fibonacci(3)
        self.assertEqual(resultado, 2)
    
    def test_con_4(self):
        resultado = fibonacci(4)
        self.assertEqual(resultado, 3)
    
    def test_con_5(self):
        resultado = fibonacci(5)
        self.assertEqual(resultado, 5)
    
    def test_con_6(self):
        resultado = fibonacci(6)
        self.assertEqual(resultado, 8)
    
    def test_con_7(self):
        resultado = fibonacci(7)
        self.assertEqual(resultado, 13)

    def test_con_8(self):
        resultado = fibonacci(8)
        self.assertEqual(resultado, 21)
        
    def test_con_9(self):
        resultado = fibonacci(9)
        self.assertEqual(resultado, 34) 

if __name__ == '__main__':
    unittest.main()

