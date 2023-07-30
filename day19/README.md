# Dice-Roll game

## How the game works

* The roll_dice function takes num_dice and num_sides as arguments and uses a for loop to generate random rolls for the specified number of dice and sides. The rolls are stored in a list and returned.
* The display_rolls function takes the list of rolls and displays each roll in a formatted manner using a for loop.
* The game loop is created using a while loop, allowing the user to input the number of dice and sides. The roll_dice function is called to generate rolls, and the display_rolls function is used to show the results. The user is prompted to roll again or quit.
* The program includes a rolls_history list to store the history of rolls. 
* After each roll, the list of rolls is appended to the rolls_history list.
* The program displays the roll history after each roll, showing the user their previous rolls.
* The user can quit the game by typing "quit" instead of "n" when prompted to roll again.
