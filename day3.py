import time
import aoc_data

# All the bits are concatenated
data = aoc_data.load(3).replace(b"\n", b"").decode("utf-8")
# Each code is of length NUMBER_OF_BITS
NUMBER_OF_BITS = 12

# -- Part 1 -- #
def get_most_frequent_bit_at_position(bits, position):
    v = bits[position::NUMBER_OF_BITS]
    if v.count("0") > v.count("1"):
        return "0"
    return "1"


s = ""
ocs = ""  # one's complement of s
d = {"0": "1", "1": "0"}
for i in range(NUMBER_OF_BITS):
    mfb = get_most_frequent_bit_at_position(data, i)
    s += mfb
    ocs += d[mfb]

print(s)
print(ocs)

print(int(s, 2) * int(ocs, 2))


# -- Part 2 -- #
NUMBER_OF_BITS = 12
data = aoc_data.load(3).rstrip(b"\n").split(b"\n")
data = [v.decode("utf-8") for v in data]


def get_most_frequent_bit_at_position_O2(position: int, data: list):
    v = ""
    for item in data:
        v += item[position]
    if v.count("1") >= v.count("0"):
        return "1"
    return "0"


def get_least_frequent_bit_at_position_CO2(position: int, data: list):
    v = ""
    for item in data:
        v += item[position]
    if v.count("0") <= v.count("1"):
        return "0"
    return "1"


def get_binary_values_with_certain_bit_at_position(
    values: list, position: int, bit: str
):
    filterted_values = []
    for v in values:
        if v[position] == bit:
            filterted_values.append(v)
    return filterted_values


o2_values_bit_criteria = data.copy()
co2_values_bit_criteria = data.copy()

# Get the oxygen generator rating
for i in range(NUMBER_OF_BITS):
    o2_bit = get_most_frequent_bit_at_position_O2(i, o2_values_bit_criteria)
    o2_values_bit_criteria = get_binary_values_with_certain_bit_at_position(
        o2_values_bit_criteria, i, o2_bit
    )
    if len(o2_values_bit_criteria) == 1:
        break

# Get the CO2 scrubber rating
for i in range(NUMBER_OF_BITS):
    co2_bit = get_least_frequent_bit_at_position_CO2(i, co2_values_bit_criteria)
    co2_values_bit_criteria = get_binary_values_with_certain_bit_at_position(
        co2_values_bit_criteria, i, co2_bit
    )
    if len(co2_values_bit_criteria) == 1:
        break

print(o2_values_bit_criteria)
print(co2_values_bit_criteria)

print(int(o2_values_bit_criteria[0], 2) * int(co2_values_bit_criteria[0], 2))
