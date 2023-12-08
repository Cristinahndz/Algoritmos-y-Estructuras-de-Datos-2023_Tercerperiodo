
from SimpleStack import Stack, StackFullException, StackEmptyException

def test_stack():
    stack = Stack(3)#instancia dela clase stack

    try:
        stack.push(1)
        stack.push(2)
        stack.push(3)
        print("Stack despues de empujar 3 elementos:", stack)
    except StackFullException as e:
        print(e)

    try:
        stack.push(4)  # Esto intentará ingresar a una pila completa y generara una excepción.
    except StackFullException as e:
        print(e)

    try:
        item = stack.pop()# Esto intentará extraer un elemento de una pila
        print("Popped item:", item)
    except StackEmptyException as e:
        print(e)

    try:
        item = stack.pop()  # se intenta extraer otro elemento de la pila, pero la pila ya está vacía como resultado se captura la excepción
        print("Popped item:", item)
    except StackEmptyException as e:
        print(e)

if __name__ == "__main__":
    test_stack()

