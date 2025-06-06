def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        min_index = i  # Suponemos que el mínimo está en la posición actual
        for j in range(i + 1, n):  # Buscamos el mínimo en el resto de la lista
            if lista[j] < lista[min_index]:
                min_index = j  # Actualizamos el índice del mínimo encontrado
        # Intercambiamos el valor mínimo con el valor en la posición actual
        lista[i], lista[min_index] = lista[min_index], lista[i]
    return lista

# Entrada del usuario
entrada = input("Escribe los números separados por comas (ej. 5,3,8,6,2): ")
mi_lista = [int(x.strip()) for x in entrada.split(",")]

print("Lista original:", mi_lista)
ordenada = selection_sort(mi_lista)
print("Lista ordenada:", ordenada)
