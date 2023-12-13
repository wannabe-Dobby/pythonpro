def Frequency_analytic(s):
	list_word = []
	words_dic = {}
	high = []
	low = []
    
	list_word = list(s)

	print(list_word)
	for char in list_word:
		if char in words_dic:
			words_dic[char] += 1
		else:
			words_dic[char] = 1
'''	
	for i in list_word:
		if ord(i) <= 96:
			high.append(i)
		else:
			low.append(i)
	
	print(high)
	print(low)
	print(words_dic)

	high_list = sorted(high.items(), key = lambda x : x[0])
	low_list = sorted(high.items(), key = lambda x : x[0])

	'''
	words_list = sorted(high.items(), key = lambda x : x[0])
	print(words_list)



if __name__ == "__main__":
	msg = input('input your message : ')
	Frequency_analytic(msg)
