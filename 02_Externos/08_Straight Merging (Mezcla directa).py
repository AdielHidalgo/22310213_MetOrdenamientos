# Función que simula la mezcla directa (merge) entre dos listas ordenadas
def mezclar(lista1, lista2):
    resultado = []
    i = j = 0

    # Mezclamos las dos listas comparando elemento por elemento
    while i < len(lista1) and j < len(lista2):
        if lista1[i] <= lista2[j]:
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    # Agregamos los elementos restantes de cada lista (si los hay)
    resultado.extend(lista1[i:])
    resultado.extend(lista2[j:])
    return resultado

# Función principal que simula Straight Merging
def straight_merging(lista):
    # Paso 1: Convertimos la lista en sublistas de 1 elemento (corridas)
    corridas = [[num] for num in lista]

    # Paso 2: Mientras haya más de una corrida, seguimos mezclando
    while len(corridas) > 1:
        nuevas_corridas = []

        # Mezclamos las corridas de dos en dos
        for i in range(0, len(corridas), 2):
            if i + 1 < len(corridas):
                mezcla = mezclar(corridas[i], corridas[i+1])
                nuevas_corridas.append(mezcla)
            else:
                nuevas_corridas.append(corridas[i])  # Si hay una sola corrida sin pareja

        # Reemplazamos las corridas por las nuevas corridas mezcladas
        corridas = nuevas_corridas

    # El resultado es la única corrida final
    return corridas[0]

# -------- Entrada del usuario --------
entrada = input("Escribe los números separados por comas (ej. 10, 7, 4, 3, 8): ")
mi_lista = [int(x.strip()) for x in entrada.split(",")]

print("Lista original:", mi_lista)

# Aplicamos Straight Merging
lista_ordenada = straight_merging(mi_lista)

print("Lista ordenada:", lista_ordenada)
