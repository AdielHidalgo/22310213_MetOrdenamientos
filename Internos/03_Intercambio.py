def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        # Bandera para saber si hubo intercambio
        hubo_intercambio = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                # Intercambiamos si están en el orden incorrecto
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                hubo_intercambio = True
        # Si no hubo ningún intercambio, la lista ya está ordenada
        if not hubo_intercambio:
            break
    return lista

# Entrada del usuario
entrada = input("Escribe los números separados por comas (ej. 5,3,8,6,2): ")
mi_lista = [int(x.strip()) for x in entrada.split(",")]

print("Lista original:", mi_lista)
ordenada = bubble_sort(mi_lista)
print("Lista ordenada:", ordenada)
