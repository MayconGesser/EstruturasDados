#-*- coding: utf-8 -*-

#Fila utilizando alocação dinâmica; basicamente comporta-se como uma lista encadeada, retirando sempre da
#primeira posição da lista. A iteração se dá de forma idêntica a uma lista encadeada.

from No import No

class Fila:

	def __init__(self):
		self.primeiro = None
		
	def add(self,elemento):
		inserido = No(elemento)
		if(not self.primeiro):
			self.primeiro = inserido
		else:
			cursor = self.primeiro	#procura o final da fila 
			while(cursor.proximo):
				cursor = cursor.proximo
			cursor.proximo = inserido

	def get(self):
		retorno = self.primeiro.valor
		self.primeiro = self.primeiro.proximo
		return retorno
	

	def imprimir(self):
		rep = 'primeiro: '
		cursor = self.primeiro
		while(cursor.proximo):
			rep += str(cursor.valor + '\n')
			cursor = cursor.proximo
		rep += str(cursor.valor + '\n')
		print(rep)

fila = Fila()
fila.add('Neal')
fila.add('Jack')
fila.add('Me')
fila.add('Absent')
fila.add('Lovers')
fila.imprimir()
print(fila.get())
print(fila.get())
print(fila.get())
fila.imprimir()
