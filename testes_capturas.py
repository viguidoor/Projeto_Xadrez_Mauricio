"""Testes automatizados das funções do Integrante 3.

Execute: python -m unittest -v testes_capturas.py
"""
import unittest

from tabuleiro import criar_tabuleiro, mover_peca
from capturas import (
    movimento_rei, movimento_cavalo, mesma_cor,
    captura_permitida, capturar_peca,
)


class TestesIntegrante3(unittest.TestCase):
    def test_posicoes_iniciais_corretas(self):
        tabuleiro = criar_tabuleiro()
        self.assertEqual(tabuleiro[7][1], "C")  # Cavalo branco
        self.assertEqual(tabuleiro[7][2], "B")  # Bispo branco
        self.assertEqual(tabuleiro[0][1], "c")  # Cavalo preto
        self.assertEqual(tabuleiro[0][2], "b")  # Bispo preto
        self.assertEqual(tabuleiro[7][4], "R")  # Rei branco

    def test_rei_movimentos_validos(self):
        self.assertTrue(movimento_rei((4, 4), (5, 5)))
        self.assertTrue(movimento_rei((4, 4), (4, 3)))
        self.assertTrue(movimento_rei((4, 4), (3, 4)))

    def test_rei_movimentos_invalidos(self):
        self.assertFalse(movimento_rei((4, 4), (6, 4)))
        self.assertFalse(movimento_rei((4, 4), (4, 4)))
        self.assertFalse(movimento_rei((7, 4), (8, 4)))

    def test_cavalo_movimentos_validos(self):
        self.assertTrue(movimento_cavalo((4, 4), (6, 5)))
        self.assertTrue(movimento_cavalo((4, 4), (5, 2)))
        self.assertTrue(movimento_cavalo((7, 1), (5, 2)))

    def test_cavalo_movimentos_invalidos(self):
        self.assertFalse(movimento_cavalo((4, 4), (6, 6)))
        self.assertFalse(movimento_cavalo((4, 4), (4, 4)))
        self.assertFalse(movimento_cavalo((7, 1), (8, 3)))

    def test_mesma_cor(self):
        self.assertTrue(mesma_cor("R", "P"))
        self.assertTrue(mesma_cor("c", "p"))
        self.assertFalse(mesma_cor("R", "p"))
        self.assertFalse(mesma_cor("P", "#"))

    def test_captura_adversario(self):
        tabuleiro = [["#" for _ in range(8)] for _ in range(8)]
        tabuleiro[4][4] = "R"  # Rei branco
        tabuleiro[5][5] = "p"  # Peão preto
        self.assertTrue(captura_permitida(tabuleiro, (4, 4), (5, 5)))
        self.assertTrue(capturar_peca(tabuleiro, (4, 4), (5, 5)))
        self.assertEqual(tabuleiro[5][5], "R")
        self.assertEqual(tabuleiro[4][4], "#")

    def test_nao_captura_mesma_cor(self):
        tabuleiro = criar_tabuleiro()
        self.assertFalse(captura_permitida(tabuleiro, (7, 4), (6, 4)))
        self.assertFalse(capturar_peca(tabuleiro, (7, 4), (6, 4)))
        self.assertEqual(tabuleiro[7][4], "R")
        self.assertEqual(tabuleiro[6][4], "P")

    def test_nao_captura_casa_vazia(self):
        tabuleiro = criar_tabuleiro()
        self.assertFalse(captura_permitida(tabuleiro, (7, 1), (5, 2)))
        self.assertFalse(capturar_peca(tabuleiro, (7, 1), (5, 2)))

    def test_nao_captura_movimento_invalido(self):
        tabuleiro = [["#" for _ in range(8)] for _ in range(8)]
        tabuleiro[4][4] = "R"
        tabuleiro[6][4] = "p"
        self.assertFalse(capturar_peca(tabuleiro, (4, 4), (6, 4)))
        self.assertEqual(tabuleiro[4][4], "R")
        self.assertEqual(tabuleiro[6][4], "p")

    def test_cavalo_salta_pecas(self):
        tabuleiro = criar_tabuleiro()
        mover_peca(tabuleiro, 7, 1, 5, 2)
        self.assertEqual(tabuleiro[5][2], "C")
        self.assertEqual(tabuleiro[7][1], "#")
        self.assertEqual(tabuleiro[6][1], "P")

    def test_integracao_cavalo_captura(self):
        tabuleiro = criar_tabuleiro()
        mover_peca(tabuleiro, 7, 1, 5, 2)
        mover_peca(tabuleiro, 5, 2, 3, 3)
        mover_peca(tabuleiro, 3, 3, 1, 2)
        self.assertEqual(tabuleiro[1][2], "C")
        self.assertEqual(tabuleiro[3][3], "#")

    def test_integracao_rei_nao_atravessa_pecas_amigas(self):
        tabuleiro = criar_tabuleiro()
        mover_peca(tabuleiro, 7, 4, 6, 4)
        self.assertEqual(tabuleiro[7][4], "R")
        self.assertEqual(tabuleiro[6][4], "P")

    def test_integracao_rei_movimento_longo_invalido(self):
        tabuleiro = criar_tabuleiro()
        mover_peca(tabuleiro, 7, 4, 5, 4)
        self.assertEqual(tabuleiro[7][4], "R")
        self.assertEqual(tabuleiro[5][4], "#")

    def test_movimento_peca_inexistente_nao_muda_tabuleiro(self):
        tabuleiro = criar_tabuleiro()
        original = [linha.copy() for linha in tabuleiro]
        mover_peca(tabuleiro, 4, 4, 3, 4)
        self.assertEqual(tabuleiro, original)

    def test_movimento_fora_tabuleiro_nao_muda_tabuleiro(self):
        tabuleiro = criar_tabuleiro()
        original = [linha.copy() for linha in tabuleiro]
        mover_peca(tabuleiro, 7, 1, 8, 2)
        self.assertEqual(tabuleiro, original)


if __name__ == "__main__":
    unittest.main()
