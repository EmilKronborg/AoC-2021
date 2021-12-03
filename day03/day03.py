# report = ['00100',
#           '11110',
#           '10110',
#           '10111',
#           '10101',
#           '01111',
#           '00111',
#           '11100',
#           '10000',
#           '11001',
#           '00010',
#           '01010']

def part_1(report):
    gamma_rate, epsilon_rate = '', ''

    for bit in range(len(report[0])):
        zeros = sum(number[bit] == '0' for number in report)
        ones = sum(number[bit] == '1' for number in report)
        if ones > zeros:
            gamma_rate += '1'
            epsilon_rate += '0'
        else:
            gamma_rate += '0'
            epsilon_rate += '1'

    # int(x, 2) converts an integer to binary representation
    return int(gamma_rate, 2) * int(epsilon_rate, 2)

with open("input.txt", "r") as f:
    report = f.read()
    report = report.splitlines()

print("The solution to question one is:", part_1(report))
print(f'The solution to question one is: {part_1(report)}')


