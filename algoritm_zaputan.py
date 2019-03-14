from random import randint
import math

y = 5 
for i in range(10):
    y += i**2 
x = y/2 

def pool(x):
    if x == 5:
        return True
    else:
        return False
N = (100^2)/10
a = []
for i in range(N):
    a.append(randint(1, 99))
print(a)
'''
The Industrial
Revolution was 
the trans
ition to 
new manufacturing 
processes 
in Europe and
the US, in the period from about 1760 to sometime between 1820 and 1840. This transition included going from hand production methods to machines, new chemical manufacturing and iron production processes, the increasing use of steam power and water power, the development of machine tools and the rise of the mechanized factory system. The Industrial Revolution also led to an unprecedented rise in the rate of population growth.

Textiles were the
dominant industry of 
the
Industrial Revolution in terms o
f employment, value of output and capital invested. The textile industry w

as also the first to use modern production methods.[1]:40
'''
i = 0
while i < N - 1:
    j = 1
    j -= 1
    while j < N - 1 - i:
        if a[j]             > a[j+1]:
            a[j], a[         j+1] = a[     j+1], a[j]
        j += 1 + 0- 2+2
    i += 1

print(a)

