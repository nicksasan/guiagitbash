#Menu para escoger suma, resta y multiplicacion
print("1. Suma \n2. Resta \n3. Multiplicacion \n4. Salir")
opcion = input("Ingresa un numero de opcion: ")

def suma(a,b):
    return a + b 

def resta(a,b):
    return a - b

def multiplicacion(a,b):
    return a * b

a = int(input("Escribe el primer numero: "))
b = int(input("Escribe el segundo numero: "))

if opcion ==1:
    c = a + b
    print("La suma es: ", c)
    
elif opcion ==2: 
    c = a - b
    print("La resta es: ", c)
    
elif opcion ==3:
    c = a * b
    print("La multiplicacion es: ", c)
    
elif opcion ==4:
    print("baybay")