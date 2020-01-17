# For loopso iteraciones
import random
# numeros = [4,4,5,5,6,7,8,9,4234,52,345]
# for num in numeros:
#     print(num)

# for i in range(10):
#     print(i)
# else:
#     print("no hay mas elementos")

# table2 = [(i+1)*2 for i in range(10)]
# print(table2)

alumnos = []
for i in range(30):
    notas = [random.randint(1,10) for i in range(3)]
    alumnos.append(notas)

promedios = []
for i in range(30):
    alumno = alumnos[i]
    suma = 0
    for nota in alumno:
        suma = nota + suma
    promedios.append(suma /3)

print(promedios) 