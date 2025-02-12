
suma = 0
contador = 0

for nota in range(10000000000):  
    nota = int(input("Ingrese calificación: "))
    if nota < 0:  
        break
    suma += nota 
    contador += 1  
if contador > 0:
    promedio = suma / contador
    print("El promedio es:", promedio)

