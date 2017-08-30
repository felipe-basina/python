import functools

# Realiza a soma dos n primeiros numeros naturais
def soma_n_numeros_naturais(numero):
    return functools.reduce(lambda x, y: x + y, 
        range(1, numero + 1))

# Realiza a leitura de um arquivo        
def ler_arquivo(arquivo):
    try:
        with open(arquivo, 'r') as file:
            for line in file:
                print(line)
    except FileNotFoundError:
        print('Nao foi possivel realizar a leitura do arquivo %s! Verifique se o mesmo existe no diretorio indicado' % arquivo)
        #raise Exception(e)