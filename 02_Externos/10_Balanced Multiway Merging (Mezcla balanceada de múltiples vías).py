# Función para mezclar 3 listas ordenadas (multiway merge con 3 vías)
def mezclar_3_listas(a, b, c):
    resultado = []
    i = j = k = 0

    # Repetimos hasta que todas estén vacías
    while i < len(a) or j < len(b) or k < len(c):
        candidatos = []

        if i < len(a):
            candidatos.append((a[i], 'a'))
        if j < len(b):
            candidatos.append((b[j], 'b'))
        if k < len(c):
            candidatos.append((c[k], 'c'))

        if candidatos:
            minimo, origen = min(candidatos)
            resultado.append(minimo)

            if origen == 'a':
                i += 1
            elif origen == 'b':
                j += 1
            else:
                k += 1

    return resultado

# Función que divide una lista en corridas (runs) de longitud n
def dividir_en_corridas(lista, tamaño):
    return [lista[i:i + tamaño] for i in range(0, len(lista), tamaño)]

# Función principal de mezcla balanceada de 3 vías
def balanced_multiway_merge(lista):
    # Paso 1: Se crean corridas ordenadas (por ejemplo, de 3 elementos)
    corridas = [sorted(sublista) for sublista in dividir_en_corridas(lista, 3)]

    # Paso 2: Mientras haya más de 1 corrida, mezclamos de 3 en 3
    while len(corridas) > 1:
        nuevas_corridas = []

        for i in range(0, len(corridas), 3):
            if i + 2 < len(corridas):
                # Mezclamos 3 corridas
                nueva = mezclar_3_listas(corridas[i], corridas[i+1], corridas[i+2])
                nuevas_corridas.append(nueva)
            else:
                # Si no hay suficientes para mezclar de 3 en 3, se agregan como están
                nuevas_corridas.extend(corridas[i:])
                break

        corridas = nuevas_corridas

    return corridas[0]

# -------- Entrada del usuario --------
entrada = input("Escribe los números separados por comas (ej. 20, 11, 45, 6, 2, 80, 17, 31, 1): ")
mi_lista = [int(x.strip()) for x in entrada.split(",")]

print("Lista original:", mi_lista)

# Aplicamos mezcla balanceada de múltiples vías
lista_ordenada = balanced_multiway_merge(mi_lista)

print("Lista ordenada:", lista_ordenada)
