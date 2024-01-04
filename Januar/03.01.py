'''
Aufgabe:
Schreiben Sie ein Python-Skript, das eine Textdatei einliest, alle Wörter im Text zählt und die Anzahl jedes einzelnen Wortes in einem Dictionary speichert.
Geben Sie am Ende das Dictionary aus, das zeigt, wie oft jedes Wort im Text vorkommt.

Anforderungen:

Schreiben Sie ein Skript, das eine Textdatei öffnet und ihren Inhalt liest.
Zählen Sie die Häufigkeit jedes Wortes im Text und speichern Sie diese in einem Dictionary.
Geben Sie das Dictionary aus, in dem jedes Wort und seine Häufigkeit aufgeführt sind.

'''
from collections import defaultdict
dd = defaultdict(int)
count = 0

with open('text_03_01', 'r') as file_reader:
    for line in file_reader:
        words = line.split()
        for word in words:
            dd[word] += 1

print(dd)