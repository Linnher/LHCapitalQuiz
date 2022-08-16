# Version Two of Yes / No Checker

# Functions below this line:
# Function to check whether the user input is valid.
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


# Main Routine below this line:
# Asking user if they would like to view the instructions
show_instructions = yesno("Would you like to view the instructions? ")
print("You selected {}." .format(show_instructions))
