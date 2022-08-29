# Version One of Play again - Asking the user if they would like to play again after they have completed the round

# Main Routine below this line:
# Initiating Variables:
play_again = True
invalid = False

while play_again:
    # This is where question code will go
    print("\n*Questions are printed here*")
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

print("\nThank you for playing the Capital Cities of Europe Quiz Game!")
print("Hopefully you were able to learn something new, see you again next time.")
