import random
import json

with open("dummy_multiple_data.json", encoding="UTF-8") as state_dict_list:
    state_dict_list = state_dict_list.read()

# print(f"data:{state_dict_list}")
state_dict_list = json.loads(state_dict_list)


# def multiple_choice_game():
#     # state = single_state_dict["Name"]
#     # print(state)
#     # return state
#     # quest = f"What is the capital of {state} ? "
#     # print(quest)
#     # return quest
#     # need to put ONLY capitals into a list

#     return

print("Running first funciton")


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
        print(f"Correct answer is: {correct_answer['Capital']}")
        return correct_answer


good_answer = right_answer()
print(f"The good answer is: {good_answer}")


def wrong_answers():
    false_answers = []
    capitals = []
    for dic in state_dict_list:
        capitals.append(dic["Capital"])

    # now we need to create a list from the capitals list of 3 random capitals
    false_answers.append(capitals[random.randrange(0, 50)])
    false_answers.append(capitals[random.randrange(0, 50)])
    false_answers.append(capitals[random.randrange(0, 50)])
    # print(f"Wrong Answers: {false_answers}")

    false_answers = list(dict.fromkeys(false_answers))

    if len(false_answers) < 3:
        wrong_answers()
    print(f"FALSE ANSWERS ARE: {false_answers}")
    return false_answers

    # print(f"Wrong Answers: {false_answers}")
    # return false_answers

    # false_answers.append(capitals[random.randrange(0, 50)])
    # false_answers.append(capitals[random.randrange(0, 50)])
    # false_answers.append(capitals[random.randrange(0, 50)])
    # print(f"Wrong Answers: {false_answers}")
    # return false_answers


wrong_list = wrong_answers()

print(f"wrong list:{wrong_list}")


def validate_answers(right: dict[str, str], wrongs: list):
    print(f"validate_answer arguments: {right}, {wrongs}")
    print(f'right answer for capital: {right["Capital"]}')
    for wrong_choice in wrongs:
        if wrong_choice == right["Capital"]:
            wrongs = wrong_answers()

    all_choices = {"Wrong Answers": wrongs, "Right Answer": right}  # []  # {}

    print(f"Wrongs are validated: {all_choices['Wrong Answers']}")
    return all_choices


four_answers = validate_answers(good_answer, wrong_list)

print(f"four answers are: {four_answers}")
# output -> four answers are: {'Wrong Answers': ['Pierre', 'Harrisburg', 'Springfield'], 'Right Answer': {'Capital': 'Jackson', 'State': 'Mississippi'}}


def playMultiple():
    shuffle_list = []
    three_caps = four_answers["Wrong Answers"]
    one_cap = four_answers["Right Answer"]["Capital"]
    new_line = "\n"

    print(f"Four choices: {one_cap}, {three_caps}")

    for city in three_caps:
        shuffle_list.append(city)
    print(f"{new_line}SHUFFLED LIST IS: {shuffle_list}")

    shuffle_list.append(four_answers["Right Answer"]["Capital"])
    print(f"COMPLETED LIST FOR SUFFLE{shuffle_list}")

    shuffle_copied_list = shuffle_list.copy()
    print(f"RANDOM LIST IS: {shuffle_copied_list}")

    random.shuffle(shuffle_copied_list)
    print(f"SHUFFLED RANDO LIST: {shuffle_copied_list}")

    # wrong_list.append(good_answer)
    # print(f"{new_line}COMBO_LIST is {wrong_list}")

    user_guess = input(
        f"{new_line}What is the capital of {four_answers['Right Answer']['State']} ?{new_line} {new_line}{new_line.join(shuffle_copied_list)}{new_line}"
    )

    # user_guess = input(
    #     f"{new_line}What is the capital of {four_answers['Right Answer']['State']} ?{new_line} {new_line}{new_line.join(three_caps)}{new_line}{four_answers['Right Answer']['Capital']}{new_line}"
    # )
    if user_guess in one_cap:
        print("Woohoo!")
    else:
        print(
            f"I'm sorry the correct answer is {four_answers['Right Answer']['Capital']}"
        )


playMultiple()


# NEXT:
# def playMultiple():
#   add question- DONE
#   add multiple choice questions in A, B, C, D format
#   user input- DONE
#   compare user input to correct answer
# make sure edge case in duplicate answer in final_answers is resolved
#####################################################################################
# DONE TODAY:
# 1. DRILLED stateApp game
# 2. DRILLED MCQ app
# 3. to def playMultiple - I added correct answer to appear among possible choices
## 4. created question and user input
## 5. added if statements to confirm if answer is correct and also to reveal correct answer if user_guess is incorrect

##########################################
# def multiple_choice_game():
#     capitals = []
#     wrong_answers = []

#     def multiple_answers():
#         for dic in state_dict_list:
#             capitals.append(dic["Capital"])

#         wrong_answers.append(capitals[random.randrange(0, 50)])
#         wrong_answers.append(capitals[random.randrange(0, 50)])
#         wrong_answers.append(capitals[random.randrange(0, 50)])

#         print(f"Wrong Answers: {wrong_answers}")
#         return wrong_answers

#     wrong_answers = multiple_answers()
#     # Validation: check all 3 wrong answers do not match the correct answer
#     for choice in wrong_answers:
#         if choice == "Trenton":
#             wrong_answers = []
#             wrong_answers = multiple_answers()

#     print("Wrong answers validated")

#     return wrong_answers


# multiple_choice_game()

#################################################
# def Wrong_Answer_List():

#     wrong_cap_list = state_dict_list[Capital]
#     print(wrong_cap_list)


# Wrong_Answer_List()

#     w_answer = []
#     count = 0


# for x in state_list["Capital"]
# #####################################################

# def capitalGame():
#     while len(state_dict_list) > 0:
#         single_state_dict = random.choice(state_dict_list)
#         state = single_state_dict["Name"]
#         capital = single_state_dict["Capital"]

#         user_guess = input("What is the capital of " + state + "? ")

#         if user_guess == capital:
#             print("Woohoo! You got it.")
#         elif user_guess not in capital:
#             print("Oh no, your answer is incorrect.")
#         else:
#             print("Please write republican or democratic.")
