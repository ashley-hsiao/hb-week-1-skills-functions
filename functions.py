# SOLUTIONS!

################################################################
# PART ONE


# 1. Write a function that does not take any arguments and
#    prints "Hello World".

def print_hello_world():
    print "Hello World"


# 2. Write a function that takes a name as a string and
#    prints "Hi" followed by the name.

def user_greeting(name):
    print "Hi {}".format(name)


# 3. Write a function that takes two integers and multiplies
#    them together. Print the result.

def mult_two_nums(x, y):
    return x * y


# 4. Write a function that takes a string and an integer and
#    prints the string that many times

def string_multipler(string, n):
    print string * n


# 5. Write a function that takes an integer and prints "Higher
#    than 0" if higher than zero and "Lower than 0" if lower
#    than zero. If integer is 0 print "Zero".

def number_greater_than_zero(num):
    if num > 0:
        print "Higher than 0"
    elif num < 0:
        print "Lower than 0"
    else:
        print "Zero"


# 6. Write a function that takes an integer and returns a
#    boolean (True or False), depending on whether the number
#    is evenly divisible by 3.

def is_divisible_by_3(num):
    return num % 3 == 0


# 7. Write a function that takes a sentence as one string and
#    returns the number of spaces.

def number_of_spaces(sentence):
    count = 0

    for char in sentence:
        if char == " ":
            count += 1

    return count


# 8. Write a function that can be passed a meal price and a
#    tip percentage. It should return the total amount paid
#    (price + price * tip). **However:** passing in the tip
#    percentage should be optional; if not given, it should
#    default to 15%.

"""Assumes user puts in whole number for percentage, not decimal. Therefore tip is floated and divided by 100.
"""

def calculate_meal(price, tip=15):
    return price + price * (float(tip)/100)


# 9. Write a function that takes an integer as an argument and
#    returns two pieces of information as strings ---
#    "Positive" or "Negative" and "Even" or "Odd". The two strings
#	 should be returned in a list.
#
# 	Then, write code that shows the calling of this function
# 	on a number and unpack what is returned into two
# 	variables --- sign and parity (whether it's positive
# 	or negative). Print sign and parity.

def integer_info(num):
    sign = None
    parity = None

    if num > 0:
        sign = "Positive"
    else:
        sign = "Negative"

    if num % 2 == 0:
        parity = "Even"
    else:
        parity = "Odd"

    return [sign, parity]


sign, parity = integer_info(32)
print sign
print parity


################################################################
# PART TWO


# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).
#
#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviaton, and the
#    default tax amount as parameters.
#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item including tax.

"""Assumes user puts in whole number for percentage, not decimal. Therefore tax is floated and divided by 100.
"""


def calculate_item_cost(cost, state, tax=5):
    if state == "CA":
        tax = 7

    return cost + cost * (float(tax)/100)


# 2. Turn the block of code from the directions into a function.
#	 Take a name and a job title as parameters, making it so the
# 	 job title defaults to "Engineer" if a job title is not passed in.
#	 Return the person's title and name.

def print_name_title(name, job_title="Engineer"):
    # Use string formatting so that output is not a string
    return "{} {}".format(job_title, name)


# 3. Given a receiver's name, receiver's job title, and sender's name, print the following letter:      
#       Dear JOB_TITLE RECEIVER_NAME, I think you are amazing! Sincerely,
#       SENDER_NAME. 
#    Use the function from #2 to construct the full title for the letter's greeting.

# 4. Turn the block of code from the directions into a function. This
#    function will take a number and append it to *numbers*. It doesn't
#    need to return anything.
