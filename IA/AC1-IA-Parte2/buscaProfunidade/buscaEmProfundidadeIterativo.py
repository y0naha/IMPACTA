from Estado import Estado
from No import No
from time import sleep

def buscaEmProfundidadeIterativo():
    #cria pilha
    pilha = []
    #cria no raiz e coloca na pilha
    estadoInicial = Estado()#colocar o nome do estado inicial
    raiz = No(estadoInicial)
    pilha.append(raiz)
    
    #verifica se há algo na pilha para da um pop

    while len(pilha) > 0:
        sleep(0.5)
        nohCorrente = pilha.pop() 

        print("--pop--", nohCorrente.estado.nome)
        
        #verifique se este é o estado da meta
        if nohCorrente.estado.funcaoObjetivo():
            print("Chegou ao estado meta!")
            break
            
        #obtem os nós filhos    
        estadosFilhos = nohCorrente.estado.funcaoSucessora()
        for estFilho in estadosFilhos:
            nohFilho = No(Estado(estFilho))
            nohCorrente.addFilho(nohFilho)

        # em ordem reversa adicionar nó à pilha
        for index in range(len(nohCorrente.filhos)-1,-1,-1):
            if (nohCorrente.filhos[index]!=nohCorrente.pai):
                pilha.append(nohCorrente.filhos[index])
            
            
        