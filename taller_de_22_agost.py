#Menu para escoger suma, resta y multiplicacion
print("1. Suma \n2. Resta \n3. Multiplicacion \n4. Salir")
opcion = int(input("Ingresa un numero de opcion: "))

def suma(a,b):
    return a + b 

def resta(a,b):
    return a - b

def multiplicacion(a,b):
    return a * b

if opcion ==1:
    a = int(input("Escribe el primer numero: "))
    b = int(input("Escribe el segundo numero: "))
    c = suma(a, b)
    print("La suma es: ", c)
    
elif opcion ==2: 
    a = int(input("Escribe el primer numero: "))
    b = int(input("Escribe el segundo numero: "))
    c = resta(a, b)
    print("La resta es: ", c)
    
elif opcion ==3:
    a = int(input("Escribe el primer numero: "))
    b = int(input("Escribe el segundo numero: "))
    c = multiplicacion(a, b)
    c = a * b
    print("La multiplicacion es: ", c)
    
elif opcion ==4:
    print("baybay ùwú")

else:
    "Salga de la opcion"