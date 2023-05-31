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
        message += "vous pouvez également quitter le programme en appuyant sur 'q' \n"

    while True:
        choice = input("")
        print("valeur choisie : " + choice + " de type " + str(type(choice)))
        try:
            # threading.Thread(target=on_event_noob, args=(choice,)).start()
            threading.Thread(target=on_event_middle, args=(choice, choice_possibilities,)).start()
            # threading.Thread(target=on_event, args=(choice, choice_possibilities[choice],quit_additionnal_option,)).start()

            return
        except ValueError:
            print("Choix invalide")


def on_event(choice, choice_possibilities: dict, quit_additionnal_option: bool):
    """
    Casting the function associated with the choice
    Returns None
    """

    if choice == "q" and quit_additionnal_option:
        print("Sortie du programme.")
        sys.exit()

    if choice_possibilities[choice] is not None:
        print("execution de " + choice_possibilities[choice])
    else:
        print("Choix invalide")


def on_event_middle(choice, choice_possibilities: dict):
    """
    Calling the function associated with the choice
    Returns None
    """

    if choice == "q":
        print("Sortie du programme.")
        sys.exit()

    if choice in choice_possibilities:
        chose_function = choice_possibilities[choice]
        chose_function()
    else:
        print("choice n'est pas dans choice_possibilities")


def on_event_noob(choice):
    """
    Casting the function associated with the choice
    Returns None
    """

    if choice == "q":
        print("Sortie du programme.")
        sys.exit()

    if choice == "1":
        noob_message1()
    elif choice == "2":
        noob_message2()
    else:
        print("Choix invalide")


def noob_message1():
    """
    msg 1
    """
    print("message 1 dskjhfqlsdkj")


def noob_message2():
    """
    msg 2
    """
    print("message 2 123456789")
