# OPERADORES ARITMETICOS
suma= 5+2 
print(suma)
# Aqui voy a interpolar el resultando insertando una f en la cadena
print(f"Suma:5+2={5+2}") 
print(f"Resta:5-2={5-2}")
print(f"Multiplicacion:5*2={5*2}")
print(f"Division:5/2={5/2}")
print(f"Division Entera:5//2={5//2}") # Retorna un numero entero sin decimales
print(f"Modulo:5%2={5%2}")
print(f"Exponente:5**2={5**2}")

# OPERADORES DE COMPARACION
print(f"Igualdad:10==3={10==3}")
print(f"Desigualdad:10!=3={10!=3}")
print(f"Mayor que:10>3={10>3}")
print(f"Menor que:10<3={10<3}")
print(f"Mayor o igual que:10>=3={10>=3}")
print(f"Menor o igual que:10<=3={10<=3}")

# OPERADORES LOGICOS
# AND nos sirve para que dos condiciones se cumplan
print(f"AND: 10+3 ==13 and 5-1== 4 es {10+3 ==13 and 5-1== 4}")
# OR nos sirve para que al menos una de las condiciones se cumpla
print(f"OR: 10+3 ==13 or 5-1== 3 es {10+3 ==13 or 5-1== 3}") 
# NOT nos sirve para negar una condicion
print(f"NOT: not(10+3 ==14) es {not(10+3 ==14)}") # Aqui si sirve bien el not porque es una condicion que se cumple, si no se cumple el resultado es False
print(f"NOT: not(10+3 ==14) es {(10+3 ==14)}") # Aqui se muestra el resultado de la condicion sin negarla

# OPERADORES DE ASIGNACION
x = 5 # Asignacion simple
print(f"Asignacion: x = {x}")
x += 2 # Asignacion con suma en mejores palabras es como decir x = x + 2
print(f"Asignacion con suma: x += 2 es {x}") 
print(f"Asignacion con resta: x -= 2 es {x - 2}") # Asignacion con resta
print(f"Asignacion con multiplicacion: x *= 2 es {x * 2}") # Asignacion con multiplicacion
print(f"Asignacion con division: x /= 2 es {x / 2}") # Asignacion con division
print(f"Asignacion con division entera: x //= 2 es {x // 2}") # Asignacion con division entera
print(f"Asignacion con modulo: x %= 2 es {x % 2}") # Asignacion con modulo
print(f"Asignacion con exponente: x **= 2 es {x ** 2}") # Asignacion con exponente

# OPERADORES DE IDENTIDAD
# Estos operadores comparan si dos variables apuntan al MISMO objeto en memoria

# Creamos una lista
a = [1, 2, 3]

# Creamos una nueva lista con el mismo contenido
b = [1, 2, 3]

# Asignamos a c la misma referencia que a
c = a

# Comparamos valores (==)
print("a == b:", a == b)  # True, porque el contenido es igual
print("a == c:", a == c)  # True, porque c tiene el mismo contenido que a

# Comparamos identidad (is)
print("a is b:", a is b)  # False, porque son objetos diferentes
print("a is c:", a is c)  # True, porque c y a son el mismo objeto en memoria

# También podemos usar 'is not'
print("a is not b:", a is not b)  # True, porque a y b son diferentes objetos

# Verificamos las direcciones en memoria con id()
print("id(a):", id(a))  # Muestra la dirección en memoria de a
print("id(b):", id(b))  # Será diferente a id(a)
print("id(c):", id(c))  # Igual que id(a), porque c = a

# OPERADORES DE PERTENENCIA
# Estos operadores verifican si un valor está presente en una secuencia (como una lista, tupla o cadena)
print(f"la letra 'a' esta en el nombre 'Karla'? = {'a' in 'Karla'}")  # True, porque 'a' está en 'Karla'
print(f"la letra 'z' no esta en el nombre 'Karla'? = {'z' not in 'Karla'}") # True, porque 'z' no está en 'Karla'

