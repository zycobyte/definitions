'''
Check your indentation
Programs must be indented correctly in python so the computer knows what parts of the code to perform when. This normally changes near key words.
The key words are usually orange

Examples include "while" and "for" loops, "if", "elif" or "else" statements, and after "def" for a function. You may also use "try" "except" for errors.

The above are at the START OF THE LINE. They all INCREASE the indentation by one

Some key words may START THE LINE but instead they DECREASE the indentation by one like "return", "continue" and "pass" (though you will likely not come across pass in code)

If a keyword typically appears WITHIN BUT NOT AT THE START such as "True", "False", "in" etc then it DOES NOT CHANGE INDENTATION

More complex keywords exist that break these rules but you shouldnt need to learn about those ones for GCSE
'''
while False:
    # code here is indented, it runs within the while loop
    # still inside the loop, so still indented
    pass # this line can be ignored, it is needed to make the file run
# outside the loop, indented back to the same level as the while


for i in range(1,2,3):
    # indented by one to run inside the for loop
    if i < 10:
        # indented by one from the if statement, so its inside the if statement
        if i > 0:
            # indented by one from the second if statement, so inside the second if statement
            # if you draw a line up at the start of the line you should hit a line of code that tells you what you are inside
            # following the #'s up hits the 2nd if statement, so we know we are inside the second if statement
            pass # this line can be ignored, it is needed to make the file run

        # If we draw a line up from the start of this line we see we are AT THE SAME LEVEL as the 2nd if statement
        # This means we are NOT inside the 2nd if statement, we are on the same level as it
        # If we keep drawing the line up we hit the first if statement (1 < 10). This means we are still inside it

        # If you imagine that its like stairs in a building, we are on the same level as the 2nd if statement which is the bottom of a staircase that leads up to a different level of identation from our level
        # We are one level up from the 1st if statement, beccause we have gone up the staircase on the level below and are now inside the level it lead up to
        
    # When we go back down the stairs, we are no longer inside the level the first if statement lead to. This code is executed after we have finished on the higher level
    # This line is still inside where the for loop leads and so it will execute each iteration of the for loop
    
# when we go back down to no indentation it takes us downstairs and outside (assuming the imaginary door to the for loops staircase goes straight from outside to a staircase)
# here we are no longer inside the for loop and any code is executed after the for loop is finished

'''
Creating a variable
This allows us to store some data into memory, and give that memory a name. The name we give it should be meaningful as often as possible.
When we want to use this data later, we use the variables name.
Variables names must be lower or uppercase characters, underscores ( _ ) or, with the exception of the first character, a number.

  valid names:
             : abc
             : _test
             : var2
invalid names:
             : 9test
             : test-variable
             : name with spacebar

The value stored may be:
                       : a specific value, such as variable or hello
                       : a calculation like mathExpression or boolean
                       : returned from some function like anotherName

'''
variable = 123 # variable is set to be 123
hello = "This is the hello message" # hello is set as a message
math_expression = 5+3 # 5+3 is calculated and math_expression is set to be 8
boolean = 5 < 4 # 5 < 4 is calculated and as 5 is not less, boolean is set to False
users_input = input("users_input >> ") # we call input and it returns the users text, which users_input is set to 

'''
Constants work like variables but do not change ever. The value is set once in the code and only ever read.
Most languages have a specific type for this but in python it is done by creating a variable with its name in all capitals
'''
PI = 3.141592  # the value of pi is never going to change
COMPANY_NAME = "bobs burgers" # the company name is assumed to never change and created as constant


'''
inputs and outputs
In a flow chart, these are diaganol rectangles, in python we either use "input" or "print"
'''
input("This is the prompt. It is shown to the user to make it clear what we are asking them to enter >> ")
print() # will print nothing then move to a new line
print("The print function takes a value to print. it can be any data type. If you want to combine data types, they should be seperated by a comma", 5, "like that which will put the number 5 between the words 'comma' and 'like' with a space")
print() # will print nothing then move to a new line
print("we can also combine variables:", variable, hello, users_input)


'''
mathematics
mathematics in programming follows BIDMAS
'''
addition         = 1 + 2  # is 3
subtraction      = 1 - 2  # is -1
multiplication   = 1 * 2  # is 2
division         = 1 / 2  # is 0.5
exponents        = 1 ** 2 # is 1 (1 to the power of 2)
integer_division = 1 // 2 # is 0 because 1/2 is 0 remainder 1
modulo_division  = 1 % 2  # is 1 because 1/2 is 0 remainder 1


'''
boolean logic

'''
# AND, OR and NOT in python
True and True
True or True
not False

# not equal and is equal
True != False
True == True

# less, greater, less than or equal, greater than or equal
1 < 2
1 <= 1
2 > 1
2 >= 2

'''
sequence is one line of code running before the one below it in order
'''
line1 = "runs first"
line2 = "runs next"
line3 = "runs after line 2"
line4 = "and then this line runs 4th"


'''
selection
This is the diamond in a flow chart. It has a true or false output and uses boolean logic to determine this
It may have multiple conditions such as if, else if, else
'''
if 1 < 2:
    pass
elif 1 > 2:
    pass
else:
    pass


'''
iteration
This is the diamond in a flow chart. It has a true or false output and uses boolean logic to determine this
Iteration is the process of executing the same line(s) of code mutiple times until a given condition is met
It is similar to selection however it runs its code until a condition is met as opposed to running it if a condition is met

Two types:
         : Definite / count controlled
         :      - There is a set number of iterations and a counter is used to keep track. typically a for loop
         : Indefinite / condition controlled
         :      - The code runs an unknown number of times until some condition becomes true. typically a while loop

The two most common are "for" and "while" though there are other types of loops
'''

for i in range(0, 10, 1):
    pass # will execute 10 times


while False == True:
    pass # will execute until False does not equal True. In this example it wont execute to prevent an infinite loop however more complex conditions will usually be used where the execution could be any number of iterations


'''
data types
1D and 2D arrays

    Integer   - a whole number
    Real      - a number which can include decimals
    Boolean   - True or False
    Character - a single letter
    String    - a series of letters
    Array     - an array is a series of any data type. A string is an array of characters
    2D Array  - an array of arrays

    Casting   - converting between different data types

'''
#casting to integer (result = 1)
integer = int(1.5)
integer = int("1")

#casting to a real number (result = 2.5)
real = float("2.5")

#casting to a boolean (result = True)
boolean = bool("True")
boolean = bool(1)

#casting to a character from character code (result = "A")
character = chr(65)

#casting to a character code from a character (result = 65)
char_code = ord("A")

#casting to a string (result = "123")
string = str(123)

## arrays
array = [0,1,2,3,4] # an array containing 5 numbers
array2d = [
      [0,1,2],
      [3,4,5],
      [6,7,8]
    ] # an array containing 3 arrays, each of which contain 3 numbers


'''
random numbers
'''


'''
function and procedures
'''
