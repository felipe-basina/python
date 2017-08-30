import sys

def imprimir_valores(numero):
    token = ''

    for n in range(1, numero + 1):
        for inner in range(1, n + 1):
            token = token + '{0:2} '

        print(token.format(n))
        token = ''
        
if __name__ == '__main__':
    if len(sys.argv) == 1:
        numero = int(input('Entre com um valor numerico: '))
    else:
        numero = int(sys.argv[1])
        
    imprimir_valores(numero)