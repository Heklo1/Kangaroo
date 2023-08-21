import hashlib	

f = open("complete.txt", encoding='utf-8')
lines = f.read().split("\n")
f.close()

sortedLines = sorted(lines)
sortedNames = []
sortedStrings = []

for line in lines:
	if ":::" in line:
		idx = line.index(":::")
		sortedNames.append(line[0:idx])
		sortedStrings.append(line[idx+3:])

print("Reading file")
f = open(r"C:\Users\stkan\Documents\MC Server Stuff\leone\dopedumpbig.txt")
mem_strings = str(f.read())
f.close()

i = 0
print("Scanning strings")
for string in sortedStrings:
	if string in mem_strings:
		print(string)
	if i%20 == 0:
		print(i/len(sortedStrings))
	i += 1



