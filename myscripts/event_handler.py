"""
this module handles events
"""
import sys
import threading


def wait_for_event(message, choice_possibilities: dict, quit_additionnal_option: bool):
    """
    Event waiting function
    message should be a str or a list
    choice_possibilities must receive int keys and function as values
    If "add_quit_message" is true, the function will add a message for quit
    Returns nothing
    """

    if isinstance(message, str):
        print("\n\n" + message + "\n")
    elif isinstance(message, list):
        for ligne in message:
            print(ligne)
    else:
        print("MESSAGE INCORRECT EN ARGUMENT")

    if quit_additionnal_option:
        print("'q' : quitter le programme. \n")

    while True:
        choice = input("")
        threading.Thread(target=on_event,
                         args=(choice, choice_possibilities, quit_additionnal_option,)).start()
        return


def on_event(choice, choice_possibilities: dict, quit_additionnal_option: bool = False):
    """
    Calling the function associated with the choice
    Returns None
    """

    if choice == "q" and quit_additionnal_option:
        print("Sortie du programme.")
        sys.exit()

    if choice in choice_possibilities:
        chose_function = choice_possibilities[choice]
        chose_function()
    else:
        print("choice n'est pas dans choice_possibilities")
