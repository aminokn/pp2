a,b = int(input()), int(input())

def squares(a,b):
    for i in range (a,b+1):
        d = i ** 2
        yield d
x = squares(a,b)
for i in x:
    print(i)
