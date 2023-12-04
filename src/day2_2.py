input_file = open('./inputs/day2.txt', 'r')

def check_rounds(rounds):
    maxRed, maxGreen, maxBlue = 0, 0, 0
    for r in rounds:
        cols = r.split(",")
        nRed, nGreen, nBlue = 0, 0, 0
        for col in cols:
            if "red" in col:
                nRed = int(col.split("red")[0])
            elif "green" in col:
                nGreen = int(col.split("green")[0])
            elif "blue" in col:
                nBlue = int(col.split("blue")[0])
        maxRed = max(maxRed, nRed)
        maxGreen = max(maxGreen, nGreen)
        maxBlue = max(maxBlue, nBlue)
    return maxRed*maxBlue*maxGreen

def check(line):
    game_split = line.split(":")
    rounds = game_split[1].split(";")
    return check_rounds(rounds)

total = 0
for line in input_file.readlines():
    total += check(line)

print(total)