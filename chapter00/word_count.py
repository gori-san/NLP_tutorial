import sys
from collections import defaultdict

counts = defaultdict(lambda:0)
file_name = sys.argv[1]

with open(file_name, 'r', encoding='utf-8') as input_file:
    for line in input_file:
        line = line.strip()
        words = line.split(' ')
        for word in words:
            counts[word] += 1

# with open('00_output.txt', 'w', encoding='utf-8') as output_file:
#     for key,value in sorted(counts.items()):
#         output_file.write('{} {}'.format(key,value))

for key,value in sorted(counts.items()):
    print('{} {}'.format(key,value))
