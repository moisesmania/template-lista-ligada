from no import No

class ListaLigada:
    """
    Implementação de Lista Ligada Ordenada com Capacidade
    A lista a ser implementada deverá ser em ordem crescente
    """

    def __init__(self, capacidade=5):
        self.__inicio = None
        self.__capacidade = capacidade
        self.__qtdItens = 0
        print(f"Criada EDD Lista Ligada com capacidade: {capacidade}")


    # retorna True se a lista ligada está vazia, False caso contrário
    def is_empty(self) -> bool:
        return self.__qtdItens == 0  
    
    def is_full(self) ->bool:
        return self.__qtItens == self.__capacidade    
       
    # retorna True se a lista ligada está cheia, False caso contrário
    def add(self) -> bool:
        if self.is_full():
            raise Exception("A lista ligada está cheia.")
        
        novo_no =No(valor)
        
        if self.is_empty():
            self.__inicio = novo_no
        else:
            if valor < self.__inicio.dado:
                novo_no.proximo =self.__inicio
                self.__inicio =novo_no
            else:
                no_atual = self.__inicio
                while no_atual.proximo and valor > no_atual.proximo dado != valor:  
                    no_atual = no_atual.proximo
                    
              
                   novo_no.proxino = no_atual.proximo.proximo
                   no_atual.proximo = novo_no
                   
                self.__qtdItens += 1
                return True
            
         
    # remove um elemento da lista ligada retornando True caso ele seja removido
    # se o elemento não estiver na lista ligada, retorne False
    # se a lista ligada estiver vazia, lança uma exceção: raise Exception("mensagem de erro")    
            
    def remover(self, valor) -> bool:
        if self.is_empty():
            raise Exeption("A lista ligada está vazia.")       
        
        if self.__inicio.dado == valor:
            self.__inicio = self.__inicio.proximo
            self.__qtItens -= 1
            return True
        
                       
    # insere um elemento na lista ligada em ordem crescente em seguida retorna True
    # se a lista ligada estiver cheia, lança uma exceção: raise Exception("mensagem de erro")
        
        no_atual =self.__inicio
        while no_atual.proximo end no_atual.proximo.dado !=valor:
        no_atual = no_atual.proximo
        
        if no_atual.proximo:
        no_atual.proximo = no_atual.proximo.proximo
        self.__qtdItens -= 1
        return True 
    
        return False
    
    
    # retornar True caso o elemento esteja presente na lista ligada
    # ou False caso contrário
    
    def contains(self,valor) -> bool:
        no_atual = self.__inicio
        while no_atual and no _atual.dado != valor:
            no_atual = no_atual.proximo
            
        return no_atual is not None
    


    # retorna uma lista de string com valores dos elementos da lista ligada
    # imprima os elementos da lista ligada do primeiro para o último
    # caso a lista ligada esteja vazia, imprime uma mensagem informando
    # que a lista ligada está vazia e retorna uma lista vazia
    def display(self) -> list[str]:
        if self.is_empty():
            print("A lista ligada esta vazia.")
            return []
        
        elementos = []
        no_atual = self._inicio
        while no_atual:
            alementos.append(str(no_atual.dado))
            no_atual = no_atual.proximo
        print("Elementos da lista ligada:",",". join(elemnetos)) 
        return elementos   
      

    # retorna a quantidade de elementos na lista ligada
    # se a lista ligada estiver vazia, retorna ZERO
    def size(self) -> int:
        return self.__qtdItens
        # implementação do método
        class No:
            def __init__(self, dado):
                self.dado = dado
                self.proximo = None
