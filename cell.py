from tkinter import Button, Label
import random
import settings
import ctypes
import sys


class Cell:
    all = []
    cell_count = settings.CELL_COUNT
    cell_count_label_object = None
    
    # TIMER VARIABLES - ADDED (Lines 13-15)
    timer_label_object = None
    start_time = 0
    timer_running = False
    game_started = False
    timer_running = False
    flag_count = 0  # Track flags placed
    flag_count_label_object = None  # Label to display
    
    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.is_opened = False
        self.is_mine_candidate = False
        self.cell_btn_object = None
        self.x = x
        self.y = y
        
        # Append the object to the cell.all list
        Cell.all.append(self)
        
    def create_btn_object(self, location):
        btn = Button(
            location,
            width=12,
            height=4,
        )
        btn.bind("<Button-1>", self.let_click_actions)
        btn.bind("<Button-3>", self.right_click_actions)
        self.cell_btn_object = btn
        
    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            bg="black",
            fg="white",
            text=f"Cells Left {Cell.cell_count}",
            font=("", 28)
        )
        Cell.cell_count_label_object = lbl
    
    def let_click_actions(self, event):
        # START TIMER ON FIRST CLICK - ADDED (Lines 39-42)
        if not Cell.timer_running and not Cell.game_started:
            Cell.game_started = True
            Cell.start_timer()
        
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mines_length == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()
            
            # STOP TIMER ON WIN - ADDED (Line 54)
            if Cell.cell_count == settings.MINES_COUNT:
                Cell.stop_timer()
                ctypes.windll.user32.MessageBoxW(0, "Congratulation! You won the game!", "Game Over", 0)
                
            # Cancel left and right event if cell is already opened
            self.cell_btn_object.unbind("<Button-1>")
            self.cell_btn_object.unbind("<Button-3>")
            
    def get_cell_by_axis(self, x, y):
        # Return a cell object based on the value x,y
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell
        return None
    
    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1),
        ]
        cells = [cell for cell in cells if cell is not None]
        return cells
    
    @property
    def surrounded_cells_mines_length(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1
        return counter
                                           
    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -= 1
            
            # COLORS FOR NUMBERS - YOUR EXISTING CODE
            colors = {
                0: "black",
                1: "blue", 
                2: "green",
                3: "red",
                4: "purple",
                5: "maroon",
                6: "turquoise",
                7: "black",
                8: "gray"
            }
            
            mine_count = self.surrounded_cells_mines_length
            
            self.cell_btn_object.configure(
                text=mine_count,
                fg=colors.get(mine_count, "black")
            )
            
            # Replace the text of cell count label with the newer count
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                    text=f"Cells Left {Cell.cell_count}"
                )
                
            # If this was a mine candidate, reset background color
            self.cell_btn_object.configure(bg="SystemButtonFace")
                
        # Mark the cell as opened
        self.is_opened = True
    
    def show_mine(self):
        self.cell_btn_object.configure(bg="red", text="Mine")
        # show all others mine  after loosing 
        for cell in Cell.all:
            if cell.is_mine and cell != self:
                cell.cell_btn_object.configure(bg= "red", text = "*")
            
            elif not cell.is_mine and not cell.is_opened:
                # Reveal unopen safe cells in gray 
                cell.cell_btn_object.configure(
                    text= cell.surrounded_cells_mines_length, fg= "gray"
                )             
           
        Cell.stop_timer()  # STOP TIMER ON LOSE - ADDED (Line 121)
        
        # Delay the game over message to ensure the last cell updates are visible
        self.cell_btn_object.after(200, self._show_game_over_message)
        def _show_game_over_message(self):
            """separate method to show message box after delay"""
            ctypes.windll.user32.MessageBoxW(0, "You clicked on mine", "Game Over", 0)
            Cell.disable_all_buttons() # Disable all buttons after game over
        
        
    def right_click_actions(self, event):
        if not self.is_opened:
            if not self.is_mine_candidate:
                self.cell_btn_object.configure(bg="orange")
                self.is_mine_candidate = True
                Cell.flag_count += 1  # Increment flag count
            else:
                self.cell_btn_object.configure(bg="SystemButtonFace")
                self.is_mine_candidate = False
                Cell.flag_count -= 1  # Decrement flag count
                
                # Update flag count label
                
            if Cell.flag_count_label_object:
                remaining = settings.MINES_COUNT - Cell.flag_count
                Cell.flag_count_label_object.configure(
                    text= f"Mines Left: {remaining}"
                    )
                
    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(
            Cell.all, settings.MINES_COUNT
        )
        for picked_cell in picked_cells:
            picked_cell.is_mine = True
            
    @staticmethod
    def restart_game(root, center_frame, left_frame):
        """Restart the game without closing window"""
        # Clear old cells
        for cell in Cell.all:
            cell.cell_btn_object.destroy()
        
        Cell.all = []
        Cell.cell_count = settings.CELL_COUNT
        
        # Reset flag count
        Cell.flag_count = 0  
        if Cell.flag_count_label_object:
            Cell.flag_count_label_object.configure(
                text= f"Mines Left: {settings.MINES_COUNT}"
            )
        
        # RESET TIMER - ADDED (Lines 155-158)
        Cell.stop_timer()
        Cell.game_started = False
        if Cell.timer_label_object:
            Cell.timer_label_object.configure(text="Time: 0")
        
        # Remove old label
        if Cell.cell_count_label_object:
            Cell.cell_count_label_object.destroy()
        
        # Create new cells
        for x in range(settings.GRID_SIZE):
            for y in range(settings.GRID_SIZE):
                c = Cell(x, y)
                c.create_btn_object(center_frame)
                c.cell_btn_object.grid(column=x, row=y)
        
        # New mines
        Cell.randomize_mines()
        
        # New label
        Cell.create_cell_count_label(left_frame)
        Cell.cell_count_label_object.place(x=0, y=0)
    
    # ==================== TIMER METHODS - ADDED (Lines 180-210) ====================
    
    @staticmethod
    def create_timer_label(location):
        """Create timer label in top frame"""
        lbl = Label(
            location,
            bg="black",
            fg="white",
            text="Time: 0",
            font=("", 28)
        )
        Cell.timer_label_object = lbl
        return lbl
    
    @staticmethod
    def start_timer():
        """Start the game timer"""
        if not Cell.timer_running:
            Cell.start_time = 0
            Cell.timer_running = True
            Cell.update_timer()
    
    @staticmethod
       
    def update_timer():
        if Cell.timer_running and Cell.timer_label_object:
            Cell.start_time += 1
            minutes = Cell.start_time // 60
            seconds = Cell.start_time % 60
            Cell.timer_label_object.configure(text=f"Time: {minutes:02d}:{seconds:02d}")
            Cell.timer_label_object.after(1000, Cell.update_timer)
    
    @staticmethod
    def stop_timer():
        """Stop the game timer"""
        Cell.timer_running = False
        
        
    # Disable all buttons (used after game over)
    @staticmethod
    def disable_all_buttons():
        """Disable all cell buttons when game ends"""
        for cell in Cell.all:
            cell.cell_btn_object.unbind("<Button-1>")
            cell.cell_btn_object.unbind("<Button-3>")
            
            
            
    
    #  Flag Counter Method 
    
   
    @staticmethod
    def create_flag_count_label(location):
        """Create flag counter label"""
        lbl = Label(
            location,
            bg="black",
            fg="white",
            text=f"Mines Left: {settings.MINES_COUNT}",
            font=("", 28)
        )
        Cell.flag_count_label_object = lbl
        return lbl
    
    
    
    def __repr__(self):
        return f"Cell({self.x}, {self.y})"