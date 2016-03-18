import math
import random
import decimal

x = 123 + 222
print(x)
print()

y = 1.5 * 4
print(y)
print()

z = 2 ** 100
print(z)
print()

#print(len(str(2 ** 1000000))) 		#сколько чисел в 2^1000000
#print()

print(math.pi)
print(math.sqrt(85))
print()

print(random.random())				#Рандомное число
print(random.choice([1, 2, 3, 4]))	#Выберает рандомно из чисел 1, 2, 3, 4
print()

S = 'Spam'
print(len(S))						#Длина строки
print(S[0])							#Первый символ (отсчет начинается с 0)
print(S[1])							#Второй символ
print(S[-1])						#Последний элемент в конце S
print(S[len(S) - 1])				#Тоже самое, что и команда выше
print(S[-2])						#Второй элемент с конца

print(S)
print(S[1:3])						#Срез от второго символа и до третьего(не включаяя его)
print(S[1:])
print(S[0:3])
print(S[:3])
print(S[:-1])
print(S[:])

##############################################
#Списки
L = [123, 'abc', 1.23] 				#Список трьох разных типов
print(len(L))						#Длина списка
print(L[0])
print(L[:-1])
L = L + [4, 5, 6]					#Конкатинация
print(L)

M = ['cc', 'aa', 'bb']
print(M)
M.sort()							#Сортировка списка
print(M)
M.reverse()							#Вывод списка в обратном направлении
print(M)

M = [[1, 2, 3],
	 [4, 5, 6],
	 [7, 8, 9]]						#Матрица 3*3*3
print(M)

col2 = [row[1] for row in M]
print(col2)
col2 = [row[1] + 1 for row in M]
print(col2)

Sava = {'name': {'first': 'Andrey', 'last':'Savchuk'}, #Словари
		'age': 21,
		'study': ['KPI', 'PW']}
print(Sava)
Sava['study']. append('MIT')
print(Sava['study'])
print('Last name is', Sava['name']['last'])
sq = [x ** 2 for x in [1, 2, 3, 4]]
print(sq)

T = (1, 2, 3, 4)					#Кортеж
print('T = ',T)
print(len(T))
print('T + (5, 6) = ', T + (5, 6))
print()

f = open('file.txt', 'w')			#Файлы
f.write('Hello\n')
f.write('World\n')
f.close()
######
f = open('file.txt')
text = f.read()
print(text)

X = set('spam')						#Множества
print('X = ', X)
Y = {'a', 'h', 'm'}
print('Y = ', Y)
print('X, Y = ', X, Y)
print('X & Y= ', X & Y)
print('X | Y = ', X | Y)
print('X - Y = ', X - Y)
print({x ** 2 for x in [1, 2, 3, 4]})
print()

print('1/3 = ', 1/3)
print('(2/3) + (1/2) = ',(2/3) + (1/2))
d = decimal.Decimal('3.141')
print('d + 1 = ', d + 1)

a = 3								#Операции над числами
b = 4
print('a + 1, a - 1 = ', a + 1, a - 1)
print('b * 3, b / 2 = ', b * 3, b / 2)
print('a % 2, b ** 2 = ', a % 2, b ** 2)
print('2 + 4.0, 2.0 ** b = ', 2 + 4.0, 2.0 ** b)
print()

print('math.pi = ', math.pi, 'math.e = ', math.e)
print('math.sqrt(144), math.sqrt(2) = ', math.sqrt(144), math.sqrt(2))
print('pow(2, 4), 2 ** 4 = ', pow(2, 4), 2 ** 4)
print('abs(-42.0), sum((1, 2, 3, 4)) = ', abs(-42.0), sum((1, 2, 3, 4)))
print('min(1, 2, 3, 4), max(1, 2, 3, 4) = ', min(1, 2, 3, 4), max(1, 2, 3, 4))
print('math.floor(2.34), math.floor(-2.34) = ', math.floor(2.34), math.floor(-2.34))
print('math.trunc(2.34), math.trunc(-2.34) = ', math.trunc(2.34), math.trunc(-2.34))
print('int(2.567), int(-2.567) = ', int(2.567), int(-2.567))
print('round(2.567), round(2.467), round(2.567, 2) = ', round(2.567), round(2.467), round(2.567, 2))
print()

S = {'s', 'p', 'a', 'm'}
print('S = ', S)
S = S.add('alot')
print('S = ', S)
print('Generetor mnogestv = ',{x ** 2 for x in [1, 2, 3 , 4]})

