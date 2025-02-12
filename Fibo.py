N = int(input("Ingrese la cantidad: "))
a, b = 0, 1
if N <= 0:
    print("Por favor, ingrese un número mayor a 0.")
else:
    print("Serie de Fibonacci:")
    for _ in range(N + 1):
        print(a, end=" ")  
        a, b = b, a + b  
