# Este es un archivo de prueba

# Fibonnaci recursivo
def rec_fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return rec_fib(n-1) + rec_fib(n-2)

print(rec_fib(40))