def max_number_bits(bits):
    num_max = 0
    bit = 1
    for i in range(bits):
        num_max += bit
        bit = bit * 2
    return num_max


def binary_place(series):
    bit = 1
    nums = 0
    for num in range(len(series) - 1, -1, -1):
        if series[num] == "1":
            nums += bit
        bit = bit * 2
    return nums


print(binary_place("10001101"))
