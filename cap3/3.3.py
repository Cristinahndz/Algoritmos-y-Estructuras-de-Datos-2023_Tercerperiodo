from SortArrayClass import Array

arr = Array(20)
arr.insert(1)
arr.insert(2)
arr.insert(2)
arr.insert(3)
arr.insert(3)
arr.insert(4)

print("Original array:", arr)

arr.deduplicate()
print("Array after deduplication:", arr)