mystring = "this is a string"
print(mystring)
print(type(mystring))
print(f"el tipo de data de {mystring} es {type(mystring)}")

primero = "water"
segundo = "fall"
tercero = primero + segundo
print(tercero)

nombre = input("¿Cual es tu nombre? ")
print(nombre)
color = input("¿Cual es tu color favorito? ")
animal = input("¿Cual es tu animal favorito? ")
print("{}, te gusta {} {}!".format(nombre,animal,color))

num = int(input("ingresa un numero: "))
num2 = int(input("ingresa otro numero: "))
resultado = num + num2
print(f"La suma de {num} y {num2} es {resultado}")