
from Estado import Estado
from No import No
import queue
from DesenhaArvore import DesenhaArvore
    

def executaBuscaBestFirst():
    """
    Esse metodo implementa a Busca Best First
    """    
    #cria a fila de prioridade
    filaP = queue.PriorityQueue()

    #lista com nos visitados
    visitado= []
    
    #cria o no raiz
    estadoInicial = Estado()
    #o no pai no noh raiz e None
    raiz = No(estadoInicial, None)
    
    #mostra a arvore de busca
    desenhaArvore = DesenhaArvore()
    desenhaArvore.criaDiagrama(raiz, raiz)
    
    #adiciona na fila de prioridade
    filaP.put((raiz.heuristica, raiz))
    visitado.append(raiz.estado.posicao)
 
    #verifica se ha um noh na fila de prioridade
    while not filaP.empty(): 
        
        #retira o primeiro noh da fila de prioridade
        _, noAtual = filaP.get()
        
        #remove da fringe
        #e coloca o noh atual no processo de busca
        noAtual.fringe = False
        
        print ("-- Noh Atual --", noAtual.estado.posicao)
        
        #verifica se esse eh o estado meta
        if noAtual.estado.funcaoObjetivo():
            print ("Alcancado o estado meta")
            #print do caminho
            print ("----------------------")
            print ("Caminho")
            noAtual.printCaminho()
            
            #mostra a arvore de busca explorada ateh aqui
            desenhaArvore = DesenhaArvore()
            desenhaArvore.criaDiagrama(raiz, noAtual)
            break
 
        #pega os nos filhos
        estadosFihos = noAtual.estado.funcaoSucessora()
        for estadoFiho in estadosFihos :
            #verifica se o no ainda nao foi visitado
            if estadoFiho not in visitado:             
                #cria um noh
                #e coloca na arvore
                noFilho = No(Estado(estadoFiho), noAtual)

                #coloca na fila de prioridade
                filaP.put((noFilho.heuristica, noFilho))
                visitado.append(noFilho.estado.posicao)

            
        #mostra a arvore de busca explorada ateh aqui
        desenhaArvore = DesenhaArvore()
        desenhaArvore.criaDiagrama(raiz, noAtual)
                
    #print arvore
    print ("----------------------")
    print ("Arvore")
    raiz.printArvore()

    