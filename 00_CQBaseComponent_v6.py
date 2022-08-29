# Base component for the Capital Cities Quiz
# Version Six - Adding in the Play Again Component

# Author - Linn Herzig
# LH 2022

# Import libraries below this line **************************
import random
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
    "What is the capital city of Spain?": [
        "Barcelona", "Madrid", "Valencia"
    ],
    "What is the capital city of England?": [
        "London", "Manchester", "Birmingham"
    ],
    "What is the capital city of Sweden?": [
        "Stockholm", "Gothenburg", "Malmo"
    ],
    "What is the capital city of Austria?": [
        "Vienna", "Salzburg", "Linz"
    ],
    "What is the capital city of Portugal?": [
        "Lisbon", "Porto", "Braga"
    ],
    "What is the capital city of Greece?": [
        "Athens", "Sparta", "Santorini"
    ],
    "What is the capital city of Serbia?": [
        "Belgrade", "Novi Sad", "Kraljevo"
    ],
    "What is the capital city of Slovakia?": [
        "Bratislava", "Levoca", "Bradejov"
    ],
    "What is the capital city of Belgium?": [
        "Brussels", "Bruges", "Antwerp"
    ],
    "What is the capital city of Romania?": [
        "Bucharest", "Brasov", "Timisoara"
    ],
    "What is the capital city of Hungary?": [
        "Budapest", "Porto", "Braga"
    ],
    "What is the capital city of Bulgaria?": [
        "Sofia", "Plovdiv", "Varna"
    ],
    "What is the capital city of Croatia ?": [
        "Zagreb", "Dubrovnik", "Split"
    ],
    "What is the capital city of Malta?": [
        "Valletta", "Mdina", "Birgu"
    ],
    "What is the capital city of Iceland?": [
        "Reykjavik", "Akureyri", "Kopavogur"
    ],
    "What is the capital city of Estonia?": [
        "Tallinn", "Narva", "Tartu"
    ],
    "What is the capital city of Latvia?": [
        "Riga", "Liepaja", "Jelgava"
    ],
    "What is the capital city of Lithuania?": [
        "Vilnius", "Kaunas", "Klaipeda"
    ],
    "What is the capital city of Ukraine?": [
        "Kyiv", "Kharkiv", "Mariupol"
    ],
    "What is the capital city of Poland?": [
        "Warsaw", "Krakow", "Wroclaw"
    ],
    "What is the capital city of Denmark?": [
        "Copenhagen", "Aarhus", "Aalborg"
    ],
    "What is the capital city of Finland?": [
        "Helsinki", "Tampere", "Turku"
    ],
    "What is the capital city of Norway?": [
        "Oslo", "Bergen", "Trondheim"
    ],
    "What is the capital city of Slovenia?": [
        "Ljubljana", "Kranj", "Piran"
    ],
    "What is the capital city of Liechtenstein?": [
        "Vaduz", "Schaan", "Triesenberg"
    ],
}

# Main Routine below this line ******************************
# Initiating Variables:
play_again = True
invalid = False
questions_per_round = 5

print("\nWelcome to the Capital Cities of Europe Quiz Game!")
# Asking user if they want to see instructions
show_instructions = yesno("\nWould you like to view the instructions? ")

if show_instructions == "yes":
    instructions()

while play_again:
    # Initiating Variables:
    score = 0

    num_of_questions = min(questions_per_round, len(questions_list))
    questions = random.sample(list(questions_list.items()), k=num_of_questions)

    # Displaying the question number and asking the user the quiz question:
    for num, (question, possible_answer) in enumerate(questions, start=1):
        print(f"\nQuestion {num}:")
        print(f"{question}")
        right_answer = possible_answer[0]
        # Ordering the possible answers:
        ordered_answers = dict(zip(ascii_lowercase, random.sample(possible_answer, k=len(possible_answer))))
        for tag, option in ordered_answers.items():
            print(f" {tag}) {option}")

        # Asking the user for their answer:
        while (answer_tag := input("\nYour answer? ").lower()) not in ordered_answers:
            print(f"Sorry, your answer was invalid. Please try again by using either {', '.join(ordered_answers)}.")

        # Communicating the results with the user:
        answer = ordered_answers[answer_tag]
        if answer == right_answer:
            score += 1
            print("Congratulations you are correct!")
        else:
            print(f"Sadly you answered incorrectly. You chose {answer}, however, the correct answer was {right_answer}.")

    # Outputting the total score the user received for the quiz round
    print(f"\nYou got {score} out of {num} questions correct!")

    invalid = False
    while not invalid:
        # Asking the user whether they would like to play again
        continue_answer = input("\nWould you like to play another round? ").lower()

        if continue_answer == "yes" or continue_answer == "y":
            play_again = True
            invalid = True

        elif continue_answer == "no" or continue_answer == "n":
            play_again = False
            invalid = True

        else:
            invalid = False
            play_again = False
            print("This is an invalid value. Please answer yes or no.")

print("\nThank you for playing the Capital Cities of Europe Quiz!")
print("Hopefully you were able to learn something new, see you again next time.")

