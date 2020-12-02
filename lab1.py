import csv
import re

symbols = 0
spaces = 0
punctuation_symbols = 0

words = 0
sentences = 0

with open('steam_description_data.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        string = ','.join(row)

        symbols += len(string)

        spaces += string.count(' ')

        punctuation_symbols += string.count('.') + string.count(',') + string.count('!') + string.count('?')

        punctuation_symbols += string.count('\"') + string.count('\'') + string.count(':') + string.count(';')

        punctuation_symbols += string.count('-') + string.count('(') + string.count(')')

        words += len(re.findall(r"(\w+'\w+)|(\w+-\w+'\w+)|(\w+-\w+'\w)|\w+", string))
        sentences += len(re.findall(r"([A-Z][^\.!?]*[\.!?])", string))

print("Количество символов:", symbols)
print("Количество символов без пробелов:", symbols - spaces)
print("Количество символов без знаков препинания:", symbols - punctuation_symbols)
print("Количество слов:", words)
print("Количество предложений:", sentences)