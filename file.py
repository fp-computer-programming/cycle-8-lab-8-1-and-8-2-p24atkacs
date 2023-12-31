"""
Create a Python file named lab_8-1.py

*** You must write a comment for every chunk of code you write from now on along with your author tag***
Create a Python file named lab_8-1
Write a function in that uses the for loop and the range function to find the sum of all the numbers up to and including the number the user input
The function should return the final total of the sum of all of the items in the list
Add a statement that prompts the user to input an integer
Call the function from step 2 and store its output as a variable
Add a statement to print the variable to see the final sum

__________________________________________________________

Create a Python file named lab_8-2

*** You must write a comment for every chunk of code you write from now on along with your author tag***

Write a function that will take a list of names and write the body of an email to invite them to a party
The body should be something like this: "Hi name, You're invited to my party on Friday!" Where name is the name of each person in the list.
The function should use a for loop and print each invitation after it is generated. There should be at least 3 names in the list.



"""

# Author: Andrew Tkacs

def generate_party_invitations(names):
    """
    prints party invitations for each person in the given list.

    """
    for name in names:
        invitation = f"Hi {name}, You're invited to my party on Friday!"
        print(invitation)

# list of names
guest_list = ["Mr. O", "Josh", "Charlie"]

# Generate and print party invitations using the defined function
generate_party_invitations(guest_list)
