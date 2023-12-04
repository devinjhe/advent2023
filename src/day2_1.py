input_file = open('./inputs/day2.txt', 'r')

def check_rounds(rounds):
    for r in rounds:
        cols = r.split(",")
        for col in cols:
            if "red" in col:
                nRed = int(col.split("red")[0])
                if nRed > 12:
                    return False
            elif "green" in col:
                nGreen = int(col.split("green")[0])
                if nGreen > 13:
                    return False
            elif "blue" in col:
                nBlue = int(col.split("blue")[0])
                if nBlue > 14:
                    return False
    return True

def check(line):
    game_split = line.split(":")
    game_id = int(game_split[0][5:])
    
    rounds = game_split[1].split(";")
    if (check_rounds(rounds)):
        return game_id

    return 0

total = 0
for line in input_file.readlines():
    total += check(line)

print(total)