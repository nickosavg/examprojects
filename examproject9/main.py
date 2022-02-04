fin = open("two_cities_ascii.txt", "r")

total_binary = ""

for line in fin:

    for i in range(len(line)):
        binary = ""
        string_ord = ord(line[i:i+1])

        while string_ord > 0:
            x = string_ord % 2
            string_ord = string_ord // 2
            binary = str(x) + str(binary)

        total_binary += binary

count1 = 0
max1 = 0
count0 = 0
max0 = 0

for i in total_binary:
    if i == str(1):
        if count0 > max0:
            max0 = count0
        count0 = 0
        count1 += 1
    else:
        if count1 > max1:
            max1 = count1
        count1 = 0
        count0 += 1

print('Η μεγαλύτερη ακολουθία απο 1 είναι ' + str(max1) + ' και από 0 είναι ' + str(max0))
