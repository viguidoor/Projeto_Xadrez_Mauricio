"""Demonstração parcial do projeto: rei, cavalo e capturas (Integrante 3)."""

from tabuleiro import criar_tabuleiro, mostrar_tabuleiro, mover_peca


def demonstrar():
    tabuleiro = criar_tabuleiro()
    print("TABULEIRO INICIAL")
    mostrar_tabuleiro(tabuleiro)

    # Uma pequena sequência de movimentos para mostrar a integração.
    jogadas = [
        ("Cavalo branco: b1 para c3", (7, 1), (5, 2)),
        ("Cavalo preto: b8 para c6", (0, 1), (2, 2)),
        ("Cavalo branco: c3 para d5", (5, 2), (3, 3)),
        ("Cavalo preto: c6 para d4", (2, 2), (4, 3)),
        ("Cavalo branco captura peão preto em c7", (3, 3), (1, 2)),
        ("Tentativa inválida: rei branco anda duas casas", (7, 4), (5, 4)),
        ("Tentativa inválida: rei captura peão branco", (7, 4), (6, 4)),
    ]

    for descricao, origem, destino in jogadas:
        print("\n" + descricao)
        antes = [linha.copy() for linha in tabuleiro]
        mover_peca(tabuleiro, origem[0], origem[1], destino[0], destino[1])
        print("Movimento realizado." if tabuleiro != antes else "Movimento recusado.")
        mostrar_tabuleiro(tabuleiro)


if __name__ == "__main__":
    demonstrar()
