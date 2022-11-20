import math
def filter_prime(arr):
    l = []
    for i in arr:
        ok = True
        num = int(math.sqrt(i))
        for j in range(2, num+1):
            if i % j == 0:
                ok = False
                break
        if ok == True:
            l.append(i)    
    return l

arr = list(map(int, input().split()))

filter = lambda list: filter_prime(list)
print(filter(arr))
