#tic-tac-toe

grid = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
done = False
while !done:
    for i in enumerate(grid):
        print("|".join(i[1]))
        if len(grid)-1 !=i[0]: print('-' *5)
    
    done=is_done()

