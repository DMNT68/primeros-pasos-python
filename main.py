# saludo = "Hola "
# nombre = input("Ingrese su nombre ")
# print(saludo + nombre)

# num1 = int(input("Ingrese el primer número: "))
# num2 = int(input("Ingrese el segundo número: "))
# print("La suma de num1 y num2 es:")
# print(num1+num2)
# print("La resta de num1 y num2 es:")
# print(num1-num2)
# print("La multiplicación de num1 y num2 es:")
# print(num1*num2)
# print("La división de num1 y num2 es:")
# print(num1/num2)

# IF Y OPERADORES DE COMPARACION
# print(5 < 10) #true
# print(2 > 20) #false
# print(6 <= 6) #true
# print(0 == 0) #true

'''
prom = input('Pedir promedio')
si prom > 6 entondes
    aprueba
sino
    reprueba
'''

nota1 = int(input("Ingrese la primera nota: "))
nota2 = int(input("Ingrese la segunda nota: "))
nota3 = int(input("Ingrese la tercera nota: "))

prom = (nota1 + nota2 + nota3)/3

print("Tú promedio es: %.2f" %prom)

if (prom>6):
    print("Aprobado")
else:
    print("Desaprobado")