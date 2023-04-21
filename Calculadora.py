products = int(input("Ingrese la cantidad de Productos: "))
int answer
for cantidad in range(products):
    cant = int(input("Costo Producto ", cantidad))
    answer += cant
total = input("Total mas IVA: ", answer* .16)
