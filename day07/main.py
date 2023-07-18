# Function to turn right by making three left turns
def turn_right():    
    turn_left()
    turn_left()
    turn_left()

# Move forward while the front is clear    
while front_is_clear():
    move()

# Turn left after reaching an obstacle or goal
turn_left()

# Continue moving until reaching the goal

while not at_goal():
    if right_is_clear():
        turn_right() # If there's a clear path to the right, turn right
        move()
    elif front_is_clear():
        move() # If the path is clear in front, move forward
    else:
        turn_left() # If there are obstacles on both the right and front, turn left