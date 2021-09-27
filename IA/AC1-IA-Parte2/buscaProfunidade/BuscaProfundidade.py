from Estado import Estado
from No import No
from time import sleep

class BuscaEmProfundidade():
    """
    Essa classe executa uma Busca em Profundidade Recursiva
    """
    def __init__(self):
        self.achou = False
        
    
    def busca(self):
        """
        Este método realiza a busca
        """
        #pega o estado inicial
        estadoInicial = Estado()
        
        #cria o nó raiz
        noRaiz = No(estadoInicial)
        
        #realizar a busca a partir do nó raiz
        self.DFS(noRaiz)
        
        noRaiz.printArvore()
        
    
    def DFS(self, no):
        sleep(0.5)
        """
        Isso cria a árvore de busca
        """
        if not self.achou:
            print ("-- proc --", no.estado.nome)
            # verifica se foi atingido o estado meta
            if no.estado.funcaoObjetivo():
                print ("Atingido o estado de meta!")
                self.achou = True
                
            else:
                # encontra os estados sucessores do estado atual
                estadosFilhos = no.estado.funcaoSucessora()
                # adiciona os nós filhos na árvore
                for estadoFilho in estadosFilhos:
                    noFilho = No(Estado(estadoFilho))
                    no.addFilho(noFilho) 
                    # faz a busca em um dos nós filhos
                    self.DFS(noFilho)
