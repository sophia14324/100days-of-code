import random # generates a series of random letters, numbers, symbols from a list

# create a list of characters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '-', '`', '?', '<', '>']

# input the desired password criteria
print("Welcome to the PyPassword Generator!")
pw_letters = (input("How many letters would you like in your password?\n"))
pw_numbers = (input(f"How many numbers would you like?\n"))
pw_symbols = (input(f"How many symbols would you like?\n"))

# validate user input
if not pw_letters.isdigit() or not pw_numbers.isdigit() or not pw_symbols.isdigit():
    print("Invalid value, enter  number instead.")
else:
    password = []

# alternative to the above code
'''
try:
    pw_letters = int(input("How many letters would you like in your password?\n"))
    pw_numbers = int(input("How many numbers would you like?\n"))
    pw_symbols = int(input("How many symbols would you like?\n"))
except ValueError:
    print("Invalid value, enter a number instead.")
else:
    password = []
'''

for i in range(0, int(pw_letters)): #the range() functon requires integer arguments
    random_letter = random.randint(0,51)
    password.append(letters[random_letter])

for i in range(0, int(pw_numbers)):
    random_number = random.randint(0,9)
    password.append(numbers[random_number])

for i in range(0, int(pw_symbols)):
    random_symbol = random.randint(0,14)
    password.append(symbols[random_symbol])

# shuffle the password
random.shuffle(password)
print(f"Here is your password: {''.join(password)}")

# assess password strength and provide feedback
if len(password) <= 6:
    print(f"Your password is weak, try to include at least 8 characters for a stronger password.")
elif len(password) == 7:
    print(f"Your password is of medium strength.")
else: 
    print("Your password is strong.")