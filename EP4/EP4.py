import csv
import re


class EP4:

    dataset = {}
    stopwords = ["de", "a", "o", "que", "e", "do", "da", "em", "um", "para", "é", "com", "não", "uma", "os", "no", "se", "na", "por", "mais", "as", "dos", "como", "mas", "foi", "ao", "ele", "das", "tem", "à", "seu", "sua", "ou", "ser", "quando", "muito", "há", "nos", "já", "está", "eu", "também", "só", "pelo", "pela", "até", "isso", "ela", "entre", "era", "depois", "sem", "mesmo", "aos", "ter", "seus", "quem", "nas", "me", "esse", "eles", "estão", "você", "tinha", "foram", "essa", "num", "nem", "suas", "meu", "às", "minha", "têm", "numa", "pelos", "elas", "havia", "seja", "qual", "será", "nós", "tenho", "lhe", "deles", "essas", "esses", "pelas", "este", "fosse", "dele", "tu", "te", "vocês", "vos", "lhes", "meus", "minhas" "teu", "tua", "teus", "tuas", "nosso", "nossa", "nossos", "nossas", "dela", "delas", "esta", "estes", "estas", "aquele", "aquela", "aqueles", "aquelas", "isto", "aquilo", "estou", "está", "estamos", "estão", "estive", "esteve", "estivemos", "estiveram", "estava", "estávamos", "estavam", "estivera", "estivéramos", "esteja", "estejamos", "estejam", "estivesse","estivéssemos", "estivessem", "estiver","estivermos","estiverem", "hei", "há", "havemos", "hão", "houve", "houvemos", "houveram","houvera","houvéramos","haja", "hajamos","hajam", "houvesse","houvéssemos", "houvessem", "houver", "houvermos", "houverem", "houverei", "houverá", "houveremos", "houverão", "houveria", "houveríamos", "houveriam", "sou", "somos", "são", "era", "éramos", "eram", "fui", "foi","fomos", "foram", "fora","fôramos","seja","sejamos", "sejam","fosse","fôssemos", "fossem", "for", "formos", "forem", "serei", "será", "seremos", "serão", "seria","seríamos","seriam","tenho","tem","temos","tém","tinha","tínhamos", "tinham", "tive","teve", "tivemos", "tiveram", "tivera", "tivéramos", "tenha", "tenhamos", "tenham", "tivesse", "tivéssemos", "tivessem", "tiver", "tivermos", "tiverem", "terei", "terá", "teremos", "terão", "teria", "teríamos", "teriam"]    
    mockup = [["Mais uma vez, o Sr. Costner arrumou um filme por muito mais tempo do que o necessário. Além das terríveis seqüências de resgate no mar, das quais há muito poucas, eu simplesmente não me importei com nenhum dos personagens. A maioria de nós tem fantasmas no armário, e o personagem Costers é realizado logo no início, e depois esquecido até muito mais tarde, quando eu não me importava. O personagem com o qual deveríamos nos importar é muito arrogante e superconfiante, Ashton Kutcher. O problema é que ele sai como um garoto que pensa que é melhor do que qualquer outra pessoa ao seu redor e não mostra sinais de um armário desordenado. Seu único obstáculo parece estar vencendo Costner. Finalmente, quando estamos bem além do meio do caminho, Costner nos conta sobre os fantasmas dos Kutchers. Somos informados de por que Kutcher é levado a ser o melhor sem pressentimentos ou presságios anteriores. Nenhuma mágica aqui, era tudo que eu podia fazer para não desligar uma hora.", "neg"],
              ["Este é um exemplo do motivo pelo qual a maioria dos filmes de ação são os mesmos. Genérico e chato, não há nada que valha a pena assistir aqui. Um completo desperdício dos talentos de Ice-T e Cubo de Gelo que foram mal aproveitados, cada um comprovando que são capazes de atuar e agir bem. Não se incomode com este, vá ver New Jack City, Ricochet ou assistir New York Undercover para Ice-T, ou Boyz no Hood, Higher Learning ou Friday for Ice Cube e ver o negócio real. Ice-Ts horrivelmente clichê diálogo sozinho faz este filme ralar os dentes, e eu ainda estou me perguntando o que diabos Bill Paxton estava fazendo neste filme? E por que diabos ele sempre interpreta exatamente o mesmo personagem? Dos extraterrestres em diante, todos os filmes que eu vi com Bill Paxton o fizeram interpretar exatamente o mesmo personagem irritante, e pelo menos em Aliens seu personagem morreu, o que o tornou um pouco gratificante ... No geral, esse é lixo de ação de segunda classe. Existem incontáveis ​​filmes melhores para ver, e se você realmente quiser ver esse filme, assista a Judgment Night, que é praticamente uma cópia carbono, mas tem melhor atuação e um roteiro melhor. A única coisa que fez isso valer a pena assistir foi uma mão decente na câmera - a cinematografia era quase refrescante, o que chega perto de compensar o horrível filme em si - mas não é bem assim. 4/10", "neg"],
              ["Eu fui e vi este filme ontem à noite depois de ser persuadido por alguns amigos meus. Eu admitiria que estava relutante em vê-lo porque, pelo que eu sabia de Ashton Kutcher, ele só conseguia fazer comédia. Eu estava errado. Kutcher interpretou o personagem de Jake Fischer muito bem, e Kevin Costner interpretou Ben Randall com tal profissionalismo. O sinal de um bom filme é que ele pode brincar com nossas emoções. Este fez exatamente isso. Todo o teatro que foi vendido foi superado pelo riso durante a primeira metade do filme, e foi levado às lágrimas durante o segundo semestre. Ao sair do teatro, eu não só vi muitas mulheres em lágrimas, mas também muitos homens adultos, tentando desesperadamente não deixar ninguém vê-los chorando. Este filme foi ótimo, e eu sugiro que você vá vê-lo antes de julgar.", "pos"],
              ["O diretor do ator, Bill Paxton, segue sua promissora estréia, o horror gótico ""Frailty"", com este drama esportivo familiar sobre o Aberto dos EUA de 1913, onde um jovem caddie americano se eleva de sua humilde experiência para jogar contra seu ídolo britânico no que foi apelidado de como ""o maior jogo já jogado."" Eu não sou fã de golfe, e esses filmes divertidos são uma dúzia de dúzias feitas recentemente com grande sucesso com ""Miracle"" e ""Cinderella Man"", mas de alguma forma esse filme era fascinante mesmo assim. O filme começa com alguns criativos. os créditos de abertura imaginam uma versão Disneyfied dos créditos de abertura animados de HBO ""Carnivale"" e ""Roma"", mas vagueiam lentamente lentamente para sua primeira hora por números. Uma vez que a ação se move para os EUA, as coisas abertas se encaixam muito bem. Paxton faz um bom trabalho e mostra um talento especial para floreios de diretoria eficazes. Adorei a montagem encharcada de chuva da ação no segundo dia do evento que impulsionou ainda mais o enredo ou acrescentou alguma profundidade psicológica inesperada ao processo. Há um desenvolvimento de caráter convincente quando o britânico Harry Vardon é assombrado por imagens de aristocratas de ternos pretos e cartolas que destruíram sua casa de família quando criança para abrir caminho para um campo de golfe. Ele também faz um bom trabalho de descrever visualmente o que se passa nas cabeças dos jogadores sob pressão. O golfe, um esporte dolorosamente entediante, é trazido vivo aqui. O crédito também deve ser dado aos cenógrafos e departamento de figurinos para criar uma envolvente atmosfera de período de Londres e Boston no início do século XX. Você sabe como isso vai acabar não só porque é baseado em uma história real, mas também porque os filmes desse gênero seguem o mesmo modelo várias vezes, mas Paxton faz um show melhor que a média e talvez indique mais talento por trás da câmera do que ele já teve na frente dela. Apesar da natureza estereotipada, este é um filme agradável e fácil de criar, que merece encontrar um público.", "pos"]]

    def __init__(self):
        self.createDataset()
    
    def separateClass(self, dataset):
        separated = dict()
        for i in range(len(dataset)):
            vector = dataset[i]
            class_value = vector[-1]
            if (class_value not in separated):
                separated[class_value] = list()
            separated[class_value].append(vector[0])
        return separated

    def formatText(self, array):
        normalized = [str.lower(item) for item in array]
        splitted = [re.findall(r"[\w']+", item) for item in normalized]

        return splitted

    def createDataset(self):
        with open('EP4/imdb-reviews-pt-br.csv', mode='r') as csvfile:
            reader = csv.reader(csvfile)
            index = 0
            skip = True
            justPTBR = []
            for item in reader:
                if skip:
                    skip = False
                    continue
                newItem = item
                newItem.pop(1)
                newItem.pop(0)
                justPTBR.append(newItem)
                if index == 4:
                    break
                else:
                    index += 1

            index = 0
            for item in justPTBR:
                self.dataset[index] = item
                index += 1
            # print(self.dataset)

            separatedDict = self.separateClass(self.mockup)
            negatives = separatedDict['neg']
            positives = separatedDict['pos']

            negatives = self.formatText(negatives)
            positives = self.formatText(positives)

            print("NEGATIVES")
            print(negatives)
            print("POSITIVES")
            print(positives)


ep4 = EP4()
