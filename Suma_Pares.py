A = int(input("Ingrese el valor de A: "))
B = int(input("Ingrese el valor de B: "))

if A > B:
    A, B = B, A  
suma = 0
for num in range(A, B + 1):
    if num % 2 == 0:  
        suma += num  
print(f"La suma de los números pares entre {A} y {B} es: {suma}")
