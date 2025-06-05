# Función para dividir una lista en sublistas ordenadas de tamaño fijo
def generar_corridas_ordenadas(lista, tamaño_corrida):
    corridas = []
    for i in range(0, len(lista), tamaño_corrida):
        corrida = sorted(lista[i:i + tamaño_corrida])
        corridas.append(corrida)
    return corridas

# Función para distribuir corridas en 'n' archivos simulados (listas)
def distribuir_corridas(corridas, num_archivos):
    archivos = [[] for _ in range(num_archivos)]
    for i, corrida in enumerate(corridas):
        archivos[i % num_archivos].append(corrida)
    return archivos

# -------- Entrada del usuario --------
entrada = input("Escribe los números separados por comas (ej. 18, 3, 25, 10, 2, 45, 12, 1): ")
mi_lista = [int(x.strip()) for x in entrada.split(",")]

# Paso 1: Generar corridas de tamaño 3 (puedes cambiarlo)
corridas = generar_corridas_ordenadas(mi_lista, 3)

# Paso 2: Distribuir en 3 archivos simulados
archivos = distribuir_corridas(corridas, 3)

# Mostrar el resultado
print("\nCorridas ordenadas:")
for i, corrida in enumerate(corridas, 1):
    print(f"Corrida {i}: {corrida}")

print("\nDistribución en archivos simulados:")
for i, archivo in enumerate(archivos, 1):
    print(f"Archivo {i}: {archivo}")
