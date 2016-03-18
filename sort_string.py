


def string_to_list(str):
	str = str.lower()
	L = []
	for i in str:
		L.append(i)
	return L

def sort_list(list):
	l = sorted(list)
	return l
	 
	
def list_to_string(list):
	res = ''
	for i in list:
		if i != ' ':
			res += i
	return res
while True:
	S = input('Input string, that you wanted to be sorted: ')	
	list = string_to_list(S)
	list1 = sort_list(list)
	result = list_to_string(list1)
	print('String = ', S)
	print(len(S))
	print('result = ', result)
	print(len(result))
#input('Input ENTER to exit!') 