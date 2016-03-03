class ListaEncadeada:
	
	def __init__(self, tamanho, valoresDos_Nos=None):
	
		#tratamento do argumento valoresDos_Nos
		if(not(isinstance(valoresDos_Nos, list))):
			raise ValueError('Erro _No argumento: certifique-se que os valores dos _Nos estao sendo passados numa lista')
	
		self._listaInterna = []
		
		#popula a lista interna com objetos _No de acordo com o tamanho especificado
		for i in range(tamanho):
			self._listaInterna.append(ListaEncadeada._No())
		
		#percorre a lista ajeitando os ponteiros de proximo de cada objeto _No
		for j in range(len(self._listaInterna)):
		
			if j == len(self._listaInterna) - 1:
				break
				
			self._listaInterna[j].setProximo(self._listaInterna[j+1]) 
		
		#passa os valores da lista passada como argumento _No construtor para os objetos _No da lista interna
		for h in range(len(valoresDos_Nos)):
			self._listaInterna[h].setValor(valoresDos_Nos[h])
			
	
	def setarValor_No(self, posicaoDo_No, valor): 
	
		#tratamento do argumento posicaoDo_No 
		if(not (isinstance(posicaoDo_No, int)) or posicaoDo_No > len(self._listaInterna) or posicaoDo_No < 0):
			raise ValueError('Forneca um valor valido para a posicao do _No')
			
		self._listaInterna[posicaoDo_No].setValor(valor)

	#esse metodo executa a seguinte logica: desmembra a lista interna em duas, sendo a cisao na posicao onde se deseja inserir um _No,
	#e as junta depois das modificacoes. A primeira parte desmembrada vai do primeiro indice da lista ateh a posicao do argumento;
	#a segunda parte eh da posicao proxima a do argumento ateh o final da lista. Faz-se a alteracao na posicao (argumento) da primeira parte
	#e depois junta as duas para formar a lista desejada
	
	# a = [1,2,3,4], posicao = 1, valor = 10
	# pedaco1 = [1,2**], pedaco2 = [2**,3,4], pedaco1[posicao] = valor (pedaco1[1] = 10), listajunta = pedaco1(1,10) + pedaco2(2,3,4)
	
	#**: copiam o mesmo valor porque eh esse valor que vai ser sobrescrito em pedaco1: 
	#[1,2=>esse valor eh sobrescrito] / [2=>esse valor eh guardado,3,4]
	
	def inserir_No(self, posicao, valor):
	
		#tratamento do argumento posicao
		if(not (isinstance(posicao, int)) or posicao > len(self._listaInterna) or posicao < 0):
			raise ValueError('Forneca um valor valido para a posicao do _No')
	
		_NoASerInserido = ListaEncadeada._No(valor)		
		pedaco1 = self._listaInterna[0:posicao+1] 		#posicao+1 para poder pegar ATEH a posicao indicada, jah q lista[comeco:fim] exclui o argumento fim
		pedaco2 = self._listaInterna[posicao:len(self._listaInterna)]
		pedaco1[posicao] = _NoASerInserido
		pedaco1[posicao-1].setProximo(_NoASerInserido)		#essas duas linhas reorganizam os ponteiros de proximo _Nos objetos _No da lista
		_NoASerInserido.setProximo(pedaco2[0])
		listaJunta = pedaco1 + pedaco2
		self._listaInterna = listaJunta
		return
		
	
	#esse metodo simplifica um pouco o processo do metodo de insercao: simplesmente cria uma lista _Nova sem o objeto _No q deve ser deletado e 
	#reajusta os ponteiros de proximo dentro da lista _Nova gerada
	def deletar_No(self, posicaoDo_No):
		
		#tratamento do argumento posicaoDo_No 
		if(not (isinstance(posicaoDo_No, int)) or posicaoDo_No > len(self._listaInterna) or posicaoDo_No < 0):
			raise ValueError('Forneca um valor valido para a posicao do _No')
			
		_NoASerDeletado = self._listaInterna[posicaoDo_No]
		
		#compreensao de lista com a condicao de exclusao do objeto _No a ser excluido
		#is not = nao eh (exatamente) o mesmo objeto 
		listaAtualizada = [no for no in self._listaInterna if no is not _NoASerDeletado]
		
		#arruma os ponteiros de proximo _Nos objetos _No
		for j in range(len(listaAtualizada)):
		
			if j == len(listaAtualizada) - 1:
				break
				
			listaAtualizada[j].setProximo(listaAtualizada[j+1])
		
		self._listaInterna = listaAtualizada
		return
	
	#metodo simples para pegar o valor do no em determinada posicao
	def getValorNo(self, posicaoDoNo):
		return self._listaInterna[posicaoDoNo].getValor()
	
	#metodo simples para pegar o valor do proximo objeto No a partir de uma posicao
	def getValorProximoNo(self, posicaoDoNo):
		return self._listaInterna[posicaoDoNo].getValorProximo()
		
	#metodo simples para pegar o valor do objeto No anterior a posicao indicada
	#esse metodo nao eh um wrapper, eh proprio da classe ListaEncadeada, jah q o objeto No possui um ponteiro 
	#apenas para o proximo e nao para o anterior
	def getValorNoAnterior(self, posicaoDoNo):
		return self._listaInterna[posicaoDoNo-1].getValor()
	
	#_No eh uma classe interna a classe ListaEncadeada pois nao faz sentido um objeto _No existir fora de uma lista encadeada
	#apesar de que ainda assim eh possivel instanciar um objeto _No fazendo _No = ListaEncadeada._No(valor), mas o principio se mantem
	class _No(object):
	
		def __init__(self, valor=None):
			
			self.valor = valor
		
		#setar o valor do _No se foi criado sem nenhum
		def setValor(self,valor):
			self.valor = valor
			
		#proximo objeto _No
		def setProximo(self,proximo):
			self.proximo = proximo
		
		#retorno simples do valor
		def getValor(self):
			return self.valor
			
		#retorno simples do valor do proximo objeto No
		def getValorProximo(self):
			return self.proximo.getValor()
			
			

#chamadas de funcao e testes		
valoresDos_Nos = ['Absent Lovers', 'Neil', 'Jack', 'Me']
listaEncadeada = ListaEncadeada(len(valoresDos_Nos), valoresDos_Nos)

print('primeiro for\n \n')

for i in listaEncadeada._listaInterna:
	print(i.valor)
	
print('\n')

listaEncadeada.inserir_No(0, 666)
listaEncadeada.inserir_No(1, 333)
listaEncadeada.inserir_No(2, 777)

print('segundo for\n \n')
for i in listaEncadeada._listaInterna:
	print(i.valor)

print('\n')
listaEncadeada.deletar_No(1)

print('terceiro for\n \n')
for i in listaEncadeada._listaInterna:
	print(i.valor)
		

valorDoTerceiroNo = listaEncadeada.getValorNo(2)		#2 pq usa a notacao de lista/array
valorDoQuartoNo = listaEncadeada.getValorNo(3)
valorDoQuintoNo = listaEncadeada.getValorProximoNo(3)
valorDoSegundoNo = listaEncadeada.getValorNoAnterior(2)

print('Segundo No: ' + str(valorDoSegundoNo) + '\n')
print('Terceiro No: ' + str(valorDoTerceiroNo) + '\n')
print('Quarto No: ' + str(valorDoQuartoNo) + '\n')
print('Quinto No: ' + str(valorDoQuintoNo) + '\n')

	
	

