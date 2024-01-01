'''
Aufgabe:
Schreiben Sie einen Python-Dekorator, der die Ausführungszeit einer Funktion misst.
Der Dekorator soll die Zeit vor und nach dem Aufruf der Funktion erfassen und die Dauer der Ausführung ausgeben.

Anforderungen:

Definieren Sie einen Dekorator namens zeitmesser.
Der Dekorator soll die Zeit vor dem Aufruf der dekorierten Funktion erfassen, die Funktion ausführen, und dann die Zeit nach der Ausführung erfassen.
Berechnen Sie die Differenz zwischen den beiden Zeitpunkten, um die Ausführungsdauer der Funktion zu ermitteln.
Geben Sie die Ausführungsdauer aus.
Testen Sie den Dekorator mit einer oder mehreren Funktionen, zum Beispiel mit einer Funktion, die eine Liste von Zahlen sortiert.
'''
import time

def zeitmesser(func):
    def zeitmessung(*args):
        start = time.time()
        result = func(*args)
        ende = time.time()
        dauer = ende - start
        print(f'Die Dauer beträgt: {dauer}')
        return result
    return zeitmessung

@zeitmesser
def addiere(a, b):
    time.sleep(2)
    return a + b


ergebnis = addiere(10,5)
print(ergebnis)
