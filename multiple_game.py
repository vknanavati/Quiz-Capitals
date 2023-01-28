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

    def playMultiple(answers):
        new_line = "\n"
        choices = answers["Wrong Answers"]
        choices.append(answers["Right Answer"]["Capital"])

        random.shuffle(choices)

        selections = f"'\n' a. {choices[0]} '\n' b. {choices[1]} '\n' c. {choices[2]} '\n' d. {choices[3]}"

        choice_map = {
            "a": choices[0],
            "b": choices[1],
            "c": choices[2],
            "d": choices[3],
        }
        # choice_map[user_guess] => choice_map['a'] => 'Trenton'

        # print(f"selections: {selections}")

        user_guess = input(
            f"{new_line}What is the capital of {answers['Right Answer']['State']} ? {selections} '\n' '\n'"
        )

        if (
            user_guess != "a"
            or user_guess != "b"
            or user_guess != "c"
            or user_guess != "d"
        ):
            print("Sorry that choice is not available")

        if choice_map[user_guess] == answers["Right Answer"]["Capital"]:
            print(f"Correct! {answers['Right Answer']['Capital']}")
        else:
            print(f"Nope! The correct answer is {answers['Right Answer']['Capital']}")

        return

    playMultiple(four_answers)

    # def playMultiple():
    #     three_caps = four_answers["Wrong Answers"]
    #     one_cap = four_answers["Right Answer"]["Capital"]
    #     state = four_answers["Right Answer"]["State"]
    #     new_line = "\n"

    #     print(f"{new_line}One cap: {one_cap}{new_line}")

    #     print(f"Three cap:{three_caps}{new_line}")

    #     three_caps.append(one_cap)
    #     print(three_caps)

    #     random.shuffle(three_caps)
    #     print(f"{new_line}Three caps shuffled: {three_caps}{new_line}")

    #     # letters = ["a", "b", "c", "d"]

    #     # print("Letters paired with options:")
    #     # for l, s in zip(letters, three_caps):
    #     #     print(l, s)

    #     # user_guess = input(f"{new_line}What is the capital of {state} ?")

    #     # {new_line} {new_line}{new_line.join(shuffle_copied_list)}{new_line}

    #     user_guess = input(
    #         f"{new_line}What is the capital of {state} ?{new_line} {new_line}{new_line.join(three_caps)}{new_line}"
    #     )
    #     while len(user_guess) > 0:
    #         if user_guess in one_cap:
    #             print("Woohoo!")
    #             return
    #         print(f"I'm sorry the correct answer is {one_cap}")
    #         return


def number_of_rounds():
    for _ in range(5):
        main()


# number_of_rounds()
# run this for whole function
number_of_rounds()

# NEXT:
# fruits and colors map
# re-write script that seb wrote
# re-write entire script
# handle validation - clicking wrong letter
# remove ' characters from answer choices
# handle duplicate wrong answer in choices
# incorporate into larger app
