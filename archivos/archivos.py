#  Archivos

# datos = 'hola mundo 2'
# file = open("datos.txt","w")
# file.write(datos)
# file.close()

# with open('db/datos.txt', 'w') as file: # escribir ene el archivo
#     file.write(datos)

# with open('db/datos.txt', 'r') as file:
#     text = file.read()

# print(text)

# Archivos prolongados parte 2

# def fixed_width_parse(datos):
#     lst = [
#         "{0:05d}".format(datos[0]),
#         datos[1],
#         "".join(datos[2].split("/")),
#         "".join(datos[3].split(":"))
#     ]
#     str_lst = "".join(lst)
#     return str_lst

# def fixed_width_read(datos_entrada):
#     lst_out = [
#         int(data_in[0:5]),
#         data_in[5:6],
#         "/".join([data_in[6:8], data_in[8:11], data_in[11:15]]),
#         ":".join([data_in[15:17], data_in[17:19], data_in[19:21]])
#     ]
#     print(lst_out)
#     # print(datos_entrada)


# '''
# id_persona | Tipo | Fecha y hora
# 00001e10may2019071530
# '''

# data = [10,'e','10/MAY/2019', '07:15:30']

# str_datos = fixed_width_parse(data)

# with open('entr_sal.txt','w') as outf:
#     outf.write(str_datos)

# with open('entr_sal.txt','r') as inf:
#     data_in = inf.read()

# # print(data_in)
# fixed_width_read(data_in)


# Archivos delimitados parte 3

'''
Leer de un archivo alumnos.csv y crear una lista de diccionarios.
Luego crear un random de faltas entr 1 y 15 para luego guardar la nueva lista 
en un nuevo archivo alumnos_nuevo.csv
'''
# import random

# with open("src/alumnos.csv") as fi:
#     alumnos = []
#     ln = fi.readline()
#     while ln != "":
#         alumnos.append(ln.replace("\n","").split(","))
#         ln = fi.readline()

 # print(alumnos)

# alumnos_nuevo = []
# for alumno in alumnos:
#     alumno.append(random.randint(1,15))
#     alumnos_nuevo.append(alumno)

# [alumno.append(str(random.randint(1,15))) for alumno in alumnos]
# print(alumnos)

# alumnos_nuevo  = [",".join(alumno) for alumno in alumnos]
# alumnos_nuevo  = "\n".join(alumnos_nuevo)

# with open("db/alumnos_nuevo.csv",'w') as fo:
#     fo.write(alumnos_nuevo)

# Archivos formato Json parte 4

'''
Leer de un archivo persona.json y pasar su contenido a un estructura de python.
Luego crear un nuevo elemento y guardarlo en  un archivo json
'''

import json

with open('src/persona.json') as fi:
    persona = json.loads(fi.read())

# print(persona['nombre'])
# print(persona['hobbies'][1])
# print(persona['hijos'][0])

eric = {
    "nombre":"Eric",
    "edad":27,
    "hobbies": ["programar","jueguitos", "editar videos"],
    "hijos": None
}

with open("db/persona_eric.json", 'w') as fo:
    json.dump(eric,fo)