"""Integrante 3: movimentos do rei e cavalo, cores e sistema de capturas.

Convenção herdada de tabuleiro.py:
    letras MAIÚSCULAS = peças brancas;
    letras minúsculas = peças pretas;
    "#" = casa vazia.

As posições são tuplas (linha, coluna), com índices de 0 a 7.
"""

from tabuleiro import posicao_valida


def movimento_rei(origem: tuple, destino: tuple) -> bool:
    """Verifica se o rei anda exatamente uma casa em qualquer direção.

    Parâmetros:
        origem (tuple): (linha, coluna) atual.
        destino (tuple): (linha, coluna) pretendida.

    Retorna:
        bool: True quando a forma do movimento é válida.

    Observação: não verifica xeque; isso não consta nas regras do módulo.
    """
    linha_inicial, coluna_inicial = origem
    linha_final, coluna_final = destino

    if not posicao_valida(linha_inicial, coluna_inicial):
        return False
    if not posicao_valida(linha_final, coluna_final):
        return False

    diferenca_linha = abs(linha_final - linha_inicial)
    diferenca_coluna = abs(coluna_final - coluna_inicial)

    return (diferenca_linha <= 1 and diferenca_coluna <= 1
            and (diferenca_linha != 0 or diferenca_coluna != 0))


def movimento_cavalo(origem: tuple, destino: tuple) -> bool:
    """Verifica o movimento em L do cavalo (duas casas e mais uma).

    O cavalo pode saltar outras peças; por isso não usa caminho_livre().
    """
    linha_inicial, coluna_inicial = origem
    linha_final, coluna_final = destino

    if not posicao_valida(linha_inicial, coluna_inicial):
        return False
    if not posicao_valida(linha_final, coluna_final):
        return False

    diferenca_linha = abs(linha_final - linha_inicial)
    diferenca_coluna = abs(coluna_final - coluna_inicial)

    return ((diferenca_linha == 2 and diferenca_coluna == 1)
            or (diferenca_linha == 1 and diferenca_coluna == 2))


def mesma_cor(peca1: str, peca2: str) -> bool:
    """Retorna True se duas peças existentes são da mesma cor.

    "#" representa uma casa vazia e não possui cor.
    """
    if peca1 == "#" or peca2 == "#":
        return False

    return ((peca1.isupper() and peca2.isupper())
            or (peca1.islower() and peca2.islower()))


def captura_permitida(tabuleiro: list, origem: tuple, destino: tuple) -> bool:
    """Confere se há uma peça adversária na casa de destino.

    Esta função avalia apenas a possibilidade de captura por COR.
    A forma do movimento é validada pela função da peça.
    """
    linha_inicial, coluna_inicial = origem
    linha_final, coluna_final = destino

    if not posicao_valida(linha_inicial, coluna_inicial):
        return False
    if not posicao_valida(linha_final, coluna_final):
        return False
    if origem == destino:
        return False

    peca_origem = tabuleiro[linha_inicial][coluna_inicial]
    peca_destino = tabuleiro[linha_final][coluna_final]

    if peca_origem == "#" or peca_destino == "#":
        return False

    return not mesma_cor(peca_origem, peca_destino)


def capturar_peca(tabuleiro: list, origem: tuple, destino: tuple) -> bool:
    """Captura a peça adversária e altera o próprio tabuleiro.

    Retorna True se realizou a captura; False caso contrário.
    Valida também a forma do movimento do rei e cavalo, que são
    as peças sob responsabilidade do Integrante 3.
    """
    if not captura_permitida(tabuleiro, origem, destino):
        return False

    linha_inicial, coluna_inicial = origem
    linha_final, coluna_final = destino
    peca = tabuleiro[linha_inicial][coluna_inicial]

    if peca.upper() == "R" and not movimento_rei(origem, destino):
        return False
    if peca.upper() == "C" and not movimento_cavalo(origem, destino):
        return False

    tabuleiro[linha_final][coluna_final] = peca
    tabuleiro[linha_inicial][coluna_inicial] = "#"
    return True
