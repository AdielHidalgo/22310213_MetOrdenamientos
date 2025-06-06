# Función para mezclar dos listas ordenadas
def mezclar_dos(lista1, lista2):
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

# Simulación de la distribución polifásica
def polyphase_sort(lista):
    # Paso 1: Dividir la lista en corridas ordenadas de tamaño fijo (por ejemplo, 2)
    tamaño_corrida = 2
    corridas = [sorted(lista[i:i+tamaño_corrida]) for i in range(0, len(lista), tamaño_corrida)]

    # Paso 2: Simular tres archivos (dos de entrada y uno de salida)
    archivo1 = corridas[::3]  # Cada tercer corrida
    archivo2 = corridas[1::3]
    archivo3 = corridas[2::3]

    print("\n--- Distribución inicial (simulación de archivos) ---")
    print("Archivo1:", archivo1)
    print("Archivo2:", archivo2)
    print("Archivo3:", archivo3)

    archivos = [archivo1, archivo2, archivo3]

    # Paso 3: Mezclar corridas mientras haya más de una corrida total
    while sum(len(a) for a in archivos) > 1:
        # Seleccionar dos archivos con más corridas como entrada
        entradas = sorted(archivos, key=len, reverse=True)[:2]
        salida = [a for a in archivos if a not in entradas][0]

        nuevas_corridas = []

        while entradas[0] and entradas[1]:
            corrida1 = entradas[0].pop(0)
            corrida2 = entradas[1].pop(0)
            nuevas_corridas.append(mezclar_dos(corrida1, corrida2))

        # Si alguna entrada aún tiene corridas, las pasamos como están
        for entrada in entradas:
            nuevas_corridas.extend(entrada)
            entrada.clear()

        # La salida ahora contiene las nuevas corridas
        salida.clear()
        salida.extend(nuevas_corridas)

    # Encontramos el archivo con la corrida final ordenada
    for archivo in archivos:
        if archivo:
            return archivo[0]

# -------- Entrada del usuario --------
entrada = input("Escribe los números separados por comas (ej. 18, 3, 25, 10, 2, 45, 12, 1): ")
mi_lista = [int(x.strip()) for x in entrada.split(",")]

print("Lista original:", mi_lista)

# Aplicamos Polyphase Sort
lista_ordenada = polyphase_sort(mi_lista)

print("\nLista ordenada:", lista_ordenada)