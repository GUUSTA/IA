# Inteligência Artificial
Exercícios realizados para a aula de Inteligência Artificial, do Bacharelado de Ciência da Computação

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
Pronto, o código deve estar rodando 100%.

Para uma explicação mais prática, temos um vídeo no YouTube que explica o código passo a passo:
[Trabalho EP2 - Inteligência Artificial](https://youtu.be/t59NHmwfkk0)
