# Función para obtener el número más grande en la lista (nos dice cuántos dígitos usar)
def obtener_maximo(lista):
    return max(lista)

# Función para hacer Counting Sort basado en un dígito específico (unidad, decena, etc.)
def counting_sort_por_digito(lista, digito):
    n = len(lista)
    salida = [0] * n  # Lista ordenada temporal
    conteo = [0] * 10  # Solo hay 10 posibles dígitos (0-9)

    # Contamos cuántas veces aparece cada dígito en la posición actual
    for num in lista:
        indice = (num // digito) % 10
        conteo[indice] += 1

    # Convertimos el conteo a posiciones reales en la lista de salida
    for i in range(1, 10):
        conteo[i] += conteo[i - 1]

    # Construimos la lista de salida ordenada
    i = n - 1
    while i >= 0:
        indice = (lista[i] // digito) % 10
        salida[conteo[indice] - 1] = lista[i]
        conteo[indice] -= 1
        i -= 1

    # Copiamos la salida ordenada a la lista original
    for i in range(len(lista)):
        lista[i] = salida[i]

# Función principal de Radix Sort
def radix_sort(lista):
    maximo = obtener_maximo(lista)  # Encontramos el número más grande
    digito = 1  # Empezamos con el dígito menos significativo (las unidades)

    # Repetimos el proceso mientras queden dígitos
    while maximo // digito > 0:
        counting_sort_por_digito(lista, digito)
        digito *= 10  # Pasamos a la siguiente posición decimal

# -------- Entrada del usuario --------
entrada = input("Escribe números enteros separados por comas (ej. 170, 45, 75, 90): ")
mi_lista = [int(x.strip()) for x in entrada.split(",")]

print("Lista original:", mi_lista)

# Aplicamos Radix Sort
radix_sort(mi_lista)

print("Lista ordenada:", mi_lista)
