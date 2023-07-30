import random
import os

rolls_history = []

def roll_dice(num_dice, num_sides):
    """Rolls specified number of dice with specified number of sides"""
    rolls = []
    for i in range(num_dice):
        roll = random.randint(1, num_sides)
        rolls.append(roll)
    rolls_history.append(rolls)
    return rolls

def display_rolls(rolls):
    """Displays the rolls in a formatted manner"""
    for roll in rolls:
        print("Roll:", roll)

def save_history():
    """save the rolls history to a file"""
    with open("rolls_history.txt", "w") as file:
        for rolls in rolls_history:
            file.write(str(rolls) + "\n")
    print("Rolls history saved to rolls_history.txt")

def clear_history():
    """clear the rolls history"""
    global rolls_history
    rolls_history = []
    print("Rolls history cleared.")

while True:
    dice_input = input("Enter the number of dice and number of sides for each die (ex: 2d6): ")
    if dice_input == "quit":
        break
    else:
        dice_list = dice_input.split("d")
        num_dice = int(dice_list[0])
        num_sides = int(dice_list[1])
        rolls = roll_dice(num_dice, num_sides)
        display_rolls(rolls)
        print("Rolls history:", rolls_history)
        action = input("Enter 'save' to save the rolls history, 'clear' to clear the history, or any other key to continue: ")
        if action == "save":
            save_history()
        elif action == "clear":
            clear_history()
        play_again = input("Would you like to roll again? (y/n) ")
        if play_again.lower() != "y":
            break
