sum = 0

for line in open("input.txt"):
    values = line.split(',')
    e1 = values[0].split('-')
    e2 = values[1].split('-')
    if (int(e1[0].strip()) <= int(e2[0].strip()) and int(e1[1].strip()) >= int(e2[1].strip())) or (int(e1[0].strip()) >= int(e2[0].strip()) and int(e1[1].strip()) <= int(e2[1].strip())):
        sum += 1
        
print(sum)        