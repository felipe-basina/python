def ordenar():
    total = 5
    print('Entre com %d nros. inteiros' % total)

    list_int = []
    for i in range(total):
        nro = int(input("%d: " % (i + 1)))
        list_int.append(nro)

    print('Nros digitados\nOriginal: {}\nOrdenado: {}'.format(
        list_int, sorted(list_int)))

if __name__ == '__main__':
    ordenar()