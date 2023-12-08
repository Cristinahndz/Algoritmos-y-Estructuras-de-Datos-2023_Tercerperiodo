
from ArrayClass import Array

arr = Array(10)
arr.insert(64)
arr.insert(34)
arr.insert(25)
arr.insert(12)
arr.insert(22)
arr.insert(11)
arr.insert(90)

print("Lista original:")
for i in range(arr._Array__nItems):
    print(arr._Array__a[i], end=" ")
print()

arr.bubbleSort()

print("Lista ordenada con bubbleSort:")
for i in range(arr._Array__nItems):
    print(arr._Array__a[i], end=" ")
print()





