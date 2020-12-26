import csv
import re

all_symb = 0
spaces = 0
punct = 0
sentences = 0
words = 0
header_symb = []

f = open("steam_description_data.csv", encoding="utf-8")
csv_reader = csv.reader(f)
for line in csv_reader:
    symb = ",".join(line)
    all_symb += len(symb)
    spaces += symb.count(" ")
    punct += symb.count(".") + symb.count(",") + symb.count("?") + symb.count("(") + symb.count(")") + symb.count(";") + symb.count("-") + symb.count("_") + symb.count(":") + symb.count("/") + symb.count("\'") + symb.count("\"")
    words += len(re.findall(r"(\w+'\w+)|(\w+-\w+'\w+)|(\w+-\w+'\w)|\w+", symb))
    sentences += len(re.findall(r"([A-Z][^\.!?]*[\.!?])", symb))
    header_symb += re.findall(r'<h1>(.*?)</h1>', str(line))
print("Число символов:", all_symb)
print("Число символов без пробелов:", all_symb - spaces)
print("Количество символов без знаков препинания:", all_symb - punct)
print("Количество слов:", words)
print("Количество предложений:", sentences)
print("Количество символов в заголовках первого уровня:",len(str(header_symb)))
f.close()