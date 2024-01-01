'''
Aufgabe:
Erstellen Sie einen Python-Dekorator, der jedes Mal, wenn eine Funktion aufgerufen wird, eine Log-Nachricht ausgibt.
Der Dekorator soll den Namen der Funktion und die übergebenen Argumente in der Log-Nachricht anzeigen.

Anforderungen:

Definieren Sie einen Dekorator namens log_funktionsaufruf.
Dieser Dekorator soll vor dem Aufruf der dekorierten Funktion eine Nachricht ausgeben, die den Namen der Funktion und die übergebenen Argumente enthält.
Die Funktion selbst soll dann wie üblich ausgeführt werden.
Testen Sie den Dekorator mit mindestens einer Funktion, die unterschiedliche Argumente akzeptiert.
'''
import logging


'''
level=logging.INFO -> der Parameter der das Logging-Level festlegt
format='%(message)s' -> bestimmt das Format der Log-Nachricht
'''
logging.basicConfig(level=logging.INFO, format='%(message)s')
def log_funktionsaufruf(func):
    def wrapper(*args):
        result = func(*args)
        logging.info(f'Die Funktion lautet: {func.__name__} mit Argumenten {args}')
        return result
    return wrapper


@log_funktionsaufruf
def addiere(a, b):
    return a + b


ergebnis = addiere(2, 3)
print(ergebnis)