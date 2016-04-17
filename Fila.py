class Fila:


	def __init__(self, tamanho):

		self.filaInterna = []
		self.tamanho = tamanho
		self.posicaoPrimeiroElemento = 0
		self.proximaPosicaoVaga = 0
		self.numeroElementos = 0

		for i in range(tamanho):

			self.filaInterna.append(None)


	def entrarNaFila(self, elemento):

		if(not self.filaInterna):

			for i in range(self.tamanho):

				self.filaInterna.append(None)

			self.proximaPosicaoVaga = 0


		if(self._estahVazia()):

			self.filaInterna[self.posicaoPrimeiroElemento] = elemento
			self.proximaPosicaoVaga += 1
			self.numeroElementos += 1

		else:

			self.filaInterna[self.proximaPosicaoVaga] = elemento
			self.proximaPosicaoVaga += 1
			self.numeroElementos += 1

	def atenderFila(self):

		primeiroElemento = self.filaInterna[self.posicaoPrimeiroElemento]
		del self.filaInterna[self.posicaoPrimeiroElemento]
		self.proximaPosicaoVaga -= 1
		self.numeroElementos -= 1
		return primeiroElemento
	
	def _estahVazia(self):

		estahVazia = True

		for i in self.filaInterna:

			if(i):
				estahVazia = False

		return estahVazia


fila = Fila(6)
fila.entrarNaFila('Neal')
fila.entrarNaFila('Jack')
fila.entrarNaFila('Me')
fila.entrarNaFila('Absent')
fila.entrarNaFila('Lovers')

print(fila.filaInterna)

listaRetorno = []

for i in range(6):

	listaRetorno.append(fila.atenderFila())

print(listaRetorno)
print(fila.filaInterna)

print(fila.posicaoPrimeiroElemento)
print(fila.proximaPosicaoVaga)

fila.entrarNaFila('King')

print(fila.filaInterna)

fila.entrarNaFila('Crimson')

print(fila.filaInterna)

king = fila.atenderFila()
crimson = fila.atenderFila()

print(king)
print(crimson)
