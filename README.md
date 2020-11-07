# Inteligência Artificial
Exercícios realizados para a aula de Inteligência Artificial, do Bacharelado de Ciência da Computação

### :warning: Caso queira visualizar individualmente as descrições de cada EP, basta mudar para a branch desejada!

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

## EP 3 - Organização no Zoológico (Problema de Satisfação de Condições)

O exercício consiste em resolver um problema de satisfação de condições fornecido pelo professor. 

###### Enunciado
A cidade vai abrir uma nova área no zoológico com animais resgatados de um antigo circo com os seguintes animais: Leão, Antílope, Hiena, Tigre, Pavão, Suricate e Javali. Essa nova área contém 4 zonas separadas onde os animais podem ficar a vontade com cuidados, local de descanso e alimentação.
Como os animais são velhos conhecidos entre si, amizades e brigas fazem
parte do histórico. Assim, há diversas restrições entre os animais:

 1) Leão e Tigre se odeiam porque um se acha o felino mais imponente que o
outro e não querem ficar na mesma zona;
 2) Suricate e Javali são amigos de aventuras antigas na selva e quererem
ficar na mesma zona;
 3) Hiena cheira mal pela sua alimentação e apenas o Tigre dividiria a mesma
zona;
 4) Tigre gosta de carne variada e quer comer o Suricate, Javali e o Pavão;
 5) O Leão e o Tigre querem comer a Antílope. Por isso, ela não pode ficar na
    mesma zona e nem em zona adjacente;
 6) O Leão, que é muito zoeiro, perturba o Pavão por causa das suas penas e
    este não quer ficar na mesma zona do Leão;
 7) Leão ainda acha que é o rei da selva e quer ficar na zona 1 que é mais
    confortável.

Por isso, você deve fazer um sistema de satisfação de restrições para
conseguir colocar os animais nas zonas e poderem viver confortavelmente no
zoológico.

Para resolver o problema nos baseamos em um problema exemplo fornecido pelo professor onde o programa deve colorir os estados de um pais sem que estados que dividem fronteira tenham cores iguais. Utilizamos o arquivo csp desse problema como base e a partir disso criamos nosso próprio bloco de restrições e satisfações adaptados do enunciado do exercício. Uma vez que esse básico foi concluido desenvolvemos uma função que aplica uma heurística (ou otimização) no problema, foi escolhida o MCV (*Most Variable Constraints*) no qual a variavel a ser analizada e utilizada é sempre aquela que apresenta o maior número de condições limitantes.
 
Para rodar o programa basta ter o Python 3 instalado em sua máquina, caso não tenha, é só acessar o link [Download Python 3](https://www.python.org/downloads/) que o download está disponível e é gratuito.

Uma vez que o Python 3 está instalado em sua máquina, basta entrar na pasta EP3 através do terminal e executar o comando:
````
python3 EP3.py
````

No arquivo:

> csp.py

Caso queira rodar o algoritmo sem a otimização, onde ele escolhe o primeiro da lista dos não alocados para aplicar suas condições em vez do MCV, basta trocar as seguintes linhas de código:
````
# first: V = unassigned[0]
first: V = self.mcvAlgorithm(unassigned)
````
Para:
````
first: V = unassigned[0]
# first: V = self.mcvAlgorithm(unassigned)
````

## EP 4 - Naive Bayes: Classificador de emoções

O exercício consiste em desenvolver um claassificador de emoções utilizando o algoritmo de Naive Bayes.

###### Enunciado
Vamos fazer um classificador de sentimentos que classifica uma avaliação do IMDB como positiva ou negativa, baseado nos seguintes dados: [Dataset IMDB](https://www.kaggle.com/luisfredgs/imdb-ptbr). Deve-se classificar os textos em língua portuguesa.
Para este EP, deve-se usar o Naive Bayes para fazer a classificação. Recomenda-se usar a distribuição Multinomial.

Para a quebra do modelo, devemos utilizar a quebra das palavras e tratamentos como:
  - Normalizar maiúsculas e minúsculas 
  - Pontuação
  - Checar o uso de "stop words"
  
O primeiro software deverá gerar um arquivo com o modelo treinado. A execução deverá ser outro software que irá carregar este modelo e classificar de acordo com os dados de entrada.

A execução deve ter um modo teste, assim, deve-se partilhar 75% do corpus para treinamento e 25% para testagem.
  - Checar o quanto se acertou no treinamento do modelo

Para resolver o problema nos baseamos em um exemplo fornecido pelo professor onde utilizando o Python eram realizadas diversos tipos de formatação e restrições em strings para deixá-las prontas para o treinamento. Assim como uma demonstração de como obter a porcentagen de uma palavra aparecer na frase.
Para ler o dataset disponibilizado utilizamos a library csv através de uma importação. Isso, junto com nossa utilizaão de dicionários facilitou o processo e de obtenção e checagem de dados.
Os dados do dataset vinham estruturados de maneira que:
  - 1˚Coluna: tinha um inteiro como id
  - 2˚Coluna: tinha uma frase em inglês
  - 3˚Coluna: tinha a mesa frase, só que traduzida para o português Brasileiro
  - 4˚Coluna: apresentava o identificador de emoção, dividido em pos(positivo) e neg(negativo)
  
Uma vez que obtivemos esses dados dividimos o dataset pelo identificador obtendo um csv com apenas positivos e um csv com apenas negativos. Depois, retiremos a 1˚,2˚ e 4˚ colunas que eram desnecessárias e começamos a manipular as frases.

Igualamos todas as letras para lowercase e separamos a pontuação das frases. Retiramos palavras que são consideradas como stopwords e calculamos o numero de palavras positivas e negativas. Separamos o dataset em 75% para treinamento e 25% para teste. Com isso a fase de treinamento de um modelo estava concluida.

Depois desse processo criamos uma função teste que recebe uma string de texto e um booleano indicativo se essa string é positiva ou negativa(esse booleano não interfere na identificação da emoção da frase, serve apenas para obter a precisão e recall, uma vez que precisamos saber se os é uma classificação correta ou errada). Nessa função calculamos o total positivo e o total negativo da frase, baseado nas palavras que ela apresenta. Uma vez que obtemos esses totais comparamos os dois e aquele que for maior define se o sentimento da frase é positivo ou negativo.

Agora que temos nosso modelo e a função de teste baseada nesse modelo, é necessário validar a funcionalidade dele e para isso usamos o método de Precisão e Recall através de uma função chamada classify. Aplicamos a fórmula de precisão e a fórmula de recall, que são: 
 - Precisão: Verdadeiro Positivo / (Verdadeiro Positivo + Falso Positivo)
 - Recall: Verdadeiro Positivo / (Verdadeiro Positivo + Falso Negativo)
 
 Uma vez que obtemos essa classificação do modelo, nosso programa termina.
 
Para rodar o programa basta ter o Python 3 instalado em sua máquina, caso não tenha, é só acessar o link [Download Python 3](https://www.python.org/downloads/) que o download está disponível e é gratuito.

Uma vez que o Python 3 está instalado em sua máquina, basta entrar na pasta EP4 através do terminal e executar o comando:
````
python3 EP4.py
````

No arquivo:

> Ep4.py

Caso queira retreinar o modelo do classificador, basta trocar as seguintes linhas de código:
````
def __init__(self):
        self.createDataset()
        # self.train()
        self.loadModel()
        self.classify()
````
Para:
````
def __init__(self):
        self.createDataset()
        self.train()
        # self.loadModel()
        # self.classify()
````
Depois de feito isso programa se encerrará com o modelo retreinado. Substitua de volta para utilizar esse modelo criado.
