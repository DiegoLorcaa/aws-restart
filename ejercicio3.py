"""
nombre = input("¿Cual es tu Nombre?")
edad = int(input("¿Cuantos años tienes? "))
edad2 = edad + 5
print (f"Tus años en 5 años será: {edad2}")

print()

fruta = ["Mandarina", "sandía", "piña", "naranja", "melón"]
print(f"La tercera fruta de la lista es:{fruta[2]}")

print()

numero = int(input(f"Ingrese un numero: "))
if numero % 2 == 0:
    #print(f"El numero {numero} es par")
else:
    #print(f"El numero {numero} es impar")
    
print()

edadP = int(input(f"Ingrese su edad: "))
if edadP >= 18:
    print(f"Eres mayor de edad")
    print(f"Puedes votar en las elecciones")
else:
    print(f"No eres mayor de edad")
    print(f"No puedes votar en las elecciones")
    
print()
    
gradosC = int(input("Ingrese la temperatura del agua:"))
if gradosC <= 0:
    print(f"El agua se comienza a congelar y el estado pasa de liquido a solido")
elif gradosC >= 100:
    print(f"El agua comienza a estar en ebullicion y el estado pasa de liquido a gaseoso")
else:
    print("El estado del agua está en estado líquido")
    
print()
    
num = int(input("Ingrese un numero:"))
if num < 0: 
    print(f"El numero es negativo")
elif num > 0:
    print(f"El numero es positivo")
else:
    print(f"el numero es 0")


num1 = int(input("ingrese un numero:"))
num2 = int(input("ingrese otro numero:"))

if num1 >= 0 and num2 >= 0:
    print(f"Ambos numeros son positivos")
else:
    print(f"1 o los 2 numeros no son positivos")
print()
edad = int(input("Ingrese su edad: "))
identificacion = input("¿Tiene una identificación válida? responda si o no:")
print()
if edad >= 18 and identificacion == "si":
    print(f"La persona está apta para votar en las elecciones")
elif edad < 18 and identificacion == "si":
    print(f"No tiene edad necesaria para poder votar")
elif edad >= 18 and identificacion == "no":
    print(f"Tiene la edad necesaria para votar pero no tiene identificacion válida")
else:
    print(f"No cumple ningun requisito para poder votar")

comidas = ["lasaña", "pantrucas", "asadito", "arroz con huevo"]
for comida in comidas:
    print(comida)
    """
i=1
for i in range(i,11):
    print(i)
print()
i=1
while i<=5:
    print(i)
    i += 1
        # TODO: write code...