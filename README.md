# Asteroids Clone

A Python implementation of the classic Asteroids arcade game using Pygame.

## Description

This game is a recreation of the 1979 classic arcade game Asteroids. Players control a spaceship in an asteroid field, shooting and destroying asteroids while avoiding collisions.

## Features

- Spaceship movement with realistic momentum-based physics
- Asteroid splitting mechanics when shot
- Progressive difficulty as asteroids break into smaller, faster pieces
- Vector-based collision detection
- Classic arcade-style graphics

## Requirements

- Python 3.x
- Pygame

## Installation

1. Create and activate a virtual environment:
```bash
# Create venv
python -m venv venv

# Activate on Windows
venv\Scripts\activate
# OR on Unix/MacOS
source venv/bin/activate
```

2. Install required packages:
```bash
pip install pygame
```

3. Run the game:
```bash
python game.py
```

## Controls

- Arrow keys: Rotate and thrust spaceship
- Spacebar: Fire bullets
- Esc: Quit game

## Development Notes

### Recent Updates
- Implemented asteroid splitting mechanics
- Added size-based fragmentation logic
- Fixed performance issues with clean venv setup

### Performance Considerations
If experiencing performance issues:
1. Ensure you're running in a clean virtual environment
2. Verify Pygame is properly installed
3. Close resource-intensive background applications

## Contributing

Feel free to fork this repository and submit pull requests for any improvements.

## License

[Add your chosen license here]