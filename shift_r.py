L = [1, 2, 3, 4, 5, 6]

def shift(list):
	n = input('Enter shift amount: ')
	k = 0
	while k <= int(n) - 1:
		i = 1
		c = list[len(list) - 1]
		while i <= len(list):
			j = 1
			while j <= len(list):
				list[len(list) - j] = list[len(list) - j - 1]
				j += 1
			i += 1
		list[0] = c
		k += 1
	return list

print('L = %s' % L)
k = shift(L)
print('shifted L = %s' % k)
input()