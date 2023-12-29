def fibonacci_rekursion(zahl):
    if zahl == 1:
        return 1
    elif zahl == 0:
        return 0
    else:
        return fibonacci_rekursion(zahl - 1) + fibonacci_rekursion(zahl - 2)