with open("input.txt") as file:
        lines = file.readlines()
        
sum = 0

for line in lines:
    s1, s2 = line[:len(line)//2], line[len(line)//2:]
    r = ''.join(set(s1).intersection(s2))
    sum += ord(r) - 96 if ord(r) >= 97 else ord(r) - 38

print(sum)           
       
  