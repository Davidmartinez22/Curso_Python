### Strings #

#Declaracion de string usando comillas simples y dobes#
variable1 = "Hola uno"
variable2 = 'Hola dos'

print(variable1)
print(variable2)

#Concatenar string con un espacio en blanco
print(variable1 + " " + variable2)

#Crear un salto de linea

variable3 = "Esto es un string\ncon salto de linea"
print(variable3)

# Insertar tabulacion
variable4 = "\tEsto es un string con salto de linea"
print(variable4)

#Escapar caracteres especiales
variable5 = "\\tEsto es un string\\ncon salto de linea"
print(variable5)

#Formateo de strings
name, surname, age = "David", "Martinez", 22

#Formateo usando .format()
print ("Mi nombre es {} {} y mi edad es {}".format(name,surname,age))

# Formateo amtiguo usando %
print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age))

#Concatenar varios string

print ("Mi nombre es" + name + " " + surname + "y mi edad es" + str(age))

#Formateo usando f-strings (moderno)
print (f"Mi nombre es {name} {surname} y mi edad es {age}")

#desempaquetando caracteres

language = "Python"

a,b,c,d,e,f = language
print(a)
print(b)

# Dividir string (Slice)
language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

#Revertir la cadena de texto
language_slice = language[::-1]
print(language_slice)

###Funciones de string###

#Remplazar caracteres de string
fruit = "Strawberry"
fruit_replace = fruit.replace('r', 'R')
print(fruit_replace)

#Convertir el primer caracter Mayusculas
print(fruit.capitalize())

#Covertir el texto a matusculas
print(fruit.upper())

#Contar cuantos caracteres hay del mismo tipo
print(fruit.count("r"))
#Contar todos los caracteres de una palabara
print(len(fruit))

print(f"la variable {fruit} tiene:" + str(len(fruit)))

numero_de_letras = len(fruit)
print(numero_de_letras)
print(str(numero_de_letras).isnumeric())

#Convertir el texto a minusculas 

print(fruit.islower())

#Verificar comienza la cadena con unos caracteres

print(language.startswith("Py"))