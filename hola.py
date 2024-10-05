# Este es un archivo de prueba

tiempo = 0

# Fibonnaci recursivo
def rec_fib(n):
    global tiempo
    tiempo += 1
    if n == 0:
        return 0
    if n == 1:
        return 1
    return rec_fib(n-1) + rec_fib(n-2)

def ite_fib(n):
    global tiempo
    if n == 0:
        return 0
    if n == 1:
        return 1
    a = 0
    b = 1
    for _ in range(2, n+1):
        tiempo += 1
        c = a + b
        a = b
        b = c
    return b

def recorrer_rec(lista):
    if len(lista) > 0:
        print(lista[0])
        recorrer_rec(lista[1:])

tiempo = 0
print("Fibonacci recursivo de 40: ", rec_fib(40))
print("Tiempo: ", tiempo)

tiempo = 0
print("Fibonacci iterativo de 40: ", ite_fib(40))
print("Tiempo: ", tiempo)

recorrer_rec([1,2,3,4])
