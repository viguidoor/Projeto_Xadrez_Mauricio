"""Integrante 3: movimentos do rei e cavalo, cores e sistema de capturas.

Convenção herdada de tabuleiro.py:
    letras MAIÚSCULAS = peças brancas;
    letras minúsculas = peças pretas;
    "#" = casa vazia.

Cada posição chega no formato (linha, coluna), com valores de 0 a 7:
    posicao[0] é a linha;
    posicao[1] é a coluna.
"""

from tabuleiro import posicao_valida


def distancia(inicio: int, fim: int) -> int:
    """Calcula quantas casas existem entre dois números.

    O resultado é sempre positivo, não importa a direção do movimento.
    Exemplo: distancia(4, 6) = 2 e distancia(6, 4) = 2.

    Parâmetros:
        inicio (int): número de partida.
        fim (int): número de chegada.

    Retorna:
        int: quantidade de casas entre os dois números.
    """
    # Sempre faz o maior menos o menor, para o resultado nunca ser negativo.
    if fim >= inicio:
        return fim - inicio
    else:
        return inicio - fim


def movimento_rei(origem, destino) -> bool:
    """Verifica se o rei anda exatamente uma casa em qualquer direção.

    Parâmetros:
        origem: posição atual do rei (linha, coluna).
        destino: posição para onde o rei quer ir (linha, coluna).

    Retorna:
        bool: True quando o movimento é válido.

    Observação: não verifica xeque; isso não consta nas regras do módulo.
    """
    # Separa a linha e a coluna de cada posição.
    linha_inicial = origem[0]
    coluna_inicial = origem[1]
    linha_final = destino[0]
    coluna_final = destino[1]

    # As duas casas precisam estar dentro do tabuleiro.
    if not posicao_valida(linha_inicial, coluna_inicial):
        return False
    if not posicao_valida(linha_final, coluna_final):
        return False

    # Quantas casas o rei andou na vertical e na horizontal.
    casas_linha = distancia(linha_inicial, linha_final)
    casas_coluna = distancia(coluna_inicial, coluna_final)

    # Se não andou nenhuma casa, não é um movimento.
    if casas_linha == 0 and casas_coluna == 0:
        return False

    # O rei pode andar no máximo uma casa em cada direção.
    if casas_linha <= 1 and casas_coluna <= 1:
        return True

    return False


def movimento_cavalo(origem, destino) -> bool:
    """Verifica o movimento em L do cavalo (duas casas e mais uma).

    O cavalo pode saltar outras peças; por isso não usa caminho_livre().

    Parâmetros:
        origem: posição atual do cavalo (linha, coluna).
        destino: posição para onde o cavalo quer ir (linha, coluna).

    Retorna:
        bool: True quando o movimento é válido.
    """
    # Separa a linha e a coluna de cada posição.
    linha_inicial = origem[0]
    coluna_inicial = origem[1]
    linha_final = destino[0]
    coluna_final = destino[1]

    # As duas casas precisam estar dentro do tabuleiro.
    if not posicao_valida(linha_inicial, coluna_inicial):
        return False
    if not posicao_valida(linha_final, coluna_final):
        return False

    # Quantas casas o cavalo andou na vertical e na horizontal.
    casas_linha = distancia(linha_inicial, linha_final)
    casas_coluna = distancia(coluna_inicial, coluna_final)

    # Formato do L: 2 casas na vertical e 1 na horizontal...
    if casas_linha == 2 and casas_coluna == 1:
        return True
    # ...ou 1 casa na vertical e 2 na horizontal.
    if casas_linha == 1 and casas_coluna == 2:
        return True

    return False


def mesma_cor(peca1: str, peca2: str) -> bool:
    """Verifica se duas peças são da mesma cor.

    "#" representa uma casa vazia e não possui cor.

    Parâmetros:
        peca1 (str): primeira peça.
        peca2 (str): segunda peça.

    Retorna:
        bool: True quando as duas peças são da mesma cor.
    """
    # Casa vazia não tem cor.
    if peca1 == "#" or peca2 == "#":
        return False

    # As duas maiúsculas: as duas são brancas.
    if peca1.isupper() and peca2.isupper():
        return True

    # As duas minúsculas: as duas são pretas.
    if peca1.islower() and peca2.islower():
        return True

    return False


def captura_permitida(tabuleiro: list, origem, destino) -> bool:
    """Confere se há uma peça adversária na casa de destino.

    Esta função avalia apenas a possibilidade de captura por COR.
    A forma do movimento é validada pela função de cada peça.

    Parâmetros:
        tabuleiro (list): matriz 8x8 com as peças.
        origem: posição da peça que ataca (linha, coluna).
        destino: posição da peça que será capturada (linha, coluna).

    Retorna:
        bool: True quando a captura é permitida.
    """
    # Separa a linha e a coluna de cada posição.
    linha_inicial = origem[0]
    coluna_inicial = origem[1]
    linha_final = destino[0]
    coluna_final = destino[1]

    # As duas casas precisam estar dentro do tabuleiro.
    if not posicao_valida(linha_inicial, coluna_inicial):
        return False
    if not posicao_valida(linha_final, coluna_final):
        return False

    # A peça não pode capturar a si mesma.
    if linha_inicial == linha_final and coluna_inicial == coluna_final:
        return False

    # Pega na matriz as peças que estão nas duas casas.
    peca_origem = tabuleiro[linha_inicial][coluna_inicial]
    peca_destino = tabuleiro[linha_final][coluna_final]

    # Precisa ter uma peça atacando e uma peça para ser capturada.
    if peca_origem == "#" or peca_destino == "#":
        return False

    # Só pode capturar peça de cor diferente.
    if mesma_cor(peca_origem, peca_destino):
        return False

    return True


def capturar_peca(tabuleiro: list, origem, destino) -> bool:
    """Captura a peça adversária e altera o próprio tabuleiro.

    Valida também a forma do movimento do rei e do cavalo, que são
    as peças sob responsabilidade do Integrante 3.

    Parâmetros:
        tabuleiro (list): matriz 8x8 com as peças.
        origem: posição da peça que ataca (linha, coluna).
        destino: posição da peça que será capturada (linha, coluna).

    Retorna:
        bool: True se realizou a captura; False caso contrário.
    """
    # Primeiro confere se a captura é permitida pela cor.
    if not captura_permitida(tabuleiro, origem, destino):
        return False

    # Separa a linha e a coluna de cada posição.
    linha_inicial = origem[0]
    coluna_inicial = origem[1]
    linha_final = destino[0]
    coluna_final = destino[1]

    peca = tabuleiro[linha_inicial][coluna_inicial]

    # Se for o rei (branco "R" ou preto "r"), confere o movimento do rei.
    if peca == "R" or peca == "r":
        if not movimento_rei(origem, destino):
            return False

    # Se for o cavalo (branco "C" ou preto "c"), confere o movimento do cavalo.
    if peca == "C" or peca == "c":
        if not movimento_cavalo(origem, destino):
            return False

    # Faz a captura: a peça vai para o destino e a origem fica vazia.
    tabuleiro[linha_final][coluna_final] = peca
    tabuleiro[linha_inicial][coluna_inicial] = "#"
    return True
