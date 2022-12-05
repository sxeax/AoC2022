with open("input.txt") as file:
    lines = file.readlines()    
sum = 0     
for i in range(0, len(lines), 3):    
    r = ''.join(set(lines[i]).intersection(lines[i + 1], lines[i + 2])).strip()
    sum += ord(r) - 96 if ord(r) >= 97 else ord(r) - 38
print(sum)