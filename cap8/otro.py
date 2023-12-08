
"""Modifique la clase BinarySearchTree descrita en este capítulo para permitir
nodos con claves duplicadas. Tres métodos se ven afectados: __find(),
insertar() y eliminar(). Elija insertar nuevos hijos izquierdos en el
nivel más superficial entre claves iguales, como se muestra en el lado izquierdo de la Figura 8-
26, y siempre busque y elimine la más profunda entre claves iguales. Más
específicamente, los métodos __find() y search() deberían devolver el
más profunda entre las claves iguales que encuentra, pero debería permitir una opción
parámetro para especificar la búsqueda de lo menos profundo. El método insert() debe
manejar el caso en el que el elemento a insertar duplica un nodo existente,
insertando un nuevo nodo con un hijo izquierdo vacío debajo del más profundo
llave duplicada. El método eliminar() debe eliminar el nodo más profundo entre
claves duplicadas, proporcionando así un LIFO o comportamiento similar a una pila entre
llaves duplicadas. Piense detenidamente en los casos de eliminación y si el
La elección de los nodos sucesores cambia. Demuestra cómo tu
La implementación funciona en un árbol insertando varias claves duplicadas.
asociados a diferentes valores. Luego borre esas claves y muestre sus
valores para dejar claro que el último duplicado insertado es el primer duplicado
eliminado."""





class Node: #clase que representa un nodo en el arbol
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None #inicializa el arbol con raiz nula

    def __find(self, key, node, least_deep=False): #busca un nodo con la clave dada
        if node is None:
            return None
        if key < node.key: #key menor que key nodo actual
            return self.__find(key, node.left, least_deep) #busqueda en subarbol izquierdo
        elif key > node.key:
            return self.__find(key, node.right, least_deep)#busqueda en "" derecho
        elif least_deep: #busca nodo menos profundo entre claves y compara izq y dere
            return self.__find(key, node.left, least_deep) or self.__find(key, node.right, least_deep)
        else:
            return node

    def search(self, key, least_deep=False): #busca nodo mas o menos profundo en caso de claves dupl
        return self.__find(key, self.root, least_deep) #llama al met find

    def insert(self, key, data):
        if self.root is None: #si esta vacia se crea un new nodo como raiz
            self.root = Node(key, data)
        else: #sino inicia el bucle para encontrar ubic para insertar el new nodo
            current = self.root
            while current:
                if key == current.key: #si coincide con clave de nodo exist, se duplica un new nodo 
                    if current.left is None:
                        current.left = Node(key, data)
                        return
                    current = current.left
                elif key < current.key: #menor que clave nodo actual, continua en subarbol izqu
                    if current.left is None:
                        current.left = Node(key, data)
                        return
                    current = current.left
                else:
                    if current.right is None:
                        current.right = Node(key, data) #si es mayor continua en el lado derecho
                        return
                    current = current.right
    def print(self):
            if self.root is not None: #verf si no es nula y llama print para imprim desde raiz
                self._print(self.root)

    def _print(self, node, level=0):
        if node is not None:
            self._print(node.right, level + 1) #imprim subarb derecho
            print(' ' * 4 * level + '->', node.key, node.data)
            self._print(node.left, level + 1)


    def delete(self, key):
        def find_deepest(node, parent): #busca el nodo mas profund y elimn
            if node.right:
                return find_deepest(node.right, node)#encuentra el nodomas profund con su nodo principal
            return node, parent #devuelve tupla

        def delete_deepest(node, parent):
            if node.left and node.right:
                deepest, deepest_parent = find_deepest(node.left, node) #se llama a find en izqu
                node.key, node.data = deepest.key, deepest.data #estos se copian al nodo que queremos elimn
                delete_deepest(deepest, deepest_parent)
            elif node.left or node.right:
                next_node = node.left if node.left else node.right
                if parent:
                    if node is parent.left:
                        parent.left = next_node
                    else:
                        parent.right = next_node
                else:
                    self.root = next_node
            else:
                if parent: #si no tiene hijos se elimina direct el izqu o dere
                    if node is parent.left:
                        parent.left = None
                    else:
                        parent.right = None
                else:
                    self.root = None

        if self.root is None:
            return
        if self.root.key == key:
            if self.root.left:
                delete_deepest(self.root.left, self.root)
            else:
                self.root = self.root.right
        else:
            parent = None
            current = self.root
            while current:
                if key == current.key:
                    delete_deepest(current, parent)
                    return
                parent = current
                if key < current.key:
                    current = current.left
                else:
                    current = current.right

# Codigo de prueba
if __name__ == "__main__":
    theTree = BinarySearchTree()

    # nodos duplicados con diferentes valores
    theTree.insert(10, "valor 1") #nodo con clave 10 y datos"valor 1"
    theTree.insert(5, "valor 2")
    theTree.insert(15, "valor 3")
    theTree.insert(5, "valor 4")
    theTree.insert(10, "valor 5")

    # imprime el arbol
    print("arbol después de insertar:")
    theTree.print()  

    # elimina nodos duplicados
    theTree.delete(5)
    theTree.delete(10)

    # Imprime el arbol después de eliminar duplicados
    print("arbol después de eliminar:")
    theTree.print() 