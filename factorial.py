def factorial(value):
    #condicion de corte
    if value in (0, 1):
        return 1
    #proceso recursivo
    return value * factorial(value - 1)


resultado = factorial(9)

print(resultado)