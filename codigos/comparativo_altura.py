lista_aluno = []
lista_tamanho =[]


def nome_altura():      
    for i in range(0,3):
        aluno = str(input('Digite o nome do aluno:\n'))
        lista_aluno.append(aluno)

        tamanho = int(input('Digite a altura:\n')) 
        lista_tamanho.append(tamanho)

    return lista_aluno, lista_tamanho

def mais_alto():  
    index = 0 # Identifica a posicao do registro no array
    
    nome_maior_aluno = lista_aluno[index]   
    maior_aluno = lista_tamanho[index] 
    
    for i in lista_tamanho: # i Possui o tamanho do aluno e nao a posicao do registro no array
        if i > maior_aluno: # Identificar a maior altura
            maior_aluno = lista_tamanho[index]
            nome_maior_aluno = lista_aluno[index]
        index += 1
    
    return nome_maior_aluno,maior_aluno

def mais_baixo(): 
    index = 0 # Identifica a posicao do registro no array
    
    nome_menor_aluno = lista_aluno[index]  
    menor_aluno = lista_tamanho[index]  
    
    for c in lista_tamanho: # i Possui o tamanho do aluno e nao a posicao do registro no array
        if c < menor_aluno: # Identificar a menor altura
            menor_aluno = lista_tamanho[index]
            nome_menor_aluno = lista_aluno[index]
        index += 1
    
    return nome_menor_aluno,menor_aluno

def imprimir():
    print('Valor mais alto = {0} :: valor mais baixo = {1}'.format(mais_alto(), mais_baixo()))
		
if __name__ == '__main__':
    nome_altura()
    imprimir()