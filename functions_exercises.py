# '''#1 Define a function named is_two.
# It should accept one input and
# return True if the passed input is either the number
# or the string 2, False otherwise.'''


def is_two(arg):
    if arg == '2' or arg == 2:
        return True
    else:
        return False



# '''#2 Define a function named is_vowel.
# It should return True if the passed string is a vowel,
# False otherwise.'''


def is_vowel(letter):
    if letter in('a', 'e', 'i', 'o', 'u'):
    # worked example alternative: if letter in 'aeiou'
        return True
    else:
        return False



# ''' #3 Define a function named is_consonant.
# It should return True if the passed string is a consonant,
# False otherwise. Use your is_vowel function to accomplish this.'''


def is_consonant(thing):
    if thing.isdigit():
        return False
    elif not is_vowel(thing):
        if len(thing) == 1 and thing.isalpha():
            return True
        else:
            return False
    else:
        return False



# '''#4 Define a function that accepts a string that is a word.
# The function should capitalize the first letter of the word if the
# word starts with a consonant.'''


def cap_cons(argument):
    if is_consonant(argument[0]):
        newstring = argument[0].upper() + argument[1:]
        return newstring
    else:
        return argument



# ''' #5: Define a function named calculate_tip.
# It should accept a tip percentage (a number between 0 and 1)
# and the bill total, and return the amount to tip.'''


def calculate_tip(percentage, bill_total):
    dollar_tip = percentage * bill_total
    return dollar_tip




# '''#6: Define a function named apply_discount,
# It should accept a original price, and a discount percentage,
# and return the price after the discount is applied'''


def apply_discount(price, discount_percentage):
    dollars_off = price * discount_percentage
    price -= dollars_off
    return price



# '''#7: Define a function named handle_commas.
# It should accept a string that is a number
# that contains commas in it as inputand returns a number as output'''


def handle_commas(arg):
    commaless = arg.replace(',', '')
    if commaless.isdigit():
        return float(commaless)
    else:
        return 'THIS FUNCTION IS FOR NUMBERS {} NUMBERS ONLY PLEASE'.format(commaless)


# '''#8: Define a function named get_letter_grade.
# It should accept a number and return the letter grade
# associated with that number (A-F).'''


def get_letter_grade(numerical_grade):
    if numerical_grade >= 88:
        return 'A'
    elif numerical_grade >= 80:
        return 'B'
    elif numerical_grade >= 67:
        return 'C'
    elif numerical_grade >= 60:
        return 'D'
    else:
        return 'F'


# '''#9: Define a function named remove_vowels that
# accepts a string and returns a string with all the vowels removed.'''


def remove_vowels(some_string):
    # Worked Example more elegant version:
    # return ''.join([letter for letter in some_string if not is_vowel(letter)])
    consonant_string = ""
    for letter in some_string:
        if letter in('a', 'e', 'i', 'o', 'u'):
            continue
        else:
            consonant_string += letter
    return consonant_string



# '''#10: Define a function named normalize_name.
# It should accept a string and return a valid python identifier,
#  that is:
# anything that is not a valid python identifier should be removed
# leading and trailing whitespace should be removed
# everything should be lowercase
# spaces should be replaced with underscores
# for example:
# Name will become name
# First Name will become first_name
# % Completed will become completed'''

LETTERS = ' abcdefghijklmnopqrstuvwxyz1234567890_'
def normalize_name(name):
    normal_name = ''
    primed_name = name.strip().lower()
    for letter in primed_name:
        if letter not in LETTERS:
            continue
        else:
            normal_name += letter
    return normal_name.strip().replace(' ', '_')



# '''#11: Write a function named cumsum that accepts
# a list of numbers and returns a list that is
# the cumulative sum of the numbers in the list.
# cumsum([1, 1, 1]) returns [1, 2, 3]
# cumsum([1, 2, 3, 4]) returns [1, 3, 6, 10]'''

def cumsum(some_list):
    new_list = []
    for i in range(0, len(some_list)):
        if i == 0:
            new_list.append(some_list[i])
        else:
            new_list.append(some_list[i] + new_list[i-1])
    return new_list






# '''Bonus 1:
# Create a function named twelveto24.
# It should accept a string in the format 10:45am or 4:30pm
# and return a string that is the representation of the time in a 24-hour format.
# Bonus write a function that does the opposite'''


def twelveto24(time_string):
    mil_time = ''
    pm_hour = ''
    if time_string[-2] in('a', 'A'):
        for digit in time_string:
            if digit in['a', 'm', 'A', 'M']:
                continue
            else:
                mil_time += digit
        return mil_time
    elif time_string[-2] in('p', 'P'):
        for digit in time_string:
            if digit == ':':
                break
            else:
                pm_hour += digit
        mil_hour = int(pm_hour) + 12
        mil_time += str(mil_hour) + ':' + time_string[-4:-2]
        return mil_time




# SUB BONUS EXTRA DO IT BACKWARDS NOW WEEEOW


def twentyfourto12(time):
    temp_hour = ''
    pm_time = ''
    am_time = ''
    for digit in time:
        if digit == ':':
            break
        else:
            temp_hour += digit
    if int(temp_hour) <= 12:
        am_time = time + 'am'
        return am_time
    else:
        new_hour = int(temp_hour) - 12
        pm_time = str(new_hour) + ':' + time[-2:len(time)] + 'pm'
        return pm_time




# Bonus #2:


def letter_val(letter):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    value = alphabet.index(letter) + 1
    return value


def col_index(col_name):
    trick = 0
    if len(col_name) > 1:
        for letter in range(0, len(col_name)-1):
            trick += 26 * letter_val(col_name[letter]) - (letter_val(col_name[letter]) - 1)
    running_total = trick
    for letter in col_name:
        running_total += letter_val(letter)
    running_total -= (len(col_name) - 1)
    return running_total



# '''1. Write a function named `add`. It should accept two arguments
# and return the result of adding the two arguments together.'''


def add(prompt1, prompt2):
    user_input1 = input(prompt1)
    if not user_input1.isdigit():
        print('Error: {} is not an integer'.format(user_input1))
        return add(prompt1, prompt2)
    user_input2 = input(prompt2)
    if not user_input2.isdigit():
        print('Error: {} is not an integer'.format(user_input2))
        return add(prompt1, prompt2)
    return int(user_input1) + int(user_input2)



# '''2. Write a function named `subtract`.
# It should accept two arugments and return
# the result of subtracting the first from the second.'''


def subtract(prompt1, prompt2):
    user_input1 = input(prompt1)
    if not user_input1.isdigit():
        print('Error: {} is not an integer'.format(user_input1))
        return add(prompt1, prompt2)
    user_input2 = input(prompt2)
    if not user_input2.isdigit():
        print('Error: {} is not an integer'.format(user_input2))
        return add(prompt1, prompt2)
    return int(user_input2) - int(user_input1)



# '''3. Write a function named `multiply`. It should accept two numbers and return the result of multiplying them together.'''

# '''Bonus: don't use the `*` operator in your `multiply` function'''
# '''Bonus Bonus: don't use a loop in your `multiply` function'''
