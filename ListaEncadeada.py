#essa classe foi implementada seguindo a logica do seguinte video: https://www.youtube.com/watch?v=OS5XLTVgMQk
class ListaEncadeada:
	
	def __init__(self):
		
		self.comeco = None
		self.tamanho = 0
		self.tamanhoMaximo = 100
		
	def getTamanho(self):
		return self.tamanho
	
	def estahCheia(self):
		return self.tamanhoMaximo < 100
		
	def estahVazia(self):
		return self.tamanho == 0
	
	#logica desse metodo: a variavel comeco comeca com valor nulo, qdo algum no eh inserido o atributo proximo desse no recebe
	#a variavel comeco como seu valor(q em primeiro momento eh nulo), e o valor da variavel comeco eh mudado para apontar para o objeto No 
	#q acabou de ser inserido, isso insere o novo objeto No na primeira posicao da lista. 
	def inserirNo(self, valor):
	
		if(self.estahCheia()):
			print('Impossivel inserir um novo No; a lista esta cheia')
			return
			
		noASerInserido = ListaEncadeada.No(valor)
		noASerInserido.setProximo(self.comeco)
		self.comeco = noASerInserido
		self.tamanho += 1
		
	#deleta o No que possui o valor passado como argumento
	def deletarNo(self, valor):
		
		#checa se a lista nao esta vazia
		if(self.estahVazia()):
			print('Nada a deletar; lista esta vazia')
			return
			
		noReferencia = self.comeco
		
		if(noReferencia.valor == valor):
		
			self.comeco = noReferencia.proximo			
			noReferencia = None
			self.tamanho -= 1
			return
		
		
		while(noReferencia.proximo.valor != valor):
		
			noReferencia = noReferencia.proximo
			
		noAlvo = noReferencia.proximo
		noReferencia.proximo = noAlvo.proximo
		del noAlvo
		self.tamanho -= 1
	
	
	def imprimirLista(self):
	
		if(not self.tamanho):
			print('A lista esta vazia')
			return
				
		noDeReferencia = self.comeco
		
		#verifica uma posicao a frente
		while(noDeReferencia.proximo):
		
			print(noDeReferencia.valor)
			noDeReferencia = noDeReferencia.proximo
		
		#qdo a condicao do while nao for mais valida, para imprimir o valor da ultima posicao
		print(noDeReferencia.valor)
		print('Tamanho da lista: ' + str(self.getTamanho()))
	
	def esvaziarLista(self):				
		
		while(self.comeco):
			
			noASerDeletado = self.comeco
			self.comeco = self.comeco.proximo
			del noASerDeletado
			
		self.tamanho = 0
		print('Lista esvaziada')
		
	
	class No:
		
		def __init__(self, valor):
			
			self.valor = valor
		
		
		def setProximo(self, proximo):
			
			self.proximo = proximo
			
			
lista = ListaEncadeada()
lista.inserirNo(111)
lista.inserirNo(222)
lista.inserirNo(333)
print('primeira impressao \n')
lista.imprimirLista()
print('\n')
lista.deletarNo(111)
print('segunda impressao \n')
lista.imprimirLista()
print('\n')
lista.deletarNo(222)
print('terceira impressao \n')
lista.imprimirLista()
print('\n')
lista.deletarNo(333)
print('quarta impressao \n')
lista.imprimirLista()
print('\n')
lista.inserirNo('Absent Lovers:')
lista.inserirNo('Neil')
lista.inserirNo('Jack')
lista.inserirNo('Me')
print('quinta impressao \n')
lista.imprimirLista()
print('\n')
print('\nEsvaziando lista')
lista.esvaziarLista()
print('\n')
lista.imprimirLista()