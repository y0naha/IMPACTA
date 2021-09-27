# Análise e Projeto de Algoritmos
# AC1: Ciência da Computação
#
# Email Impacta: larissa.ionafa@aluno.faculdadeimpacta.com.br


def somatorio(n):
	"""
	Função recursiva que recebe um valor inteiro n >= 0, e devolve o somatório de 0 até n.

	Exemplos:
	------------
	somatorio(0) deve devolver 0;
	somatorio(2) deve devolver 3, pois 0+1+2 = 3;
	somatorio(5) deve devolver 15, pois 0+1+2+3+4+5 = 15;

	Retorno:
	-----------
	int: soma dos números inteiros de 0 até n.
	"""
	
	if n == 0:
		return 0
	else:
		return n + somatorio(n-1)
	


def potencia_de_2(n):
	"""
	Função recursiva que recebe um valor inteiro n >= 1, e devolve True se n é
	potência de 2 e False caso contrário.

	Para testar se um número é potência de 2, podemos usar os seguintes testes:
		- Se n == 1, então devolva True;
		- Caso contrário, se n % 2 == 1 (isto é, se n é ímpar mas não é igual a 1),
		devolva False;
		- Caso contrário (se n é par), calcule a divisão inteira (operador //) de n por 2 e 
		repita os dois testes acima no próximo passo.
	
	Exemplos:
	-----------
	potencia_de_2(4) devolve True, pois 4 = 2**2;
	potencia_de_2(6) devolve False, pois 6 não é potência de 2;
	potencia_de_2(11) devolve False, pois 11 não é potência de 2;
	potencia_de_2(32) devolve True, pois 32 = 2**5;

	Retorno:
	-----------
	bool: True se n é potência dsoma_digitose 2, False caso contrário.
	"""

	if n == 1:
		return True
	elif n % 2 == 1:
		return False
	else:
		n = n//2
		return potencia_de_2(n)


def qtd_digitos(n):
	"""
	Função recursiva que recebe um valor inteiro n : e devolve um valor inteiro
	indicando o número de dígitos de n.

	Exemplos:
	------------
	qtd_digitos(4) devolve 1, pois 4 contém somente 1 dígito;
	qtd_digitos(9) devolve 1, pois 9 contém somente 1 dígito;
	qtd_digitos(10) devolve 2, pois 10 contém 2 dígitos;
	qtd_digitos(99) devolve 2, pois 99 contém 2 dígitos;
	qtd_digitos(1071) devolve 4, pois 1071 contém 4 dígitos;

	Retorno:
	------------
	int: número de digitos de n.
	"""
#primeira tentativa 

	# total = 0
	# if n < 10:
	# 	total = 1
	# elif(n>=10):
	# 	total += qtd_digitos(n//10)
	# 	return total +1
	# return total

#correcao do professor

	if n <= 9:
		return 1
	else:
		return qtd_digitos(n//10)+1


def soma_digitos(n):
	"""
	Função recursiva que recebe um valor inteiro n >= 1, e devolve o somatório de
	todos os dígitos de n.

	Exemplo:
	------------print(str(n+"Somado com")ve 14, pois 2+3+4+5 = 14;

	Retorno:
	------------
	int: soma dos dígitos de n.
	"""

	#primeira tentativa
	# total = 0
	# if n<10:
	# 	total += n
	# elif(n>=10):
	# 	total += n%10
	# 	total += soma_digitos(n//10)
	# return total
	
	#correcao do professor
	if n==0:
		return 0
	else:
		return (n%10) + soma_digitos(n//10)
	


def soma_lista(lista, i):
	"""
	Função recursiva que recebe uma lista com números inteiros (tipo list do Python) e
	um valor inteiro i >= 0, que representa um índice da lista.

	A função devolve o somatório de todos os números da lista a partir do índice i
	até o final da lista.

	Exemplo:
	------------
	Caso lista = [1,2,3,4] e i = 0,
		o retorno deve ser: 10, pois lista[0]+lista[1]+lista[2]+lista[3] = 10.
	Caso lista = [1,2,3,4] e i = 2,
		o retorno deve ser: 7, pois lista[2]+lista[3] = 7.
	Caso lista = [22, 33, 44, 55] e i = 1,
		o retorno deve ser 132, pois lista[1]+lista[2]+lista[3] = 132.
	
	Retorno:
	------------
	int: soma dos valores da lista.	
	"""

	#primeira tentativa
	# total = 0
	# if(i==len(lista)-1):
	# 	return lista[i]
	# else:
	# 	total+=lista[i]
	# 	total+=soma_lista(lista,i+1)
	
	# return total

	#correcao do professor
	if i < len(lista):
		return lista[i] + soma_lista(lista, i+1)
	else:
		return 0


