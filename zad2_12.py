for k in range(1, 200+1):
    if k > 1:
        for i in range(2, k):
            if (k % i) == 0:
                break
        else:
            print(k)