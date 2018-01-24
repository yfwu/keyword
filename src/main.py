#!/bin/env python

from acora import AcoraBuilder
from functools import reduce

def transform(filename):
    with open(filename, 'r', encoding = "cp1252") as f:
        temporary = f.read()
        for i in range(0, 10):
            temporary = temporary.replace(str(i), "")
        temporary = temporary.replace(" ", "")
    return list(filter(None, temporary.split("\n")[1:]))


DDID = transform("dict/DDID.txt")
DDID_builder = AcoraBuilder(DDID)
DDID_AC = DDID_builder.build()

GAMUTS = transform('dict/GAMUTS.txt')
GAMUTS_builder = AcoraBuilder(GAMUTS)
GAMUTS_AC = GAMUTS_builder.build()


with open('reports/01.txt', 'r') as f:
    text = f.read()
    for sentence in text.split("\n"):
        print(sentence)
        print(DDID_AC.findall(sentence.replace(" ", "")))
        print(GAMUTS_AC.findall(sentence.replace(" ", "")))