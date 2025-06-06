# Creamos una clase para representar cada nodo del árbol
class Nodo:
    def __init__(self, valor):
        self.valor = valor      # El valor almacenado en este nodo
        self.izq = None         # Referencia al subárbol izquierdo
        self.der = None         # Referencia al subárbol derecho

# Función para insertar un nuevo valor en el árbol
def insertar(nodo, valor):
    if nodo is None:
        return Nodo(valor)     # Si no hay nodo, creamos uno nuevo
    if valor < nodo.valor:
        # Si el valor es menor, insertamos en el subárbol izquierdo
        nodo.izq = insertar(nodo.izq, valor)
    else:
        # Si el valor es mayor o igual, insertamos en el subárbol derecho
        nodo.der = insertar(nodo.der, valor)

    return nodo  # Devolvemos el nodo actualizado

# Recorrido inorden (izquierda, nodo, derecha) para obtener los valores ordenados
def inorden(nodo, lista):
    if nodo:
        inorden(nodo.izq, lista)       # Recorremos el subárbol izquierdo
        lista.append(nodo.valor)       # Agregamos el valor del nodo actual
        inorden(nodo.der, lista)       # Recorremos el subárbol derecho

# Función principal de ordenamiento por árbol
def tree_sort(lista):
    raiz = None  # Inicialmente el árbol está vacío

    # Insertamos todos los valores en el árbol
    for valor in lista:
        raiz = insertar(raiz, valor)

    lista_ordenada = []  # Lista donde guardaremos los valores ordenados

    # Llenamos lista_ordenada con los valores del árbol en orden
    inorden(raiz, lista_ordenada)

    return lista_ordenada  # Devolvemos la lista ordenada

# ---------- Entrada del usuario ----------
# Pedimos al usuario que escriba los números separados por comas
entrada = input("Escribe los números separados por comas (ej. 5,3,8,6,2): ")

# Convertimos la cadena ingresada en una lista de enteros
mi_lista = [int(x.strip()) for x in entrada.split(",")]

# Mostramos la lista original
print("Lista original:", mi_lista)

# Ordenamos la lista usando Tree Sort
ordenada = tree_sort(mi_lista)

# Mostramos la lista ordenada
print("Lista ordenada:", ordenada)
