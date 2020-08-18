reply = input("Would you like to continue?")

if reply == "y" or "yes":
    print("Continuing . . . \nComplete!")

elif reply == "n" or "no":
    print("Exiting")
else:
    print("Please try again and respond with yes or no")