collatz_dict = dict()

def collatz(n):
	return n/2 if n%2 == 0 else 3*n + 1

def get_collatz_length(n):
	length = 1
	while collatz(n) != 1:
		n = collatz(n)
		length += 1
	return length
	# while collatz(n) > n:
	# 	length += 1
	# 	n = collatz(n)
	# return [length + dict[n], new_dict]

longest_length = 0
longest_starting_num = 0

for i in range(1, 1000000):
	length = get_collatz_length(i)
	longest_length = length if length > longest_length else longest_length
	longest_starting_num = i if length == longest_length else longest_starting_num

print(longest_length)
print(longest_starting_num)