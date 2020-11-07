# Inteligência Artificial
Exercícios realizados para a aula de Inteligência Artificial, do Bacharelado de Ciência da Computação

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

Para resolver o problema nos baseamos em um problema exemplo fornecido pelo professor onde o programa deve ccolorir os estados de um pais sem que estados que dividem fronteira tenham cores iguais. Utilizamos o arquivo csp desse problema como base e a partir disso criamos nosso próprio bloco de restrições e satisfações adaptados do enunciado do exercício. Uma vez que esse básico foi concluido desenvolvemos uma função que aplica uma heurística (ou otimização) no problema, foi escolhida o MCV (*Most Variable Constraints*) no qual a variavel a ser analizada e utilizada é sempre aquela que apresenta o maior número de condições limitantes.
 
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
Para uma explicação mais prática, temos um vídeo no YouTube que explica o código passo a passo:
[Trabalho EP3 - Inteligência Artificial](https://youtu.be/IG2jiuGAzGA)
