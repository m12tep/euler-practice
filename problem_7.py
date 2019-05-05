from helper.prime import check_prime

prime_count = 2
largest_prime = 3
check_num = 4
while prime_count <= 10001:
    if(check_prime(check_num) == True):
        print(f"{prime_count} | {largest_prime}")
        prime_count += 1
        largest_prime = check_num
    check_num += 1