from functools import reduce
import time

def contacts(queries):
    contact_dict = {}
    count_arr = []
    count_arr_append = count_arr.append

    for el in queries:
        command, value = el
        print('command', command, 'value', value)
        if command == 'add':
            for index in range(1, len(value) + 1):
                partial = value[0:index]
                print('partial', partial)
                if contact_dict.get(partial) == None:
                    contact_dict[partial] = 1
                else:
                    contact_dict[partial] = contact_dict.get(partial) + 1
        else:
            if not contact_dict.get(value):
                count_arr_append(0)
            else:
                count_arr_append(contact_dict.get(value))
        
    return count_arr

queries = [['add', 's'],
            ['add', 'ss'],
            ['add', 'sss'],
            ['add', 'ssss'],
            ['add', 'sssss'],
            ['find', 's'],
            ['find', 'ss'],
            ['find', 'sss'],
            ['find', 'ssss'],
            ['find', 'sssss'],
            ['find', 'ssssss']]

for total in contacts(queries):
    print(total)
   