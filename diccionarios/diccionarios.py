
'''
Diccionarios
'''
# mi_dic = {"nombre":"Andrés","edad":26,"verdad":True}
# print(mi_dic["nombre"])
# print(mi_dic["apellido"]) # Bota error key_error
# print(mi_dic.get("apellido")) # Bota None
# print(mi_dic.get("apellido","NO exite esta key"))

# mi_dic["verdad"] = False

# for key, value in mi_dic.items():
#     print(key)
#     print(value)

# if "apellido" in mi_dic:
#     print("hay edad")

# mi_dic["apellido"] = "Salgado"
# print(mi_dic)

import random
import nombres


noms = nombres.get_nombres()
alumnos = {}

for nombre in noms:
    notas = [random.randint(1,10) for i in range(3)]
    alumnos[nombre] = notas

promedios = {}
for nom in alumnos:
    notas = alumnos[nom]
    suma = 0
    for nota in notas:
        suma = nota + suma
    promedios[nom] = suma /3

print(promedios) 