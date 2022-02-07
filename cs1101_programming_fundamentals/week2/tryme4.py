def new_line():
    print('.')

def three_lines():
    new_line()
    new_line()
    new_line()

# To print 9 lines, call three_lines function 3 times.
def nine_lines():
    three_lines()
    three_lines()
    three_lines()

def clear_screen():
    print("Calling clearScreen()")


#########################################################
# main section of the program which calls the functions #
#########################################################

nine_lines()
clear_screen()

# To print 25 lines, call three_lines() twice, nine_lines() twice and new_line()
# once. Then the total lines will be 3 + 3 + 1 + 9 + 9 = 25.
three_lines()
three_lines()
new_line()
nine_lines()
nine_lines()
clear_screen()
