#!/bin/env python

from acora import AcoraBuilder

def transform(filename):
    with open(filename, 'r', encoding = "cp1252") as f:
        temporary = f.read()
        for i in range(0, 10):
            temporary = temporary.replace(str(i), "")
        temporary = temporary.replace(" ", "")
    return list(filter(None, temporary.split("\n")[1:]))


def buildac(keywords):
    builder = AcoraBuilder(keywords)
    return builder.build()


DDID_AC = buildac(transform('dict/DDID.txt'))
GAMUTS_AC = buildac(transform('dict/GAMUTS.txt'))


with open('reports/01.txt', 'r') as f:
    text = f.read()
    for sentence in text.split("\n"):
        print(sentence)
        print(DDID_AC.findall(sentence.replace(" ", "")))
        print(GAMUTS_AC.findall(sentence.replace(" ", "")))