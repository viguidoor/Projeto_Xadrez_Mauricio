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
            if(i == 0 and j == 2 or i == 0 and j == 5):
                tabuleiro[i][j] = "b"
            if(i == 0 and j == 1 or i == 0 and j == 6):    
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
            if(i == 7 and j == 2 or i == 7 and j == 5):    
                tabuleiro[i][j] = "B"     
            if(i == 7 and j == 1 or i == 7 and j == 6):
                tabuleiro[i][j] = "C"                  
            if(i == 7 and j == 3):
                tabuleiro[i][j] = "Q"
            if(i == 7 and j == 4):
                tabuleiro[i][j] = "R"
            if(i == 6):                  
                tabuleiro[i][j] = "P"
    return tabuleiro

def mostrar_tabuleiro(tabuleiro: list) -> None:
    """Imprime o tabuleiro usando símbolos das peças e casas vazias."""
    simbolos = {
        "R": "♔", "Q": "♕", "T": "♖", "B": "♗", "C": "♘", "P": "♙",
        "r": "♚", "q": "♛", "t": "♜", "b": "♝", "c": "♞", "p": "♟",
    }

    print("    0  1  2  3  4  5  6  7")
    for i in range(8):
        linha_impressao = []
        for j in range(8):
            peca = tabuleiro[i][j]
            if peca == "#":
                simbolo = "□" if (i + j) % 2 == 0 else "■"
            else:
                simbolo = simbolos[peca]
            linha_impressao.append(simbolo)
        print(f"{i}   " + "  ".join(linha_impressao))


def posicao_valida(linha: int, coluna: int) -> bool:
    """
    Verifica se a linha e a coluna estão dentro dos limites do tabuleiro 8x8.
    
    """

    if(linha >= 0 and linha < 8 and
       coluna >= 0 and coluna < 8):
        return True
    else:
        return False

def mover_peca(tabuleiro: list, l_inicial: int, c_inicial: int,
               l_final: int, c_final: int) -> list:
    """Move uma peça, preservando a assinatura original do projeto.

    Retorna o próprio tabuleiro. Em caso de movimento inválido, não o altera.
    Nesta etapa, valida o rei e cavalo e impede capturas da mesma cor.
    As regras das outras peças serão integradas por seus responsáveis.
    """
    # Importação local para evitar dependência circular entre os módulos.
    from capturas import (movimento_rei, movimento_cavalo,
                          mesma_cor, capturar_peca)

    if not posicao_valida(l_inicial, c_inicial):
        return tabuleiro
    if not posicao_valida(l_final, c_final):
        return tabuleiro

    origem = (l_inicial, c_inicial)
    destino = (l_final, c_final)
    if origem == destino:
        return tabuleiro

    peca = tabuleiro[l_inicial][c_inicial]
    peca_no_destino = tabuleiro[l_final][c_final]

    if peca == "#":
        return tabuleiro
    if mesma_cor(peca, peca_no_destino):
        return tabuleiro

    if peca.upper() == "R" and not movimento_rei(origem, destino):
        return tabuleiro
    if peca.upper() == "C" and not movimento_cavalo(origem, destino):
        return tabuleiro

    if peca_no_destino != "#":
        capturar_peca(tabuleiro, origem, destino)
    else:
        tabuleiro[l_final][c_final] = peca
        tabuleiro[l_inicial][c_inicial] = "#"

    return tabuleiro
