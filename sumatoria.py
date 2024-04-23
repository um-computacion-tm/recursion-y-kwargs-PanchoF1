def sumatoria(value):
    #condicion de corte
    if value == 0:
        return 0
    #proceso recursivo
    return value + sumatoria(value - 1)


resultado = sumatoria(6)

print(resultado)
