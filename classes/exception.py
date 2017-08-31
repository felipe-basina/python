class B(Exception):    
    pass
    
class C(B): # Heranca = herda classe B
    pass
    
class D(C): # Heranca = herda classe C
    pass
    
def executa_sequencia(sequencia):
    for cls in sequencia:
            try:
                raise cls() # Cria a instancia de uma classe
            except D:
                print("D")
            except C:
                print("C")
            except B:
                print("B")

def executa_sequencia_inverso(sequencia):
    for cls in sequencia:
            try:
                # raise = forca o lancamento de uma excecao
                raise cls() # Cria a instancia de uma classe
            except B as b:
                print("B")
            except C as c:
                print("C")
            except D:
                print("D")
                
if __name__ == '__main__':
    # Invoca o metodo passando como parametro uma lista de classes
    executa_sequencia([B, C, D])
    print('\n')
    executa_sequencia_inverso([B, C, D])