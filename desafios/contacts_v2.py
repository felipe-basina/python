from functools import reduce

def count_terms(names, term):
    value = reduce(lambda x, y: x + y, 
            map(lambda contact: 1 if contact != None and term in contact else 0, names), 0)
    print(value)
    return value

def contacts(queries):
    names = [name for name in list(map(lambda el: el[1] if 'add' == el[0] else None, queries)) if name != None]
    terms = [term for term in list(map(lambda el: el[1] if 'find' == el[0] else None, queries)) if term != None]

    count_arr = []
    for term in terms:
        if term != None:
            count = reduce(lambda x, y: x + y, 
                            map(lambda contact: 1 if contact != None and term in contact else 0, names), 0)
            count_arr.append(count)

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