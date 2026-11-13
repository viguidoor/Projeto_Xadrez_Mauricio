                           #Representação das Peças

"""    
Peças brancas = letras Maiúsculas
Peças pretas = letras minusculas


♔   -> 	'\u2654'  ->   r       ♚   ->  '\u265A'  ->  R
♕   -> 	'\u2655'  ->   q       ♛   ->  '\u265B'  ->  Q
♖   -> 	'\u2656'  ->   t       ♜   ->  '\u265C'  ->  T
♗   -> 	'\u2657'  ->   b       ♝   ->  '\u265D'  ->  B 
♘   -> 	'\u2658'  ->   c       ♞   ->  '\u265E'  ->  C
♙   -> 	'\u2659'  ->   p       ♟   ->  '\u265F'  ->  P


⬛  ->  '\u2B1C'               ⬜   ->  '\u2B1B'  

"""



def criar_tabuleiro() -> list:
    """
    Cria e inicializa a matriz 8x8 do tabuleiro de xadrez 
    com as peças nas posições iniciais oficiais.

    Parâmetros:
        Nenhum.

    Retorna:
        list: Uma matriz 8x8 (lista de listas) contendo as peças 
              nas posições padrão e '#' nas casas vazias.

    """
    tabuleiro = []
                    # Criando uma matriz 8x8 e preenchendo todos os espaços com #
    for i in range(8):
        tabuleiro_linhas = []
        for j in range(8):
            tabuleiro_linhas.append("#")
        tabuleiro.append(tabuleiro_linhas) 

                     # Percorrendo a lista e alterando os valores das peças para letras com base no indice inicial
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[i])):
                            # Peças Pretas
            if(i == 0 and j == 0 or i == 0 and j == 7):
                tabuleiro[i][j] = "t"
            if(i == 0 and j == 1 or i == 0 and j == 6):
                tabuleiro[i][j] = "b"
            if(i == 0 and j == 2 or i == 0 and j == 5):    
                tabuleiro[i][j] = "c"
            if(i == 0 and j == 3):                 
                tabuleiro[i][j] = "q"
            if(i == 0 and j == 4):
                tabuleiro[i][j] = "r"
            if(i == 1):
                tabuleiro[i][j] = "p"  

                           # Peças Brancas
            if(i == 7 and j == 0 or i == 7 and j == 7):
                tabuleiro[i][j] = "T"
            if(i == 7 and j == 1 or i == 7 and j == 6):    
                tabuleiro[i][j] = "B"     
            if(i == 7 and j == 2 or i == 7 and j == 5):
                tabuleiro[i][j] = "C"                  
            if(i == 7 and j == 3):
                tabuleiro[i][j] = "Q"
            if(i == 7 and j == 4):
                tabuleiro[i][j] = "R"
            if(i == 6):                  
                tabuleiro[i][j] = "P"
    return tabuleiro

def mostrar_tabuleiro(tabuleiro: list) -> None:
    """
    Recebe a função criar_tabuleiro e imprime o tabuleiro 8x8
    com as peças nas posições iniciais oficiais.

    Parâmetros:
       list: Uma matriz 8x8 (lista de listas) contendo as peças 
             nas posições padrão e '#' nas casas vazias.

    Retorna:
        None: Apenas imprime o tabuleiro no console.

          
    """
                       # Percorrendo a matriz e alterando as letras das peças por emojis correspondentes
    for i in range(len(tabuleiro)):
        linha_impressao = []

        
        for j in range(len(tabuleiro[i])):
                       # Definindo as casas brancas e pretas
            if(tabuleiro[i][j] == "#"):
                if((i + j) % 2 == 0):
                    linha_impressao.append("\u2b1c")
                else:
                    linha_impressao.append("\u2B1B")   

                      # Alterando as peças brancas
            elif(tabuleiro[i][j] == "T"):
                linha_impressao.append("\u265C ")
            elif(tabuleiro[i][j] == "C"):       
                linha_impressao.append("\u265E ")
            elif(tabuleiro[i][j] == "B"):       
                linha_impressao.append("\u265D ")
            elif(tabuleiro[i][j] == "Q"):            
                linha_impressao.append("\u265B ")
            elif(tabuleiro[i][j] == "R"):   
                linha_impressao.append("\u265A ")
            elif(tabuleiro[i][j] == "P"):   
                linha_impressao.append("\u265F ")

                      # Alterando as peças pretas 
            elif(tabuleiro[i][j] == "t"):            
                linha_impressao.append("\u2656 ")        
            elif(tabuleiro[i][j] == "c"):                
                linha_impressao.append("\u2658 ")             
            elif(tabuleiro[i][j] == "b"):            
                linha_impressao.append("\u2657 ")         
            elif(tabuleiro[i][j] == "q"):            
                linha_impressao.append("\u2655 ")         
            elif(tabuleiro[i][j] == "r"):            
                linha_impressao.append("\u2654 ")         
            elif(tabuleiro[i][j] == "p"):            
                linha_impressao.append("\u2659 ")  
    
        print(" ".join(linha_impressao))


def posicao_valida(linha: int, coluna: int) -> bool:
    """
    Verifica se a linha e a coluna estão dentro dos limites do tabuleiro 8x8.
    
    """

    if(linha >= 0 and linha < 8 and
       coluna >= 0 and coluna < 8):
        return True
    else:
        return False

def mover_peca(tabuleiro: list, l_inicial: int, c_inicial: int, l_final: int, c_final: int) -> list:
    """
    Move um peça para outro quadrado, com base na sua posição inicial e posição final

    Parâmetros:                                                 
       list: Uma matriz 8x8 (lista de listas) contendo as peças 
             nas posições padrão e '#' nas casas vazias.   
       int:  Posição inicial onde a peça se encontra, e final aonde o usuario deseja coloca-la           
    Retorna:                                                    
        list: Uma matriz 8x8 (lista de listas) contendo as peças
        nas posições atualizadas com base nos indices.             
    
    
    """
    
    if (posicao_valida(l_inicial, c_inicial) == True and posicao_valida(l_final, c_final) == True):
        tabuleiro[l_final][c_final] = tabuleiro[l_inicial][c_inicial]
        tabuleiro[l_inicial][c_inicial] = "#"
    return tabuleiro    








    
                      






