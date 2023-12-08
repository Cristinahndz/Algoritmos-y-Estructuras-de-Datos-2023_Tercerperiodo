# Compute factorial numbers

def factorial(n):            # Get factorial of n
   if n <= 1: return 1        # It's 1 for anything < 1
   return (n *               # Otherwise, multiply n 
           factorial(n - 1)) # by preceding factorial

def factorialNoRecursivo(n):
    if n < 0:
        return "El factorial no está definido para números negativos"
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Prueba sin recursividad
numero = 10
resultado = factorialNoRecursivo(numero)
print(f"El factorial de {numero} es {resultado}")

# Prueba con recursividad
numero = 10
resultado = factorial(numero)
print(f"El factorial de {numero} es {resultado}")
