import csv
import re
import math
import csv
from collections import Counter
from CsvHandler import *


class EP4:
    stopwords = ["de", "a", "o", "que", "e", "do", "da", "em", "um", "para", "é", "com", "não", "uma", "os", "no", "se", "na", "por", "mais", "as", "dos", "como", "mas", "foi", "ao", "ele", "das", "tem", "à", "seu", "sua", "ou", "ser", "quando", "muito", "há", "nos", "já", "está", "eu", "também", "só", "pelo", "pela", "até", "isso", "ela", "entre", "era", "depois", "sem", "mesmo", "aos", "ter", "seus", "quem", "nas", "me", "esse", "eles", "estão", "você", "tinha", "foram", "essa", "num", "nem", "suas", "meu", "às", "minha", "têm", "numa", "pelos", "elas", "havia", "seja", "qual", "será", "nós", "tenho", "lhe", "deles", "essas", "esses", "pelas", "este", "fosse", "dele", "tu", "te", "vocês", "vos", "lhes", "meus", "minhas" "teu", "tua", "teus", "tuas", "nosso", "nossa", "nossos", "nossas", "dela", "delas", "esta", "estes", "estas", "aquele", "aquela", "aqueles", "aquelas", "isto", "aquilo", "estou", "está", "estamos", "estão", "estive", "esteve", "estivemos", "estiveram", "estava",
                 "estávamos", "estavam", "estivera", "estivéramos", "esteja", "estejamos", "estejam", "estivesse", "estivéssemos", "estivessem", "estiver", "estivermos", "estiverem", "hei", "há", "havemos", "hão", "houve", "houvemos", "houveram", "houvera", "houvéramos", "haja", "hajamos", "hajam", "houvesse", "houvéssemos", "houvessem", "houver", "houvermos", "houverem", "houverei", "houverá", "houveremos", "houverão", "houveria", "houveríamos", "houveriam", "sou", "somos", "são", "era", "éramos", "eram", "fui", "foi", "fomos", "foram", "fora", "fôramos", "seja", "sejamos", "sejam", "fosse", "fôssemos", "fossem", "for", "formos", "forem", "serei", "será", "seremos", "serão", "seria", "seríamos", "seriam", "tenho", "tem", "temos", "tém", "tinha", "tínhamos", "tinham", "tive", "teve", "tivemos", "tiveram", "tivera", "tivéramos", "tenha", "tenhamos", "tenham", "tivesse", "tivéssemos", "tivessem", "tiver", "tivermos", "tiverem", "terei", "terá", "teremos", "terão", "teria", "teríamos", "teriam"]
    allPositives = []
    allNegatives = []
    trainablePositiveItems = []
    trainableNegativeItems = []
    testablePositiveItems = []
    testableNegativeItems = []

    positiveWords = {}
    negativeWords = {}
    totalValues = []

    verifiedPositives = 0
    verifiedNegatives = 0

    def __init__(self):
        self.createDataset()
        # self.train()
        self.loadModel()
        self.classify()
        # self.test("O filme é um espetáculo visual! Fui assisti desprendido do original e deixei fluir, isso me proporcionou aproveitar e se surpreender com o novo Rei Leão. Claro que comparações são inevitáveis, ainda mais pra quem é fã do de 1994, mas esse tem algumas cenas diferentes e respeita bem a história do anterior. Filmaço!! Não tem como não se emocionar. A história por si só já é uma obra de arte. Nota 10!", True)

    def loadModel(self):
        self.positiveWords = readWordsFile("EP4/positives.csv")
        self.negativeWords = readWordsFile("EP4/negatives.csv")
        self.totalValues = readWordsFile("EP4/wordsValues.csv")

    def formatText(self, array):
        normalized = [str.lower(item) for item in array]
        splitted = [re.findall(r"[\w']+|[,.!?;]", item) for item in normalized]
        counted = [Counter(item) for item in splitted]
        summed = Counter({})
        for item in counted:
            summed += Counter(item)

        return summed

    def createDataset(self):
        print("Opening file: EP4/imdb-reviews-pt-br.csv")
        with open('EP4/imdb-reviews-pt-br.csv', mode='r') as csvfile:
            reader = csv.reader(csvfile)
            skip = True
            print("Creating dataset")
            for item in reader:
                if skip:
                    skip = False
                    continue
                newItem = item
                newItem.pop(1)
                newItem.pop(0)
                if newItem[-1] == "neg":
                    self.allNegatives.append(newItem[0])
                elif newItem[-1] == "pos":
                    self.allPositives.append(newItem[0])

            print("\nAll Negatives items: \n")
            print(len(self.allNegatives))
            print("\nAll Positives items\n")
            print(len(self.allPositives))

            self.trainablePositiveItems = self.allPositives[:18520]
            self.trainableNegativeItems = self.allNegatives[:18573]
            self.testablePositiveItems = self.allPositives[18520:]
            self.testableNegativeItems = self.allNegatives[18573:]

    def train(self):

        print("Training dataset")

        print("Formatting training dataset")
        negatives = self.formatText(self.trainableNegativeItems)
        positives = self.formatText(self.trainablePositiveItems)

        print("Remove stopwords from training dataset")
        for word in self.stopwords:
            if negatives[word] > 0:
                del negatives[word]
            if positives[word] > 0:
                del positives[word]

        print("Calculate the number of positives words and negatives words from training dataset")
        totalPositives = 0
        totalNegatives = 0
        for value in positives.values():
            totalPositives += value

        for value in negatives.values():
            totalNegatives += value

        print("Write Model")
        totalValues = {totalPositives: len(
            positives), totalNegatives: len(negatives)}
        writeWordValueFile(totalValues)
        writePositiveFile(positives)
        writeNegativeFile(negatives)
        print("Training completed")

    def formatForTest(self, text):
        normalized = str.lower(text)
        splitted = re.findall(r"[\w']+|[,.!?;]", normalized)
        return splitted

    def test(self, text, positives):
        numberOfPositiveSentence = 24694
        numberOfNegativeSentence = 24765
        formattedText = self.formatForTest(text)
        totalPositivo = 0.0
        first = True
        for word in formattedText:
            if first:
                totalPositivo += math.log((numberOfPositiveSentence / (
                    numberOfNegativeSentence + numberOfPositiveSentence)), 10)
                first = False
                continue
            wordCount = self.positiveWords[word] if word in self.positiveWords.keys(
            ) else 0
            totalPositivo += math.log(((int(wordCount) + 1) / (int(self.totalValues['positiveTotalWords']) + int(
                self.totalValues['positiveWordsAmount']) + int(self.totalValues['negativeWordsAmount']))), 10)
        # print("%.10f" % totalPositivo)

        totalNegativo = 0.0
        first = True
        for word in formattedText:
            if first:
                totalNegativo += math.log((numberOfNegativeSentence / (
                    numberOfNegativeSentence + numberOfPositiveSentence)), 10)
                first = False
                continue
            wordCount = self.negativeWords[word] if word in self.negativeWords.keys(
            ) else 0
            totalNegativo += math.log(((int(wordCount) + 1) / (int(self.totalValues['negativeTotalWords']) + int(
                self.totalValues['negativeWordsAmount']) + int(self.totalValues['positiveWordsAmount']))), 10)
        # print("%.10f" % totalNegativo)

        if totalPositivo > totalNegativo and positives:
            self.verifiedPositives += 1
        elif totalNegativo > totalPositivo and positives:
            self.verifiedNegatives += 1
        elif totalPositivo > totalNegativo and not positives:
            self.verifiedPositives += 1
        elif totalNegativo > totalPositivo and not positives:
            self.verifiedNegatives += 1

        print()
        if positives:
            temp = len(self.testablePositiveItems)
            print("{} out of {} positives".format(self.verifiedPositives,
                                                  temp))
            print("{} negatives out of {} positives".format(
                self.verifiedNegatives, temp))
        else:
            temp = len(self.testableNegativeItems)
            print("{} out of {} negatives".format(self.verifiedNegatives,
                                                  temp))
            print("{} positives out of {} negatives".format(
                self.verifiedPositives, temp))
        print("Resultado: %s" %
              ("positivo" if totalPositivo > totalNegativo else "negativo"))

    def classify(self):
        for text in self.testablePositiveItems:
            self.test(text, True)

        percentageP = self.verifiedPositives/len(self.testablePositiveItems)
        positiveResult = {"verdadeiroPositivo": self.verifiedPositives, "falsoNegativo": self.verifiedNegatives, "percentage": percentageP}

        self.verifiedPositives = 0
        self.verifiedNegatives = 0

        for text in self.testableNegativeItems:
            self.test(text, False)

        percentageN = self.verifiedNegatives/len(self.testableNegativeItems)
        negativeResult = {"falsoPositivo": self.verifiedPositives, "verdadeiroNegativo": self.verifiedNegatives, "percentage": percentageN}
        print()
        print("=-"*50)
        print()
        print("FRASES POSITIVAS")
        print("Porcentagem de Positivos: {:.2f}%".format(positiveResult["percentage"]*100))
        print("Porcentagem de Falsos Negativos: {:.2f}%".format(
            (1 - positiveResult["percentage"])*100))

        print()
        print("FRASES NEGATIVAS")
        print("Porcentagem de Negativos: {:.2f}%".format(negativeResult["percentage"]*100))
        print("Porcentagem de Falsos Positivos: {:.2f}%".format(
            (1 - negativeResult["percentage"])*100))
        
        print("\nPrecisão Positivos: {:.2f}".format((positiveResult["verdadeiroPositivo"] / (positiveResult["verdadeiroPositivo"] + negativeResult["falsoPositivo"]))))
        print("Recall Positivos: {:.2f}".format((positiveResult["verdadeiroPositivo"] / (positiveResult["verdadeiroPositivo"] + positiveResult["falsoNegativo"]))))

        print("\nPrecisão Negativos: {:.2f}".format((negativeResult["verdadeiroNegativo"] / (negativeResult["verdadeiroNegativo"] + positiveResult["falsoNegativo"]))))
        print("Recall Negativos: {:.2f}".format((negativeResult["verdadeiroNegativo"] / (negativeResult["verdadeiroNegativo"] + negativeResult["falsoPositivo"]))))


ep4 = EP4()
