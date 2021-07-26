fileName = 'inputFile.txt'
f = open(fileName, 'r')

# for line in f:
#     # print(line)
#     line_split = line.split()
#     #print(line_split)
#     if line_split[2] == "F":
#         print(line)

for i in range(4):
    print(f.readline())

