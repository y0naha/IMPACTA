import pydot
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

class DesenhaArvore:
    '''
    Essa classe desenha a arvore de busca
    '''
    def __init__(self):
        """
        Construtor
        """
        # cria o objeto grafo
        self.grafo = pydot.Dot(graph_type='graph', dpi = 300)
        #indice do no
        self.indice = 0
          
    def criaGrafo(self, no, noAtual):
        """
        Este metodo adiciona nos e arcos ao objeto grafo
        semelhante ao printArvore() da classe No
        """        
        # associa cor
        if no.estado.posicao == noAtual.estado.posicao:
            cor = "#ee0011" # cor vermelha
        elif no.fringe:
            cor = "#3399ff" # cor Azul
        else:
            cor = "#00ee11" # cor verde          
        #cria no
        grafoDoNoPai = pydot.Node(str(self.indice) + " " + no.estado.posicao, style="filled", \
                                      fillcolor = cor, xlabel = no.heuristica)
        self.indice += 1
        
        #add no
        self.grafo.add_node(grafoDoNoPai)
        
        #chama esse metodo para os nos filhos
        for noFilho in no.filhos:
            grafoComNosFilhos = self.criaGrafo(noFilho, noAtual)
            
            #cria arco
            arco= pydot.Edge(grafoDoNoPai, grafoComNosFilhos)
            
            #adiciona arco ao objeto grafo
            self.grafo.add_edge(arco)
            
        return grafoDoNoPai
        
    
    def criaDiagrama(self, noRaiz, noAtual):
        """
        Esse metodo desenha o diagrama
        """
        #adiciona nos e arcos ao diagrama
        self.criaGrafo(noRaiz, noAtual)
        
        #mostra o diagrama
        self.grafo.write_png('grafo.png')
        img=mpimg.imread('grafo.png')
        plt.imshow(img)
        plt.axis('off')
        mng = plt.get_current_fig_manager()
        #mng.window.state('normal')
        plt.show()