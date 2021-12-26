import time
import aoc_data

data = aoc_data.load(4).split("\n\n")

NUMBERS = data[0].split(",")

BOARDS = []
for i in range(1, len(data)):
    BOARDS.append([v.split() for v in data[i].split("\n")])

NUM_ROWS = len(BOARDS[0][0])
NUM_COLUMNS = len(BOARDS[0][1])
NUM_BOARDS = len(BOARDS)

# Initialize all the board markings to zero. As the numbers are drawn they will
# be marked as one.

# NOTE: This does not work. It points to the same list for each board.
"""
https://pythontutor.com/visualize.html#code=NUM_BOARDS%20%3D%202%0ANUM_ROWS%20%3D%203%0ANUM_COLUMNS%20%3D%203%0Amarkings%20%3D%20%5B%5B%5B%220%22%5D*NUM_ROWS%5D*NUM_COLUMNS%5D*NUM_BOARDS%0A&cumulative=false&curInstr=4&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
# markings = [[["0"]*NUM_ROWS]*NUM_COLUMNS]*NUM_BOARDS
"""

markings = []
for idx in range(NUM_BOARDS):
    board = []
    for i in range(NUM_ROWS):
        row = []
        for j in range(NUM_COLUMNS):
            row.append("0")
        board.append(row)
    markings.append(board)

# Keep track of which boards already hit bingo. Initialize all boards to False.
bingo_tracker = [False] * NUM_BOARDS


def mark_boards(n: str, boards: list, markings: list):
    """
    Change the board element marking from "0" to "1" if it is equal to n
    """
    for idx in range(NUM_BOARDS):
        for i in range(NUM_ROWS):
            for j in range(NUM_COLUMNS):
                if boards[idx][i][j] == n:
                    markings[idx][i][j] = "1"


def is_bingo(boards, markings):
    """
    Mark the boards which have bingo
    """
    for idx in range(NUM_BOARDS):
        if not bingo_tracker[idx]:  # check if the board already has bingo
            # check rows
            bingo_row_flag = False
            for i in range(NUM_ROWS):
                for j in range(NUM_COLUMNS):
                    if markings[idx][i][j] == "0":
                        break
                else:
                    bingo_row_flag = True
                    bingo_tracker[idx] = True

            # check columns
            if not bingo_row_flag:
                bingo_column_flag = False
                for j in range(NUM_COLUMNS):
                    for i in range(NUM_ROWS):
                        if markings[idx][i][j] == "0":
                            break
                    else:
                        bingo_column_flag = True
                        bingo_tracker[idx] = True


# Go through all the numbers and keep marking the boards and keep track of
# which boards hit bingo.
for n in NUMBERS:
    mark_boards(n, BOARDS, markings)
    is_bingo(BOARDS, markings)
    if bingo_tracker.count(True) == NUM_BOARDS - 1:
        # Get the index of the last board which is yet to hit bingo
        final_board_idx = bingo_tracker.index(False)
    if bingo_tracker.count(True) == NUM_BOARDS:
        # The last board has hit bingo!
        break


s = 0
for i in range(NUM_ROWS):
    for j in range(NUM_COLUMNS):
        if markings[final_board_idx][i][j] == "0":
            s += int(BOARDS[final_board_idx][i][j])

print(int(n) * s)
