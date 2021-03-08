n = int(input('Podaj liczbę n:'))
m = int(input('Podaj liczbę m:'))

if m > n:
    for i in range(n,m+1):
        print(i, end=" ")
elif n > m:
    for i in range(n,m-1,-1):
        print(i, end=" ")
else:
    print(n)