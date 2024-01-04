'''
Aufgabe:
Erstellen Sie ein Python-Skript, das eine Liste von Tupeln hat, wobei jedes Tupel zwei Elemente enthält (zum Beispiel Name und Alter).
Verwenden Sie eine Lambda-Funktion, um die Liste nach dem zweiten Element jedes Tupels (in diesem Fall dem Alter) zu sortieren.

Anforderungen:

Definieren Sie eine Liste von Tupeln, wobei jedes Tupel zwei Elemente (zum Beispiel Name und Alter) enthält.
Verwenden Sie die Funktion sorted() zusammen mit einer Lambda-Funktion, um die Liste basierend auf dem Alter zu sortieren.
Geben Sie die sortierte Liste aus.

'''

liste = [('Max', 20), ('Anna', 30), ('Erik', 25)]

sortierte_liste = sorted(liste, key=lambda x: x[1])
print(sortierte_liste)
