from functools import reduce

results = {'1': ['R', 'S', 'L', 'F', 'Q' ], 
           '2': ['N', 'Z', 'Q', 'G', 'P', 'T'], 
           '3': ['S', 'M', 'Q', 'B'], 
           '4': ['T', 'G', 'Z', 'J', 'H', 'C', 'B', 'Q'], 
           '5': ['P', 'H', 'M', 'B', 'N', 'F', 'S'], 
           '6': ['P', 'C', 'Q', 'N', 'S', 'L', 'V', 'G'], 
           '7': ['W', 'C', 'F'], 
           '8': ['Q', 'H', 'G', 'Z', 'W', 'V', 'P', 'M'], 
           '9': ['G', 'Z', 'D', 'L', 'C', 'N', 'R']}

for line in open("input.txt"):
    data = line.split()
    for i in range(int(data[1])):
        results[data[5]].append(results[data[3]].pop())
          
print(reduce(lambda x, value: x + value.pop(), results.values(), ""))