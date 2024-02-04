file = open('file.txt', 'r')
lines_to_read = file.readlines(-1)[0]
print(lines_to_read)
file.close()

file2 = open('file.txt', 'w')
file2.write('Hello i`m a new entity here')
file2.writelines(['first line\n', 'second line\n'])
file2.close()

file3 = open('file.txt', 'a')
file3.write('this is new line, new hope')
file3.close()

permanent_lines = []
with open('file.txt', 'r') as alias_a:
    temp_lines = alias_a.readlines()
    permanent_lines += temp_lines
    print(permanent_lines)

with open('b.txt', 'w') as alias_b:
    for line in permanent_lines:
        if len(line) > 20:
            permanent_lines[permanent_lines.index(line)] = 'sorry, this line so too long'
        alias_b.writelines(permanent_lines)