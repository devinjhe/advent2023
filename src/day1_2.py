input_file = open('./inputs/day1.txt', 'r')

numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def get_first_forwards(line):
    for i in range(len(line)):
        c = line[i]
        if c.isnumeric():
            return int(c)
        for j in range(len(numbers)):
            num = numbers[j]
            if (num == line[i:i+len(num)]):
                return int(j+1)

def get_first_backwards(line):
    reversed_line = line[::-1]
    for i in range(len(reversed_line)):
        c = reversed_line[i]
        if c.isnumeric():
            return int(c)
        for j in range(len(numbers)):
            num = numbers[j]
            if (num[::-1] == reversed_line[i:i+len(num)]):
                return int(j+1)

total = 0
for line in input_file.readlines():
    first_num = get_first_forwards(line)
    last_num = get_first_backwards(line)
    total += (first_num*10 + last_num)

print(total)