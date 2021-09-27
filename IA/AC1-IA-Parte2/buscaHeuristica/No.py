from Mapa import *
import math

class No:
    '''
    Essa classe representa um noh na arvore de busca
    '''
    
    def __init__(self, estado,noPai):
        """
        Construtor
        """
        self.estado = estado
        self.profundidade = 0
        self.filhos = []
        self.pai= None
        self.colocaPai(noPai)
        self.fringe = True
        self.heuristica = 0
        self.custoAteRaiz = 0
        self.calculaCusto()
        self.calculaHeuristica()
                   
    def colocaPai(self, noPai):
        """
        Esse metodo adiciona um noh em outro noh
        """
        if noPai != None:
            noPai.filhos.append(self)
            self.pai = noPai
            self.profundidade = noPai.profundidade + 1
        else:
            self.pai = None


    def addFilho(self, noFilho):
        """
        Este método adiciona um nó em outro nó
        """
        self.filhos.append(noFilho)
        noFilho.pai = self   # o noFilho aponta para o nó atual
        noFilho.profundidade = self.profundidade + 1


    def printArvore(self):
        """
        Este metodo faz um print da arvore de busca 
        """
        print (self.profundidade , " - " , self.estado.posicao)
        for filho in self.filhos:
            filho.printArvore()


    def printCaminho(self):
        """
        Este metdo faz um print do estado inicial ateh o estado meta
        """
        if self.pai != None:
            self.pai.printCaminho()
        print ("-> ", self.estado.posicao)
        

    def calculaDistancia(self, local1, local2):
        """
        Este metodo calcula a distancia entre dois pontos
        """
        #delta na coordenada x
        dx = local1[0] - local2[0]
        #delta na coordenada y
        dy = local1[1] - local2[1]
        #distancia
        distancia = math.sqrt(dx ** 2 + dy ** 2)
        return distancia
    
        
    def calculaCusto(self):
        """
        Este metodo calcula a distancia do noh atual ateh o o no raiz
        """
        
        if self.pai!= None:
            #encontrar distância do nó atual ao pai
            distancia = self.calculaDistancia(localizacao[self.estado.posicao], localizacao[self.pai.estado.posicao])
            #custo = custo do pai + distancia
            self.custoAteRaiz = self.pai.custoAteRaiz + distancia 
        else:
            self.custoAteRaiz = 0
        
    
        
    def calculaHeuristica(self):
        """
        Esta funcao calcula o valor heuristico do noh
        """        
        # encontre a distância entre este estado e o estado objetivo
        localMeta = localizacao["Impacta"]
        localCorrente = localizacao[self.estado.posicao]
        distanciaParaMeta = self.calculaDistancia(localMeta,localCorrente )
        
        #usa a distancia para formar um valor heurístico
        heuristica = self.custoAteRaiz + distanciaParaMeta
              
        print ("Heuristica para ", self.estado.posicao, "=", heuristica," (",self.custoAteRaiz, distanciaParaMeta,")")
        self.heuristica = heuristica  


