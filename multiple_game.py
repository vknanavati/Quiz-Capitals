import random
import json

with open("dummy_multiple_data.json", encoding="UTF-8") as state_dict_list:
    state_dict_list = state_dict_list.read()

# print(f"data:{state_dict_list}")
state_dict_list = json.loads(state_dict_list)


def main():
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

        selections = f"\n a. {choices[0]} \n b. {choices[1]}\n c. {choices[2]} \n d. {choices[3]}"

        # object mapping
        choice_map = {
            "a": choices[0],
            "b": choices[1],
            "c": choices[2],
            "d": choices[3],
        }

        print(
            f"\nWhat is the capital of {answers['Right Answer']['State']} ? \n{selections} \n \n"
        )

        user_guess = input("Enter answer: ")

        user_entry = choice_map.get(user_guess)

        if user_entry == answers["Right Answer"]["Capital"]:
            print(f"Correct! {answers['Right Answer']['Capital']}")
        if user_entry not in answers["Right Answer"]["Capital"]:
            print(f"Nope! The correct answer is {answers['Right Answer']['Capital']}")

        # print(choice_map[user_guess])
        # while user_guess in choice_map and choice_map[user_guess]:

        #     if choice_map[user_guess] == answers["Right Answer"]["Capital"]:
        #         print(f"Correct! {answers['Right Answer']['Capital']}")
        #         break
        #     if choice_map[user_guess] not in answers["Right Answer"]["Capital"]:
        #         print(
        #             f"Nope! The correct answer is {answers['Right Answer']['Capital']}"
        #         )
        #         break

        # while user_guess in choice_map and choice_map[user_guess]:

        #     if choice_map[user_guess] == answers["Right Answer"]["Capital"]:
        #         print(f"Correct! {answers['Right Answer']['Capital']}")
        #         break
        #     if choice_map[user_guess] not in answers["Right Answer"]["Capital"]:
        #         print(
        #             f"Nope! The correct answer is {answers['Right Answer']['Capital']}"
        #         )
        #         break

        #     else:
        #         print("Incorrect character, try again")
        #         continue

    play_multiple(four_answers)


def number_of_rounds():
    for _ in range(5):
        main()


number_of_rounds()
##############################
# import random
# import json

# with open("dummy_multiple_data.json", encoding="UTF-8") as state_dict_list:
#     state_dict_list = state_dict_list.read()

# # print(f"data:{state_dict_list}")
# state_dict_list = json.loads(state_dict_list)


# def main():
#     def right_answer():
#         # grab correct answer
#         while len(state_dict_list) > 0:
#             single_state_dict = random.choice(state_dict_list)
#             # Checking that it returns single_state_dict
#             # print(single_state_dict)
#             # return single_state_dict
#             correct_answer = {
#                 "Capital": single_state_dict["Capital"],
#                 "State": single_state_dict["Name"],
#             }
#             # print(f"\nCorrect answer is: {correct_answer['Capital']}\n")
#             return correct_answer

#     good_answer = right_answer()
#     # print(f"The good answer is: {good_answer}")

#     def wrong_answers():
#         false_answers = []
#         capitals = []
#         for dic in state_dict_list:
#             capitals.append(dic["Capital"])

#         # now we need to create a list from the capitals list of 3 random capitals
#         false_answers.append(capitals[random.randrange(49)])
#         false_answers.append(capitals[random.randrange(49)])
#         false_answers.append(capitals[random.randrange(49)])

#         # print(f"\nBefore fromkeys method: {false_answers}\n")

#         false_answers = list(dict.fromkeys(false_answers))

#         # print(f"\nAfter fromkeys: {false_answers}\n")

#         if len(false_answers) < 3:
#             wrong_answers()
#         return false_answers

#     wrong_list = wrong_answers()

#     def validate_answers(right: dict[str, str], wrongs: list):
#         # print(f"validate_answer arguments: {right}, {wrongs}")
#         # print(f'right answer for capital: {right["Capital"]}')
#         for wrong_choice in wrongs:
#             if wrong_choice == right["Capital"]:
#                 wrongs = wrong_answers()

#         all_choices = {"Wrong Answers": wrongs, "Right Answer": right}  # []  # {}

#         # print(f"Wrongs are validated: {all_choices['Wrong Answers']}")
#         return all_choices

#     four_answers = validate_answers(good_answer, wrong_list)

#     # print(f"four answers are: {four_answers}")
#     # output -> four answers are: {'Wrong Answers': ['Pierre', 'Harrisburg', 'Springfield'], 'Right Answer': {'Capital': 'Jackson', 'State': 'Mississippi'}}

#     def play_multiple(answers):
#         choices = answers["Wrong Answers"]
#         choices.append(answers["Right Answer"]["Capital"])

#         random.shuffle(choices)

#         selections = f"\n a. {choices[0]} \n b. {choices[1]}\n c. {choices[2]} \n d. {choices[3]}"

#         # object mapping
#         choice_map = {
#             "a": choices[0],
#             "b": choices[1],
#             "c": choices[2],
#             "d": choices[3],
#         }

#         # choice_map[user_guess] => choice_map['a'] => 'Trenton'

#         # print(f"selections: {selections}")

#         # user_guess = input(
#         #     f"\nWhat is the capital of {answers['Right Answher']['State']} ? \n{selections} \n \n"
#         # )
#         print(
#             f"\nWhat is the capital of {answers['Right Answer']['State']} ? \n{selections} \n \n"
#         )

#         user_guess = input()

#         # print(choice_map[user_guess])

#         if choice_map[user_guess] == answers["Right Answer"]["Capital"]:
#             print(f"Correct! {answers['Right Answer']['Capital']}")
#         elif choice_map[user_guess] not in answers["Right Answer"]["Capital"]:
#             print(f"Nope! The correct answer is {answers['Right Answer']['Capital']}")
#         else:
#             print("Incorrect character, try again")
#             print(user_guess)

#     play_multiple(four_answers)


# def number_of_rounds():
#     for _ in range(5):
#         main()


# number_of_rounds()
############################


# NEXT:
# fruits and colors map - DONE!
# re-write script that seb wrote - DONE!
# re-write entire script
# handle validation - if user clicks wrong letter
# handle allowing for user to guess again if incorrect character entered
# handle moving onto next question if wrong answer entered
# handle .capitilize for answer choices
# incorporate into larger app
