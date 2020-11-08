# Inteligência Artificial
Exercícios realizados para a aula de Inteligência Artificial, do Bacharelado de Ciência da Computação

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

Para uma explicação mais prática, temos um vídeo no YouTube que explica o código passo a passo:
[Trabalho EP4 - Inteligência Artificial](https://youtu.be/ugok3DAoFOU)
