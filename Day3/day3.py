# shared function

def alter_data_layout(lines=None):
    if not lines:
        with open('input.txt', 'r') as file:
            lines = [line.strip() for line in file.readlines()]
    number_of_bits = len(lines[0])
    bits_dct = {i: [] for i in range(number_of_bits)}

    for k, v in bits_dct.items():
        for line in lines:
            bits_dct[k].append(line[k])

    return bits_dct, lines


# part 1
bits, lines = alter_data_layout()
gamma_bits = []
epsilon_bits = []

for k, v in bits.items():
    for line in lines:
        bits[k].append(line[k])

for k, v in bits.items():
    num_zeros = 0
    num_ones = 0
    for num in v:
        if num == '0':
            num_zeros += 1
        else:
            num_ones += 1

    if num_zeros > num_ones:
        gamma_bits.append('0')
        epsilon_bits.append('1')
    else:
        gamma_bits.append('1')
        epsilon_bits.append('0')

gamma_int = int(''.join(gamma_bits), 2)
epsilon_int = int(''.join(epsilon_bits), 2)
print(gamma_int*epsilon_int)


# part 2

def calc_o2_num(o2_num):
    position = 0
    while len(o2_num) > 1:
        bits = alter_data_layout(o2_num)[0]
        num_zeros = 0
        num_ones = 0
        for num in bits[position]:
            if num == '0':
                num_zeros += 1
            else:
                num_ones += 1

        if num_zeros > num_ones:
            o2_num = [line for line in o2_num if line[position] == '0']
        elif num_zeros == num_ones:
            o2_num = [line for line in o2_num if line[position] == '1']
        else:
            o2_num = [line for line in o2_num if line[position] == '1']
        position += 1

    return int(o2_num[0], 2)


def calc_co2_num(co2_num):
    position = 0
    while len(co2_num) > 1:
        bits = alter_data_layout(co2_num)[0]
        num_zeros = 0
        num_ones = 0
        for num in bits[position]:
            if num == '0':
                num_zeros += 1
            else:
                num_ones += 1

        if num_zeros > num_ones:
            co2_num = [line for line in co2_num if line[position] == '1']
        else:
            co2_num = [line for line in co2_num if line[position] == '0']
        position += 1

    return int(co2_num[0], 2)


print(calc_co2_num(lines.copy()) * calc_o2_num(lines.copy()))
