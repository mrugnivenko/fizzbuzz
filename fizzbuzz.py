import re

def is_5(chislo1):
    chislo = str(chislo1)
    if chislo[-1] == '5' or chislo[-1] == '0':
        return True
    else:
        return False

def is_3(chislo1):
    chislo = str(chislo1)
    summ = 0
    for simvol in chislo:
        summ += int(simvol)
    if summ == 0 or summ == 3 or summ == 6 or summ == 9:
        return True
    elif summ == 1 or summ == 2 or summ == 4 or summ == 5 or summ == 7 or summ == 8:
        return False
    else:
        return is_3(summ)

def is_3_or_5(chislo1):
    if is_3(chislo1) and is_5(chislo1):
        return True
    else:
        return False

def func(posl):
    posl.split()
    length = len(posl)
    for i in range(length):
        if is_3_or_5(posl[i]):
            posl[i] = 'fizzbuzz'
        elif is_3(posl[i]):
            posl[i] = 'fizz'
        elif is_5(posl[i]):
            posl[i] = 'buzz'
    s = ''
    for i in range(length):
        s += str(posl[i]) + ' ' 
    return s 
