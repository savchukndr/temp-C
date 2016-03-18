F = open(r'C:\temp\morze\dict.txt')
def get_sym_out(file):
	aString = file.readline()
	aList = []
	aList.append(aString)
	temp = eval(aList[0])
	return temp

dictWord = get_sym_out(F)
dictWordRev = get_sym_out(F)	
dictDigit = get_sym_out(F)
dictDigitRev = get_sym_out(F)
dictSpecSymb = get_sym_out(F)
dictSpecSymbRev = get_sym_out(F)
##############
def con_str(list):
	string = ''
	for i in list:
		string += i + ' '
	return string
##############	
strSSW = ''.join(list(dictWordRev.values()))		#normal
strSSD = ''.join(list(dictDigitRev.values()))
strSS = ''.join(list(dictSpecSymbRev.values()))
strSSR = con_str(list(dictSpecSymb.values()))	#reversed
strSSWR = con_str(list(dictWord.values()))
strSSDR = con_str(list(dictDigit.values()))	

def convert_into(list):
	K = []
	res = ''
	for i in list:
		if i in strSSW:
			temp = dictWord[i]
			K.append(temp)
		elif i in strSSD: 				#if i in specialSymDig:
			temp = dictDigit[i]
			K.append(temp)
		elif i in strSS:
			temp = dictSpecSymb[i]
			K.append(temp)
	for j in K:
		res += j + ' '
	return res

def convert_out(list):
	K = []
	res = ''
	for i in list:
		if i in strSSWR:
			temp = dictWordRev[i]	
			K.append(temp)
		elif i in strSSDR:
			temp = dictDigitRev[i]	
			K.append(temp)
		elif i in strSSR:
			temp = dictSpecSymbRev[i]	
			K.append(temp)
	for j in K:
		res += j
	return res
		
