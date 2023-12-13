def Frequency_analytic(s):
	list_word = []
	words_dic = {}
    
	list_word = list(s)

	print(list_word)
	for char in list_word:
		if char in words_dic:
			words_dic[char] += 1
		else:
			words_dic[char] = 1

	words_list = sorted(words_dic.items(), key = lambda x : x[0])
	
	print(words_list)

	for i in words_list:
		print(*i)

if __name__ == "__main__":
	msg = input('input your message : ')
	Frequency_analytic(msg)
