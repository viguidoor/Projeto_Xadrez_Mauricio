import tabuleiro

def caminho_livre(tabuleiro: list, l_atual: int, c_atual: int, l_final: int, c_final: int) -> bool:
    """
      Recebe uma matriz, indices inicias da peça desejada e os indices do destino final,
      e verifica se durante o trajeto as casas estão livres para passar.

      Parametros:
           list: Uma matriz 8x8 (lista de listas) contendo as peças 
                 nas posições padrão e '#' nas casas vazias. 
           int: O indice das posições das peças.

      Retorna:
           bool: Retorna True ou False dependendo do resultado da verificação.
    """
    
                    # Verificação sobre a direção para aonde a peça vai andar
      
    
    if(l_final > l_atual):           
        passo_l = +1                 
    elif(l_final < l_atual):         
        passo_l = -1                 
    else:                            
        passo_l = 0                  
    if(c_final > c_atual):           
        passo_c = +1                 
    elif(c_final < c_atual):         
        passo_c = -1                 
    else:                            
        passo_c = 0                 
                    # Dá o primeiro passo para sair da casa de origem
    l_atual += passo_l
    c_atual += passo_c
                    # Verifica apenas as casas intermediárias até encostar no destino
    while (l_atual != l_final or c_atual != c_final):
        if(tabuleiro[l_atual][c_atual] != "#"):
             return False
        
        l_atual += passo_l
        c_atual += passo_c

                    # Se chegou até aqui sem retornar False, o caminho está livre 
    return True


def movimento_torre(tabuleiro: list, l_atual: int, c_atual: int, l_final: int, c_final: int) -> bool:
        """
        Recebe uma matriz, indices inicias da peça desejada e os indices do destino final,
        e verifica se a peça Torre durante o trajeto andou na vertical ou horizontal.                 
        Parametros:                                                                       
             list: Uma matriz 8x8 (lista de listas) contendo as peças                     
                   nas posições padrão e '#' nas casas vazias.                            
             int: O indice das posições das peças.                                        
        Retorna:                                                                          
             bool: Retorna True ou False dependendo do resultado da verificação.          
        """
               #Verificando se os indices do usuario são pelo menos 1 par igual e outro diferente.
               #Sendo assim o movimento horizontal e vertical.
    
        if(l_atual == l_final and c_atual != c_final or
           l_atual != l_final and c_atual == c_final):

               #Chamando a função caminho livre para verificar se não tem nenhuma peça na frente da Torre.
             if(caminho_livre(tabuleiro, l_atual, c_atual, l_final, c_final) == True):
                  return True
             else: 
                  return False
        else:
             return False


def movimento_bispo(tabuleiro: list, l_atual: int, c_atual: int, l_final: int, c_final: int) -> bool:
     """                                                                                
     Recebe uma matriz, indices inicias da peça desejada e os indices do destino final, 
     e verifica se a peça Bispo durante o trajeto andou na vertical ou horizontal a mesma quantidade de casas.      
     Parametros:                                                                        
          list: Uma matriz 8x8 (lista de listas) contendo as peças                      
                nas posições padrão e '#' nas casas vazias.                             
          int: O indice das posições das peças.                                         
     Retorna:                                                                           
          bool: Retorna True ou False dependendo do resultado da verificação.           
      """    

                     # Calculando a distancia de linha e coluna percorrida, usando a função abs(),
                     # para converter os valores para positivo 
                     
     l_percorrida = abs(l_final - l_atual)
     c_percorrida = abs(c_final - c_atual)

                     # Verificando se a distancia de linha e coluna percorrida são iguais

     if(l_percorrida == c_percorrida and l_percorrida > 0):
                     # Caso a comparação seja verdadeira, ele verifica se a função caminho_livre(),
                     # é verdadeira, retornado assim True e encerrando a função

          if(caminho_livre(tabuleiro, l_atual, c_atual, l_final, c_final) == True):
               return True
          else:
               return False
     else:
          return False     


def movimento_dama(tabuleiro: list, l_atual: int, c_atual: int, l_final: int, c_final: int) -> bool:
     """                                                                                                      
     Recebe uma matriz, indices inicias da peça desejada e os indices do destino final,                       
     e verifica se a peça Dama durante o trajeto andou na vertical e  horizontal a mesma quantidade de casas,
      ou andou horizontalmente ou verticalmente.
     Parametros:                                                                                              
          list: Uma matriz 8x8 (lista de listas) contendo as peças                                            
                nas posições padrão e '#' nas casas vazias.                                                   
          int: O indice das posições das peças.                                                               
     Retorna:                                                                                                 
          bool: Retorna True ou False dependendo do resultado da verificação.                                 
      """                                                                                                     
            # Verifica se pelo menos uma das funções:
            # movimento_torre() ou movimento_bispo() são verdadeiras.

     if(movimento_torre(tabuleiro, l_atual, c_atual, l_final, c_final) == True or
        movimento_bispo(tabuleiro, l_atual, c_atual, l_final, c_final) == True):
          return True
     else:
          return False
          







