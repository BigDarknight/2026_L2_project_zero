# Functions go here
def string_check(question, valid_ans_list, num_letters):
    """checks that the user enters the full word
    or 'n' letter/s of a word fom a list of responses"""

    while True:

        response = input(question).lower()

        for item in valid_ans_list:
            if response == item:
                return item

            elif response == item[:num_letters]:
                return item

        print(f"please choose an option from {valid_ans_list}")

# Main routine goes here
yes_no_list = ['yes', 'no']
payment_list = ['cash', 'credit']

like_coffee = string_check("do you like coffee? ", yes_no_list, 1)
print(f"you chose {like_coffee}")
pay_method = string_check("payment method: ", payment_list, 2)
print(f"you chose: {pay_method}")