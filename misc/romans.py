import math

roman_value_map = {
	'I':1,
	'V':5,
	'X':10,
	'L':50,
	'C':100,
	'D':500,
	'M':1000,
}

def romanToInt(roman_form):
	i = 0
	length = len(roman_form)
	roman_form = list(roman_form)
	
	while i < length:
		roman_form[i] = roman_value_map[roman_form[i]]
		i+=1
	i=0
	numeral = 0

	while i < length:

		if i+1 < length:
			if roman_form[i] >= roman_form[i+1]:
				numeral+=roman_form[i]
			else:
				numeral+=roman_form[i+1]-roman_form[i]
				i+=1
			i+=1
		else:
			numeral+=roman_form[i]
			i+=1
	return numeral

def intToRoman(numeral):
	temp = numeral
	roman = ""
	while temp != 0:
		if temp >= 1000:
			i = 0
			while i < math.floor(temp/1000):
				roman+='M'
				i+=1
			temp = temp%1000
		elif temp >= 500:
			if temp < 900:
				i = 0
				while i < math.floor(temp/500):
					roman+='D'
					i+=1
				temp = temp%500
			else:
				roman+='C'+'M'
				temp = temp%100
		elif temp >= 100:
			if temp < 400:
				i = 0
				while i < math.floor(temp/100):
					roman+='C'
					i+=1
				temp = temp%100
			else:
				roman+='C'+'D'
				temp = temp%100
		elif temp >= 50:
			if temp < 90:
				i = 0
				while i < math.floor(temp/50):
					roman+='L'
					i+=1
				temp = temp%50
			else:
				roman+='X'+'C'
				temp = temp%50
		elif temp >= 10:
			if temp < 40:
				i = 0
				while i < math.floor(temp/10):
					roman+='X'
					i+=1
				temp = temp%10
			else:
				roman+='X'+'L'
				temp = temp%10
		elif temp >= 5:
			if temp < 9:
				i = 0
				while i < math.floor(temp/5):
					roman+='V'
					i+=1
				temp = temp%5
			else:
				roman+='I'+'X'
				temp = 0 
		elif temp >= 1:
			if temp < 4:
				i = 0
				while i < temp:
					roman+='I'
					i+=1
				temp = 0
			else:
				roman+='I'+'V'
				temp = 0 
	return roman