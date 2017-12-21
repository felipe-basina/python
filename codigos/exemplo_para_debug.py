'''
 - Executar o script com o seguinte comando:
    python -m pdb <nome_script.py>

 - Tambem sera possivel importando a funcao .set_trace(),
 onde o script sera executado em um prompt ja iniciado com o pdb
 Comando:
    import pdb
    pdb.set_trace()
'''
class NumberList(object):
    def __init__(self):
        self.numbers = list()

    def add(self, number):
        if not isinstance(number, (int, float)):
            raise TypeError
        self.numbers.append(number)

    def sum(self):
        result = 0
        for i in self.numbers:
            result += i
        return result


if "__main__" == __name__:
    numbers = NumberList()

    numbers.add(5)
    assert numbers.sum() == 5

    numbers.add(10)
    assert numbers.sum() == 15

    print("The End")