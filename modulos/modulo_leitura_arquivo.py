'''
 Script utilizado para leitura de arquivo
 from modulo_leitura_arquivo import ler_arquivo
 arquivo = 'e:/instalados/python/dev/exercicios/modulos/arquivo_leitura.txt'
 ler_arquivo(arquivo)
'''
def ler_arquivo(nome_arquivo):
    if not nome_arquivo:
        print('Um nome de arquivo deve ser definido!')
    else:
        # Utilizar 'with' para nao precisar utilizar bloco try-finally
        conteudo = ''
        with open(nome_arquivo, encoding='utf-8') as f:
            conteudo = f.read()
        f.closed
        
        print('\nConteudo do arquivo\n')
        print(conteudo)
        print('\n')

# Realizando leitura linha por linha = mais eficiente!
def ler_arquivo_por_linha(nome_arquivo):
    if not nome_arquivo:
        print('Um nome de arquivo deve ser definido!')
    else:
        with open(nome_arquivo, encoding='utf-8') as f:
            print('\n')
            for line in f:
                print(line, end='')