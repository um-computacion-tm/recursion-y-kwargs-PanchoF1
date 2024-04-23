def fibonacci(value):
    #condicion de corte
    if value in (0, 1):
        return value
    return fibonacci(value - 1) + fibonacci(value - 2)


resultado = fibonacci(9)

print(resultado)