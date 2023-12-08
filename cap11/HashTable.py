import random

class HashTable:
    def __init__(self, capacity=11): #capacidad de la tabla
        self.capacity = capacity
        self.size = 0
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity #inicializa la matriz para almac valores
        
    def hash(self, key): #convierte la clave de entrada en un valor hash
        hash_value = 0 #almacena el valor del hash intermedio
        prime1 = 31
        prime2 = 37
        for byte in key.to_bytes((key.bit_length() + 7) // 8, 'little'): #convierte el #key en una secuencia de bytes 
            hash_value = hash_value * prime1 + byte + prime2 #se actualiza el valor hash
        return hash_value % self.capacity #mod de valor hash con la capacidad
    
    # Modif 11.4
    def doubleHashProbe(self, start, key): #start indice inicial para doble hsh;método doublehash genera una secuencia de índices para doble hash
        yield start % self.capacity
        step = self.doubleHashStep(key) #Calcula el tamaño del paso para el doble hash 
        for i in range(1, self.capacity): #genera secuencia de indices
            yield (start + i * step) % self.capacity
        
    def doubleHashStep(self, key): #calcula el tamaño del paso para la secuenc de indices
        prime = self.primeBelow(self.capacity) #Calcula un número primo por debajo de la capacidad de la tabla 
        return prime - (self.hash2(key) % prime)
    
    def hash2(self, key):
        hash_value = 0
        prime1 = 53
        prime2 = 59
        for byte in key.to_bytes((key.bit_length() + 7) // 8, 'little'):
            hash_value = hash_value * prime1 + byte + prime2
        return hash_value
        
    def primeBelow(self, n):
        n -= 1 if n % 2 == 0 else 2 #Disminuye n en 1 si es par; de lo contrario, lo disminuye en 2
        while (3 < n and not self.is_prime(n)):
            n -= 2 #avanzando hacia números impares más pequeños
        return n # devuelve el número primo más grande y menor que el original 
    
    def is_prime(self, n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1): #desde 2 hasta la raíz cuadrada de n
            if n % i == 0: #significa que n no es un número primo
                return False
        return True
    
    def insert(self, key, value):
        if self.size == self.capacity:
            print("La tabla Hash esta llena")
            return
        index = self.hash(key)
        if self.keys[index] is None: #Comprueba si la ranura en el índice calculado está vacía 
            self.keys[index] = key
            self.values[index] = value
            self.size += 1
        elif self.keys[index] == key: #Si la ranura no está vacía pero contiene la misma clave que la que se está insertando
            self.values[index] = value
        else: #Si la ranura inicial está ocupada por una clave diferente, ingresa a un bucle usando el doubleHashProbe
            for i in self.doubleHashProbe(index, key):
                if self.keys[i] is None:
                    self.keys[i] = key
                    self.values[i] = value
                    self.size += 1
                    break
                elif self.keys[i] == key:
                    self.values[i] = value
                    break
                    
    def get(self, key): #recupera el valor asociado con una clave determinada en la tabla hash
        index = self.hash(key)
        for i in self.doubleHashProbe(index, key):
            if self.keys[i] == key:
                return self.values[i]
            elif self.keys[i] is None:
                return None
        return None

# Prueba
table = HashTable()
print("Insertando 20 claves seleccionadas aleatoriamente del rango [0, 99999]:")
print("{:<10} {:<20} {:<20} {:<20}".format("Key", "Dirección cifrada", "Módulo con Prime", "Secuencia de sonda"))
print("{:<10} {:<20} {:<20} {:<20}".format("---", "--------------", "----------------", "-------------"))
for i in range(20): #inicia un bluce generando una clave aleatoria 
    key = random.randint(0, 99999)
    hashed_address = table.hash(key)
    prime = table.primeBelow(table.capacity)
    step = table.doubleHashStep(key)
    modulo_prime = hashed_address % prime
    probe_sequence = [str(j) for j in table.doubleHashProbe(hashed_address, key)]
    probe_sequence_str = '->'.join(probe_sequence)
    table.insert(key, i)
    print("{:<10} {:<20} {:<20} {:<20}".format(key, hashed_address, modulo_prime, probe_sequence_str))
