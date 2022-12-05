max = []
cur_sum = 0
for line in open("input.txt"):
    if line != '\n':
        cur_sum += int(line)
    else:
        max.append(cur_sum)
        cur_sum = 0
        
print(sum(sorted(max)[-3:]))      
