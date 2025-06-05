# Función principal que ordena una lista usando MergeSort
def merge_sort(lista):
    # Si la lista tiene 0 o 1 elemento, ya está ordenada
    if len(lista) <= 1:
        return lista

    # Paso 1: Dividir la lista en dos mitades
    mitad = len(lista) // 2  # Encontramos la mitad
    izquierda = lista[:mitad]  # Tomamos la mitad izquierda
    derecha = lista[mitad:]    # Tomamos la mitad derecha

    # Paso 2: Llamamos a merge_sort recursivamente en cada mitad
    izquierda_ordenada = merge_sort(izquierda)
    derecha_ordenada = merge_sort(derecha)

    # Paso 3: Fusionamos las dos mitades ordenadas
    return fusionar(izquierda_ordenada, derecha_ordenada)

# Esta función une (fusiona) dos listas ordenadas en una sola
def fusionar(lista1, lista2):
    resultado = []  # Aquí guardamos la lista final ordenada
    i = 0  # Índice para recorrer lista1
    j = 0  # Índice para recorrer lista2

    # Mientras haya elementos en ambas listas
    while i < len(lista1) and j < len(lista2):
        if lista1[i] <= lista2[j]:
            resultado.append(lista1[i])  # Agregamos el más pequeño
            i += 1  # Avanzamos en lista1
        else:
            resultado.append(lista2[j])  # Agregamos el más pequeño
            j += 1  # Avanzamos en lista2

    # Agregamos los elementos restantes de lista1 (si quedaron)
    while i < len(lista1):
        resultado.append(lista1[i])
        i += 1

    # Agregamos los elementos restantes de lista2 (si quedaron)
    while j < len(lista2):
        resultado.append(lista2[j])
        j += 1

    return resultado  # Devolvemos la lista completamente ordenada

# ---------- Parte donde el usuario ingresa datos ----------

# Pedimos al usuario que escriba los números separados por comas
entrada = input("Escribe los números separados por comas (ej. 10, 5, 3, 8): ")

# Convertimos la cadena en una lista de números (enteros)
mi_lista = [int(x.strip()) for x in entrada.split(",")]

# Mostramos la lista original
print("Lista original:", mi_lista)

# Ordenamos la lista usando MergeSort
lista_ordenada = merge_sort(mi_lista)

# Mostramos la lista ya ordenada
print("Lista ordenada:", lista_ordenada)
