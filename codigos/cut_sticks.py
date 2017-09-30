'''
 Exemplos de entrada:
 1.
    6
    5 4 4 2 2 8
 2.
    8
    1 2 3 4 3 3 2 1
'''
def recuperar_menor_valor(arr):
    if arr:
        if len(arr) > 0:
            arr = [num for num in sorted(arr) if num != 0]
            if arr:
                return arr[0]
    return 0
    
def subtrair(arr, valor):
    return [(num - valor) for num in arr if (num - valor) > 0]
    
def imprimir(arr):
    if arr:
        if len(arr) > 0:
            print(len(arr))

def cortar(arr):
    imprimir(arr)
    menor_valor = recuperar_menor_valor(arr)
    while (menor_valor > 0):
        arr = subtrair(arr, menor_valor)
        imprimir(arr)
        menor_valor = recuperar_menor_valor(arr)

if __name__ == "__main__":
    n = int(input().strip())
    arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    cortar(arr)