import csv
fileName = 'input.csv'
with open(fileName, 'r') as file:
    csv_reader = csv.reader(file)
    for line in csv_reader:
        # print(line)
        # print(line[2])
        if line[2] == "P":
            print(line)
            print(line[0])


