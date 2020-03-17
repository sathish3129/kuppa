# tic-tac-toe
from IPython.display import clear_output

grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
done = False
player = 1


def is_done(v='X'):
    if v == 9:
        for i in enumerate(grid):
            print("|".join(i[1]))
        if len(grid) - 1 != i[0]: print('-' * 5)

        return True
    return False


print('Welcome to Tic Tac Toe!')
while not done:
    clear_output()
    for i in enumerate(grid):
        print("|".join(i[1]))
        if len(grid) - 1 != i[0]: print('-' * 5)

    print("Player {}'s input:".format(player))
    try:
        value = int(input())
    except ValueError:
        print("Could not convert data to an integer.try again..")
        continue
    if value > 9:
        print("input is out of range. try again..")
        continue

    print(value)
    done = is_done(value)
    if player > 1:
        player -= 1
    else:
        player += 1

print("Done")

'''
while not done:
    for i in enumerate(grid):
        print("|".join(i[1]))
        if len(grid) - 1 != i[0]: print('-' * 5)

    done = is_done()
'''
