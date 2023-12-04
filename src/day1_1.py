input_file = open('./inputs/day1.txt', 'r')

def get_first(line):
    for c in line:
        if c.isnumeric():
            return int(c)

total = 0
for line in input_file.readlines():
    first_num = get_first(line)
    last_num = get_first(line[::-1])
    total += (first_num*10 + last_num)

print(total)