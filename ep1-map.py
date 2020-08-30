# tictactoe.py
# From Classic Computer Science Problems in Python Chapter 8
# Copyright 2018 David Kopec
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import random
from typing import List
from enum import Enum
from board import Piece, Board, Move


class TTTPiece(Piece, Enum):
    Player = "🤠"
    Terra = "🌲"
    Agua = "🌊"
    Areia = "🌵"
    E = " "  # stand-in for empty

    @property
    def opposite(self) -> TTTPiece:
        return TTTPiece.Player

    def __str__(self) -> str:
        return self.value


class MapaJogo:
    def iniciar(self):
        # estamos usando tuplas () porque podemos usar dentro de conjuntos
        # não é possível usar listas [] em Sets {}
        lista_inicial = ["_", "1", "2", "3", "4", "5", "6", "7", "8"]
        random.shuffle(lista_inicial)
        return tuple(lista_inicial)

    def imprimir(self, estado):
        return "| " + estado[0] + " | " + estado[1] + " | " + estado[2] + " |\n| " + estado[3] + " | " + estado[4] + " | " + estado[5] + " |\n| " + estado[6] + " | " + estado[7] + " | " + estado[8] + " |"

    def testar_objetivo(self, estado):
        return estado == ("1", "2", "3", "4", "5", "6", "7", "8", "_")

    # movimento do quadrado vazio
    def gerar_sucessores(self, estado):
        sucessores = []

        # encontra a posição do _
        posicao = estado.index("_")

        expansoes = [self._direita, self._esquerda, self._cima, self._baixo]
        random.shuffle(expansoes)
        for expansao in expansoes:
            sucessor = expansao(posicao, estado)
            if sucessor is not None:
                sucessores.append(sucessor)

        return sucessores

    def _esquerda(self, posicao, estado_atual):
        # movimento para esquerda
        if posicao not in [0, 3, 6]:
            # peça de baixo desce
            sucessor = list(estado_atual)
            sucessor[posicao] = sucessor[posicao - 1]
            sucessor[posicao - 1] = "_"
            return (tuple(sucessor), "⬅️")

    def _cima(self, posicao, estado_atual):
        # movimento para cima
        # Não gera se estiver no topo
        if posicao not in [0, 1, 2]:
            # peça de baixo sobe
            sucesso = list(estado_atual)
            sucesso[posicao] = sucesso[posicao - 3]
            sucesso[posicao - 3] = "_"
            return (tuple(sucesso), "⬆️")

    def _baixo(self, posicao, estado_atual):
        # movimento para baixo
        # Não gera se estiver no fundo
        if posicao not in [6, 7, 8]:
            # peça de baixo desce
            sucessor = list(estado_atual)
            sucessor[posicao] = sucessor[posicao + 3]
            sucessor[posicao + 3] = "_"
            return (tuple(sucessor), "⬇️")

    def _direita(self, posicao, estado_atual):
        # movimento para direita
        # Não gera se estiver na direita
        if posicao not in [2, 5, 8]:
            # peça de baixo desce
            sucessor = list(estado_atual)
            sucessor[posicao] = sucessor[posicao + 1]
            sucessor[posicao + 1] = "_"
            return (tuple(sucessor), "➡️")

    def heuristica(self, estado):
        resultado = ["1", "2", "3", "4", "5", "6", "7", "8", "_"]
        return sum(1 for i in range(len(resultado)) if resultado[i] == estado[i])

    def custo(self, estado_origem, estado_destino):
        return 1
