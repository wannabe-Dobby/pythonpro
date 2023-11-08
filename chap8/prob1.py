print("Opening and closing the file.\n")

text_file = open("read_it.txt", "r")

print(text_file.read(1))


text_file.close()