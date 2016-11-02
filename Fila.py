# -*- coding: utf-8 -*-

class Fila:

	def __init__(self, tamanho):

		self.filaInterna = [None] * tamanho
		self.tamanho = tamanho
		self.posicaoPrimeiroElemento = 0
		self.proximaPosicaoVaga = 0
		self.numeroElementos = 0


	def entrarNaFila(self, elemento):

		if(self._estahVazia()):
			self.posicaoPrimeiroElemento = 0
			self.filaInterna[self.posicaoPrimeiroElemento] = elemento  #primeiro elemento a ser adicionado na vida da fila, entra na primeira posicao do array
			self.proximaPosicaoVaga += 1
			self.numeroElementos += 1

		else:

			if(self._estahCheia()):
				raise Exception('Fila cheia, sem espaço para novas adições')

			self.filaInterna[self.proximaPosicaoVaga] = elemento
			self.proximaPosicaoVaga += 1
			self.numeroElementos += 1

	def atenderFila(self):

		if(self._estahVazia()):
			raise Exception('Fila vazia, nada a retornar')

		primeiroElemento = self.filaInterna[self.posicaoPrimeiroElemento]
		self.filaInterna[self.posicaoPrimeiroElemento] = None
		self.posicaoPrimeiroElemento += 1
		self.proximaPosicaoVaga -= 1
		self.numeroElementos -= 1
		return primeiroElemento
	
	def _estahCheia(self):
		return self.numeroElementos == self.tamanho

	def _estahVazia(self):

		estahVazia = True

		for i in self.filaInterna:
		#fila interna inicializada com placeholder None; testa se algum valor ja foi adicionado	
			if(i):				
				estahVazia = False

		return estahVazia

	def imprimirFila(self):

		rep = []
		for i in self.filaInterna:
			if(not i):
				rep.append('lugar vazio')
			else:				
				rep.append(i)

		print(rep)

#fim da classe

def pegarInputEntrarFila(fila):

	print('Forneça a entrada a ser adicionada na fila')
	elemento = raw_input()
	try:
		fila.entrarNaFila(elemento)

	except Exception as e:
		print(e)	

passou = False
tamanho = 0
while(not passou):

	print('Forneça o tamanho da fila:\n')
	tamanho = raw_input()

	try:
		tamanho = int(tamanho)
		passou = True
	except ValueError:
		print('Forneça uma entrada válida\n')

fila = Fila(tamanho)

while(True):
	print('---------')
	print('1: Adicionar item na fila')
	print('2: Atender fila')
	print('3: Imprimir fila')
	print('4: Sair')
	opcao = raw_input()
	
	if(opcao == '1'):

		pegarInputEntrarFila(fila)

	elif(opcao == '2'):

		try:
			print(fila.atenderFila())
		except Exception as e:
			print(e)

	elif(opcao == '3'):
		fila.imprimirFila()

	elif(opcao == '4'):
		break

	else:
		print('Opção desconhecida\n')