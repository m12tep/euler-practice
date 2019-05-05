from helper.prime import check_prime, math

largest_prime = 0
for num in range(2, math.ceil(600851475143/2)):
    if 600851475143 % num == 0:
        if check_prime(600851475143/num) == True:
            print(f"Largest prime: {600851475143/num}")
            break