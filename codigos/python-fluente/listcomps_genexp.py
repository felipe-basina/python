def imprimir(colecao, tipo):
    print('Combinacoes por %s. Total %d' % (tipo, len(combinacoes)))
    for item in colecao:
        print(item)

'''
Criacao de listcomprehension
Para criacao de listas
A lista e criada em memoria
Notacao = []
'''
# Criar combinacoes de cores e tamanhos
cores = ['branco', 'preto', 'verde']
tamanhos = ['P', 'M', 'G', 'GG', 'XG', 'U']
combinacoes = [(cor, tamanho) for cor in cores for tamanho in tamanhos]
imprimir(combinacoes, 'listcomprehensions')

'''
Expressoes geradoras ou genexp
Para criacao de colecoes que nao sejam listas
A expressao nao gera uma lista em memoria, por isso e mais otimizada
Ja que, para cada elemento, itera a colecao para recuperar/gerar o proximo valor
Notacao = ()
'''
for cor, tamanho in ((cor, tamanho) for cor in cores for tamanho in tamanhos):
    print(cor, tamanho)