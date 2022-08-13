# Version Two of Yes / No Checker

# Function below this line:
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
show_instructions = yesno("Would you like to view the instructions? ")
print("You selected {}." .format(show_instructions))
