print("Opening and closing the file.\n")

text_file = open("read_it.txt", "r")
text_file.close()

print(text_file.read(1))