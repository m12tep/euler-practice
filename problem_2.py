num1 = 1
num2 = 2
sum = 0

while num2 < 4000000:
    if num2 % 2 == 0:
        sum += num2
    temp = num1
    num1 = num2
    num2 = temp + num1
print(sum)