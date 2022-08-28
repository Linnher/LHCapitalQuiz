# Version One of Question Generator - Initial Version

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
# Sorting the Multichoice answers:
for question, possible_answer in questions_list.items():
    right_answer = possible_answer[0]
    for option in sorted(possible_answer):
        print(f" * {option}")

    #  Asking the user the quiz question:
    answer = input(f"{question} ")
    # Communicating the results with the user:
    if answer == right_answer:
        print("Congratulations you are correct!")
    else:
        print(f"Sadly you answered incorrectly. You chose {answer}, however, the correct answer was {right_answer}. ")



