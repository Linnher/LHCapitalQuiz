# Base component for the Capital Cities Quiz
# Version Two - Adding in Question Generator

# Author - Linn Herzig
# LH 2022

# Import libraries below this line **************************
from string import ascii_lowercase


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


# Lists below this line ******************************
# List of Questions
questions_list = {
    "What is the capital city of Italy?": [
        "Rome", "Milan", "Florence"
    ],
    "What is the capital city of France?": [
        "Paris", "Nice", "Bordeaux"
    ],
    "What is the capital city of Germany?": [
        "Berlin", "Hamburg", "Frankfurt"
    ],
    "What is the capital city of Switzerland?": [
        "Bern", "Zurich", "Geneva"
    ],
    "What is the capital city of the Netherlands?": [
        "Amsterdam", "Utrecht", "Rotterdam"
    ],
}

# Main Routine below this line ******************************
print("\nWelcome to the Capital Cities of Europe Quiz Game!")
# Asking user if they want to see instructions
show_instructions = yesno("\nWould you like to view the instructions? ")

if show_instructions == "yes":
    instructions()

# Displaying the question number and asking the user the quiz question:
for num, (question, possible_answer) in enumerate(questions_list.items(), start=1):
    print(f"\nQuestion {num}:")
    print(f"{question}")
    right_answer = possible_answer[0]
    # Ordering the possible answers:
    ordered_answers = dict(zip(ascii_lowercase, sorted(possible_answer)))
    for tag, option in ordered_answers.items():
        print(f" {tag}) {option}")

    # Asking the user for their answer:
    answer_tag = input("\nYour answer? ")
    answer = ordered_answers.get(answer_tag)

    # Communicating the results with the user:
    if answer == right_answer:
        print("Congratulations you are correct!")
    else:
        print(f"Sadly you answered incorrectly. You chose {answer}, however, the correct answer was {right_answer}.")
