import time
import aoc_data

data = aoc_data.load(2).rstrip(b"\n").split(b"\n")
data = [v.decode("utf-8") for v in data]


# -- Part 1 -- #
movements = dict(forward=0, down=0, up=0)
for item in data:
    direction, value = item.split()
    movements[direction] += int(value)

print(movements["forward"] * abs(movements["down"] - movements["up"]))


# -- Part 2 -- #
horizontal_position = 0
depth = 0
aim = 0
for item in data:
    direction, value = item.split()
    value = int(value)
    if direction == "forward":
        horizontal_position += value
        depth += aim * value
    if direction == "down":
        aim += value
    if direction == "up":
        aim -= value

print(horizontal_position * depth)
