import csv

def readWordsFile(file):
    with open(file, mode='r') as csvfile:
        reader = csv.reader(csvfile)
        skip = True
        words = {}
        for item in reader:
            if skip:
                skip = False
                continue
            words[item[0]] = item[1]
        return words

def writeNegativeFile(dict):
    with open('EP4/negatives.csv', mode='w') as csv_file:
        fieldnames = ['word', 'negative_count']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for key, value in dict.items():
            writer.writerow({'word': key, 'negative_count': value})

def writePositiveFile(dict):
    with open('EP4/positives.csv', mode='w') as csv_file:
        fieldnames = ['word', 'positive_count']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for key, value in dict.items():
            writer.writerow({'word': key, 'positive_count': value})

def writeWordValueFile(dict):
    with open('EP4/wordsValues.csv', mode='w') as csv_file:
        fieldnames = ['word_total_count', 'words_amount']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for key, value in dict.items():
            writer.writerow({'word_total_count': key, 'words_amount': value})