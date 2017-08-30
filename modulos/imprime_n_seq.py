import sys

def imprimir_valores_sequencial(numero):
    token = ''
    lista = []
    indice = 0
    
    for n in range(1, numero + 1):
        for inner in range(1, n + 1):
            token = token + '{' + str(indice) + ':2} '
            indice = indice + 1
            lista.append(inner)

        print(token.format(*lista))
        token = ''
        lista = []
        indice = 0

if __name__ == '__main__':
    if len(sys.argv) == 1:
        numero = int(input('Entre com um numero: '))
    else:
        numero = int(sys.argv[1])
        
    imprimir_valores_sequencial(numero)



