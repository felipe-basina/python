'''
 Exempo de entrada:
 3
 2147483647 
 1
 0
'''
def flipping_bits(arr):
    print("\n")
    for num in arr:
        _bin = '{0:032b}'.format(num)
        temp = ''
        for dig in _bin:
            if dig == '0':
                temp = temp + '1'
            else:
                temp = temp + '0'
        print(num, temp, " : ", int(temp, 2))

if __name__ == '__main__':
    list_size = int(input())
    arr = []
    for v in range(0, list_size):
        arr.append(int(input()))
    flipping_bits(arr)