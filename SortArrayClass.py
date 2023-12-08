class Array(object):
    def __init__(self, initialSize):  # Constructor
        self.__a = [None] * initialSize  # The array stored as a list
        self.__nItems = 0  # No items in array initially

    def __len__(self):  # Special def for len() func
        return self.__nItems  # Return the number of items

    def get(self, n):  # Return the value at index n
        if 0 <= n < self.__nItems:  # Check if n is in bounds
            return self.__a[n]  # Only return item if in bounds

    def set(self, n, value):  # Set the value at index n
        if 0 <= n < self.__nItems:  # Check if n is in bounds
            self.__a[n] = value  # Only set item if in bounds

    def swap(self, j, k):  # Swap the values at two indices
        if (0 <= j < self.__nItems and 0 <= k < self.__nItems):  # Check if indices are in bounds
            self.__a[j], self.__a[k] = self.__a[k], self.__a[j]

    def insert(self, item):  # Insert item at the end
        if self.__nItems >= len(self.__a):  # If the array is full, raise an exception
            raise Exception("Array overflow")
        self.__a[self.__nItems] = item  # Item goes at the current end
        self.__nItems +=1
        self.__nItems +=1  # Increment the number of items

    def find(self, item):  # Find the index for an item
        for j in range(self.__nItems):  # Among current items
            if self.__a[j] == item:  # If the item is found
                return j  # Return the index of the element
        return -1  # Not found, return -1

    def search(self, item):  # Search for an item and return it if found
        index = self.find(item)
        if index != -1:
            return self.__a[index]

    def delete(self, item):  # Delete the first occurrence of an item
        for j in range(self.__nItems):  # Among current items
            if self.__a[j] == item:  # If the item is found
                self.__nItems -= 1  # One fewer at the end
                for k in range(j, self.__nItems):  # Move items to the left
                    self.__a[k] = self.__a[k + 1]
                return True  # Return success flag
        return False  # Couldn't find the item

    def traverse(self, function=print):  # Traverse all items and apply a function
        for j in range(self.__nItems):
            function(self.__a[j])

    def __str__(self):  # Special def for str() func
        ans = "["  # Surround with square brackets
        for i in range(self.__nItems):  # Loop through items
            if len(ans) > 1:  # Except next to left bracket
                ans += ", "  # Separate items with a comma
            ans += str(self.__a[i])  # Add the string form of the item
        ans += "]"  # Close with a right bracket

        return ans

    def bubbleSort(self):  # Sort comparing adjacent values
        for last in range(self.__nItems - 1, 0, -1):  # Bubble up
            for inner in range(last):  # Inner loop goes up to last
                if self.__a[inner] > self.__a[inner + 1]:  # If the element is less than the adjacent value, swap
                    self.swap(inner, inner + 1)

    def selectionSort(self):  # Sort by selecting the minimum and swapping it to the leftmost
        for outer in range(self.__nItems - 1):  # Mark one element
            min_index = outer  # Assume the minimum is the leftmost
            for inner in range(outer + 1, self.__nItems):  # Hunt to the right
                if self.__a[inner] < self.__a[min_index]:  # If a smaller element is found
                    min_index = inner  # Update the index of the minimum element
            # Swap the leftmost element with the minimum element
            self.swap(outer, min_index)

    def insertionSort(self):  # Sort by repeated inserts
        for outer in range(1, self.__nItems):  # Mark one element
            temp = self.__a[outer]  # Store the marked element in temp
            inner = outer  # Inner loop starts at the mark
            while inner > 0 and temp < self.__a[inner - 1]:  # If marked element is smaller, shift elements to the right
                self.__a[inner] = self.__a[inner - 1]
                inner -= 1  # Move the marked element to the 'hole'
            self.__a[inner] = temp  # Move the marked element to its correct position


#Metodo mediana
    def mediana(self):
        # Eliminar valores nulos (None) de la matriz
        cleaned_array = [item for item in self.__a if item is not None]

        # Ordenar la matriz  de manera ascendente sin valores nulos
        cleaned_array.sort()

        # Calcular la mediana
        n = len(cleaned_array)
        if n % 2 == 1:
            # Si la longitud de la matriz es impar, la mediana es el valor en el medio
            return cleaned_array[n // 2]#Si la longitud es impar, la mediana es el valor en el medio de la lista, que se encuentra en cleaned_array[n // 2].s
            # se usa la división entera //para obtener el índice del valor central.
        else:
            # Si la longitud de la matriz es par, la mediana es el promedio de los dos valores centrales
            middle1 = cleaned_array[(n // 2) - 1]
            middle2 = cleaned_array[n // 2]
            return (middle1 + middle2) / 2

    def deduplicate(self):
        if self.__nItems <= 1: # Esta línea verifica si la matriz tiene uno o ningún elemento, en cuyo caso no hay duplicados para eliminar, por lo que el método simplemente retorna sin hacer nada.
            return

        write_index = 1

        for read_index in range(1, self.__nItems):
            found_duplicate = False#se inicializa en False. Esta variable se utilizará para rastrear si se encuentra un duplicado mientras se compara el elemento actual con los elementos únicos escritos hasta ahora.

            for i in range(write_index):
                if self.__a[i] == self.__a[read_index]:#verifica si el elemento actual en la matriz ( self.__a[read_index]) es igual a uno de los elementos únicos ya escritos. si se encuentrafound_duplicatese establece en True, y se rompe el bucle interno.
                    found_duplicate = True
                    break

            if not found_duplicate:
                self.__a[write_index] = self.__a[read_index]
                write_index += 1

        self.__nItems = write_index#Finalmente, se actualiza self.__nItemspara reflejar el nuevo número de elementos en la matriz, que es igual a write_index, ya que los duplicados se han eliminado y solo quedan elementos únicos.