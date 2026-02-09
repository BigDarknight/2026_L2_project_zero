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
