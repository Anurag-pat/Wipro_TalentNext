"""
Create a dictionary that contains a list of people and one interesting fact about each of them.

Display each person and his or her interesting fact to the screen. Next, change a fact about one of the people. Also add an additional person and corresponding fact. Display the new list of people and facts. Run the program multiple times and notice if the order changes.

Sample output:

Jeff: Is afraid of Dogs.

David: Plays the piano.

Jason: Can fly an airplane.

Jeff: Is afraid of heights.

David: Plays the piano.

Jason: Can fly an airplane.

Jill: Can hula dance.
"""

people_facts = {
    "Jeff": "Is afraid of Dogs.",
    "David": "Plays the piano.",
    "Jason": "Can fly an airplane."
}


print("Original facts:\n")
for person, fact in people_facts.items():
    print(f"{person}: {fact}")


people_facts["Jeff"] = "Is afraid of heights."


people_facts["Jill"] = "Can hula dance."


print("\nUpdated facts:\n")
for person, fact in people_facts.items():
    print(f"{person}: {fact}")
