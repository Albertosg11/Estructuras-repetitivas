base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

if base == 0 and exponente <= 0:
    print("Error")
else:
    resultado = base ** exponente
    print(f"{base} elevado a {exponente} es: {resultado}")
