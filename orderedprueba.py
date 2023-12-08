from OrderedRecordArray import OrderedRecordArray
array1 = OrderedRecordArray(10)

def key_function(item):
    # Lógica para calcular la clave de un elemento
    if isinstance(item, dict) and 'key' in item:
        return item['key']
    else:
        raise ValueError("Element does not have a valid 'key'")


array1.set_key_function(key_function)

array1.insertOrdered({'key': 3, 'value': 'A'})
array1.insertOrdered({'key': 5, 'value': 'B'})
array1.insertOrdered({'key': 7, 'value': 'C'})

array2 = OrderedRecordArray(10)
array2.set_key_function(key_function)

array2.insertOrdered({'key': 2, 'value': 'D'})
array2.insertOrdered({'key': 4, 'value': 'E'})
array2.insertOrdered({'key': 6, 'value': 'F'})

array1.merge(array2)

array1.display()





