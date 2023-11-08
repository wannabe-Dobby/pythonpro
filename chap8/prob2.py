print("Createing a text file with the write() method.")
text_file = open("write_it.txt", "w")
text_file.write("Line 1\n")
text_file.write("This is line 2\n")
text_file.write("That makes this line 3\n")

print("Creating a text file with the writelines() method.")
text_file = open("write_it.txt", "w")
lines = ["Line 1\n", "This is line 2\n", "That makes this line 3\n"]
text_file.writelines(lines)

print("Read the newly created file.")
text_file = open("write_it.txt", "r")
whole_thing = text_file.read()
print(whole_thing)
text_file.close()