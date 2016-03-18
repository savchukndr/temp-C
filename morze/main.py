import morze


print('Hello, this is program for encryption/unencryption on cypher MORZE!!!')
while True:
	option = input('You want encrypt or unencrypt?: ')
	if option == 'encrypt' or option == 'en':
		S = input('Input words: ')
		L = list(S.upper())
		convInto = morze.convert_into(L)
		print('Result: ', convInto)
	elif option == 'unencrypt' or option == 'un':
		S1 = input('Input cypher: ')
		L1 = S1.split()
		convOut = morze.convert_out(L1)
		print('Result: ', convOut)
	else:
		print('I can\'t do it =(')
	posib = input('Do You want exit or You want continue?: ')
	if posib == 'exit':
		break
	elif posib != 'continue':
		print('Hm, I do not understend you, so I think, you want to continue =)!')
	