import requests

r = requests.get('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})

data = r.json()

d = data.get('randomness')

list = []
c = 0
for i in range(len(d) // 2):
    y = d[c*2:c*2+2]
    list.append(y)
    c += 1


def dig(digit):
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    for x in range(len(digits)):
        if digit == digits[x]:
            return x


def num(hexNum):
    decNum = 0
    power = 0
    for digit in range(len(hexNum), 0, -1):
        decNum = decNum + 16 ** power * dig(hexNum[digit-1])
        power += 1
    decNum = decNum % 80
    return str(decNum)


for i in range(len(list)):
    list[i] = num(list[i])


for i in range(len(list)):
    for y in range(len(list)):
        if i != y and list[i] == list[y]:
            list[y] = ''

r2 = requests.get('https://api.opap.gr/draws/v3.0/1100/last-result-and-active')

data2 = r2.json()

kino = data2.get('last').get('winningNumbers').get('list')
win = 0

for i in range(len(list)):
    for y in range(len(kino)):
        if list[i] == str(kino[y]):
            win += 1

print(str(win) + ' αριθμοί κληρώθηκαν στην τελευταία κλήρωση του ΚΙΝΟ')
