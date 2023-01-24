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
        correct_answer = single_state_dict["Capital"]
        print(f"Correct answer is: {correct_answer}")
        return correct_answer


good_answer = right_answer()

false_answers = []


def wrong_answers():
    capitals = []
    for dic in state_dict_list:
        capitals.append(dic["Capital"])

    # now we need to create a list from the capitals list of 3 random capitals
    false_answers.append(capitals[random.randrange(0, 50)])
    false_answers.append(capitals[random.randrange(0, 50)])
    false_answers.append(capitals[random.randrange(0, 50)])
    print(f"Wrong Answers: {false_answers}")
    return false_answers


wrong_list = wrong_answers()

print(f"wrong list:{wrong_list}")

combined_list = []


def validate_answers(right=str, wrongs=list):
    for wrong_choice in wrongs:
        if wrong_choice == right:
            wrong_answers()

        # This adds the wrongs to a new list and the right to that same new list --> combined list has 2 elements = wrong list and right (str)
        if wrong_choice not in right:
            combined_list.append(wrongs)
            combined_list.append(right)
        print(f"combined list is: {combined_list}")
        return combined_list

    print(f"Wrongs are validated: {wrongs}")
    return wrongs


validate_answers(good_answer, wrong_list)

#########################################
# ALTERNATIVE CONDENSE: This good_answer to false answers to create a combined list with 4 elements
# I tried putting this statement in the validate answers definition but the code won't work so far when i do that
false_answers.append(good_answer)
print(f"FALSE and RIGHT: {false_answers}")
copied_list = false_answers.copy()
print(f"Copied list is: {copied_list}")
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

# 2. In the validate answers function I added another if statement in the for loop that will combine the right and wrongs if the wrongs are validated
# # This combined list contains 2 elements, of list of wrongs and the second is the right string
# 3. I wrote code for an alternative way to combine lists that creates one list with 4 elements


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
