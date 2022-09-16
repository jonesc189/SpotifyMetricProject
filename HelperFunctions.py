
def get_choice():
    choice = None
    try:
        choice = int(input("Choice: "))
    except(ValueError) :
        exit_program()
    return choice

def exit_program():
    print("Exiting\n")
    exit()

