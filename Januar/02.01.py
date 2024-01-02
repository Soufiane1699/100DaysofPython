'''
Aufgabe:
Erstellen Sie ein Python-Skript, das eine Liste von Zahlen mit einer Lambda-Funktion filtert, um nur gerade Zahlen zu behalten.

Anforderungen:

Erstellen Sie eine Liste von Zahlen, sowohl gerade als auch ungerade.
Verwenden Sie die filter()-Funktion zusammen mit einer Lambda-Funktion, um nur die geraden Zahlen aus Ihrer Liste zu extrahieren.
Konvertieren Sie das Ergebnis in eine Liste und geben Sie es aus.

filter(function, iterable)

'''

liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
gerade_liste = []

gerade = lambda x: x % 2 == 0

gerade_liste_filter = filter(gerade, liste)

for element in gerade_liste_filter:
    gerade_liste.append(element)


print(gerade_liste)
