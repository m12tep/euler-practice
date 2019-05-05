from helper.prime import get_factors

done = False

natural_num = 1
triangle_num = 0
while done == False:
    triangle_num += natural_num
    num_factors = len(get_factors(triangle_num))
    print(f"{triangle_num} | {num_factors}")
    natural_num += 1
    if len(get_factors(triangle_num)) > 500:
        print(triangle_num)
        done = True