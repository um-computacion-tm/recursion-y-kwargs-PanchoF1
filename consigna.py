def buscar_datos(*args, **kwargs):
    for key, person_data in database.items():
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

resultado = buscar_datos("Pablo", "Diego", "Ruiz", "Picasso", **database)
print(resultado)