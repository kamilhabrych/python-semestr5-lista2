n = int(input('Podaj n:'))

k = 1
dzielnik = 0

for k in range(1, n+1):
    if n % k == 0:
        dzielnik = dzielnik + 1

print('Ilość dzielników:',dzielnik)