from tkinter import *
from cell import Cell
import settings
import utils
root = Tk()
#override the settings of the window 
root.configure(bg= "black")
# root.geometry("Width x Hight ")

root.geometry(f"{settings.WIDTH}x{settings.HEIGHT}")
root.title("MineSweeper Game")
# root.resizable(False, False)  comminting this line because it is going more than my laptop screen pixels 
def restart_game():
    Cell.restart_game(root, center_frame, left_frame)
top_frame = Frame(
    root,
    bg= "black", 
    width=settings.WIDTH,
    height=utils. height_perc(25)
)
top_frame.place(x=0, y=0)

game_title = Label(
    top_frame,
    bg="black",
    text= "MInesweeper Game",
    font= ("", 48)
)
game_title.place(
    x= utils.width_perc(25),  y=0
)

# RESTART BUTTON
restart_btn = Button(
    top_frame,
    text="Restart",
    font=("", 16),
    bg="green",
    fg="white",
    width=10,
    height=2,
    command=restart_game
)
restart_btn.place(x=utils.width_perc(80), y=10)

# Create timer label
Cell.create_timer_label(top_frame)
Cell.timer_label_object.place(x=utils.width_perc(5), y=10)


# Create flag counter label 
Cell.create_flag_count_label(top_frame)
Cell.flag_count_label_object.place(x=0, y= 50) # Below cells left 


left_frame = Frame(
    root,
    bg= "black",
    width =utils.width_perc(25),
    height = utils.height_perc(75)
)
left_frame.place(x=0, y=utils.height_perc(25))

center_frame = Frame(
    root,
    bg= "black",
    width= utils.width_perc(75),
    height= utils.height_perc(75)
)
center_frame.place(
    x=utils.width_perc(25),
    y=utils.height_perc(25)  
)

# c1 = cell()
# c1.create_btn_object(center_frame)
# c1.cell_btn_object.place(
#     x= 0 , y= 0
# )

# c2 = cell()
# c2.create_btn_object(center_frame)
# c2.cell_btn_object.place(
#     x=40, y=0
# )

# we can create this by using grid mathod by row opration by removing the place funtion 


# c1 = cell()
# c1.create_btn_object(center_frame)
# c1.cell_btn_object.grid(
#     column=0 , row= 0 # because in python the index start from the 0
# )

# c2 = cell()
# c2.create_btn_object(center_frame)
# c2.cell_btn_object.grid(
#     column= 0, row=1
# )


#  doing this for multiple times is headace so to prevent this we use the for loop 

for x in range (settings.GRID_SIZE):
    for y in range (settings.GRID_SIZE):
        c= Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x , row=y
        )
Cell.randomize_mines()

# Call the label from Cell class 
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(
        x=0, y=0
)

        
print(Cell.all)
# Run the window 
root.mainloop()