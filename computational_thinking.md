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
```
The game Guess Who is a good example of computational thinking.
You must think logically to break up the problem into a smaller and smaller group if people. You ignore any irrelevant details (such as excluded characters or details present in no characters) as you focus on finding the solution. Different questions asked (like algorithms) have different efficiencies. For example if 1/100 characters have green eyes then 99% of the time that would be a very inefficient first question to ask. A better question would be to ask about their gender presentation, as you would be able to exclude about half of the options immediately with consistent results.
```

#### Resources
- Intro into computational thinking: https://www.bbc.co.uk/bitesize/guides/zp92mp3/revision/1
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
- The two types of programs are procedures and functions
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
> a
- b

##### Pros
- 
##### Cons
- 

#### Example

#### Resources


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
Algoriths: https://www.bbc.co.uk/bitesize/guides/zbssv9q/revision/6 

------

## Flow Charts
> a
- b

##### Pros
- 
##### Cons
- 

#### Example

#### Resources


## Pseudo Code
> a
- b

##### Pros
- 
##### Cons
- 

#### Example

#### Resources


## Written Descriptions
> a
- b

##### Pros
- 
##### Cons
- 

#### Example

#### Resources


## Procedure
> A procedure is a ***block of code*** that is called to ***perform a task***.
- does ***NOT*** return a value

##### Pros
- 
##### Cons
- 

#### Example

#### Resources


## Function
> A function is a ***block of code*** that is called to ***perform a task*** and will ***return one or more values***
- returns values

##### Pros
- 
##### Cons
- 

#### Example

#### Resources


## Arithmetic Operators
> a
- b

##### Pros
- 
##### Cons
- 

#### Example
![https://cdn.discordapp.com/attachments/1158345889845350461/1161179483953446952/image.png](https://cdn.discordapp.com/attachments/1158345889845350461/1161179483953446952/image.png)

#### Resources
- Algorithms: https://www.bbc.co.uk/bitesize/guides/zbssv9q/revision/3

## Relational Operators
> a
- b

##### Pros
- 
##### Cons
- 

#### Example
![https://cdn.discordapp.com/attachments/1158345889845350461/1161179516505440347/image.png](https://cdn.discordapp.com/attachments/1158345889845350461/1161179516505440347/image.png)

#### Resources
- Algorithms: https://www.bbc.co.uk/bitesize/guides/zbssv9q/revision/3

## Logic Error
> a
- b

##### Pros
- 
##### Cons
- 

#### Example

#### Resources


## Runtime Error
> a
- b

##### Pros
- 
##### Cons
- 

#### Example

#### Resources


## Syntax Error
> a
- b

##### Pros
- 
##### Cons
- 

#### Example

#### Resources
