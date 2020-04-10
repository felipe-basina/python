from functools import reduce

def contacts(queries):
    contacts_arr = []
    count_arr = []

    for el in queries:
        if 'add' == el[0]:
            contacts_arr.append(el[1])
        else:
            term_to_find = el[1]
            count = reduce(lambda x, y: x + y, 
                            map(lambda contact: 1 if term_to_find in contact else 0, contacts_arr))
            count_arr.append(count)

    return count_arr

queries = [['add', 'hack'], ['add', 'hackerrank'], ['find', 'hac'], ['find', 'hak']]
for total in contacts(queries):
    print(total)