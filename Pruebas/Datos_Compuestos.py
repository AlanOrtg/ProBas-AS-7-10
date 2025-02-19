
#La lista se puede modificar despues y se usa entre corchetes
lista = ["pyro", "hydro", "electro", "dendro", "cryo", "anemo", "geo"]
print(lista[2])

#La tulpa ya no se puede modificar despues y se usa entre parenstesis
#Siempre el indice ya se de la tulpa o la lista que se quiera mostrar (en este caso el 5 o el 2) va entre "[]" 
tulpa =("Py", "Hy", "El", "De", "Cr", "An","Geo")
print(tulpa[5])

#el conjunto o "SET" no tiene orden de indice y se usa entre llaves ademas no se pueden repetir los datos en el
conjunto = {"Py", "Hy", "El", "De", "Cr", "An","Geo"}


#Esto no se puede hacer ya que no tienen indice al estar por haci decirlo al azar
# print(conjunto[5])

#Esto es lo que se hace: 

print(conjunto)

#el diccionario tambien se usa con llaves y en este los indices (0,1,2,3,4,5, etc) son remplazados por claves ejemplo

diccionario = {
    "nombre" : "Alan",
    "Matricuula" : "2009042", 
    "Materia" : "ProBras"
    }
print(diccionario["nombre"])


#El type sirve para saber que tipo de dato es una variable
tipo_Dato = type(conjunto)
print(tipo_Dato)