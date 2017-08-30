def desenhar_retangulo(linhas, colunas):
    if linhas < 1 or linhas > 20:
        linhas = 1
        
    if colunas < 1 or colunas > 20:
        colunas = 20

    print('+' + ('-' * colunas) + '+')

    for n in range(1, linhas + 1):
        print('|' + (' ' * (colunas)) + '|')

    print('+' + ('-' * colunas) + '+')
        
if __name__ == '__main__':
    linhas = int(input('Entre com o total de linhas: '))
    colunas = int(input('Entre com o total de colunas: '))
    
    desenhar_retangulo(linhas, colunas)