def Frequency_analytic(s):
	list_word = []
	words_dic_high = {}
	words_dic_low = {}
    
	list_word = list(s)

	print(list_word)
	for char in list_word:
		if ord(char) < 96:
			if char in words_dic_high:
				words_dic_high[char] += 1
			else:
				words_dic_high[char] = 1
		else:
			if char in words_dic_low:
				words_dic_low[char] += 1
			else:
				words_dic_low[char] = 1

	words_list_high = sorted(words_dic_high.items(), key = lambda x : x[0])
	words_list_low = sorted(words_dic_low.items(), key = lambda x : x[0])
	
	print(words_list_high)
	print(words_list_low)

	for i in words_list_low:
		print(*i)
	
	for i in words_list_high:
		print(*i)

if __name__ == "__main__":
	msg = input('input your message : ')
	Frequency_analytic(msg)