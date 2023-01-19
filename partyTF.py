# import random

# state_list = [
#     {
#         "Name": "Alabama",
#         "Capital": "Montgomery",
#         "Population": 0000,
#         "Best Universities": ["College1", "College2", "College3"],
#         "Party": {"rep": True, "dem": False},
#     },
#     {
#         "Name": "Connecticut",
#         "Capital": "Hartford",
#         "Population": 0000,
#         "Best Universities": ["College1", "College2", "College3"],
#         "Party": {"rep": False, "dem": True},
#     },
#     {
#         "Name": "Pennsylvania",
#         "Capital": "Harrisburg",
#         "Population": 0000,
#         "Best Universities": ["College1", "College2", "College3"],
#         "Party": {"rep": False, "dem": True},
#     },
# ]

# ####################################################
# # x = [d["Party"] for d in state_list]
# # retrieve value of "Party"
# # print(x)
# # # output: [{'rep': True, 'dem': False}, {'rep': False, 'dem': True}, {'rep': False, 'dem': True}]

# x = map(lambda d: d["Party"], state_list)
# another way to retrieve value of "Party"
# print(list(x))
# # output: [{'rep': True, 'dem': False}, {'rep': False, 'dem': True}, {'rep': False, 'dem': True}]

# y = map(lambda d: d["Name"], state_list)
# print(list(y))
# # output: ['Alabama', 'Connecticut', 'Pennsylvania']
# #####################
# states = [
#     {"rep": "True", "dem": "False"},
#     {"rep": "False", "dem": "True"},
#     {"rep": "False", "dem": "True"},
# ]
#I was attempting to loop through the list of dictionaries in order to append keys that had the value "True" to a list so that I could zip the list of states to their party but I can't figure out how to do this

################################
# SCRATCH PAD:

# def politicalParty():

#     states = list(state_list.keys("Name"))

#     while len(state_list) > 0:
#         state = random.choice(states)
#         party =

#     while len(state_list) > 0:
#         state_party_dict = random.choice(state_list)
#         state_party = state_party_dict["Name"]
#         state_color = state_party_dict["Party"]

#         user_guess = input("Is" + state_party + "Republican or Democract?")

#         if user_guess == :
#             print("Yay")
#         else:
#             print("boo")

******************************************
def friend(x):
    arr = []
    for name in x:
        if len(name) == 4:
            arr.append(name)
    return arr


def solution(s):
    new_text = ''
    for i, letter in enumerate(s):
        if i and letter.isupper():
            new_text += ' '
        new_text += letter
    return new_text

*********************************************

def open_or_senior(data):
    output = []
    for a, b in data:
        if a >= 55 and b > 7:
            output.append('Senior')
        else:
            output.append('Open')
    return output

************************************************

def points(games):
    s = []
    for i in games:
        i = i.split(":")
        if int(i[0]) > int(i[1]):
            s.append(3)
        elif int(i[0]) == int(i[1]):
            s.append(1)
    return sum(s)

**********************************************

def min_max(lst):
    new_lst =[]
    for i in lst:
        new_lst.append(min(lst))
        new_lst.append(max(lst))
        return new_lst

******************************************

def double_char(s):
    result = []
    for i in s:
        result.append(i + "" + i)
    return "".join(result)

********************************************************

def summation(num):
    digit = range(0, num +1)
    total = 0
    for i in digit:
        total = total + i
    return total