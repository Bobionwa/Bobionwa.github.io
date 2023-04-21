products = int(input("Ingrese la cantidad de Productos: "))
answer = 0
cantidad = 1
for cantidad in range(products):
    cant = int(input(f"Costo Producto {cantidad}: "))
    answer += cant
print("Total mas IVA: ", answer* .16 + answer)
