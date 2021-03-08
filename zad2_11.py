n =  int(input('Podaj n:'))

x = 0
y = 0

if n <= 1:
    print('Liczba nie jest złożona ani pierwsza')

for k in range(2, n+1):
    if 2 <= k <= n - 1 and n % k == 0:
        x = x + 1

if n % n == 0 and n % 1 == 0:
    y = y + 1

if x > y:
    print('Jest złozona')
elif y > x:
    print('Jest pierwsza')
else:
    print('Jest złozona')