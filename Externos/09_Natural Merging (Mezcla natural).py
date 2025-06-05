# Función que mezcla dos listas ordenadas en una sola
def mezclar(lista1, lista2):
    resultado = []
    i = j = 0

    while i < len(lista1) and j < len(lista2):
        if lista1[i] <= lista2[j]:
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    resultado.extend(lista1[i:])
    resultado.extend(lista2[j:])
    return resultado

# Función que encuentra corridas naturales (sublistas ya ordenadas)
def encontrar_corridas(lista):
    corridas = []
    i = 0
    while i < len(lista):
        corrida = [lista[i]]
        i += 1
        while i < len(lista) and lista[i - 1] <= lista[i]:
            corrida.append(lista[i])
            i += 1
        corridas.append(corrida)
    return corridas

# Función principal: mezcla natural
def natural_merging(lista):
    corridas = encontrar_corridas(lista)

    while len(corridas) > 1:
        nuevas_corridas = []

        for i in range(0, len(corridas), 2):
            if i + 1 < len(corridas):
                nueva = mezclar(corridas[i], corridas[i+1])
                nuevas_corridas.append(nueva)
            else:
                nuevas_corridas.append(corridas[i])  # Corrida sin pareja
        corridas = nuevas_corridas

    return corridas[0]

# -------- Entrada del usuario --------
entrada = input("Escribe los números separados por comas (ej. 2, 5, 8, 4, 6, 9, 1, 3): ")
mi_lista = [int(x.strip()) for x in entrada.split(",")]

print("Lista original:", mi_lista)

# Aplicamos Natural Merging
lista_ordenada = natural_merging(mi_lista)

print("Lista ordenada:", lista_ordenada)
