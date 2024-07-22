  #  Booleanos bools 
   # Tipo de dato primitivo
    #Valor de verdad: True o False
"""
"""
"""
"""
"""
"""
"""
"""
# IndexError: list index out of range
# Puedo cambiar el valor de los elementos
# Quiero cambiar banana por coco (indice 1)
# Si quiero imprimir un elemento (banana) debo hacerlo por su índice
# Un error típico es intentar acceder a un índice que no existe
#### LISTA
#print(myFruitList[5])
#* Los elementos pueden ser de cualquier tipo de dato
#* Mantiene un orden (Vale la pena aclarar)
#* Se define con [] y separa sus elementos con ,
#Colecciones
#Es una colección ordenada de valores
#Muy similar a la lista
#NO es mutable
#Se define con corchetes redondos () y se separa con ,
#TUPLA
#Tipos de datos compuestos
almuerzo = True
descanso = False
myFinalAnswerTuple = ("apple", "banana", "pineapple")
myFruitList = ["apple", "banana", "cherry"]
mFruitList[1] = "coco"
numeros = [100, 95, 82]
personas = ["Anahi", "David", "Ariel", 34, True, False]
personas = ["Anahi", "David", "Ariel"]
print(f"El segundo elemento es {myFruitList[1]}") 
print(f"El tipo de dato es {type(myFruitList)}")
print(f"La lista de frutas es {myFruitList}")
print(f"La nueva lista es {myFruitList}
print(f"La variable almuerzo tiene el valor {almuerzo} y es de tipo {type(almuerzo)}")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

"""
Diccionarios

Colección de valores guardados con un modelo llave valor
El diccionario se define con {} y elementos separados por ,
Cada elemento se ve llave : valor
La llave podría ser un string o entero
El valor podría ser de cualquier tipo de dato
"""

persona={"Nombre": "Julian Vasquez", "Ciudad": "Santiago", "Edad": 26}

print(persona)
print(type(persona))
# La manera de acceder a un valor es por su llave
print(persona["Ciudad"])

# Puedo cambiar un valor 
persona["Ciudad"] = "Viña del Mar"
#persona["Ciudad"] = input("Cuál es tu ciudad? ")

print(persona["Ciudad"])