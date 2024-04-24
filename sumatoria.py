import unittest
def sumatoria(value):
    #condicion de corte
    if value == 0:
        return 0
    #proceso recursivo
    return value + sumatoria(value - 1)


#resultado = sumatoria(6)
#print(resultado)

class Testsumatoria(unittest.TestCase):
    def test_con_1(self):
        resultado = sumatoria(1)
        self.assertEqual(resultado, 1)
    
    def test_con_2(self):
        resultado = sumatoria(2)
        self.assertEqual(resultado, 3)
    
    def test_con_3(self):
        resultado = sumatoria(3)
        self.assertEqual(resultado, 6)
    
    def test_con_4(self):
        resultado = sumatoria(4)
        self.assertEqual(resultado, 10)
    
    def test_con_5(self):
        resultado = sumatoria(5)
        self.assertEqual(resultado, 15)
    
    def test_con_6(self):
        resultado = sumatoria(6)
        self.assertEqual(resultado, 21)
    
    def test_con_7(self):
        resultado = sumatoria(7)
        self.assertEqual(resultado, 28)

    def test_con_8(self):
        resultado = sumatoria(8)
        self.assertEqual(resultado, 36)
        
    def test_con_9(self):
        resultado = sumatoria(9)
        self.assertEqual(resultado, 45) 

if __name__ == '__main__':
    unittest.main()