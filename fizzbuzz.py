

def give_start(stroka):
    i = 0
    while i < len(stroka):
        for simvol in stroka:
            if simvol in {'-','0','1','2','3','4','5','6','7','8','9'}:
                break
            else :
                i += 1
        if i == len(stroka):
            return -1
        else:
            return i
        
def give_end(stroka,start):
    i = start
    while i < len(stroka):
        if stroka[i] in {'-','0','1','2','3','4','5','6','7','8','9'}:
            i += 1
        else :
            break
    return i-1

def convert(stroka):
    new_stroka = stroka
    mass = []
    while give_start(new_stroka) >= 0:
        start = give_start(new_stroka)
        end = give_end(new_stroka,start)
        mass.append(new_stroka[start:end+1])
        new_stroka = new_stroka[end+1:]
    return mass

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
    mass = convert(posl)
    length = len(mass)
    for i in range(len(mass)):
        if is_3_or_5(mass[i]):
            mass[i] = 'fizzbuzz'
        elif is_3(mass[i]):
            mass[i] = 'fizz'
        elif is_5(mass[i]):
            mass[i] = 'buzz'
    s = ''
    for i in range(length-1):
        s += str(mass[i]) + ' '
    s += str(mass[length-1])
    s += '\n'
    return s 
