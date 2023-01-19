import random

state_dict_list = [
    {
        "Name": "Alabama",
        "Capital": "Montgomery",
        "Population": 0000,
        "Best Universities": ["College1", "College2", "College3"],
    },
    {
        "Name": "Alaska",
        "Capital": "Juneau",
        "Population": 0000,
        "Best Universities": ["College1", "College2", "College3"],
    },
    {
        "Name": "Arizona",
        "Capital": "Phoenix",
        "Population": 0000,
        "Best Universities": ["College1", "College2", "College3"],
    },
    {
        "Name": "Arkansas",
        "Capital": "Litte Rock",
        "Population": 0000,
        "Best Universities": ["College1", "College2", "College3"],
    },
    {
        "Name": "California",
        "Capital": "Sacramento",
        "Population": 0000,
        "Best Universities": ["College1", "College2", "College3"],
    },
    {
        "Name": "Colorado",
        "Capital": "Denver",
        "Population": 0000,
        "Best Universities": ["College1", "College2", "College3"],
    },
    {
        "Name": "Connecticut",
        "Capital": "Hartford",
        "Population": 0000,
        "Best Universities": ["College1", "College2", "College3"],
    },
    {
        "Name": "Delaware",
        "Capital": "Dover",
        "Population": 0000,
        "Best Universities": ["College1", "College2", "College3"],
    },
    {
        "Name": "Florida",
        "Capital": "Tallahassee",
        "Population": 0000,
        "Best Universities": ["College1", "College2", "College3"],
    },
    {
        "Name": "Georgia",
        "Capital": "Atlanta",
        "Population": 0000,
        "Best Universities": ["College1", "College2", "College3"],
    },
    {
        "Name": "Hawaii",
        "Capital": "Honolulu",
        "Population": 0000,
        "Best Universities": ["College1", "College2", "College3"],
    },
    {
        "Name": "Idaho",
        "Capital": "Boise",
        "Population": 0000,
        "Best Universities": ["College1", "College2", "College3"],
    },
    {
        "Name": "Illinois",
        "Capital": "Springfield",
        "Population": 0000,
        "Best Universities": ["College1", "College2", "College3"],
    },
    {
        "Name": "Indiana",
        "Capital": "Indianapolis",
        "Population": 0000,
        "Best Universities": ["College1", "College2", "College3"],
    },
    {
        "Name": "Iowa",
        "Capital": "Ds Moines",
        "Population": 0000,
        "Best Universities": ["College1", "College2", "College3"],
    },
    {
        "Name": "Kansas",
        "Capital": "Topeka",
        "Population": 0000,
        "Best Universities": ["College1", "College2", "College3"],
    },
    {
        "Name": "Kentucky",
        "Capital": "Frankfort",
        "Population": 0000,
        "Best Universities": ["College1", "College2", "College3"],
    },
    {
        "Name": "Louisiana",
        "Capital": "Batn Rouge",
        "Population": 0000,
        "Best Universities": ["College1", "College2", "College3"],
    },
    {
        "Name": "Maine",
        "Capital": "Augusta",
        "Population": 0000,
        "Best Universities": ["College1", "College2", "College3"],
    },
    {
        "Name": "Maryland",
        "Capital": "Annapolis",
        "Population": 0000,
        "Best Universities": ["College1", "College2", "College3"],
    },
    {
        "Name": "Massachusetts",
        "Capital": "Boston",
        "Population": 0000,
        "Best Universities": ["College1", "College2", "College3"],
    },
    {
        "Name": "Michigan",
        "Capital": "Lansing",
        "Population": 0000,
        "Best Universities": ["College1", "College2", "College3"],
    },
    {
        "Name": "Minnesota",
        "Capital": "Sait Paul",
        "Population": 0000,
        "Best Universities": ["College1", "College2", "College3"],
    },
    {
        "Name": "Mississippi",
        "Capital": "Jackson",
        "Population": 0000,
        "Best Universities": ["College1", "College2", "College3"],
    },
    {
        "Name": "Missouri",
        "Capital": "Jeffersn City",
        "Population": 0000,
        "Best Universities": ["College1", "College2", "College3"],
    },
    {
        "Name": "Montana",
        "Capital": "Helena",
        "Population": 0000,
        "Best Universities": ["College1", "College2", "College3"],
    },
    {
        "Name": "Nebraska",
        "Capital": "Lincoln",
        "Population": 0000,
        "Best Universities": ["College1", "College2", "College3"],
    },
    {
        "Name": "Nevada",
        "Capital": "Carsn City",
        "Population": 0000,
        "Best Universities": ["College1", "College2", "College3"],
    },
    {
        "Name": "New Hampshire",
        "Capital": "Concord",
        "Population": 0000,
        "Best Universities": ["College1", "College2", "College3"],
    },
    {
        "Name": "New Jersey",
        "Capital": "Trenton",
        "Population": 0000,
        "Best Universities": ["College1", "College2", "College3"],
    },
    {
        "Name": "New Mexico",
        "Capital": "SanaFe",
        "Population": 0000,
        "Best Universities": ["College1", "College2", "College3"],
    },
    {
        "Name": "New York",
        "Capital": "Albany",
        "Population": 0000,
        "Best Universities": ["College1", "College2", "College3"],
    },
    {
        "Name": "North Carolina",
        "Capital": "Raleigh",
        "Population": 0000,
        "Best Universities": ["College1", "College2", "College3"],
    },
    {
        "Name": "North Dakota",
        "Capital": "Bismarck",
        "Population": 0000,
        "Best Universities": ["College1", "College2", "College3"],
    },
    {
        "Name": "Ohio",
        "Capital": "Columbus",
        "Population": 0000,
        "Best Universities": ["College1", "College2", "College3"],
    },
    {
        "Name": "Oklahoma",
        "Capital": "Oklahoa City",
        "Population": 0000,
        "Best Universities": ["College1", "College2", "College3"],
    },
    {
        "Name": "Oregon",
        "Capital": "Salem",
        "Population": 0000,
        "Best Universities": ["College1", "College2", "College3"],
    },
    {
        "Name": "Pennsylvania",
        "Capital": "Harrisburg",
        "Population": 0000,
        "Best Universities": ["College1", "College2", "College3"],
    },
    {
        "Name": "Rhode Island",
        "Capital": "Providence",
        "Population": 0000,
        "Best Universities": ["College1", "College2", "College3"],
    },
    {
        "Name": "South Carolina",
        "Capital": "Columbia",
        "Population": 0000,
        "Best Universities": ["College1", "College2", "College3"],
    },
    {
        "Name": "South Dakota",
        "Capital": "Pierre",
        "Population": 0000,
        "Best Universities": ["College1", "College2", "College3"],
    },
    {
        "Name": "Tennessee",
        "Capital": "Nashville",
        "Population": 0000,
        "Best Universities": ["College1", "College2", "College3"],
    },
    {
        "Name": "Texas",
        "Capital": "Austin",
        "Population": 0000,
        "Best Universities": ["College1", "College2", "College3"],
    },
    {
        "Name": "Utah",
        "Capital": "Salt Lae City",
        "Population": 0000,
        "Best Universities": ["College1", "College2", "College3"],
    },
    {
        "Name": "Vermont",
        "Capital": "Montpelier",
        "Population": 0000,
        "Best Universities": ["College1", "College2", "College3"],
    },
    {
        "Name": "Washington",
        "Capital": "Olympia",
        "Population": 0000,
        "Best Universities": ["College1", "College2", "College3"],
    },
    {
        "Name": "West Virginia",
        "Capital": "Charleston",
        "Population": 0000,
        "Best Universities": ["College1", "College2", "College3"],
    },
    {
        "Name": "Wisconsin",
        "Capital": "Madison",
        "Population": 0000,
        "Best Universities": ["College1", "College2", "College3"],
    },
    {
        "Name": "Wyoming",
        "Capital": "Cheyenne",
        "Best Universities": ["College1", "College2", "College3"],
        "Population": 800000,
    },
]


def multiple_choice_game():
    capitals = []
    wrong_answers = []

    def multiple_answers():
        for dic in state_dict_list:
            capitals.append(dic["Capital"])

        wrong_answers.append(capitals[random.randrange(0, 50)])
        wrong_answers.append(capitals[random.randrange(0, 50)])
        wrong_answers.append(capitals[random.randrange(0, 50)])

        print(f"Wrong Answers: {wrong_answers}")
        return wrong_answers

    wrong_answers = multiple_answers()
    # Validation: check all 3 wrong answers do not match the correct answer
    for choice in wrong_answers:
        if choice == "Trenton":
            wrong_answers = []
            wrong_answers = multiple_answers()

    print("Wrong answers validated")

    return wrong_answers


multiple_choice_game()


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
