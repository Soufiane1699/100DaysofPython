# Python filter() - Funktion
# Allgemeine Syntax filter(function, iterables)

zahlen = [-2, -1, 0, 1, 2, 3]
zahlen2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

positive_zahlen = filter(lambda x: x > 0, zahlen)
gerade_zahlen = filter(lambda x: x % 2 == 0, zahlen2)

print(list(gerade_zahlen))



