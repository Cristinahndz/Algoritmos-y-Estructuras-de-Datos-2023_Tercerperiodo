from ArrayClass import Array



arr = Array(10)
arr.insert(2)
arr.insert("texto")
arr.insert(2.5)
arr.insert(0)
arr.insert("otro texto")
arr.insert(8)
arr.insert(None)

# Obtener el valor máximo de la matriz
max_num = arr.getMaxNum()

if max_num is not None:
    print("El valor máximo en la matriz es:", max_num)
else:
    print("La matriz no contiene números.")

# Crear una matriz que no contiene números
arr2 = Array(5)
arr2.insert("uno")
arr2.insert("dos")
arr2.insert("tres")

# Obtener el valor máximo de la segunda matriz
max_num2 = arr2.getMaxNum()

if max_num2 is not None:
    print("El valor máximo en la segunda matriz es:", max_num2)
else:
    print("La segunda matriz no contiene números.")







