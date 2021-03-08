from math import sqrt

n = int(input('Podaj n:'))

pierwiastek = 1
kwadrat = int(sqrt(n))

if (kwadrat * kwadrat) != n:
    print('Nie ma kwadratu')
else:
    while (pierwiastek * pierwiastek) != n:
        pierwiastek = pierwiastek + 1  
    print(pierwiastek,'*',pierwiastek)