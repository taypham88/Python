def yes_or_no(question):
    answer = input(question + "(y/n): ").lower().strip()
    while not(answer == "y" or answer == "yes" or \
    answer == "n" or answer == "no"):
        print("Please enter y or n")
        answer = input(question + "(y/n):").lower().strip()
    if answer[0] == "y":
        return True
    else:
        return False
    