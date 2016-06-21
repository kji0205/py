'''인덱스-값 페어 시퀀스 순환'''

my_list = ['a', 'b', 'c']
for idx, val in enumerate(my_list):
    print(idx, val)
for idx, val in enumerate(my_list, 1):
    print(idx, val)


from collections import defaultdict


def parse_data(filename):
    with open(filename, 'rt') as f:
        for lineno, line in enumerate(f, 1):
            fields = line.split()
            try:
                count = int(fields[1])
            except ValueError as e:
                print('Line {}: Parse error: {}'.format(lineno, e))

line = parse_data('etc/passwd')
print(line)

word_summary = defaultdict(list)
print(type(word_summary))

with open('etc/passwd', 'r') as f:
    lines = f.readlines()

# print(lines)

for idx, line in enumerate(lines):
    words = [w.strip().lower() for w in line.split()]
    for word in words:
        word_summary[word].append(idx)

print(word_summary)
