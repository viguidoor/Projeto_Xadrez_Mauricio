# Projeto de Xadrez em Python

Projeto integrador de Lógica de Programação. Esta versão reúne a estrutura original de `tabuleiro.py` com a **parte do Integrante 3 — Peças Especiais e Sistema de Capturas**.

## Como executar

É necessário ter o Python 3 instalado. Abra o terminal na pasta do projeto.

```bash
python main.py
```

O programa mostra um tabuleiro inicial e uma demonstração parcial com movimentos de cavalos, captura de peão adversário, uma tentativa de movimento inválido do rei e uma tentativa de capturar peça aliada.

Para executar os testes automatizados desse módulo:

```bash
python -m unittest -v testes_capturas.py
```

## Arquivos

| Arquivo | Responsabilidade |
|---|---|
| `tabuleiro.py` | Integrante 1: cria, mostra e atualiza o tabuleiro. A função `mover_peca` agora chama as regras do Integrante 3. |
| `capturas.py` | **Integrante 3:** valida os movimentos do rei e do cavalo, compara cores e realiza capturas. |
| `testes_capturas.py` | Testes da implementação e da integração do Integrante 3. |
| `main.py` | Demonstração provisória para executar pelo terminal. |

## Convenções do projeto

- O tabuleiro é uma matriz de 8 linhas por 8 colunas.
- Uma posição é uma tupla `(linha, coluna)`; os índices vão de `0` a `7`.
- `#` significa casa vazia.
- Letras **maiúsculas** identificam peças **brancas** e **minúsculas** identificam peças **pretas**.
- `R/r` = rei; `C/c` = cavalo; `T/t` = torre; `B/b` = bispo; `Q/q` = dama; `P/p` = peão.

## Funções do Integrante 3

### `movimento_rei(origem, destino)`

Retorna `True` se o rei muda uma casa na horizontal, vertical ou diagonal. Não permite ficar parado nem sair dos limites do tabuleiro. O tratamento de xeque ainda não foi implementado.

```python
movimento_rei((4, 4), (5, 5))  # True
movimento_rei((4, 4), (6, 4))  # False
```

### `movimento_cavalo(origem, destino)`

Retorna `True` quando o deslocamento forma um L (duas casas numa direção e uma na outra). O cavalo pode saltar peças.

```python
movimento_cavalo((4, 4), (6, 5))  # True
movimento_cavalo((4, 4), (6, 6))  # False
```

### `mesma_cor(peca1, peca2)`

Retorna `True` se ambas são peças existentes e pertencem à mesma cor.

```python
mesma_cor("R", "P")  # True
mesma_cor("R", "p")  # False
```

### `captura_permitida(tabuleiro, origem, destino)`

Retorna `True` se existe uma peça na origem e uma peça **adversária** no destino. A função verifica a condição de **cor**, não a geometria do movimento.

### `capturar_peca(tabuleiro, origem, destino)`

Se a captura for válida, coloca a peça atacante no destino e limpa a origem, modificando a matriz recebida. Retorna `True` quando captura e `False` quando recusa. Para rei e cavalo, também valida a geometria do movimento. A validação de trajetória das demais peças depende dos módulos restantes.

## Integração com `tabuleiro.py`

A função `mover_peca(tabuleiro, l_inicial, c_inicial, l_final, c_final)` mantém sua assinatura original e retorna o próprio tabuleiro. Ela agora:

1. Verifica se as posições existem e se a origem contém uma peça.
2. Não permite que uma peça capture outra da mesma cor.
3. Valida a geometria dos movimentos de **rei** e **cavalo**.
4. Chama a função de captura quando o destino contém uma peça adversária.
5. Deixa o tabuleiro inalterado em caso de movimento recusado.

Também foram corrigidas as posições iniciais de bispo e cavalo, que estavam trocadas, e os símbolos Unicode das peças por cor.

## O que ainda falta para o projeto completo

Esta versão **não é um jogo de xadrez completo**. Ainda precisam ser integrados:

- Integrante 2: movimentos da torre, bispo e dama, incluindo verificação de caminho livre.
- Integrante 4: movimento do peão, controle de turnos, testes completos e documentação final.
- Integração final: uma partida com pelo menos 10 jogadas válidas envolvendo todas as peças exigidas, além do relatório.

**Atenção:** o `mover_peca` ainda não valida a forma do movimento de torre, bispo, dama ou peão. Até que os outros módulos sejam adicionados, não use essas peças para demonstrar a legalidade de movimentos. Xeque, xeque-mate, roque, promoção e en passant também não foram implementados.
