# Version Three of Question Generator - Ordering the possible answers alphabetically

# Importing Libraries
from string import ascii_lowercase

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

# Main Routine below this line:
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
