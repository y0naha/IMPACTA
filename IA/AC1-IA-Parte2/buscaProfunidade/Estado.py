#Estado Profundiade

from GrafoDados import *
class Estado():
    '''
    Esta classe recupera informações do estado para o aplicativo de busca
    '''
    
    # Construtor
    def __init__(self, nome = None):  
        if nome == None:
            #cria o estado inicial
            self.nome = Estado.getEstadoInicial()
        else:
            self.nome = nome
    
    def getEstadoInicial():
        """
        Este método retorna o diretório atual
        """
        estadoInicial= "Casa"
        return estadoInicial
        
    def funcaoSucessora(self):
        """
        Esta é a função sucessora. Gera todo os possiveis
        caminhos que podem ser alcançados a partir do caminho atual.
        """
        return conexoes[self.nome]
            
    def funcaoObjetivo(self):
        """
        Este método verifica se o caminho está no estado objetivo final
        """
        return self.nome == "Impacta"
