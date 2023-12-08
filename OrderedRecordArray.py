def identity(x): # The identity function
    return x
class OrderedRecordArray(object):
    def __init__(self, initialSize, key=identity): # Constructor
        self.__a = [None] * initialSize # The array stored as a list
        self.__nItems = 0 # No items in array initially
        self.__key = key # Key function gets record key
    def __len__(self): # Special def for len() func
         return self.__nItems # Return number of items

    def get(self, n): # Return the value at index n
         if n >= 0 and n < self.__nItems: # Check if n is in bounds,and
             return self.__a[n] # only return item if in bounds

         raise IndexError("Index " + str(n) + " is out of range")
    def traverse(self, function=print): # Traverse all items
         for j in range(self.__nItems): # and apply a function
            function(self.__a[j])
    def __str__(self): # Special def for str() func
        ans = "[" # Surround with square brackets
        for i in range(self.__nItems): # Loop through items
            if len(ans) > 1: # Except next to left bracket,
                ans += ", " # separate items with comma
            ans += str(self.__a[i]) # Add string form of item
        ans += "]" # Close with right bracket
        return ans

    def insertOrdered(self, item):
        key = self.__key_function(item)
        index = 0
        while index < len(self.__a) and key > self.__key_function(self.__a[index]):
            index += 1
        self.__a.insert(index, item)

    def merge(self, source_array):
        if self.__key_function != source_array.__key_function:
            raise ValueError("Key functions of source and destination arrays must be identical.")

        merged_array = []
        i, j = 0, 0

        while i < len(self.__a) and j < len(source_array.__a):
            if self.__key_function(self.__a[i]) < self.__key_function(source_array.__a[j]):
                merged_array.append(self.__a[i])
                i += 1
            else:
                merged_array.append(source_array.__a[j])
                j += 1

        while i < len(self.__a):
            merged_array.append(self.__a[i])
            i += 1

        while j < len(source_array.__a):
            merged_array.append(source_array.__a[j])
            j += 1

        self.__a = merged_array

    def display(self):
        for item in self.__a:
            print(item)

    def __init__(self, initialSize):
        if not isinstance(initialSize, int):
            raise ValueError("Initial size must be an integer")
        self.__a = [None] * initialSize

    def set_key_function(self, key_function):
        self.__key_function = key_function








