import game_logic
import tkinter as tk
import pygame

# Create main window
def play_game():
    root = tk.Tk()
    root.title("AI Tic Tac Toe")
    root.geometry("400x480")
    root.resizable(False, False)
    root.configure(bg="#1a1a2e")  # Dark blue-gray background
    root.iconbitmap('logo.ico')

    # Status label
    status_label = tk.Label(root, text="Your turn", font=("Impact", 16), bg="#16c784", fg="#ffffff")
    status_label.pack(pady=10, fill='x')

    # Frame for buttons
    button_frame = tk.Frame(root, bg="#1a1a2e")
    button_frame.pack()

    global total_games, player_wins, ai_wins, draws
    total_games = 0
    player_wins = 0
    ai_wins = 0
    draws = 0

    score_label = tk.Label(
        root,
        text="Games: 0  |  You: 0  |  AI: 0  | Draws: 0",
        font=("Segoe print", 12),
        bg = "#1779f0"
    )
    score_label.pack(fill='x')

    # Initilyzing mixer for sound effects
    pygame.mixer.init()
    win_sound = pygame.mixer.Sound('winner_sound.mp3')
    lose_sound = pygame.mixer.Sound('loser_sound.mp3')
    draw_sound = pygame.mixer.Sound('draw_sound.mp3')

    # Function for player move
    def on_button_click(index):

        if game_logic.board[index] != ' ':
            return
        
        game_logic.board[index] = 'X'
        buttons[index // 3][index % 3].config(text='X', state='disabled', fg="#2980b9", bg="#00d4ff")

        if game_logic.check_winner('X'):
            status_label.config(text='YOU WIN!')
            update_score(player=True)
            win_sound.play()
            disable_all()
            return

        if game_logic.is_draw():
            status_label.config(text='Draw!')
            update_score(draw=True)
            draw_sound.play()
            return

        status_label.config(text="AI thinking...")
        root.after(1000, ai_move)

    # Function for AI move
    def ai_move():
        game_logic.win_or_block()

        for i in range(9):
            if game_logic.board[i] == 'O':
                buttons[i // 3][i % 3].config(text='O', state='disabled', bg="#ffd60a", fg="#2980b9")

        if game_logic.check_winner('O'):
            status_label.config(text='AI WINS!')
            update_score(ai=True)
            lose_sound.play()
            disable_all()
            return

        if game_logic.is_draw():
            status_label.config(text='Draw!')
            update_score(draw=True)
            draw_sound.play()

        status_label.config(text='Your turn')

    # Function to disable all when the game is finished
    def disable_all():
        for row in buttons:
            for btn in row:
                btn.config(state='disabled')

    # Update score after each game
    def update_score(player=False, ai=False, draw=False):
        global total_games, player_wins, ai_wins, draws

        total_games += 1
        if player:
            player_wins += 1
        elif ai:
            ai_wins += 1
        elif draw:
            draws += 1

        score_label.config(
            text=f"Games: {total_games} | You: {player_wins} | AI: {ai_wins} | Draws: {draws}"
        )

    def reset_board():
        game_logic.board[:] = [' '] * 9
        for row in buttons:
            for btn in row:
                btn.config(text="", state="normal", bg='white')
        status_label.config(text="Your turn") 

    def reset_data():
        global total_games, player_wins, ai_wins, draws
        total_games = 0
        player_wins = 0
        ai_wins = 0
        draws = 0

        score_label.config(
            text=f"Games: {total_games} | You: {player_wins} | AI: {ai_wins} | Draws: {draws}"
        )

    # Only part I didn't understood and used A.I
    buttons = [[None for _ in range(3)] for _ in range(3)]

    for row in range(3):
        for col in range(3):
            index = row * 3 + col
            btn = tk.Button(
                button_frame,
                text='',
                font=('Arial', 24),
                bg="#ecf0f1",      # light gray button background
                fg="black",
                activebackground="#3498db",  # bright blue when pressed
                activeforeground="white",
                width=5,
                height=2,
                command=lambda i=index: on_button_click(i)
            )
            btn.grid(row=row, column=col, padx=5, pady=5)
            buttons[row][col] = btn

    # Frame for bottom buttons
    bottom_frame = tk.Frame(root, bg="#1a1a2e")
    bottom_frame.pack(pady=10)

    # Restart button
    reset_btn = tk.Button(
        bottom_frame,
        text="Restart", 
        font=("Segoe print", 14),
        bg="#e94560",
        fg="white",
        command=reset_board
    )
    reset_btn.pack(side='left', padx=5)

    # Reset score button
    reset_score_btn = tk.Button(
        bottom_frame, 
        text='Reset Score',
        font=('Segoe print', 9),
        bg='red',
        fg='white',
        command=reset_data
    )
    reset_score_btn.pack(side='left', padx=5)

    root.mainloop()
