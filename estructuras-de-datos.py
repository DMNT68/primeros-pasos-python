# Estructura de datos: estas son herramientas para guardar información de forma más compleja i con mas facilidades
# Lista: conjunto de variables de cualquier tipo (integer,float string, incluso otras listas) 

# mi_lista = [5,3,4,5]
# mi_lista2 = [True,"hola",23,[1,3,4,False]]
#print(sum(mi_lista))

nombre=["A","N","D","R","E","S","-","S","A","L","G","A","D","O"]
# print(nombre[5]) # Obtiene el elemento de la lista en la posición.
# print(nombre[-1]) # Obtiene el ultimo elemento de la lista.
# print(nombre[0:6]) # obtiene un rango en la lista, formado una nueva lista.
# print(nombre[:-7]) # obtiene un rango desde primero hasta el el final, menos lo 7 útimos elementos.
# print(nombre[1:]) # obtiene un rango desde el segundo hasta el final
# nombre[6] = "_" # permite cambiar el valor del elemento de una posición
# print(nombre)
# nombre[1:6] = ["n","d","r","e","s"]
# print(nombre)


# Ordenar una lista
# nums = [6,5,9,8,2]
# print(nums)
# nums.sort() # sort() ordena los elementos de una lista
# print(nums)
# altos = nums[1:]
# print(altos)
# res = sum(altos)
# print(res)

# Agregar elementos
#  nums = [1,2,3,4]
# nums.append(5) # agrega un elemento al final de la lista
# nums.extend([5,6,7,8])
# print(nums) # agrega varios elementos al final de la lista

# Cancatenación de listas (no altera nuestra lista inicial)
# print (nombre + ["24"])

# multiplicar la lista (no altera nuestra lista inicial)
# print(["hola"]*4)

# insert() Este agrega un elemento en una posición que se desea insertar
# nums = [1,2,3]
# nums.insert(1,5)
# print(nums)

# "del" Borra elementos o listas enteras

mi_lista = [2,4,6,8,5,3,1]
print(mi_lista)
# del mi_lista[1:5]
# # del mi_lista # Borra la lista entera
# print(mi_lista)

# "remove" quita un elemento indicado
# mi_lista.remove(5)
# print(mi_lista)

# "pop" Quita elementos por su indice, si no se especifica un indice, se quita el ultimo elemento
mi_lista.pop(5)
print(mi_lista)