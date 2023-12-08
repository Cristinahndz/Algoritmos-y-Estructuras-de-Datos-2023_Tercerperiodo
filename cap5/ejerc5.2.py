
"""Implemente una cola de prioridad basada en una lista vinculada ordenada. El
Los elementos almacenados en la cola se pueden pasar a una función que extrae
su valor de prioridad (o clave) como en el módulo PriorityQueue.py en
Capítulo 4. La operación de eliminación en la cola de prioridad debe eliminar
el elemento con la clave más pequeña."""



class PriorityQueueNode: #es una clase que se utiliza para representar los elementos de la cola de prioridad
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority #prioridad o clave del elem
        self.next = None #apunta al sigu. nodo en la lista


class PriorityQueue: #cola de proridad
    def __init__(self):
        self.head = None #apunta al primer nodo de la lista

    def is_empty(self): #verif si la cola de proridad esta vacia
        return self.head is None

    def insert(self, data, priority):
        new_node = PriorityQueueNode(data, priority) #crea un nuevo nodo

        if self.is_empty() or priority < self.head.priority: #si la cola esta vacia del nuevo eleme. es menor que la del primero
            new_node.next = self.head #apunta al antiguo head
            self.head = new_node #head se actualiza y apunta al nuevo nodo
        else:
            current = self.head #itera a traves de la lista vinculada
            while current.next is not None and current.next.priority <= priority: #mientras no se llegue al final de la lista
                current = current.next #permite encontrar la posición adecuada en la lista para insertar el nuevo nodo
            new_node.next = current.next
            current.next = new_node

    def remove(self):
        if not self.is_empty():
            data = self.head.data
            self.head = self.head.next
            return data
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.head.data
        else:
            return None


# Ejemplo de uso
if __name__ == "__main__":
    priority_queue = PriorityQueue()

    priority_queue.insert("A", 3)
    priority_queue.insert("B", 1)
    priority_queue.insert("C", 2)

    print("Elementos en la cola de prioridad:")
    while not priority_queue.is_empty():
        print(priority_queue.remove())
