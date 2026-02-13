# Functions go here
def int_checker(question):
    """checks that the users enter an integer"""

    error = "Oops - please enter an integer"




    while True:

        try:
            # return the response if it's an integer
            response = int(input(question))

            return response

        except ValueError:
            print(error)




# Main routine goes here

# testing loop
while True:
    print()

    #ask user for their name
    name = input("name: ") #replace with a call to the 'not blank function'

    #ask user for their age and check it's between 12 and 120
    age = int_checker("age: ")

    if age < 12:
        print(f"{name} is too young, sorry kid.")
        continue
    elif age > 120:
        print(f"{name} is too old, sorry grandpa.")
        continue
    else:
        print(f"{name} bought a ticket, enjoy the movie!")
