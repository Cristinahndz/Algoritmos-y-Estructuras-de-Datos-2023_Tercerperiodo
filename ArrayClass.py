# Implement an Array data structure as a simplified type of list.

class Array(object):
    def __init__(self, initialSize):    # Constructor
      self.__a = [None] * initialSize  # The array stored as a list
      self.__nItems = 0 # No items in array initially

    def __len__(self): # Special def for len()func
      return self.__nItems  # Return number of items
   
    def get(self, n): # Return the value at index n
      if 0 <= n and n < self.__nItems: # Check if n is in bounds, and bounds
        return self.__a[n]            # only return item if in and bounds

    def insert(self, item):     # Insert item at end
        self.__a[self.__nItems] = item # Item goes at current end
        self.__nItems += 1          # Increment number of items

    def set(self, n, value):            # Set the value at index n
        if 0 <= n and n < self.__nItems: # Check if n is in bounds,
            self.__a[n] = value             # only set item if in


    def find(self, item):           # Find index for item
        for j in range(self.__nItems):  # Among current items
            if self.__a[j] == item: # If found,
                return j    # then return index to item
        return -1           # Not found -> return -1


    def search(self, item):                 # Search for item
        return self.get(self.find(item))    # and return item if found
    
    def delete(self, item):             # Delete first occurrence
        for j in range(self.__nItems):  # of an item
            if self.__a[j] == item:     # Found item
                self.__nItems -= 1           # One fewer at end
                for k in range(j, self.__nItems):  # Move items from
                    self.__a[k] = self.__a[k+1]     # right over 1
                return True                # Return success flag
        return False     # Made it here, so couldn't find the item
    
    def traverse(self, function=print): # Traverse all items
       for j in range(self.__nItems):   # and apply a function
          function(self.__a[j])

    def __iter__(self):
        self.__iter_index = 0
        return self

    def __next__(self):
        if self.__iter_index < self.__nItems:
            result = self.__a[self.__iter_index]
            self.__iter_index += 1
            return result
        else:
            raise StopIteration

    def __str__(self):
        ans = "["  # Surround with square brackets
        for i in range(len(self.__a)):  # Loop through items
            if len(ans) > 1:  # Except next to left bracket
                ans += ", "  # Separate items with a comma
            ans += str(self.__a[i])  # Add the string form of the item
        ans += "]"  # Close with a right bracket

        return ans

#metodo Maximo numero
    def getMaxNum(self):
        max_num = None  # Inicialmente, no hay números

        for item in self.__a[:self.__nItems]:
            if isinstance(item, (int, float)): #comprueba si item es una instancia de tipo int,float
                if max_num is None or item > max_num: #comprueba si el valor de item es mayor que el valor actual de max_num
                    max_num = item #si lo es se actualiza max_num
                return max_num

#metodo eliminarmaxnum
    def deleteMaxNum(self):
        max_num = None
        max_index = -1

        for i in range(self.__nItems):
            item = self.__a[i]
            if isinstance(item, (int, float)):
                if max_num is None or item > max_num:
                    max_num = item
                    max_index = i

        if max_index != -1:
            # Remove the item with the highest numeric value
            self.delete(self.__a[max_index])

        return max_num
#eliminar duplicados
    def removeDupes(self):
        unique_elements = []  # Lista para almacenar elementos únicos
        for item in self.__a:
            if item not in unique_elements:
                unique_elements.append(item)

        self.__a = unique_elements
        self.__nItems = unique_elements

    def swap(self, i, j):
        """
        Intercambia los elementos en las posiciones i y j en la matriz.
        """
        if 0 <= i < self.__nItems and 0 <= j < self.__nItems:
            # Realiza el intercambio de elementos
            self.__a[i], self.__a[j] = self.__a[j], self.__a[i]
#3.1
    def bubbleSort(self):
        left = 0  # Índice izquierdo
        right = self.__nItems - 1  # Índice derecho
        while left < right:
            # Mueve el elemento más grande hacia la derecha (de izquierda a derecha)
            for i in range(left, right):
                if self.__a[i] > self.__a[i + 1]:
                    self.swap(i, i + 1)# recorre desde lefthasta right, comparando cada elemento con su siguiente. Si un elemento es mayor que el siguiente, se intercambiarán utilizando el método self.swap(i, i + 1). Esto mueve el elemento más grande hacia la derecha.

            # Decrementa el índice derecho para excluir el elemento más grande ya ordenado
            right -= 1

            # Mueve el elemento más pequeño hacia la izquierda (de derecha a izquierda)
            for i in range(right, left, -1):
                if self.__a[i] < self.__a[i - 1]:
                    self.swap(i, i - 1)#En el segundo bucle for, recorre desde righthasta leften orden inverso, comparando cada elemento con su anterior. Si un elemento es menor que el anterior, se intercambiarán utilizando self.swap(i, i - 1). Esto mueve el elemento más pequeño hacia la izquierda.

            # Incrementa el índice izquierdo para excluir el elemento más pequeño ya ordenado
            left += 1







