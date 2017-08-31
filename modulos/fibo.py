'''
 1. Via terminal acessar o diretorio onde se encontra esse arquivo
 2. Realizar o import desse arquivo. Ex: import fibo
 3. Invocar os metodos da seguinte forma: fibo.fib(10) ou fibo.fib2(10)
'''
# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

'''
 Para executar o script a partir da linha de comando deve-se:
 1. Adicionar a linha abaixo (if __name__ ....) no script
 2. Executar o seguinte comando: python e:\instalados\python\dev\exercicios\modulos\fibo.py 50
'''    
if __name__ == '__main__':
    import sys
    fib(int(sys.argv[1]))