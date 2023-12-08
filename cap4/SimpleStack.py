class StackFullException(Exception):
    pass

class StackEmptyException(Exception):
    pass

class Stack(object):
    def __init__(self, max_size):
        self.__stackList = []
        self.__max_size = max_size

    def push(self, item): #nos permite agg elementos a la pila
        if self.isFull():
            raise StackFullException("Stack está lleno. No se pueden enviar más elementos.")
        self.__stackList.append(item)

    def pop(self): #nos permite extraer elementos de la pila
        if self.isEmpty():
            raise StackEmptyException("Stack esta vacio. No se puede sacar de una pila vacía.")
        return self.__stackList.pop()

    def peek(self):#nos permite ver el elemento en la parte superior de la pila sin eliminarlo
        if self.isEmpty():
            raise StackEmptyException("Stack esta vacio. No puedo echar un vistazo a una pila vacía.")
        return self.__stackList[-1]

    def isEmpty(self):
        return len(self.__stackList) == 0

    def isFull(self):
        return len(self.__stackList) >= self.__max_size

    def __len__(self):
        return len(self.__stackList)

    def __str__(self):
        return str(self.__stackList)
