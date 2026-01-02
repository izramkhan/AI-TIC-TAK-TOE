# AI Tic Tac Toe

A modern, AI-powered Tic Tac Toe game built with Python and Tkinter. Play against an intelligent opponent with sound effects and score tracking.

## Features

- **AI Opponent**: Smart AI that plays optimally using the minimax algorithm
- **Sound Effects**: Win and lose audio feedback for enhanced gameplay
- **Score Tracking**: Keep track of total games, wins, losses, and draws
- **Modern UI**: Clean, colorful interface built with Tkinter
- **Game Reset**: Easy restart and score reset functionality
- **Responsive Design**: Smooth gameplay with no lag

## Installation

### Prerequisites
- Python 3.8 or higher

### Setup

1. Clone the repository:
```bash
git clone https://github.com/izramkhan/AI-TIC-TAK-TOE.git
cd AI-TIC-TAK-TOE
```

2. Install required dependencies:
```bash
pip install pygame
```

3. Ensure audio files are in the project directory:
   - `winner_sound.mp3`
   - `loser_sound.mp3`
   - `draw_sound.mp3`

4. (Optional) Add a window icon:
   - Place `tic_tac_toe.ico` in the project directory

## Usage

Run the application:
```bash
python main.py
```

### How to Play

1. Click on any empty square to make your move (X)
1. The AI will automatically respond with its move (O)
1. Use **Restart** to play a new game
1. Use **Reset Score** to clear all statistics

## Project Structure

```
AI-Tic-Tac-Toe/
├── main.py              # Main GUI and game interface
├── game_logic.py        # Game logic and AI algorithm
├── winner_sound.mp3     # Win sound effect
├── loser_sound.mp3      # Lose sound effect
|── draw_sound.mp3       # Draw sound effet
├── tic_tac_toe.ico      # Window icon (optional)
└── README.md            # Project documentation
```

## Files Description

### main.py
The main application file containing:
- Tkinter GUI setup and layout
- Button event handlers
- Score tracking and updates
- Sound effect integration

### game_logic.py
Game logic module containing:
- Board management
- Win condition checking
- Draw detection
- AI move calculation using optimal strategy

## Requirements

- `tkinter` (included with Python)
- `pygame` (for audio playback)

Install pygame:
```bash
pip install pygame
```

## Future Enhancements

- Difficulty levels (Easy, Medium, Hard)
- Player vs Player mode
- Game history and statistics
- Undo move functionality
- Customizable themes

## License

This project is open source. Feel free to use, modify, and distribute it as you wish.

**Created by**: Izram Khan  
**Date**: January 2, 2026

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests
- Improve documentation

## Support

If you encounter any issues, please:
1. Check that all audio files are in `.mp3` format
2. Ensure Pygame is properly installed
3. Verify Python version is 3.8 or higher
4. Open an issue on GitHub with detailed description

## Acknowledgments

This project demonstrates:
- GUI development with Tkinter
- Game logic implementation
- AI algorithm optimization
- Audio integration in Python applications

---

**Enjoy the game! Can you beat the AI? 🎮**
