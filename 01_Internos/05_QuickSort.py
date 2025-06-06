# Función principal de QuickSort
def quicksort(lista):
    if len(lista) <= 1:
        return lista  # Si la lista tiene 0 o 1 elemento, ya está ordenada

    pivote = lista[0]  # Elegimos el primer elemento como pivote

    # Creamos tres listas:
    menores = [x for x in lista[1:] if x < pivote]      # Menores al pivote
    iguales = [x for x in lista if x == pivote]         # Iguales al pivote
    mayores = [x for x in lista[1:] if x > pivote]      # Mayores al pivote

    # Aplicamos QuickSort recursivamente y combinamos los resultados
    return quicksort(menores) + iguales + quicksort(mayores)

# -------- Entrada del usuario --------
entrada = input("Escribe los números separados por comas (ej. 5,3,8,6,2): ")

# Convertimos la entrada en una lista de enteros
mi_lista = [int(x.strip()) for x in entrada.split(",")]

# Mostramos la lista original
print("Lista original:", mi_lista)

# Ordenamos usando QuickSort
ordenada = quicksort(mi_lista)

# Mostramos la lista ordenada
print("Lista ordenada:", ordenada)
