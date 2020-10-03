import string
import re

marks_list = list(string.punctuation)
spaces_amount = 0
punctuation_amount = 0

all_letter_amount = 0
letter_amount_without_spaces = 0
words_amount = 0
sentences_amount = 0

with open('steam_description_data.csv', encoding='utf-8') as f:
    for line in f:
        all_letter_amount += len(line)
        spaces_amount += line.count(' ')
        words_amount += len(line.split())
        for mark in marks_list:
            punctuation_amount += line.count(mark)
        sentences_amount += len(re.findall(r"([A-Z][^\.!?]*[\.!?])", line))


letter_amount_without_spaces = all_letter_amount - spaces_amount
letter_amount_without_punctuation = letter_amount_without_spaces - punctuation_amount

print("Всего символов: ", all_letter_amount, "\n",
      "Символов без пробелов: ", letter_amount_without_spaces, "\n",
      "Символов без пунктуации: ", letter_amount_without_punctuation, "\n",
      "Всего слов: ", words_amount, "\n",
      "Всего предложений: ", sentences_amount)



