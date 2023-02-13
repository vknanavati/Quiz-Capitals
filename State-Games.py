import random
import json
import re

# with open("dummy_data.json", encoding="UTF-8") as state_dict_list:
#     state_dict_list = state_dict_list.read()

# state_dict_list = json.loads(state_dict_list)

with open("dummy_multiple_data.json", encoding="UTF-8") as state_dict_list:
    state_dict_list = state_dict_list.read()

# print(f"data:{state_dict_list}")
state_dict_list = json.loads(state_dict_list)

# global count
USER_SCORE = {"party_game": 0, "capital_game": 0, "multiple_choice_game": 0}


def partyGame():
    # local count
    # count = 0
    number_guesses = 0
    while number_guesses < 5:
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

            number_guesses = number_guesses + 1
            if number_guesses == 5:
                break

            if user_guess == answer:
                # count = count + 1  # set local count
                # USER_SCORE["party_game"] = count  # set global count
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


def multipleChoiceGame():
    def right_answer():
        # grab correct answer
        while len(state_dict_list) > 0:
            single_state_dict = random.choice(state_dict_list)
            # Checking that it returns single_state_dict
            # print(single_state_dict)
            # return single_state_dict
            correct_answer = {
                "Capital": single_state_dict["Capital"],
                "State": single_state_dict["Name"],
            }
            # print(f"\nCorrect answer is: {correct_answer['Capital']}\n")
            return correct_answer

    good_answer = right_answer()
    # print(f"The good answer is: {good_answer}")

    def wrong_answers():
        false_answers = []
        capitals = []
        for dic in state_dict_list:
            capitals.append(dic["Capital"])

        # now we need to create a list from the capitals list of 3 random capitals
        false_answers.append(capitals[random.randrange(49)])
        false_answers.append(capitals[random.randrange(49)])
        false_answers.append(capitals[random.randrange(49)])

        # print(f"\nBefore fromkeys method: {false_answers}\n")

        false_answers = list(dict.fromkeys(false_answers))

        # print(f"\nAfter fromkeys: {false_answers}\n")

        if len(false_answers) < 3:
            wrong_answers()
        return false_answers

    wrong_list = wrong_answers()

    def validate_answers(right: dict[str, str], wrongs: list):
        # print(f"validate_answer arguments: {right}, {wrongs}")
        # print(f'right answer for capital: {right["Capital"]}')
        for wrong_choice in wrongs:
            if wrong_choice == right["Capital"]:
                wrongs = wrong_answers()

        all_choices = {"Wrong Answers": wrongs, "Right Answer": right}  # []  # {}

        # print(f"Wrongs are validated: {all_choices['Wrong Answers']}")
        return all_choices

    four_answers = validate_answers(good_answer, wrong_list)

    # print(f"four answers are: {four_answers}")
    # output -> four answers are: {'Wrong Answers': ['Pierre', 'Harrisburg', 'Springfield'], 'Right Answer': {'Capital': 'Jackson', 'State': 'Mississippi'}}

    def play_multiple(answers):
        choices = answers["Wrong Answers"]
        choices.append(answers["Right Answer"]["Capital"])

        random.shuffle(choices)

        selections = f"\n a. {choices[0]} \n b. {choices[1]} \n c. {choices[2]} \n d. {choices[3]}"

        # object mapping
        choice_map = {
            "a": choices[0],
            "b": choices[1],
            "c": choices[2],
            "d": choices[3],
        }

        print(
            f"\nWhat is the capital of {answers['Right Answer']['State']} ? \n{selections} \n"
        )

        while True:
            user_guess = input("\nEnter answer: ")
            user_entry = choice_map.get(user_guess)
            if user_guess not in choice_map:
                print("\nInvalid character please try again.\n")
                continue

            if user_entry == answers["Right Answer"]["Capital"]:
                print(f"\nCorrect! {answers['Right Answer']['Capital']}\n")
                break
            if user_entry not in answers["Right Answer"]["Capital"]:
                print(
                    f"\nNope! The correct answer is {answers['Right Answer']['Capital']}\n"
                )
                break

    play_multiple(four_answers)


def number_of_rounds():
    for _ in range(5):
        multipleChoiceGame()


def startGame():
    user_answer = input(
        "Which game would you like to play? Party game or Capital game or Multiple game? "
    )

    capital_game = re.search("capital", user_answer)
    party_game = re.search("party", user_answer)
    multiple_game = re.search("multiple", user_answer)
    exit_game = re.search("exit", user_answer)

    if capital_game:
        print("Play capital game!")
        capitalGame()

    if party_game:
        print("Play party game!")
        partyGame()

    if multiple_game:
        print("Play multiple game!")
        number_of_rounds()

    if exit_game:
        print("Good bye!")
        quit()

    else:
        print("Oh no, we don't have that game!")

    # WHY ARE THESE IF ALL IF STATEAMENTS AND NOT ELIF ELSE
    # if statement sets a specific condition
    # elif statement sets another speific condition after an if statement
    # else has no conditional statement, handles any exceptions that are not specified


startGame()
