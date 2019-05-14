num_dict = {
    1: len('one'), 2: len('two'), 3: len('three'),
    4: len('four'), 5: len('five'), 6: len('six'),
    7: len('seven'), 8: len('eight'), 9: len('nine'),
    10: len('ten'), 11: len('eleven'), 12: len('twelve'),
    13: len('thirteen'), 14: len('fourteen'), 15: len('fifteen'),
    16: len('sixteen'), 17: len('seventeen'), 18: len('eighteen'),
    19: len('nineteen'), 20: len('twenty'), 30: len('thirty'),
    40: len('forty'), 50: len('fifty'), 60: len('sixty'), 
    70: len('seventy'), 80: len('eighty'), 90: len('ninety'),
    100: len('hundred'), 1000: len('onethousand'), 'and': len('and')
}

def get_length(num):
    if num == 100:
        return num_dict[1] + num_dict[100]
    elif num in num_dict.keys():
        return num_dict[num]
    elif len(str(num)) == 2:
        first_digit = int(str(num)[0] + '0')
        second_digit = int(str(num)[1])
        return num_dict[first_digit] + num_dict[second_digit]
    elif str(num)[1:] == '00':
        first_digit = int(str(num)[0])
        return num_dict[first_digit] + num_dict[100]
    else:
        first_digit = num_dict[int(str(num)[0])] + num_dict[100] + num_dict['and']
        if int(str(num)[1:]) in num_dict.keys():
            next_digits = int(str(num)[1:])
            return first_digit + num_dict[int(str(num)[1:])]
        else: 
            second_digit = int(str(num)[1] + '0')
            third_digit = int(str(num)[2])
            return first_digit + num_dict[second_digit] + num_dict[third_digit]

char_sum = 0
for i in range(1, 1000+1):
    length = get_length(i)
    char_sum += length

print(char_sum)