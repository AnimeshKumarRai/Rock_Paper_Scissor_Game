# Rock Paper Scissors Ultimate Game

A modern, feature-rich implementation of the classic Rock Paper Scissors game with power-ups, achievements, special moves, and multiple game modes.

[Play Game](https://github.com/AnimeshKumarRai/Rock_Paper_Scissor-Ultimate-Game) 
--
![HTML5](https://img.shields.io/badge/HTML5-orange) ![CSS3](https://img.shields.io/badge/CSS3-blue) ![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow) ![Responsive](https://img.shields.io/badge/Responsive-Yes-green)

## 🎮 Game Features

### Core Gameplay
- **Classic Rock Paper Scissors**: The timeless game you know and love
- **Multiple Game Modes**:
  - Classic: First to 5 points wins
  - Best of 5: Win 3 rounds to win the game
  - Endless: Play as long as you want without a winning condition
  - Battle: Use power-ups to defeat your opponent (first to 10 points)

### Power-ups System (Battle Mode)
- **Lightning**: 50% chance to win regardless of choice
- **Fire**: Beats rock and scissors
- **Ice**: Beats paper and scissors
- **Earth**: Beats rock and paper
- Power bars that fill up as you win rounds
- Earn power-ups when your power bar reaches 100%

### Special Moves
- **Well**: Beats rock and scissors, loses to paper
- **Dynamite**: Beats everything except well
- **Nuke**: Beats everything (can only be used once per game)

### Achievements System
- 10 different achievements to unlock:
  - First Victory: Win your first game
  - On Fire: Get a 3 game winning streak
  - Unstoppable: Get a 5 game winning streak
  - Perfect Game: Win without losing a round
  - Power User: Use all power-ups in a single game
  - Specialist: Use all special moves
  - Comeback Kid: Win after being down 0-2
  - Veteran: Play 50 games
  - Rock Paper Scissors Master: Win 25 games
  - Battle Master: Win a battle mode game

### Visual Features
- **Dark/Light Theme**: Toggle between themes with preference saved
- **Animations**: Bounce, shake, pulse, glow, and floating animations
- **Confetti Celebration**: Animated confetti when winning games
- **Visual Feedback**: Clear indicators for all game states and actions
- **Responsive Design**: Works perfectly on all device sizes

### Data Persistence
- Game statistics saved between sessions
- Achievement progress preserved
- Game history maintained
- Theme preference remembered

## 🚀 How to Play

### Basic Rules
1. Choose your move: Rock, Paper, or Scissors
2. Rock beats Scissors, Scissors beats Paper, Paper beats Rock
3. First player to reach the target score wins (depends on game mode)

### Special Moves Rules
- **Well**: Beats rock and scissors, loses to paper
- **Dynamite**: Beats everything except well
- **Nuke**: Beats everything (limited to one use per game)

### Power-ups (Battle Mode)
1. Power-ups are earned when your power bar reaches 100%
2. Click a power-up button to activate it before making your move
3. Each power-up has a unique effect that can influence the game outcome

## 🛠️ Technologies Used

- **HTML5**: For the game structure and semantic markup
- **CSS3**: For styling, animations, and responsive design (including Tailwind CSS)
- **JavaScript (ES6)**: For game logic, interactivity, and data management
- **Font Awesome**: For icons and visual elements
- **LocalStorage**: For data persistence between sessions

## 📱 Installation

To run this game locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/AnimeshKumarRai/Rock_Paper_Scissor-Ultimate-Game.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Rock_Paper_Scissor-Ultimate-Game
   ```


## 🎯 Game Mechanics

### Scoring System
- Points are awarded for winning rounds
- No points for draws or losses
- Target score depends on game mode:
  - Classic: First to 5 points
  - Best of 5: First to 3 points
  - Battle: First to 10 points
  - Endless: No target score

### Power System (Battle Mode)
- Power bars fill up as you win rounds
- Win streaks fill the bar faster
- When your power bar reaches 100%, you earn a power-up
- Power-ups can be activated before making your move

### Achievement System
- Achievements are unlocked based on various accomplishments
- Progress is tracked and saved between sessions
- Notifications appear when achievements are unlocked

## 🎨 Customization

To customize the game:

1. **Colors**: Modify the CSS variables and Tailwind classes:
   ```css
   .bg-gradient-to-r.from-purple-500.to-blue-500 {
       background: linear-gradient(to right, #your-color, #your-color);
   }
   ```

2. **Game Modes**: Adjust the parameters in the `setGameMode()` function:
   ```javascript
   case 'classic':
       gameInfo.textContent = 'First to 5 points wins the game!';
       break;
   ```

3. **Power-ups**: Modify power-up effects in the `determineWinner()` function:
   ```javascript
   case 'lightning':
       if (Math.random() < 0.5) {
           userBonus = 1;
       }
       break;
   ```

4. **Achievements**: Add new achievements to the `achievements` object:
   ```javascript
   newAchievement: { 
       name: "Achievement Name", 
       description: "Achievement description", 
       unlocked: false 
   }
   ```

## 🤝 Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👏 Acknowledgments

- [Tailwind CSS](https://tailwindcss.com/) for the utility-first CSS framework
- [Font Awesome](https://fontawesome.com/) for the icon library
- [Google Fonts](https://fonts.google.com/) for fonts used in the project

## 📧 Contact
---

Enjoy the game! 🎮✨
