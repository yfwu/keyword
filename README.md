# Keyword

## Build the dictionary

``` bash
awk -F "\"*,\"*" '{print $2}' DDID.csv | grep -v "DOID" > DDID.txt
awk -F "\"*,\"*" '{print $2}' GAMUTS.csv > GAMUTS.txt
```

This two steps created two txt file which contains the preferred terms. Then we can use the ``build`` function to create two list for further Acora algorithm.

The ``build`` function turned the txt file into a list, and filter out empty string and useless numbers.

## Text search

We use the ``Acora`` module, which is based on the Aho-Corasick algorithm.yu