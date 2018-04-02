class Despesa():

	def __init__(self, tipo, id, descricao):
		self.tipo = tipo
		self.id = id
		self.descricao = descricao

	def __str__(self):
		return str(self.id) + ' >> ' + self.descricao + ' ( ' + self.tipo + ' )'

despesas = []

def criar_despesa():
	despesas.append(Despesa('posto de gasolina', 1, 'uma despesa'))
	despesas.append(Despesa('compras do mes', 2, 'supermercado'))
	despesas.append(Despesa('viagem', 3, 'almocos na viagem'))

def despesa_existente(id_despesa):
	return any(despesa.id == id_despesa for despesa in despesas)

def recuperar_despesa_por_id(id_despesa):
    despesa = [despesa for despesa in despesas if despesa.id == id_despesa]
    return despesa[0]

if __name__ == '__main__':
	criar_despesa()

	for index in range(1, 5):
		if despesa_existente(index):
			print('ID {0} ENCONTRADO'.format(index))
			print('DESPESA:', recuperar_despesa_por_id(index))
		else:
			print('ID {0} NAO ENCONTRADO'.format(index))
		