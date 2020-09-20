# Inteligência Artificial
Exercícios realizados para a aula de Inteligência Artificial, do Bacharelado de Ciência da Computação

## EP 1 - O Desenvolvedor Aventureiro(Algoritmo de Busca A*)
O exercício consiste em aplicar o algoritmo de busca A*(A Estrela) em um mapa para encontrar o melhor caminho entre um ponto inicial e o ponto final. É possível se movimentar para as direções:
  - Esquerda
  - Direita
  - Cima
  - Baixo
  - Diagonal Superior Direita
  - Diagonal Superior Esquerda
  - Diagonal Inferior Direita
  - Diagonal Inferior Esquerda
  
Com esses movimentos devem ser considerados duas condições, o mapa apresentas terrenos diferentes com custos para serem atravessados e barreiras que são intransponíveis. Os Custos são:
  - Terra: 1 Ponto
  - Água: 3 Ponto
  - Areia Movediça: 6 Ponto
  - Barreira: Não pode atravessar

Para rodar o programa basta ter o Python 3 instalado em sua máquina, caso não tenha, é só acessar o link [Download Python 3](https://www.python.org/downloads/) que o download está disponível e é gratuito.

Uma vez que o Python 3 está instalado em sua máquina, basta entrar na pasta EP1 através do terminal e executar o comando:
````
python3 EP1.py
````

## EP 2 - Problema da Ladra Viajante
O exercício consiste em criar um algoritmo genético, que resolva o problema da Ladra Viajante. Esse problema é uma junção dos problemas da Mochila e do Caixeiro Viajante. A ladra deve viajar entre as cidades, sem retornar para uma cidade que ela já tenha passado (com exceção de Escondidos que é tanto a cidade inicial como a final) e roubar itens que estão disponíveis (1 item por cidade), para vendelos posteriormente. Busca-se o maior lucro possível com seus roubos, no entanto parte do desafio é que a ladra está limitada por alguns elementos, sendo eles:
  - Tamanho máximo da mochila de 20Kg
  - Custo para viajar entre as cidades($)
  - Tempo Limite de 72 horas

O algoritmo é composto por multiplas funções, sendo as principais:
  - População Inicial
  - Fitness 
  - Crossover
  - Mutation
  - Condição de Parada
  
O algoritmo fica rodando e gera multiplas gerações de resultados, em cada geração imprimimos o melhor caminho, ou seja aquele com o maior Fitness. Quando ele atinge a condição de parada, ele finaliza com o melhor caminho encontrado.
 
Para rodar o programa basta ter o Python 3 instalado em sua máquina, caso não tenha, é só acessar o link [Download Python 3](https://www.python.org/downloads/) que o download está disponível e é gratuito.

Uma vez que o Python 3 está instalado em sua máquina, basta entrar na pasta EP2 através do terminal e executar o comando:
````
python3 EP2.py
````
