# Given a string of integers, write a program to generate an output string as follows.
#  i) From the input integers, filter the integers that are perfect squares. Ex: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100...
#  ii) For each perfect square obtained from step 1, find its factorial. If the factorial of the
#      number is trailing by zeros, three digits present before the trailing zeros should be appended to 
#      output string. If not trailing by zeros append last three digits to output string. If there is a
#      preceding zero, it is ignored.
#    i. if the number is 2 then 2!=2, it does not have any trailing zeros and there is only one digit in
#       it, so append 2 to output.
#    ii. if the number is 5 then 5!=120, then it has one trailing zero, before trailing zero there are
#        only two digits present so append 12 to output.
#    iii. if the number is 9 then 9!=362880, it has one trailing zero, before trailing zero there are 
#         five digits present, so consider three digits before trailing zero that is 288 and append to
#         output
#    iv. if the number is 12 then 12!=479001600, it has two trailing zeros there are seven digits present,
#        so consider three digits before trailing zero that is 016 as 0 is preceded here, 0 is ignored
#        and 16 is appended to output.
#  iii) If there are no positive perfect squares in the input string print -1

import math

def perfect_square(input_string):
    out_string = ''
    list_of_numbers = input_string.split(',')
    #['2', '4', '8', '9', '35', '100']
    list_of_squares = []
    #[4, 9, 100]
    for number in list_of_numbers:
        if int(number)**(1/2) == int(int(number)**(1/2)):
            list_of_squares.append(int(number))
    if len(list_of_squares) > 0:
        for number in list_of_squares:
            num_factorial = str(math.factorial(number))
            num_factorial = num_factorial.rstrip('0')
            num_to_append = num_factorial[-3:]
            num_to_append = num_to_append.lstrip('0')
            out_string += num_to_append
    else:
        # list_of_squares = []
        return -1



    return out_string




input_string = '2,4,8,9,16'
print(perfect_square(input_string))