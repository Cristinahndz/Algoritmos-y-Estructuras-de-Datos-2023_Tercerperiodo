from ArrayClass import Array

# Create an array with values
arr = Array(20)
arr.insert(1)
arr.insert(4)
arr.insert(2)
arr.insert(3)
arr.insert(9)

# Get the maximum value
max_value = arr.deleteMaxNum()

# Convert the Array to a list
arr_list = [arr.get(i) for i in range(len(arr))]

# Sort the list in ascending order
sorted_list = sorted(arr_list)

# Print the results
print(f"Original array: {arr}")
print(f"Maximum value deleted: {max_value}")
print(f"Sorted array: {sorted_list}")