import sys

searcharray = list()
fname = "wordsearch1.txt"
with open(fname) as f:
    rows = f.readlines()
    print(rows)
    for line in rows:
        searcharray.append(list(line.strip()))
