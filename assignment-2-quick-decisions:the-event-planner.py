# 2. Quick Decisions: The Event Planner 🎉
# Objective:
# To practice the use of shorthand if statements in determining event-related decisions.

# Task 1: Code Correction
# You are provided with a Python script that is supposed to help in event planning, but it has errors. Identify and fix them.

# Buggy Code:
# attendees = input("Enter number of attendees: ")
# venue = "large hall" if attendees > 100 else "conference room"
# print(venue)

#FIXED CODE
# attendees = int(input("Enter number of attendees: "))
# venue = "large hall" if attendees > 100 else "conference room"
# print(venue)


# Task 2: Venue Selection
# Based on the corrected code from Task 1, further enhance the program to recommend additional facilities like "audio system" or "projector" based on the number of attendees.

# attendees = int(input("Enter number of attendees: "))
# venue = "large hall" if attendees > 100 else "conference room"
# additional_facilities = "We recoomend audio equipment & a projector." if attendees > 100 else "We recommend small catering."
# print(venue)
# print(additional_facilities)


# Task 3: Catering Choices
# Ask the user if they want "vegetarian" food. Recommend "Veggie Delight Caterers" if yes, otherwise recommend "Gourmet Meals Caterers".

attendees = int(input("Enter number of attendees: "))
venue = "We recommend a large hall." if attendees > 100 else "We recommend a conference room."
print(venue)
additional_facilities = "We recommend audio equipment & a projector." if attendees > 100 else "We recommend small catering."
print(additional_facilities)
if additional_facilities == "We recommend small catering.":
    food_type = input("Would you like vegetarian food? ")
    food = "We'll get Veggie Delight Caterers." if food_type == "yes" else "We'll get Gourmet Meals Caterers."
    print(food)


