# Análise e Projeto de Algoritmos
# AC2: Ciência da Computação
#
# Email Impacta: larissa.ionafa@aluno.faculdadeimpacta.com.br


"""
ATENÇÃO: nesta AC estão proibidos comandos como: sort(), sorted(), list(), e similares.
Você deve construir as funções solicitadas sem fazer uso de funções auxiliares do Python.
Também não reaproveite as funções da atividade.

Funções permitidas: len() e range().

Não obedecer essas regras pode resultar na anulação da sua atividade!
"""


def esta_ordenada(lista):
	"""
	Implemente a função esta_ordenada(lista), que recebe uma lista por parâmetro e 
	retorna True caso a lista já esteja ordenada e False caso contrário.

	Uma lista L está ordenada quando:
	L[0] <= L[1] <= L[2] <= ... <= L[n-1], onde n é o tamanho da lista, ou seja, n = len(L).

	RESTRIÇÕES: você deve fazer esse algoritmo de forma EFICIENTE, isto é, cada índice
	da lista só pode ser acessado no máximo 2 vezes.

	Note que para construir o algoritmo você terá que comparar os elementos da lista
	dois a dois: L[0] com L[1], depois L[1] com L[2], depois L[2] com L[3], e assim
	por diante!
	"""
	cont = 0
	for i in range(1, len(lista)):
		if (lista[i - 1] <= lista[i]):
			cont += 1
		else:
			return False
	if cont == (len(lista) - 1):
		return True


def ordenacao_bolha(lista):
	"""
	Com base no algoritmo de ordenação pelo método da bolha visto em aula, construa
	a função ordenacao_bolha(lista) que recebe uma lista por parâmetro e ordena essa
	lista. Como listas são passadas por referência, a função não deve retornar nada.

	RESTRIÇÕES: existe uma maneira mais eficiente de implementar o método da bolha.
	Note que durante a execução do algoritmo, os elementos são comparados dois a dois
	(de forma parecida com o algoritmo que você construiu acima), ou seja, o algoritmo
	compara se L[j-1] > L[j], e se o elemento da esquerda (L[j-1]) for maior que o
	elemento da direita (L[j]), eles são trocados.
	Você deve modificar o algoritmo para detectar se durante a comparação dois a dois dos
	elementos  da lista (feita pelo laço mais interno) houve ou não alguma troca. Se nenhuma
	troca ocorreu, significa que a lista já está ordenada, e o laço mais externo não precisará
	executar outra iteração, fazendo com que o algoritmo encerre e execute menos passos.
	
	DICA: utilize um flag booleano para detectar se houve ou não troca. No laço mais externo,
	mude o comando for por um while, pois assim você poderá incluir o valor do flag booleano
	na condição lógica.

	No exemplo a seguir, note que esta lista está QUASE ordenada. É aqui que a versão
	modificada do método da bolha que você deve construir será mais eficiente.

	EXEMPLO: suponha a seguinte lista de entrada: [21, 60, 44, 57, 80].
	Marcamos o flag booleano como False.
	O algoritmo irá comparar se:
		L[0] > L[1], que é falso.
		L[1] > L[2], que é verdadeiro, portanto troque-os: [21, 44, 60, 57, 80].
		Neste ponto, marque o flag booleano como True.

		Considerando a lista atualizada, continuamos:
		L[2] > L[3], que é verdadeiro, então troque-os: [21, 44, 57, 60, 80]
		
		Considerando a lista atualizada, continuamos:
		L[3] > L[4], que é falso.
	
	Neste ponto teremos encerrado o laço mais interno. Mas o algoritmo não termina por aqui.
	Ele irá executar outras iterações do laço mais externo. Ou seja:
	Voltamos a marcar o flag booleano como False.
	Considere a última versão da lista: [21, 44, 57, 60, 80]
		L[0] > L[1], que é falso.
		L[1] > L[2], que é falso.
		L[2] > L[3], que é falso.
		Não precisamos comparar L[4] porque ele já está na posição correta de acordo com o algoritmo.
	Aqui teremos encerrado o laço mais interno mais uma vez. Note que o valor do flag
	booleano não foi mais alterado, isto é, ele permanece False.
	Ou seja, nenhum elemento da lista precisou ser trocado, então ela já está ordenada!!!
	Neste caso, não precisamos mais executar o laço mais externo e o algoritmo encerra!	
	"""
	troca = True
	i = 0
	while True: 
		troca = False
		for j in range(1, len(lista)-i):
			
			if lista[j-1] > lista[j]:
				temp = lista[j-1]
				lista[j-1] = lista[j]
				lista[j] = temp
				troca = True
		i += 1
		if troca is False:
			break

