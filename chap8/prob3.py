print("Input your string...")
text_file = open("Input.txt", "w")

lines = []
while True:
    str = input()

    if str == 'Q':
        break

    lines.append(str)
    lines.append("\n")

print("Write process has been finished")
text_file.writelines(lines)
text_file.close()

print("\n\n\nYour inputs are below..")
text_file = open("Input.txt", "r")
whole_things = text_file.read()
print(whole_things)
text_file.close()