"""Implemente una deque basada en una lista doblemente enlazada. (Ver
Proyecto de Programación 4.3 del capítulo anterior). Debe incluir
insertarIzquierda(), insertarDerecha(), eliminarIzquierda(), eliminarDerecha(),
Métodos peekLeft(), peekRight() y isEmpty()."""




class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertIzquierda(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insertDerecha(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def eliminarIzquierda(self):
        if self.head is None:
            return None
        data = self.head.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return data

    def eliminarDerecha(self):
        if self.tail is None:
            return None
        data = self.tail.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return data

    def peekLeft(self):
        return self.head.data if self.head else None

    def peekRight(self):
        return self.tail.data if self.tail else None

    def isEmpty(self):
        return self.head is None

if __name__ == "__main__":
    deque = DoublyLinkedList()  # Crear un nuevo deque

    print("Is Empty:", deque.isEmpty())  # True, el deque está vacío

    # Insertar elementos en el deque
    deque.insertDerecha(1)
    deque.insertDerecha(2)
    deque.insertIzquierda(0)

    print("Is Empty:", deque.isEmpty())  # False, el deque ya no está vacío

    print("Left:", deque.peekLeft())  # 0, el elemento más a la izquierda
    print("Right:", deque.peekRight())  # 2, el elemento más a la derecha

    # Eliminar elementos del deque
    deque.eliminarIzquierda()
    deque.eliminarDerecha()

    print("Left:", deque.peekLeft())  # 1, el elemento más a la izquierda después de eliminar
    print("Right:", deque.peekRight())  # 1, el elemento más a la derecha después de eliminar

    # Eliminar el último elemento
    deque.eliminarDerecha()

    print("Is Empty:", deque.isEmpty())  # True, el deque está vacío nuevamente

