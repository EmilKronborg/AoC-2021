# puzzle_input = ["forward 5",
#               "down 5",
#               "forward 8",
#               "up 3",
#               "down 8",
#               "forward 2"]

def task_1(puzzle_input):
    horizontal = 0
    depth = 0

    for i in range(len(puzzle_input)):
        current_line = puzzle_input[i].split()

        if current_line[0] == "forward":
            horizontal += int(current_line[1])
        elif current_line[0] == "down":
            depth += int(current_line[1])
        elif current_line[0] == "up":
            depth -= int(current_line[1])
        else:
            print("Unkown direction")

    return horizontal * depth

def task_2(puzzle_input):
    horizontal = 0
    depth = 0
    aim = 0

    for i in range(len(puzzle_input)):
        current_line = puzzle_input[i].split()

        if current_line[0] == "forward":
            horizontal += int(current_line[1])
            depth += int(current_line[1]) * aim
        elif current_line[0] == "down":
            aim += int(current_line[1])
        elif current_line[0] == "up":
            aim -= int(current_line[1])
        else:
            print("Unkown direction")

    return horizontal * depth

# Read the input file and split the lines
with open("input.txt", "r") as f:
    puzzle_input = f.read()
    puzzle_input = puzzle_input.splitlines()

print("The answer to task one is:", task_1(puzzle_input))
print("The answer to task two is:", task_2(puzzle_input))
