def insertion_sort(lista):
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > actual:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = actual
    return lista

# Entrada del usuario
entrada = input("Escribe los números separados por comas (ej. 5,3,8,6,2): ")
# Convertimos la cadena en una lista de enteros
mi_lista = [int(x.strip()) for x in entrada.split(",")]

print("Lista original:", mi_lista)
ordenada = insertion_sort(mi_lista)
print("Lista ordenada:", ordenada)
