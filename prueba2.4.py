from ArrayClass import Array

arr = Array(10)
arr.insert(1)
arr.insert(2)
arr.insert(2)
arr.insert(3)
arr.insert(3)
arr.insert(4)

print("Original array:", arr)
arr.removeDupes()
print("Array after removing duplicates:", arr)