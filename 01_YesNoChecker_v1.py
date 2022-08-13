# Version One of Yes / No Checker

show_instructions = ""
while show_instructions.lower() != "xxx":

    # Ask the user if they want to see the instructions
    show_instructions = input("Would you like to view the instructions? ").lower()

    # If the user inputs no, output 'program continues'
    if show_instructions == "no" or show_instructions == "n":
        show_instructions = "no"
        print("You selected no. - Program Continues")

    # If the user inputs yes, output 'display instructions'
    elif show_instructions == "yes" or show_instructions == "y":
        show_instructions = "yes"
        print("You selected yes. - Display Instructions")

    # If user inputs anything else, output 'This is an invalid value.'
    else:
        print("This is an invalid value. Please answer yes or no.")

