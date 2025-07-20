# 🐦 Flappy Bird – Built with Pygame

A fully functional clone of the classic Flappy Bird game, built using **Python** and **Pygame** in one continuous coding session (**9 hours and 38 minutes**). This project was developed using the **watch-and-learn** method from a YouTube tutorial by _Gameplay Artist_, where I carefully understood and recreated every piece of logic without copying code directly.

---

## 🎮 Gameplay Preview

▶️ [Watch Gameplay Video](assets/demo.mp4)

> _You can add a `.gif` or `.mp4` file here once available._

---

## 🚀 Features

- Smooth bird physics with gravity and jump mechanics
- Randomly generated pipe obstacles
- Collision detection with pipes and ground
- Score tracking system
- Sprite-based animations for bird and background
- Game over and restart logic

---

## 🛠️ Technologies Used

- **Python 3**
- **Pygame**
- Object-Oriented Programming (OOP)
- Custom class structures for modularity
- External asset handling for images and sounds

---

## 📚 What I Learned

This project provided several practical insights and deepened my understanding of:

### 🎯 Game Development Basics

- Constructing a game loop with proper frame management
- Handling events like key presses and game state transitions
- Managing in-game entities like the bird and pipes

### 🧠 Logic Building from Scratch

- I avoided shortcuts or built-in features and implemented:
  - Gravity and jumping
  - Pipe generation
  - Collision detection using bounding boxes
  - Score tracking logic

### 🖼️ Sprite and Asset Management

- Efficient loading of assets using relative paths
- Organizing sprite animations frame-by-frame
- Designing a clean layout and parallax scrolling background

### 🔁 Procedural Generation

- Dynamically generating pipes with randomized heights
- Managing off-screen elements for memory efficiency

### 🐞 Debugging and Optimization

- Identifying and fixing frame lag and logic bugs in real time
- Structuring the project into files like `main.py`, `bird.py`, `pipe.py` etc. for better scalability and maintenance

---

## 🧑‍🏫 Inspiration and Credits

Big thanks to **[Gameplay Artist](https://www.youtube.com/@GameplayArtist)** on YouTube for the structured and insightful walkthrough.

> I followed the _watch-and-learn_ approach — no code was copied directly. Instead, I rebuilt the project line-by-line, understanding and internalizing each concept.

---

## 💡 Future Improvements

Here are some features I may consider adding next:

- Background music and sound effects for jump, score, and collision
- Start screen and pause/resume functionality
- Save and display high scores locally
- Add increasing difficulty over time

---

## 🧩 Project Structure

```plaintext

Flappy-bird/
├── assets/ # Game assets: sprites, background, ground
│ ├── birdup.png
| ├── birddown.png
│ ├── pipeup.png
| ├── pipedown.png
│ ├── background.png
│ ├── ground.png
| └── font.ttf
├── bird.py # Bird class and logic
├── pipe.py # Pipe generation and movement logic
├── game.py # Game loop and main mechanics
└── README.md # Project documentation

## Install dependencies:

pip install pygame

## Run the game:

python game.py
```
