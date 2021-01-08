# CalculateAndConvert
Our project Calculate And Convert basically consists of a) A calculator which can evaluate expressions and b) A converter. The details of these are mentioned below. Our website is made using the following - 
1. HTML and CSS - For the frontend design of the website. 
2. Flask - For making the website and its various buttons responsive.
3. Python - To code up the different computations and conversions.

First, we will take a look at the Calculator part.

# Calculator
In python, we have a very powerful method for performing complex computations which is the eval() function. In the eval() function, we can pass an expression(String) as an argument and that expression will be evaluated. Say we pass the String "2+2" into the function as eval("2+2"), we will get the output as 4 . 
Some important points to note and directions of use :
1. The user can enter a number "a" and an expression in terms of a. It must be noted that entering the number a is totally the user's choice. The user can just enter any expression and that would be accepted. 
2. If a number is entered, and an expression is to be evaluated where the input to a variable is the number, then the expression must be written in terms of "a" only, otherwise it would throw an error. At the present moment, we haven't accounted for multivariate expressions.
3. Python syntax should be followed. For Eg. If you want to evaluate 2^3, then you have to enter 2**3 and not 2^3.
4. Functions of modules such as numpy and math have been included. Eg. a) If you want to get a precise value of pi, then you can enter math.pi b) Trigonometric functions can be evaluated by using numpy.sin(a) or numpy.cos(a).
