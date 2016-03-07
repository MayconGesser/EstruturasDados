class Pilha:
	
	def __init__(self, tamanho):
		
		self._pilhaInterna = []	
		self._tamanho = tamanho
		self._indicePilhaInterna = -1			#variavel para referencia da ultima posicao inserida
		
	#push
	def inserir(self, objeto):
		
		if(len(self._pilhaInterna) >= 10):
			print('Impossivel inserir: pilha esta cheia')
			return
			
		self._pilhaInterna.append(objeto)
		self._indicePilhaInterna += 1
		return
		
	#pop
	def pegarValor(self):
	
		valor = self._pilhaInterna[self._indicePilhaInterna]
		del self._pilhaInterna[self._indicePilhaInterna]
		self._indicePilhaInterna -= 1
		return valor
	
	def imprimirPilha(self):
	
		for objeto in self._pilhaInterna:
			print(objeto)
			
		return
	
	
pilha = Pilha(10)
pilha.inserir(20)
pilha.inserir('String')
pilha.inserir('Mierdas')
pilha.inserir(['Neil', 'Jack', 'Me'])
pilha.inserir(object())
pilha.imprimirPilha()
pop1 = pilha.pegarValor()
pop2 = pilha.pegarValor()
print('primeiro pop:' + str(pop1) + '\n')
print('segundo pop: ' + str(pop2) + '\n')