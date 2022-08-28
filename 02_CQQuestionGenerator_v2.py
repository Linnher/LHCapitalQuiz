# Version Two of Question Generator - Ordering the possible answers numerically

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
    ordered_answers = sorted(possible_answer)
    for tag, option in enumerate(ordered_answers):
        print(f" {tag}) {option}")

    # Asking the user the quiz question:
    answer_tag = int(input(f"{question} "))
    answer = ordered_answers[answer_tag]

    # Communicating the results with the user:
    if answer == right_answer:
        print("Congratulations you are correct!")
    else:
        print(f"Sadly you answered incorrectly. You chose {answer}, however, the correct answer was {right_answer}.")

