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
make_statement("emoji in action", decoration= "😊" ,lines=1)
