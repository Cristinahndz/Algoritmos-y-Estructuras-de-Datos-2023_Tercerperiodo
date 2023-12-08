from BinarySearchtree import BinarySearchtree
# Crear una instancia de BinarySearchTree
theTree = BinarySearchTree()

# Insertar nodos duplicados con diferentes valores
theTree.insert(10, "Data 1")
theTree.insert(5, "Data 2")
theTree.insert(15, "Data 3")
theTree.insert(5, "Data 4")
theTree.insert(10, "Data 5")

# Imprimir el árbol
theTree.print()

# Eliminar nodos duplicados
theTree.delete(5)
theTree.delete(10)

# Imprimir el árbol después de eliminar duplicados
theTree.print()
