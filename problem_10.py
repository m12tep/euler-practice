from helper.prime import check_prime

sum = 0
for num in range(1, 2000000):
    if check_prime(num) == True:
        print(num)
        sum += num
print(sum)