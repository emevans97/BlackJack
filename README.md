# BlackJack
OOP practice

Single player game vs the computer, enjoy!

## Deck.py
* Handles playing cards ♠️♥️♦️♣️
* Stores cards in embedded list, aces given extra element for scoring high 🙌 or low ⬇️
* Returns cards at random from deck, removes them from deck so can't be drawn again

## Main.py
* Handles game logic 🧩
* Initialises other classes, holds twist logic 🌪️
* Checks for outcome vs computer 🏆

## Player.py
* Player has a hand and score 
* Cards are dealt to start and added to hand if we twist
* Score is calculated, if over 21 we check for aces and change to low, until score is under 21 
* Score uses recursive function to check for changing aces to low 😎
