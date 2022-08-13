# Version Three of Yes / No Checker

# Functions below this line:
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


def instructions():
    print()
    print("**** How to Play ****")
    print(" - Every round consists of five questions.")
    print(" - Each question will have three possible answers either a, b or c.")
    print(" - To answer the question please press the corresponding letter on the keyboard.")
    return""


# Main Routine below this line:
print("Welcome to the Capital Cities Quiz Game!")
show_instructions = yesno("Would you like to view the instructions? ")

if show_instructions == "yes":
    instructions()

