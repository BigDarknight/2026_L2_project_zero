[C_01_make_statement_V2.py](https://github.com/user-attachments/files/25192465/C_01_make_statement_V2.py)
# functions go here
def make_statement(statement, decoration, lines):
    """creates decoration for headings (3 lines) subheadings (2 lines) and emphazied text (1 line)
     only use emoji for single line statements"""

    middle = f"{decoration * 3} {statement} {decoration * 3}"
    top_bottom = decoration * len(middle)

    if lines == 1:
        print(middle)
    elif lines == 2:
        print(top_bottom)
        print(middle)[sandbox.py](https://github.com/user-attachments/files/25192467/sandbox.py)
[C_01_make_statement_V3.py](https://github.com/user-attachments/files/25192466/C_01_make_statement_V3.py)

    else: 
        print(top_bottom)
        print(middle)
        print(top_bottom)

# Main routine goes here
make_statement("programming is fun!", decoration= "=",lines=3)
print()
make_statement("programming is still fun!", decoration="*", lines =2)
print()
make_statement("emoji in action", decoration= "😊" ,lines=1)

# functions go here
def make_statement(statement, decoration, lines=1):
    """creates decoration for headings (3 lines) subheadings (2 lines) and emphasized text (1 line)
     only use emoji for single line statements. default is one line"""

    middle = f"{decoration * 3} {statement} {decoration * 3}"
    top_bottom = decoration * len(middle)

    if lines == 1:
        print(middle)
    elif lines == 2:
        print(top_bottom)
        print(middle)
    else: 
        print(top_bottom)
        print(middle)
        print(top_bottom)

# Main routine goes here
make_statement("programming is fun!", decoration= "=",lines=3)
print()
make_statement("programming is still fun!", decoration="*", lines =2)
print()
make_statement("emoji in action", decoration= "😊")

number = 5
print(number * 5)

num_string = "5"
print(num_string * 5)

example_text = "hello world"
text_length = len(example_text)

print(f"'{example_text}' is {text_length} charicters long")
