WIDTH = 1440
HEIGHT = 720
GRID_SIZE = 6  # 6x6 grid but we can change it to any size we want but it should be
               # a square grid so that we can easily calculate the number of mines and cells.
            
CELL_COUNT = GRID_SIZE ** 2 

# we can change the mines count by easy modrate and hard mode but it should 
# be less than the cell count otherwise the game will be impossible to win.
# MINES_COUNT = (CELL_COUNT) // 3 # hard mode
MINES_COUNT = (CELL_COUNT) // 5 # easy mode
