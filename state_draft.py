import random

state_list = [
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

#####################################################################################################
# Pretend this is top of the file. Imports always go at the top.


def stateNames(state):
    return state


states = map(stateNames, state_list)
# print(f"State list: {list(states)}")

# Notice the way I log, providing a detailed word, in this case, State List:, and using string interposlation.
# It helps when you log multiple things and is a common good practice.
# I'm not sure why I needed the list() method, but it didn't work without it. Maybe you can look into this method.
# pulling out state names from dictionary and setting it to variable
# print(states)--> ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']


while len(state_list) > 0:
    single_state_dict = random.choice(state_list)
    state = single_state_dict["Name"]
    capital = single_state_dict["Capital"]

    user_guess = input("What is the capital of " + state + "? ")

    if user_guess == capital:
        print("Woohoo! You got it.")
    elif user_guess not in capital:
        print("Oh no, your answer is incorrect.")
    else:
        break

# Notice my use of the list of capitals, or rather it's length, as the while conditional statement.
# while len(state_list) > 0:
# Instead of True. Probably should never do that because you risk creating an infinite loop, which will crash your script.

# Notice how I use the data object (state_list) I showed you when I last saw you.

# Notice how I was able to pull how the state and capital name into variables similar to what you were doing, but from a dictionary.
# This is a much more common practice on how to handle the way you'd normally see data displayed.

# Think about what else you can add to the object to make an even more interesting question.
# Maybe some kind of true/false question, adding a boolean to each state.
# Is this state republican or democratic/ blue or red?
# or true to red, then false would be blue

# Maybe a guess on the population?
# You could even make a guessing game out of it, check if there answer is wihtin 5000, or 1000, or 100, and respond with closer but too high or too low...

# Maybe have a set amount of guesses or infinite till they guess the number for that game.
# Think about key words they can use to skip the question. The way you have exit.
# Think about key word, change question, then maybe it asks a different sort, like the population guessing game, or something else.

# For those games, you may add new info to each object.
# Some will be specific.
# Some will be generic.
#  highlight something generic each object has, but just once
# use the key commands: command + D
# keep hitting d or hold it down, until it's highlighed the same thing on all 50 dictionaries within the list.
# e.g. highlight      "Name":     and then hold command + d
# Then tap the arrows to move your cursor to a new line and add a new key/value
# value being a boolean, list, diction, depending on what you want to add.

# Also get use to running a pythond program like a programmer.
# Instead of pressing Run in vs code,
# Open a terminal, cd into your project, at the root, aka the top file,
# type python or python3, then the name of the file.
# e.g. root folder: Quiz-Capitals, python3 sebs.py

# Let me know if you have any questions about clarification.
# Clarification is important. I'll let you do it, I won't help, but please ask for clarification. THat's important and different than help.
# And incredibly foolish not to ask because it makes sure you're thinking abou things the right way.
# Good luck, it looks great so far. I'm happy you're understanding how to use loops very well.
# Now just fine tuning real use cases and deeper ideas.
