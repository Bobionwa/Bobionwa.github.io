products = int(input("Ingrese la cantidad de Productos: "))
answer, cantidad = 1, 0
for cantidad in range(products):
    cant = int(input(f"Costo Producto {cantidad}: "))
    answer += cant
answer = answer-1 
print("Total mas IVA: ", ((answer-((answer/100)*15))+(answer*.16))) if answer >= 2000 else print("Total mas IVA: ", answer*.16+answer)
