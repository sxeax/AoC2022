max = 0
cur_sum = 0

for line in open("input.txt"):
    if line != '\n':
        cur_sum += int(line)
    else:
        max = cur_sum if cur_sum > max else max
        cur_sum = 0

print(max)    