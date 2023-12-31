'''
Aufgabe:
Erstellen Sie ein Python-Skript, das ein Dictionary mit mehreren Schlüssel-Wert-Paaren enthält.
Konvertieren Sie dieses Dictionary in einen JSON-String und speichern Sie diesen in einer Datei.
Lesen Sie anschließend die Datei und konvertieren Sie den JSON-String zurück in ein Python-Dictionary.

Definieren Sie ein Dictionary mit einigen Schlüssel-Wert-Paaren in Python.
Verwenden Sie das json-Modul, um das Dictionary in einen JSON-String zu konvertieren.
Schreiben Sie diesen JSON-String in eine Datei.
Lesen Sie die Datei, extrahieren Sie den JSON-String und konvertieren Sie ihn zurück in ein Python-Dictionary.
Vergleichen Sie das ursprüngliche Dictionary mit dem aus der Datei gelesenen Dictionary, um sicherzustellen, dass die Konvertierung korrekt war.
'''
import json
schueler_noten = {
    "Max": 92,
    "Anna": 88,
    "Erik": 75,
    "Sophie": 93
}
schueler_noten_json = json.dumps(schueler_noten)

with open('text.json', 'w') as file_write:
    file_write.write(schueler_noten_json)

with open('text.json', 'r') as file_read:
    read_file = file_read.readline()
    d = json.loads(read_file)




