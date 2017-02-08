f = open('teste.py', 'r')

cont = 0
array = list()
for line in f:
    cont += 1
    print line

    if len(line.split('(')) != 2:
        continue
    print line.split('(')
    array.append((line.split('(')[1].split(')')[0])[1:-1])
    if cont == 36:
        break

print array
