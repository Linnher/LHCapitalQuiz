# Base component for the Capital Cities Quiz
# Version One - Adding in the Yes / No Checker

# Author - Linn Herzig
# LH 2022

# Import libraries below this line **************************

# All Functions below this line ******************************
# Function to check  whether the user input to the instructions question is valid
def yesno(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("This is an invalid value. Please answer yes or no.")


# Function for displaying the instructions.
def instructions():
    print()
    print("**** How to Play ****")
    print(" - Every round consists of five questions.")
    print(" - Each question will have three possible answers either a, b or c.")
    print(" - To answer the question please press the corresponding letter on the keyboard.")
    return""


# Main Routine below this line ******************************
print("Welcome to the Capital Cities Quiz Game!")
# Asking user if they want to see instructions
show_instructions = yesno("Would you like to view the instructions? ")

if show_instructions == "yes":
    instructions()