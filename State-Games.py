import random
import json
import re

with open("dummy_data.json", encoding="UTF-8") as state_dict_list:
    state_dict_list = state_dict_list.read()

state_dict_list = json.loads(state_dict_list)


def partyGame():
    while len(state_dict_list) > 0:
        single_state_dict = random.choice(state_dict_list)

        state = single_state_dict["Name"]
        dem = single_state_dict["Party"]["dem"]

        answer = " "
        if dem == "True":
            answer = "democratic"
        if dem == "False":
            answer = "republican"

        user_guess = input(f"Is {state} republican or democratic? ")

        if user_guess == answer:
            print("Woohoo! You got it!")
        elif user_guess not in answer:
            print("Oh no, your answer is incorrect.")
        else:
            break


def capitalGame():
    while len(state_dict_list) > 0:
        single_state_list = random.choice(state_dict_list)

        state = single_state_list["Name"]
        capital = single_state_list["Capital"]

        user_guess = input(f"What is the capital of {state} ? ")

        if user_guess == capital:
            print("Woohoo! You got it!")
        elif user_guess not in capital:
            print("Oh no, your answer is incorrect.")
        else:
            print("Please write republican or democratic.")


def startGame():
    user_answer = input(
        "Which game would you like to play? Party game or Capital game? "
    )

    capital_game = re.search("capital", user_answer)
    party_game = re.search("party", user_answer)
    exit_game = re.search("exit", user_answer)

    if capital_game:
        print("Play capital game!")
        capitalGame()

    if party_game:
        print("Play party game!")
        partyGame()

    if exit_game:
        print("Good bye!")
        quit()

    else:
        print("Oh no, we don't have that game!")

    # WHY ARE THESE IF ALL IF STATEAMENTS AND NOT ELIF ELSE


startGame()
