# 🎉 Fun With Python

Welcome to **Fun With Python** — a creative collection of beginner-to-intermediate level Python mini projects that blend learning with fun! Each project in this repository is designed to sharpen your core Python skills while building interactive and enjoyable programs.

Whether you're generating secure passwords, guessing random numbers, playing Rock-Paper-Scissors, or building GUI tools using `tkinter`, this repo has something for every Python enthusiast.

Perfect for students, hobbyists, or anyone starting their Python journey.

---

## 📁 Project Descriptions

### 1. 🎯 floating_button_game.py  
A fun and interactive Tkinter-based GUI project that displays a window asking the user:  
_"Are you free to talk?"_  
It has two buttons: **Yes** and **No**. When the user tries to hover over the **No** button, it randomly moves to a different location on the screen, making it unclickable. Clicking **Yes** opens a popup thanking the user. This project demonstrates event handling and dynamic button movement using `tkinter` and `random`.

---

### 2. 🔐 password_generator.py  
This command-line program generates a secure random password of any desired length.  
It uses a mix of uppercase letters, lowercase letters, and digits. The user inputs the desired length, and the program prints a strong password using the `random` and `string` modules. A great example of using loops, character sets, and input/output interaction.

---

### 3. 🔢 number_guessing_game.py  
A console-based number guessing game.  
The program selects a random number between 1 and 50. The user tries to guess it, and the program provides hints such as:
- “Too high”
- “Too low”
- “Very close”
- “Closer than last guess”  

It also gives feedback based on the number of attempts taken. This project is ideal for practicing loops, conditionals, random numbers, and user input handling.

---

### 4. ⏱️ countdown_timer_gui.py  
A graphical countdown timer with a simple user interface built using `tkinter`.  
The user enters time in seconds, and clicks **Start Countdown**. A large timer appears along with a progress bar that fills as the time elapses. Includes **Pause** and **Reset** buttons and plays a sound when the timer ends (Windows only via `winsound`). Demonstrates GUI design, multithreading, and real-time updates.

---

### 5. ✊✋✌️ rock_paper_scissors.py  
A console-based **Rock-Paper-Scissors** game where the user competes against the computer in a best-of-five format. Each round, both the user and the computer choose between "rock", "paper", or "scissors". The game applies standard rules:

- Rock beats Scissors  
- Scissors beats Paper  
- Paper beats Rock  

It keeps track of the scores and displays:
- Who won the round
- Updated scores after each round
- Final game winner (first to 5 points)

**Highlights:**
- Uses `random.choice()` for computer input  
- Validates user input with a loop  
- Implements game logic with conditional statements  
- Modular functions for scoring, displaying results, and declaring winner  

This project is a great exercise in input validation, loop control, and game logic using Python basics.

---
