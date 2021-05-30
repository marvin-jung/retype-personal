---
icon: hubot
---

# Yoshimi Battles the Pink Robot

Jisung Jung

Users can play this Text Adventure Game in the [following notebook](https://colab.research.google.com/drive/1Zlr5qVcj5Pvwz4yfTi3z39porB4RMJjG?usp=sharing)

Original Python script - [Yoshimi-battles-the-pink-robot.py](scripts/Yoshimi-battles-the-pink-robot.py)

Its game story and characters are inspired from 'Yoshimi Battles the Pink Robots' album recorded by The Flaming Lips.

![](images/Album-covers.jpg)

You're getting into a future world, also you will meet a nearest and dearest friend of Yoshimi. As you expected from the game title, you will be in a danger and experienced a series of threats from artificial intelligence machines. Together with your friend Yoshimi, the pair must clear the four main quests (including bonus stage).

- Quest 1: Choose from the options
- Quest 2: Win the enemies with a random skill guess
- Quest 3: True or False guess game
- Bonus Quest: Number Guess game

**Known Bugs and/or Errors**

- quit() or exit() funtion can't work in the Jupyter Notebook After a user failed the game, 'Would you like to play again? ( Yes / No )' message keeps looping although he/she entered 'No'. (But, No bug happened on the Powershell Prompt)
- Although a user takes the victory of the game, the quiz input message keeps looping. Therefore, the user must interrupt kernel after the final victory. (But, No bug happened on the Powershell Prompt)