import random

state_list = [
    {
        "Name": "Alabama",
        "Capital": "Montgomery",
        "Population": 0000,
        "Best Universities": ["College1", "College2", "College3"],
        "Party": {
            "rep": True,
            "dem": False
        },
    },
    {
        "Name": "Connecticut",
        "Capital": "Hartford",
        "Population": 0000,
        "Best Universities": ["College1", "College2", "College3"],
        "Party": {
            "rep": False,
            "dem": True
        },
    },
    {
        "Name": "Pennsylvania",
        "Capital": "Harrisburg",
        "Population": 0000,
        "Best Universities": ["College1", "College2", "College3"],
        "Party": {
            "rep": False,
            "dem": True
        },
    },
]

####################################################
# x = [d["Party"] for d in state_list]
# retrieve value of "Party"
# print(x)
# # output: [{'rep': True, 'dem': False}, {'rep': False, 'dem': True}, {'rep': False, 'dem': True}]

party_dict = map(lambda d: d["Party"], state_list)
# another way to retrieve value of "Party"
print(list(party_dict))
# output: [{'rep': True, 'dem': False}, {'rep': False, 'dem': True}, {'rep': False, 'dem': True}]

state_names = map(lambda d: d["Name"], state_list)
print(list(state_names))
# output: ['Alabama', 'Connecticut', 'Pennsylvania']
#####################
states = [
    {"rep": "True", "dem": "False"},
    {"rep": "False", "dem": "True"},
    {"rep": "False", "dem": "True"},
]
# I was attempting to loop through the list of dictionaries in order to append keys that had the value "True" to a list so that I could zip the list of states to their party but I can't figure out how to do this

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
