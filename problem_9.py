import math

for a in range(1, 500):
    for b in range(1, 500):
        c = math.sqrt(a**2 + b**2)
        if int(c) == c and a + b + c == 1000:
            print(int(a*b*c))
            break