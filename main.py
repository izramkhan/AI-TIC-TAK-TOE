import gui

if __name__ == '__main__':
    gui.play_game()

#----------------------------------------------------------------------------------------------------
# Created by: Izram Khan
# Date completed: 2-Jan-2026
# Licensed: This is an open source game use it or modify it. It's all yours
#----------------------------------------------------------------------------------------------------

# Q: What is happening at (23 - 27) in game_logic.py

# Ans: In line 20 all the cells that are empty are filtered in empty_cells. The whole loop runs
# on the empty cells if any win combos are found with 'O' It will keep it and will make all other
# cells empty. Same thing is happening in (30 - 35)