import random

state_list = [
    {
        "Name": "Alabama",
        "Capital": "Montgomery",
        "Population": 0000,
        "Best Universities": ["College1", "College2", "College3"],
        "Party": {"rep": True, "dem": False},
    },
    {
        "Name": "Connecticut",
        "Capital": "Hartford",
        "Population": 0000,
        "Best Universities": ["College1", "College2", "College3"],
        "Party": {"rep": False, "dem": True},
    },
    {
        "Name": "Pennsylvania",
        "Capital": "Harrisburg",
        "Population": 0000,
        "Best Universities": ["College1", "College2", "College3"],
        "Party": {"rep": False, "dem": True},
    },
]


x = [d["Party"] for d in state_list]
# retrieve value of "Party"
# print(x)
# output: [{'rep': True, 'dem': False}, {'rep': False, 'dem': True}, {'rep': False, 'dem': True}]

x = map(lambda d: d["Party"], state_list)
# another way to retrieve value of "Party"
# print(list(x))
# output: [{'rep': True, 'dem': False}, {'rep': False, 'dem': True}, {'rep': False, 'dem': True}]

y = map(lambda d: d["Name"], state_list)
print(list(y))


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
