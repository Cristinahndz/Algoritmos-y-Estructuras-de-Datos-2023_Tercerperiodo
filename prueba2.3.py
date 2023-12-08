from ArrayClass import Array

# Create an array with values
arr = Array(10)
arr.insert(1)
arr.insert(4)
arr.insert(2)
arr.insert(3)
arr.insert(5)

# Get the maximum value
max_value = arr.deleteMaxNum()

# Sort the array in ascending order (default)
sorted_array = sorted(arr)

# Print the results
print(f"Arreglo original: {arr}")
print(f"Maximo valor eliminado: {max_value}")
print(f"Arreglo ordenado: {sorted_array}")