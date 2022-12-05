with open("input.txt") as file:
    lines = file.readlines()

sum = 0
for line in lines:
    values = line.split(',')
    e1 = values[0].split('-')
    e2 = values[1].split('-')
    
    e1s = int(e1[0])
    e1e = int(e1[1])

    e2s = int(e2[0])
    e2e = int(e2[1])
    
    sum += (e1e >= e2s) and (e2e >= e1s)

print(sum)