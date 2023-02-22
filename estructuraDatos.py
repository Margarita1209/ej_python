# ver si el numero es primo

def es_numero_primo(numero):

    if numero <= 1:
        return False

    for i in range(2, numero):
        if numero % i == 0:
            return False

    return True


numero=input("ingrese un numero para ver si es primo")

print(es_numero_primo(12)) # False
print(es_numero_primo(43)) # True
print(es_numero_primo(int(numero)))

# clcular el factorial de un numero

def calcular_factorial(numero):

    factorial = 1
    for i in range(1, numero+1):
        factorial = factorial * i

    return factorial

numero=input("ingrese un numero para calcular factorial")
print(calcular_factorial(int(numero)))
print(calcular_factorial(0)) # 1
print(calcular_factorial(3)) # 6
print(calcular_factorial(4)) # 24
print(calcular_factorial(5)) # 120


def calcular_factorial_recursivo(numero):

    if numero == 0 or numero == 1:
        return 1

    return numero * calcular_factorial_recursivo(numero-1)


print(calcular_factorial_recursivo(0)) # 1
print(calcular_factorial_recursivo(3)) # 6
print(calcular_factorial_recursivo(4)) # 24
print(calcular_factorial_recursivo(5)) # 120
