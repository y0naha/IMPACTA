#Estado Profundiade

from GrafoDados import *
class Estado():
    '''
    Esta classe recupera informações do estado para o aplicativo de busca
    '''
    
    # Construtor
    def __init__(self, posicao= None, destino = None):
        if posicao== None:
            #cria o estado inicial
            self.posicao = self.pegaEstadoInicial()
        else:
            self.posicao = posicao

        if destino == None:
            #cria estado meta padrao
            self.destino = "Impacta"
        else:
            self.destinoo = destino
    

    def pegaEstadoInicial(self):
        """
        Este metodo retorna o estado incial da busca
        """
        estadoInicial= "Casa"
        return estadoInicial


    def funcaoSucessora(self):
        """
        Esta é a função sucessora. Gera todo os possiveis
        lugares que podem ser alcançados a partir do estado atual.
        """
        return conexoes[self.posicao]        


    def funcaoObjetivo(self):
        """
        Este método verifica se o caminho está no estado objetivo
        """
        #verifica que o lugar atual eh o carregamento
        return self.posicao == self.destino