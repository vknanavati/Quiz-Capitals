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

    three_caps = four_answers["Wrong Answers"]
    one_cap = four_answers["Right Answer"]["Capital"]
    new_line = "\n"

    input(
        f"What is the capital of {four_answers['Right Answer']['State']} ? {new_line}{new_line.join(three_caps)} "
    )

    print(f"Four choices: {one_cap}, {three_caps}")


playMultiple()


# NEXT:
# def playMultiple():
#   add question
#   add multiple choice questions in A, B, C, D format
#   user input
#   compare user input to correct answer
# make sure edge case in duplicate answer in final_answers is resolved
#####################################################################################
# DONE TODAY:
# 1. DRILL multiple_game.py
# # import json file: open(), read(), loads()
# # create function to select random state capital as correct answer: while loop, create variable to hold random correct capital, return cap
# # GLOBAL: create variable to set this function to
# # create empty list to hold 3 false answers
# # create function to select three false answers
# # from state dict use for loop to pull all capital names to be held in a created list
# # from this list randomly choose three capitals to be put into false_answers list
# # print/return false answers
# # GLOBAL: create variable to set this function to
# # create validate answers fnx: for loop to compare false answers to correct answer, return wrongs
# # invoke validate_answers


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