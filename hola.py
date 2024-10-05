# Este es un archivo de prueba

# Fibonnaci recursivo
def rec_fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return rec_fib(n-1) + rec_fib(n-2)

def ite_fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    a = 0
    b = 1
    for i in range(2, n+1):
        c = a + b
        a = b
        b = c
    return b

print(ite_fib(10))