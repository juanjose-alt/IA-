def ordenar_tres(a, b, c):
    # Paso 1: asegurar que a <= b
    if a > b:
        a, b = b, a

    # Paso 2: asegurar que b <= c (así c queda como el mayor)
    if b > c:
        b, c = c, b

    # Paso 3: volver a comparar a y b, porque b pudo cambiar
    if a > b:
        a, b = b, a

    return a, b, c

n1 = float(input("Primer número: "))
n2 = float(input("Segundo número: "))
n3 = float(input("Tercer número: "))

menor, medio, mayor = ordenar_tres(n1, n2, n3)
print(f"Ordenados de menor a mayor: {menor}, {medio}, {mayor}")