class Deque:
    def __init__(self, size):
        self.size = size
        self.data = [None] * size
        self.front = -1
        self.rear = 0

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.front == 0 and self.rear == self.size - 1) or (self.rear + 1 == self.front)

    def insert_left(self, item):
        if self.is_full():
            print("Deque is full. Cannot insert left.")
            return
        if self.front == -1:
            self.front = self.rear = 0
        elif self.front == 0:
            self.front = self.size - 1
        else:
            self.front -= 1
        self.data[self.front] = item

    def insert_right(self, item):
        if self.is_full():
            print("Deque is full. Cannot insert right.")
            return
        if self.front == -1:
            self.front = self.rear = 0
        elif self.rear == self.size - 1:
            self.rear = 0
        else:
            self.rear += 1
        self.data[self.rear] = item

    def delete_left(self):
        if self.is_empty():
            print("Deque is empty. Cannot delete left.")
            return
        if self.front == self.rear:
            self.front = self.rear = -1
        elif self.front == self.size - 1:
            self.front = 0
        else:
            self.front += 1

    def delete_right(self):
        if self.is_empty():
            print("Deque is empty. Cannot delete right.")
            return
        if self.front == self.rear:
            self.front = self.rear = -1
        elif self.rear == 0:
            self.rear = self.size - 1
        else:
            self.rear -= 1

    def peek_left(self):
        if self.is_empty():
            return None
        return self.data[self.front]

    def peek_right(self):
        if self.is_empty():
            return None
        return self.data[self.rear]

# Ejemplo de uso:
deque = Deque(5)
deque.insert_left(1)
deque.insert_left(2)
deque.insert_right(3)
deque.insert_right(4)

print("Left Peek:", deque.peek_left())
print("Right Peek:", deque.peek_right())

deque.delete_left()
deque.delete_right()

print("Left Peek after deletion:", deque.peek_left())
print("Right Peek after deletion:", deque.peek_right())
