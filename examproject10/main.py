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
        binary = binary[0:2] + binary[-2:]
        total_binary += binary

x = len(total_binary)//16
list = []
c = 0
for i in range(x):
    y = total_binary[c*16:c*16+16]
    list.append(y)
    c += 1

sumlist = []
for i in range(x):
    num = (list[i])
    sum = 0
    for l in range(16):
        if num[l] == '1':
            sum += 2**(15-l)
    sumlist.append(sum)

n2 = 0
n3 = 0
n5 = 0
n7 = 0
for i in range(x):
    if int(sumlist[i]) % 2 == 0:
        n2 += 1
    if int(sumlist[i]) % 3 == 0:
        n3 += 1
    if int(sumlist[i]) % 5 == 0:
        n5 += 1
    if int(sumlist[i]) % 7 == 0:
        n7 += 1

p2 = n2 * 100 / x
p3 = n3 * 100 / x
p5 = n5 * 100 / x
p7 = n7 * 100 / x

print("Το ποσοστό των ζυγών είναι : " + str(p2) + " %")
print("Το ποσοστό που διαιρείται με το 3 είναι : " + str(p3) + " %")
print("Το ποσοστό που διαιρείται με το 5 είναι : " + str(p5) + " %")
print("Το ποσοστό που διαιρείται με το 7 είναι : " + str(p7) + " %")
