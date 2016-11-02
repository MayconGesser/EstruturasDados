class No:
	def __init__(self,valor,proximo=None):
		self.valor = valor
		self.proximo = proximo
		self.topo = None

class Pilha:
	
	def __init__(self):
		self.topo = None
	
	def push(self,elemento):
		inserido = No(elemento)
		if(not self.topo):
			self.topo = inserido
		else:
			topo_antigo = self.topo
			inserido.proximo = topo_antigo
			self.topo = inserido

	def pop(self):
		novo_topo = self.topo.proximo
		retorno = self.topo.valor
		self.topo = novo_topo
		return retorno

	def imprimir(self):
		cursor = self.topo
		rep = 'topo :'
		while(cursor.proximo):
			rep += str(cursor.valor) + '\n'
			cursor = cursor.proximo
		
		rep += str(cursor.valor)
		print(rep)


pilha = Pilha()
pilha.push('Neal')
pilha.push('Jack')
pilha.push('Me')
pilha.push('Absent')
pilha.push('Lovers')
pilha.imprimir()
pilha.pop()
pilha.pop()
pilha.imprimir()
