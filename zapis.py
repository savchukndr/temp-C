L = [['olya','deva','sava'], [4,5,6], [7,8,9]]

file = open(r'C:\temp\matrix.txt', 'w')
for i in L:
	file.write('| ')
	for j in i:
		j = str(j)
		file.write(j + ' ')
	file.write('|')
	file.write('\n')
file.close()
	
file1 = open(r'C:\temp\matrix.txt')
f = file1.read()
print(f)
file1.close()