# OPERADORES BIT A BIT
# Estos operadores realizan operaciones a nivel de bits
a= 5 # 0101
b= 3  # 0011

print(f"AND: 5 & 3 = {a & b}") # AND compara bits y retorna 1 si ambos son 1
print(f"OR: 5 | 3 = {a | b}") # OR compara bits y retorna 1 si alguno es 1
print(f"XOR: 5 ^ 3 = {a ^ b}") # XOR compara bits y retorna 1 si son diferentes
print(f"NOT: ~5 = {~a}") # NOT invierte los bits, 0 se convierte en 1 y 1 en 0
print(f"Desplazamiento a la izquierda: 5 << 1 = {a << 1}") # Desplazamiento a la izquierda multiplica por 2
print(f"Desplazamiento a la derecha: 5 >> 1 = {a >> 1}")  # Desplazamiento a la derecha divide por 2

# OPERADORES DE PRIORIDAD
# Estos operadores determinan el orden en que se evalúan las expresiones
# La prioridad de los operadores es la siguiente (de mayor a menor):
# 1. Exponentiation (**)
# 2. Unary plus and minus (+, -)
# 3. Multiplication, division, floor division, and modulo (*, /, //
#    %)
# 4. Addition and subtraction (+, -)
# 5. Bitwise shifts (<<, >>)
# 6. Bitwise AND (&)
# 7. Bitwise XOR (^)
# 8. Bitwise OR (|)
# 9. Comparisons (<, <=, >, >=, ==, !=)
# 10. Identity (is, is not)
# 11. Membership (in, not in)

''' Estructuras de 
control'''

# Estructuras de control son instrucciones que permiten tomar decisiones en el flujo de un programa
# Existen dos tipos de estructuras de control: condicionales y iterativas

# Condicionales: 
# if, elif, else
# if: permite ejecutar un bloque de código si una condición es verdadera
# elif: permite evaluar una segunda condición si la primera es falsa
# else: permite ejecutar un bloque de código si todas las condiciones anteriores son falsas
# Ejemplo de estructura condicional
my_string = "Karla"

if my_string == "Gamboa":
    print("my_string es Gamboa") 
elif my_string == "Karla":
    print("my_string es Karla")
else:
    print("my_string no es Gamboa ni Karla")


# Iterativas: for, while
# Iterar es repetir un bloque de código varias veces

# for: permite iterar sobre una secuencia (lista, tupla, cadena, etc.)
for i in range(11):  # hace un bucle desde 0 hasta 10
    print(f"Iteracion {i}")  # Imprime el numero de iteracion

# while: permite ejecutar un bloque de código mientras una condición sea verdadera
contador = 0
while contador <= 10:  # Mientras contador sea menor o igual que 10
    print(f"Contador: {contador}") # Bucle infinito hasta que contador sea mayor que 10
    contador += 1  # Incrementa contador en 1 en cada iteracion

# Manejo de excepciones
# Las excepciones son errores que ocurren durante la ejecucion del programa
# try: permite ejecutar un bloque de código y capturar excepciones
# except: permite manejar las excepciones que ocurren en el bloque try
try:
    print(10 / 2) 
except:
    print("Error: Division por cero")  # Captura el error y muestra un mensaje 
# finally: permite ejecutar un bloque de código al final, independientemente de si se produjo una excepción o no
finally:
    print("Ha finalizado el manejo de excepciones")  # Este bloque se ejecuta siempre al final

'''Extra'''

'''Crea un programa que imprima por consola todos los números comprendidos
 entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.'''
# Utilizando solamente los operadores vistos en este ejercicio

for i in range(10, 56):  # Itera desde 10 hasta 55
    if i % 2 == 0 and i != 16 and i % 3 != 0:  # i debe ser modulo 2 (par),tiene que ser distinto de 16 y tiene que ser modulo 3 (no múltiplo de 3)
        print(i)  # Imprime el número si cumple las condiciones 



