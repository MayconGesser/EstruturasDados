class ListaCheiaException(Exception):
	pass

class ListaEncadeadaINE5609:


	def __init__(self, tamanho):

		self.tamanho = tamanho
		self.listaElementos = []
		self.listaPosicoes = []
		self.posicaoPrimeiro = 0
		self.proximaPosicaoVaga = 0
		self.numeroElementos = 0

		#inicializa listas com valores placeholder
		for i in range(tamanho):

			self.listaElementos.append(None)
			self.listaPosicoes.append(-2)

	def inserirNoFim(self, elemento):

		#verifica antecipadamente se a lista estah cheia
		if(self.numeroElementos == self.tamanho):

			raise ListaCheiaException('A lista esta cheia')

		if(not self.listaElementos[self.posicaoPrimeiro]):

			self.listaElementos[self.posicaoPrimeiro] = elemento
			self.proximaPosicaoVaga += 1
			self.listaPosicoes[self.posicaoPrimeiro] = -1
			self.numeroElementos += 1

		else:

			self.listaElementos[self.proximaPosicaoVaga] = elemento
			self.proximaPosicaoVaga += 1
			ultimaPosicao = self.listaElementos.index(elemento)-1
			self.listaPosicoes[ultimaPosicao] = self.listaElementos.index(elemento)
			self.listaPosicoes[self.listaElementos.index(elemento)] = -1
			self.numeroElementos += 1

	#fim da funcao

	def inserirNoComeco(self, elemento):

		if(self.numeroElementos == self.tamanho):

			raise ListaCheiaException('A lista esta cheia')

		# a variavel posicaoDoElementoQEraPrimeiro pega a posicao do elemento q era o primeiro da lista antes desse metodo ser chamado
		# e vai ateh essa posicao para comecar a refatorar a lista de posicoes
		# dentro do for reutilizei essa mesma variavel para nao ter q criar outra, visto q a semantica dela jah tinha cumprido 
		# seu objetivo
		posicaoDoElementoQEraPrimeiro = self.posicaoPrimeiro
		self.posicaoPrimeiro = self.proximaPosicaoVaga
		self.listaElementos[self.posicaoPrimeiro] = elemento

		# refatora a lista de posicoes 
		# esse for pega o indice do elemento q essa funcao adicionou a lista de elementos como primeiro como indice para suas iteracoes
		# a logica q eu segui foi q a posicao em q o elemento estah eh o mesmo numero de vezes em q a lista tera q ser percorrida para
		# alcanca-lo, ou seja, esse for refatora apenas os elementos q ha "atras" do elemento inserido
		for i in range(self.listaElementos.index(elemento)):

			self.listaPosicoes[posicaoDoElementoQEraPrimeiro] = posicaoDoElementoQEraPrimeiro
			posicaoDoElementoQEraPrimeiro += 1
			

		self.listaPosicoes[self.posicaoPrimeiro] = -1
		self.proximaPosicaoVaga += 1
		self.numeroElementos += 1		

	# fim da funcao

	def inserirAntesDe(self, elementoASerInserido, elementoDeReferencia):

		posicaoDeInsercao = self.listaElementos.index(elementoDeReferencia)-1
		self.listaElementos[self.proximaPosicaoVaga] = elementoASerInserido
		self.listaPosicoes[posicaoDeInsercao] = self.proximaPosicaoVaga
		#self.listaPosicoes[posicaoDeInsercao+1] = self.listaElementos.index(elementoDeReferencia)

	#fim da funcao

	def inserirDepoisDe(self, elementoASerInserido, elementoDeReferencia):

		posicaoDeInsercao = self.listaElementos.index(elementoDeReferencia)+1
		self.listaPosicoes[self.proximaPosicaoVaga] = posicaoDeInsercao



le = ListaEncadeadaINE5609(5)

try:
	le.inserirNoFim('Neal')
	le.inserirNoFim('Jack')	
	le.inserirNoFim('Absent')
	le.inserirNoFim('Lovers')
	

except ListaCheiaException as e:

	print(e.message)


print(le.listaElementos)
print(le.listaPosicoes)

le.inserirAntesDe('Me', 'Absent')

print(le.listaElementos)
print(le.listaPosicoes)
