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

def dup_lista(lista):
    nueva_lista = []
    for i in range(len(lista)):
        nueva_lista.append(lista[i] * 2)

    return nueva_lista

def recorrer_rec(lista):
    if len(lista) > 0:
        print(lista[0])
        recorrer_rec(lista[1:])

def recorrer_iter(lista):
    for i in range(len(lista)):
        print(lista[i])

def sumar_lista_doble(lista):
    suma = 0
    nueva_lista = dup_lista(lista)
    for i in range(len(nueva_lista)):
        suma += nueva_lista[i]

    return suma

def insertion_sort(lista):
    for i in range(1, len(lista)):
        k = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > k:
            lista[j+1] = lista[j]
            j -= 1 
        lista[j+1] = k

    return lista


tiempo = 0
print("Fibonacci recursivo de 40: ", rec_fib(40))
print("Tiempo: ", tiempo)

tiempo = 0
print("Fibonacci iterativo de 40: ", ite_fib(40))
print("Tiempo: ", tiempo)

recorrer_rec([1,2,3,4])
recorrer_iter([1,2,3,4])
