**[Back](https://github.com/zycobyte/definitions/blob/master/README.md)**

***BOLD ITALIC*** - key words

# Key Definitions


## Computational Thinking
> A ***problem-solving method*** using ***computer science techniques*** such as decomposition, pattern recognition, abstraction, generalisation, and algorithms, where ***possible solutions are developed*** and presented in a way that can be ***understood by humans and computers***.
- It involves breaking down a complex problem into simple steps
- It involves problem solving, logical thinking and pattern recognition as well as evaluation
- It is not "thinking like a computer" rather "thinking in a way a computer can understand"

##### Pros
- Develops robust systems that are ***easier to maintain***
- Helps to organise codebases
- Allows you to focus on only the important parts
##### Cons
- Requires practice

#### Example
The game Guess Who is a good example of computational thinking.
You must think logically to break up the problem into a smaller and smaller group if people. You ignore any irrelevant details (such as excluded characters or details present in no characters) as you focus on finding the solution. Different questions asked (like algorithms) have different efficiencies. For example if 1/100 characters have green eyes then 99% of the time that would be a very inefficient first question to ask. A better question would be to ask about their gender presentation, as you would be able to exclude about half of the options immediately with consistent results.

#### Resources
- Intro into computational thinking: https://www.bbc.co.uk/bitesize/guides/zp92mp3/revision/3
- Computational thinking, decomposition and abstraction: https://www.bbc.co.uk/bitesize/guides/z4rbcj6/revision/1
- Applications of computational thinking: https://www.bbc.co.uk/bitesize/topics/zbg7gwx

## Decomposition
> The process of ***breaking down*** a ***complex problem*** into ***smaller sub-tasks*** which are ***easier to understand*** and work through.
- similar to how when an organism decomposes, it is broken down into smaller parts
- allows you to view a large task in manageble steps

##### Pros
- Helps programmers notice where code can be re-used
- Makes a problem more manageable and easier to understand
##### Cons
- Must understand the problem well to fully and efficiently decompose it
- Could lose some info or context during decomposition process

#### Example
![https://sp-ao.shortpixel.ai/client/to_auto,q_glossy,ret_img,w_876/https://www.knowitallninja.com/wp-content/uploads/2018/10/1.2.jpg](https://sp-ao.shortpixel.ai/client/to_auto,q_glossy,ret_img,w_876/https://www.knowitallninja.com/wp-content/uploads/2018/10/1.2.jpg)

#### Resources
- Evaluating a solution: https://www.bbc.co.uk/bitesize/guides/zssk87h/revision/1
- Decomposition: https://www.bbc.co.uk/bitesize/guides/zqqfyrd/revision/1
- Decomposition, Abstraction and sub-programs: https://www.bbc.co.uk/bitesize/guides/z7ddqhv/revision/1
- Computational thinking, decomposition and abstraction: https://www.bbc.co.uk/bitesize/guides/z4rbcj6/revision/2


## Abstraction
> Abstraction is the process of ***filtering out irrelevant/unnecessary characteristics/details*** of a problem to focus on what is ***important to solve the problem or reduce complexity for users***
- Allows you to generalise a problem, like calculating the area of a square, the algorithm would be written as *width \* width* to work for all squares, and then can be told what the width is at runtime.
- Allows you to hide complexity at a lower level. The user may only see the rendered screen and not worry about how the screen is rendered. Similarly a programmer may see modules that have been abstracted, so "render board" and "render objects" have their complexity hidden at a lower level in the program.

##### Pros
- Allows you to focus on what is important
- Can re-use code easily
- Can be easier to get an overview of how the system is working
##### Cons
- Software can be over-abstracted and become more complex
- Can be harder to figure out all the exact details of how a system is working

#### Example
The london underground has lots of features and details that could be added to a map. Some are not important for a user of the system when planning a journey such as the depth of a station, distance between stations or frequency of trains.

Other details are important for planning a journey such as the different lines, available stations, accessibility options or changes available.
![https://ichef.bbci.co.uk/images/ic/1008xn/p06rm6k4.jpg](https://ichef.bbci.co.uk/images/ic/1008xn/p06rm6k4.jpg)

#### Resources
- Computational thinking, decomposition and abstraction: https://www.bbc.co.uk/bitesize/guides/z4rbcj6/revision/3
- Decomposition, Abstraction and sub-programs: https://www.bbc.co.uk/bitesize/guides/z7ddqhv/revision/1
- Useful video: https://discord.com/channels/@me/1156995970140221486/1159898169283457074

## Sub Programs
> A ***smaller program*** written ***within or imported*** into a ***larger program*** that performs a ***specific task*** and can be ***run any number of times***.
- The two types of programs are [procedures](https://github.com/zycobyte/definitions/blob/master/computational_thinking.md#procedure) and [functions](https://github.com/zycobyte/definitions/blob/master/computational_thinking.md#function)
- When the sub program is complete the main program continues

##### Pros
- Easier to write, test and debug
- Can be saved seperately and re-used
- Writing code once and re-using it saves time
##### Cons
- Must be tested independently and as a part of the whole system

#### Example
Built in sub programs exist in python, such as the int and str functions which can be called anywhere within a program to convert a string to a number or a number to a string

#### Resources
- Decomposition, Abstraction and sub-programs: https://www.bbc.co.uk/bitesize/guides/z7ddqhv/revision/3

## Algorithms
> An algorithm is a set of ***step by step instructions*** that are to be followed to ***achieve the required result***
- Can be represented as program code, [psuedo code](https://github.com/zycobyte/definitions/blob/master/computational_thinking.md#pseudo-code), [written desctiptions](https://github.com/zycobyte/definitions/blob/master/computational_thinking.md#written-descriptions) or [flow charts](https://github.com/zycobyte/definitions/blob/master/computational_thinking.md#flow-charts)
- draft program code may contain syntax errors as long as it is clear
  
##### Pros & Cons
- pros and cons are related to the efficiency of the algorithm implemented, such as speed and memory usage

#### Example
- I will add links to the searching algorithms when we go through them next week

#### Resources
- Algorithms: https://www.bbc.co.uk/bitesize/guides/z7kkw6f/revision/1

## Truth Tables
> A truth table is a type of table that ***lists all possible inputs and outputs*** for a logical expression
- The number of rows will always be 2 to the power of the number of inputs
- True may be represented as 1, ON or YES
- False may be represented as 0, OFF or NO
- Middle steps can be labled to save space

##### Pros
- Good for testing logical expressions
- Easy to read especially with more complex expressions
- Easier to notice patterns
##### Cons
- Can get large very quickly
- May be time consuming

#### Example
![https://cdn.discordapp.com/attachments/1158345889845350461/1161176598331011113/image.png](https://cdn.discordapp.com/attachments/1158345889845350461/1161176598331011113/image.png)
![https://cdn.discordapp.com/attachments/1158345889845350461/1161176363127013426/image.png](https://cdn.discordapp.com/attachments/1158345889845350461/1161176363127013426/image.png)

#### Resources
- Truth tables: https://www.bbc.co.uk/bitesize/guides/zr33rwx/revision/1
- Video explanation: https://www.youtube.com/watch?v=rwhGZs-U20g


## Trace Tables
> ***Tracks the changes*** of variable states throughout program execution
- If a variable does not change, a cell is left blank

##### Pros
- Allows you to step through the program execution
- Good for finding logic errors
##### Cons
- May be time consuming

#### Example
![https://ibcomputerscience.xyz/wp-content/uploads/2018/09/Capture-3.png](https://ibcomputerscience.xyz/wp-content/uploads/2018/09/Capture-3.png)

#### Resources
- Algoriths: https://www.bbc.co.uk/bitesize/guides/zbssv9q/revision/6 

------

## Flow Charts
> A ***diagram*** that represents the overview of a program. They use ***standard symbols*** to represent instructions. ***Flowcharts show a step by step solution***
- may be called a flow diagram
- please refer to the example image for the different symbols and their meaning

##### Pros
- Easy to visualise
- Internationally standardised
##### Cons
- Large problems can result in large charts
- Changes can result in a lot of editing re-formatting

#### Example
![https://bam.files.bbci.co.uk/bam/live/content/zmt4xyc/medium](https://bam.files.bbci.co.uk/bam/live/content/zmt4xyc/medium)
![https://bam.files.bbci.co.uk/bam/live/content/zdkwhbk/medium](https://bam.files.bbci.co.uk/bam/live/content/zdkwhbk/medium)

#### Resources
- Flowcharts: https://www.bbc.co.uk/bitesize/guides/z7kkw6f/revision/3

## Pseudo Code
> A way of ***describing step by step instructions*** in a code-like format
- Resembles a programming language
- Has its own syntax
- Must be converted to program code to run

##### Pros
- easy to convert to code
- simple to understand
- syntax errors not important
- easy to edit

##### Cons
- harder to see program flow
- could be time consuming

#### Example
[List of instructions](https://tools.withcode.uk/ks4pseudo/media/edexcel_pseudocode.pdf)

#### Resources
- psuedo code: https://www.bbc.co.uk/bitesize/guides/z7kkw6f/revision/2
- written, psuedo and program code: https://learnlearn.uk/edexcel-igcse-computer-science/pseudocode/

## Written Descriptions
> An algorithm is layed out as instructions in english
- short sentances
- no unnecessary details
- clear instructions

##### Pros
- no syntz
- most like english
##### Cons
- can become over-complicated
- may become more wordy or descriptive as opposed to instructional

#### Example
The program prompts the user to enter the width and height. It then calculates the area of a rectangle based on the two numbers. Finally it displays the result on the screen.

#### Resources
- written descriptions: https://www.bbc.co.uk/bitesize/guides/z7kkw6f/revision/4
- written, psuedo and program code: https://learnlearn.uk/edexcel-igcse-computer-science/pseudocode/

## Procedure
> A procedure is a ***block of code*** that is called to ***perform a specific task***.
- does ***NOT*** return a value

##### Pros
- Allows you to organise the code
- Avoid duplicating code
- Easier to fix bugs or update with new features when the functionality is called from multiple places in the codebase

#### Example
```python
def display_message(text):
    print("pretty formatting here >> ", text)
```

#### Resources
- Procedures and functions: https://teachcomputerscience.com/gcse/programming/functions-and-procedures/
- Programming constructs: https://www.bbc.co.uk/bitesize/guides/z433rwx/revision/11


## Function
> A function is a ***block of code*** that is called to ***perform a specific task*** and will ***return one or more values***
- returns values

##### Pros
- Allows you to organise the code
- Avoid duplicating code
- Easier to fix bugs or update with new features when the functionality is called from multiple places in the codebase

#### Example
```python
def area(width, height):
    return width * height
```

#### Resources
- Procedures and functions: https://teachcomputerscience.com/gcse/programming/functions-and-procedures/
- Programming constructs: https://www.bbc.co.uk/bitesize/guides/z433rwx/revision/11

## Arithmetic Operators
> Arithmetic operators are the mathematical operators that can be performed on variables and data.
- ***a DIV b*** is integer division. It is the number of times that b can go into a. it is like doing **a/b** and rounding the number down.
- ***a MOD b*** is modulous. It is the remainder left over after performing DIV.
- if ***a MOD b == 0*** then a is a multiple of b. If the result is ***not equal to 0*** then it will always be less than b

#### Example
![https://cdn.discordapp.com/attachments/1158345889845350461/1161179483953446952/image.png](https://cdn.discordapp.com/attachments/1158345889845350461/1161179483953446952/image.png)

#### Resources
- Algorithms: https://www.bbc.co.uk/bitesize/guides/zbssv9q/revision/3

## Relational Operators
> Relational oprerators allow for assignments and enable comparisons on variables and data
- Can be combined with logical operators (AND, OR, NOT) to add complexity to decisions

#### Example
![https://cdn.discordapp.com/attachments/1158345889845350461/1161179516505440347/image.png](https://cdn.discordapp.com/attachments/1158345889845350461/1161179516505440347/image.png)

#### Resources
- Algorithms: https://www.bbc.co.uk/bitesize/guides/zbssv9q/revision/3

## Logic Error
> A logic error is an error in the way the program operates. It runs without any obvious errors however the results are unexpected
- They are caused by the programer either by making small mistakes or poor design
- These errors can only be found during bug testing as, according to the computer, there is nothing inherently wrong with the code written

#### Examples
- incorrect relational operators (such as < instead of >)
- incorrect logical operators (such as AND instead of OR)
- accidental infinite loops
- incorrect mathematical brackets (1+(2*3)) == 7 vs ((1+2)*3) == 9
- using the wrong variable
- poor program design
  
#### Resources
- https://www.bbc.co.uk/bitesize/guides/zbssv9q/revision/7

## Runtime Error
> A runtime error is an error that occurs while the program is running. It usually results in a crash unless explicitly handled
- The error is detected by the system during the running of the program and a message will be printed to give info on where and what occurred

#### Examples
- Trying to open a file that does not exist
- Trying to access an array index that does not exist
- Trying to do something with a null value
- Trying to send something over the internet while the system is not connected to any network
- Trying to convert "Hello, world!" into its numeric value
Though there are many more and they can be created by you too for specific scenarios in your code

#### Resources
- https://www.bbc.co.uk/bitesize/guides/zbssv9q/revision/7

## Syntax Error
> A syntax error is an error that occurs when the code written is incorrectly formatted with regards to how the language defines its rules.
- A computer may be able to point out where some errors are but will not be able to understand what is written until it is corrected

- its. like how ive used apostrophies in the wrong place's and have spelt words wrong in this sentance as well as missing out or mis(using) other punctuation symbles  
- Other than spelling and punctuation symbols you could have used a variable before it is declared
- Its like saying "It was a really good time going there with her" and not giving the context "I went to the theme park with mary" until after. 

#### Examples
Common examples you should look for in python include 
- ensuring all variables are declared before they are used
- all brackets are in the right places and correctly closed
- that indentation is consistent
- that there are colons in all the correct places
- that strings have consistent "" or ''
though there may be others.

#### Resources
- https://www.bbc.co.uk/bitesize/guides/zbssv9q/revision/7
