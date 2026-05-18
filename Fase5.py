

# Programa de inbentario



inventario = [
    [101, "Teclado", 5, 10],
    [102, "Mouse", 15, 10],
    [103, "Monitor", 3, 8],
    [104, "Impresora", 7, 7],
    [105, "USB", 2, 12]
]


def calcular_pedido(stock_actual, stock_minimo):

    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0


print("===================================")
print("   LISTA DE PEDIDOS DE INVENTARIO")
print("===================================")


for articulo in inventario:

    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    cantidad_pedir = calcular_pedido(stock_actual, stock_minimo)

    print("\nCódigo:", codigo)
    print("Artículo:", nombre)
    print("Stock actual:", stock_actual)
    print("Stock mínimo:", stock_minimo)
    print("Cantidad a pedir:", cantidad_pedir)

print("\nFin del programa")