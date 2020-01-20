def mi_funcion(nombre):
    print(f"soy {nombre}")

# mi_funcion("Andres")

def suma(a,b):
    res = a+b
    return "soy una suma", res

tipo, resultado = suma(2,3)

# print(tipo)
# print(resultado)
# import random
# def get_stats():
#     dados = [random.randint(1,6) for i in range(4)]
#     dados.sort()
#     max_dados = dados[1:]
#     return sum(max_dados)

# stats = {
#     "Fuerza": get_stats(),
#     "Destreza": get_stats(),
#     "Inteligencia": get_stats(),
#     "Sabiduria": get_stats(),
#     "Constitución": get_stats(),
# }
# print(stats)


# Variable locales
# def change_var(v, l=[]):
#     l.append(v)
#     return l

# change_var(2)
# change_var(5)
# change_var(6)
# lst = change_var(8)

# print(lst)

def suma(a,b):
    return a+b

def resta(a,b):
    return a-b
    
def mult(a,b):
    return a*b

def div(a,b):
    return a/b

# "args" es una tupla que tiene los elemento que se requiera
def argumentos(*args):
    print (args)
# argumentos("hola",2,"chau")

# "kwargs" son como los args pero se puede pasar variables con key words
def kwargumentos(**kwargs):
    print (kwargs)
# kwargumentos(nombre="Andrés", años=26, despedida ="Chau")

op = {
    "suma":suma,
    "resta":resta,
    "mult":mult,
    "división":div
}

print(op["división"](12,3))