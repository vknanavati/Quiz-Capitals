# state_cap = [
#     ("Alabama", "Montgomery"),
#     ("Alaska", "Juneau"),
#     ("Arizona", "Phoenix"),
#     ("Arkansas", "Little Rock"),
#     ("California", "Sacramento"),
#     ("Colorado", "Denver"),
#     ("Connecticut", "Hartford"),
#     ("Delaware", "Dover"),
#     ("Florida", "Tallahassee"),
#     ("Georgia", "Atlanta"),
#     ("Hawaii", "Honolulu"),
#     ("Idaho", "Boise"),
#     ("Illinois", "Springfield"),
#     ("Indiana", "Indianapolis"),
#     ("Iowa", "Des Moines"),
#     ("Kansas", "Topeka"),
#     ("Kentucky", "Frankfort"),
#     ("Louisiana", "Baton Rouge"),
#     ("Maine", "Augusta"),
#     ("Maryland", "Annapolis"),
#     ("Massachusetts", "Boston"),
#     ("Michigan", "Lansing"),
#     ("Minnesota", "Saint Paul"),
#     ("Mississippi", "Jackson"),
#     ("Missouri", "Jefferson City"),
#     ("Montana", "Helena"),
#     ("Nebraska", "Lincoln"),
#     ("Nevada", "Carson City"),
#     ("New Hampshire", "Concord"),
#     ("New Jersey", "Trenton"),
#     ("New Mexico", "Santa Fe"),
#     ("New York", "Albany"),
#     ("North Carolina", "Raleigh"),
#     ("North Dakota", "Bismarck"),
#     ("Ohio", "Columbus"),
#     ("Oklahoma", "Oklahoma City"),
#     ("Oregon", "Salem"),
#     ("Pennsylvania", "Harrisburg"),
#     ("Rhode Island", "Providence"),
#     ("South Carolina", "Columbia"),
#     ("South Dakota", "Pierre"),
#     ("Tennessee", "Nashville"),
#     ("Texas", "Austin"),
#     ("Utah", "Salt Lake City"),
#     ("Vermont", "Montpelier"),
#     ("Washington", "Olympia"),
#     ("West Virginia", "Charleston"),
#     ("Wisconsin", "Madison"),
#     ("Wyoming", "Cheyenne"),
# ]
# d = dict(state_cap)
# print(d)

import random

state_cap = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
    "Colorado": "Denver",
    "Connecticut": "Hartford",
    "Delaware": "Dover",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
    "Hawaii": "Honolulu",
    "Idaho": "Boise",
    "Illinois": "Springfield",
    "Indiana": "Indianapolis",
    "Iowa": "Des Moines",
    "Kansas": "Topeka",
    "Kentucky": "Frankfort",
    "Louisiana": "Baton Rouge",
    "Maine": "Augusta",
    "Maryland": "Annapolis",
    "Massachusetts": "Boston",
    "Michigan": "Lansing",
    "Minnesota": "Saint Paul",
    "Mississippi": "Jackson",
    "Missouri": "Jefferson City",
    "Montana": "Helena",
    "Nebraska": "Lincoln",
    "Nevada": "Carson City",
    "New Hampshire": "Concord",
    "New Jersey": "Trenton",
    "New Mexico": "Santa Fe",
    "New York": "Albany",
    "North Carolina": "Raleigh",
    "North Dakota": "Bismarck",
    "Ohio": "Columbus",
    "Oklahoma": "Oklahoma City",
    "Oregon": "Salem",
    "Pennsylvania": "Harrisburg",
    "Rhode Island": "Providence",
    "South Carolina": "Columbia",
    "South Dakota": "Pierre",
    "Tennessee": "Nashville",
    "Texas": "Austin",
    "Utah": "Salt Lake City",
    "Vermont": "Montpelier",
    "Washington": "Olympia",
    "West Virginia": "Charleston",
    "Wisconsin": "Madison",
    "Wyoming": "Cheyenne",
}

states = list(state_cap.keys())
# pulling out state names from dictionary and setting it to variable
# print(states)--> ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

while True:
    state = random.choice(states)
    capital = state_cap[state]
    user_guess = input("What is the capital of " + state + "? ").capitalize()

    if user_guess == capital:
        print("Woohoo! You got it.")
    elif user_guess not in capital:
        print("Oh no, your answer is incorrect.")
    else:
        break

#  if user_guess == "exit":
#         break
#     elif user_guess == capital:
#         print("Correct!")
#     else:
#         print("Incorrect")

# use .capitalize
# space
