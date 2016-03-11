#Tabela Hash implementando encadeamento direto (cria uma lista encadeada no evento de uma colisao)
from ListaEncadeada import ListaEncadeada

class Produto(object):
	
	def __init__(self, nome=None, preco=None):
		
		self._nome = nome
		self._preco = preco		
		
	def getNome(self):
		return self._nome

class TabelaHash:
	
	def __init__(self, tamanho, objetos=None):	
		
		#tratamento do argumento tamanho
		if(not(isinstance(tamanho, int)) or tamanho <= 0):
			raise ValueError('Forneca um argumento valido para o construtor no formato de um numero inteiro > 0')
		
		#atributos
		self._tabelaInterna = []		
		
		#inicializa tabelaInterna
		for i in range(tamanho):
				self._tabelaInterna.append('...')		#valor dummy para inicializar posicoes da lista
				
		
		#se uma lista de objetos foi passada no construtor 
		if(objetos and isinstance(objetos, list)):
			pass
			
	
	#funcao hash simples de mapeamento direto; hash gerado combina o valor numerico ASCII da primeira letra do argumento 
	#somado com o modulo do comprimento do argumento pelo comprimento da tabela(lista) interna
	def __funcaoHash__(self, argumento):
		
		valorHash = len(argumento) % len(self._tabelaInterna)
		
		#se o valorHash obtido da expressao acabar sendo maior q um indice valido, esse while diminui a um valor aceitavel
		while(valorHash > len(self._tabelaInterna)):
			valorHash -= 1
		
		return valorHash
		
		
	def __rotinaDeColisao__(self, posicaoDaColisao, item):	
	
		print('Houve uma colisao na posicao ' + str(posicaoDaColisao))
	
		#se na posicao de colisao houver um objeto No quer dizer q jah houve uma colisao anterior
		#e o algoritmo criou a lista encadeada naquela posicao 
		if(isinstance(posicaoDaColisao, ListaEncadeada)):
		
			self._tabelaInterna[posicaoDaColisao].inserirNo(item)
			return
		
		#houve colisao mas a lista ainda nao foi criada; cria uma lista encadeada na posicao
		#da colisao, adiciona o valor q jah havia na tabela interna e adiciona o valor 
		#que se foi tentar inserir
		else:
		
			valorDaPosicao = self._tabelaInterna[posicaoDaColisao]			#cria uma referencia ao valor da posicao (um objeto Produto) antes de sobrescrever
			self._tabelaInterna[posicaoDaColisao] = ListaEncadeada()
			self._tabelaInterna[posicaoDaColisao].inserirNo(valorDaPosicao)
			self._tabelaInterna[posicaoDaColisao].inserirNo(item)
			return
	
	
	def processarEntrada(self, entrada):
		
		valorHash = self.__funcaoHash__(entrada)		
		
		#esse if trata o caso de uma colisao(jah ha um item presente na posicao)
		if(self._tabelaInterna[valorHash] != '...'):				#se o valor da posicao for diferente do valor dummy do construtor da classe
			self.__rotinaDeColisao__(valorHash, entrada)
			return
			
		else:
			self._tabelaInterna[valorHash] = entrada
			return
			
	def procurarEntrada(self, entrada):
		
		valorHash = self.__funcaoHash__(entrada)
		
		#se achou o valor em primeiro momento ao acessar o indice 
		if(self._tabelaInterna[valorHash] == entrada):
			return entrada
		
		#se houve uma colisao no indice e uma lista foi criada, percorre a lista ateh encontrar a entrada
		elif(isinstance(self._tabelaInterna[valorHash], ListaEncadeada)):
		
			noInspecionado = self._tabelaInterna[valorHash].primeiroNo
			
			while(noInspecionado.valor != entrada):
				noInspecionado = noInspecionado.proximo
				
			return noInspecionado.valor
		
		#tratamento de excecao
		else:
			raise ValueError('A entrada fornecida nao consta na tabela')
			
		
	def imprimirTabela(self):
		
		for i in self._tabelaInterna:					
				
				if(isinstance(i, str)):
				
					print(i)
				
				elif(isinstance(i, Produto)):
					print(i._nome)
				
				elif(isinstance(i, ListaEncadeada)):
					i.imprimirLista()
					
		return


#Rotinas de teste		
tabela = TabelaHash(10)
produtoInserido = Produto('Console', 666)
produtoInserido2 = Produto('PC', 1488)
tabela.processarEntrada(produtoInserido.getNome())
tabela.processarEntrada(produtoInserido2.getNome())
print('Primeira impressao\n')
tabela.imprimirTabela()
print('\n')
produtoInserido3 = Produto('Ventilador', 544)
tabela.processarEntrada(produtoInserido3.getNome())
print('Segunda Impressao\n')
tabela.imprimirTabela()
print('\n')
produtoInserido4 = Produto('Monitor', 22)
tabela.processarEntrada(produtoInserido4.getNome())
print('Quarta impressao\n')
tabela.imprimirTabela()
print('\n')
produto5 = Produto('Impressora', 5555)
tabela.processarEntrada(produto5.getNome())
print('Quinta impressao\n')
tabela.imprimirTabela()
print('\n')
print('Imprimindo resultados de busca\n')					#chamadas de funcao sem try/except
print('Resultado 1')
print(tabela.procurarEntrada('PC'))
print('\n')
print('Resultado 2')
print(tabela.procurarEntrada('Console'))
print('\n')
print('Resultado 3')
print(tabela.procurarEntrada('Monitor'))
print('\n')
