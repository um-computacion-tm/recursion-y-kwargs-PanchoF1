import unittest
def buscar_datos(*args, **kwargs):
    for key, person_data in kwargs.items():
        if all(arg in person_data.values() for arg in args):
            return key  
    return None 
database = {
            "1":{
                "nombre1":"Pablo",
                "nombre2":"Diego",
                "apellido1":"Ruiz",
                "apellido2":"Picasso"
            },
            "2":{
                "nombre1":"Elio",
                "apellido1":"Anci"
            },
            "3":{
                "nombre1":"Elias",
                "nombre2":"Marcos",
                "nombre3":"Luciano",
                "apellido1":"Marcelo",
                "apellido2":"Gonzalez"
            }
}

#resultado = buscar_datos("Pablo", "Diego", "Ruiz", "Picasso", **database)
#print(resultado)

class TestBuscarDatos(unittest.TestCase):
    def test_pablo(self):
        resultado = buscar_datos("Pablo","Diego","Ruiz","Picasso",**database)
        self.assertEqual(resultado, "1")
    def test_elio(self):
        resultado = buscar_datos("Elio", "Anci", **database)
        self.assertEqual(resultado, "2")

    def test_elias(self):
        resultado = buscar_datos("Elias", "Marcos", "Luciano", "Marcelo", "Gonzalez", **database)
        self.assertEqual(resultado, "3")

    def test_nn(self):
        resultado = buscar_datos("Fernando", "Alonso", "14", **database)
        self.assertIsNone(resultado)

    def test_nn2(self):
        resultado = buscar_datos("George", "Russell", "Perez", **database)
        self.assertIsNone(resultado)

    def test_nn3(self):
        resultado = buscar_datos("Lando", "Mercedes", "Norris", "2", **database)
        self.assertIsNone(resultado)
    
if __name__ == '__main__':
    unittest.main()