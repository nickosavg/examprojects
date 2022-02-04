import json

fin = open("dictionaries.txt", "r")

lst = []
for line in fin:
    lst.append(line.strip())

for i in range(len(lst)):
    lst[i] = json.loads(lst[i])

print(lst[0].keys())
userk = input("Εισάγεται κλειδί")

valuelist = []
for i in range(len(lst)):
    valuelist.append(lst[i].get(userk))

max = valuelist[0]
min = valuelist[0]
for i in range(len(valuelist)):
    if valuelist[i] > max:
        max = valuelist[i]
    if valuelist[i] < min:
        min = valuelist[i]

print("Η μικρότερη τιμή είναι " + str(min) + " και η μεγαλύτερη " + str(max))
