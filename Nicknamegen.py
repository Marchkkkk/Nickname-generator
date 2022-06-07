import random

Numberlist = []

for x in range(1, 99):
    Numberlist.append(random.randint(1, 100))

amount = int (input('Amount of nicknames: '))

f = open('Nicknames.txt','w+')

with open("myfile.txt") as inp:
    lines = inp.readlines()

for x in range(1,amount +1):
    part1 = random.choice(lines).strip()
    part2 = random.choice(lines).strip()
    part3 = str (random.choice(Numberlist))

    Nickname = part1+part2+part3

    f.write(Nickname + '\n')

f.close()











