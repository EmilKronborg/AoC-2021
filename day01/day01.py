def part_1(depths):
    count = 0

    for i in range(1, len(depths)):
        if depths[i] > depths[i - 1]:
            count += 1

    return count


def part_2(depths):
    count = 0

    for i in range(3, len(depths)):
        first_window = depths[i - 1] + depths[i - 2] + depths[i - 3]
        second_window = depths[i] + depths[i - 1] + depths[i - 2]
        if second_window > first_window:
            count += 1

    return count

# depths = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
depths = [int(line.strip()) for line in open("input.txt", 'r')]
print("The solution to question one is:", part_1(depths))
print("The solution to question two is:", part_2(depths))
