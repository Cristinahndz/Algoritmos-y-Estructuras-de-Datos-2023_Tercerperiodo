
"""Reescribe los métodos traverse(), __str__() y __len__() del
Clase LinkedList que se muestra en el Listado 5-4 para usar el iterador (creado por
el generador) que se muestra en el Listado 5-23."""


class Link:
    def __init__(self, data): #representan nodos con dato y ref al sig. nodo
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.first = None

    def append(self, data):
        new_link = Link(data)
        if self.first is None:
            self.first = new_link
        else:
            current = self.first
            while current.next is not None:
                current = current.next
            current.next = new_link

    def __iter__(self):
        next_link = self.first
        while next_link is not None:
            yield next_link.data  # Devuelve el dato del enlace actual
            next_link = next_link.next

    def traverse(self, func=print):
        for item in self:
            func(item)

    def __len__(self):
        return sum(1 for _ in self)

    def __str__(self):
        elements = [str(item.data) if isinstance(item, Link) else str(item) for item in
                    self]  # Utiliza item.data si es un objeto Link
        return "[" + " > ".join(elements) + "]"

if __name__ == "__main__":
    my_list = LinkedList()
    my_list.append("A")
    my_list.append("B")
    my_list.append("C")

    print("Iterando a traves de la lista: ")
    for item in my_list:
        print(item)

    print("Usando el metodo traverse:")
    my_list.traverse()

    print("Longitud de la lista:", len(my_list))
    print("Representacion de cadena de la lista:", my_list)



