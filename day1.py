import time
import aoc_data

data = aoc_data.load(1)  # load data for day 1
data = [int(v) for v in data.split()]

# -- Part 1 -- #
increased_count = 0
for i in range(len(data) - 1):
    if data[i + 1] > data[i]:
        increased_count += 1
print(increased_count)


# -- Part 2 -- #
WINDOW_LENGTH = 3
previous_window_sum = None
increased_count = 0
for i in range(len(data) - WINDOW_LENGTH + 1):
    window_sum = 0
    for j in range(WINDOW_LENGTH):
        window_sum += data[i + j]
    if previous_window_sum is not None and window_sum > previous_window_sum:
        increased_count += 1
    previous_window_sum = window_sum
print(increased_count)
