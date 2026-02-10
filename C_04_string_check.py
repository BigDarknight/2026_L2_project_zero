# Functions go here
def string_check(question, valid_ans_list):
    """checks that the user enters the full word
    or first letter of a word fom a list of responses"""

    while True:

        response = input(question).lower()

        for item in valid_ans_list:
            if response == item:
                return item

            elif response == item[0]:
                return item

        print(f"please choose an option from {valid_ans_list}")

# Main routine goes here
levels = ['easy', 'medium', 'hard']

like_coffee = string_check("do you like coffee? ", ['yes', 'no'])
print(f"you chose {like_coffee}")
choose_level = string_check("choose a level: ", levels)
print(f"you chose {choose_level}")