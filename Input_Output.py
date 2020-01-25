"""lets talk about first ouput statement python is very straightforward its like if you want to propose a girl then python will tell direct I LVE YOU instead of saying any boring compliments
okay lets go to the point directly okay python use print function to print an out put"""
##print(values,sep,end,file,flush) this is what a print function consists of
##values: the thing you wanna say its like eg:
print("I love you")

# Sep: it means separator which is used to provide or adding separator into the string provided by the way by default it will take only space but you can give whatever you want
#eg:
print(1,2,3,4,4,sep=" ")##with the values
print('i','love','you',sep="_")##for strings
"""end: after all vallues are printed end will be printed,bydefault it will print new line"""
print("I love you","but as a friend",sep=" " ,end="***fuck")
###
# file is the object where the values are printed and its default value is sys.stdout(screen)
print("Hello world!", flush=True)
"""The file argument must be an object with a write(string) method; if it is not present or None, sys.stdout will be used. Whether output is buffered is usually determined by file, but if the flush keyword argument is true, the stream is forcibly flushed.
"""
"""formatter:
str.format() is used for string formatting methods in Python3,which allows multiple substituitions and value for matting .This method lets us concatenate elements within
a string through positional formatting .
##using a single formatter:
formatters are actually like place holder like you are in a Indian bus and you told your friend to 
please reserve some seat for you and he used his handkerchief to reserve the seat    
for you .its like place holder 
{}.format(value)
placeholders defined by a pair of curly braces{} into a string and calling the str.format()."""
"""parameters :
(value ): can be an integer,floating point numeric constant,string charecters or even variables .
return type :returns a formatted string with the value passed aas parameter in the placeholder position
"""
print("{},but as a friend".format("i love you but "))
print("Hello,I am {}".format(21))
print("{1}{0}".format("dk","bose"))

"""now its different for different cases so lets seee what sthe differences 
"""
print("the number is differnet  is decimal :{:d}".format(123))
print("the number is float :{:f}".format(212.22))
print("bin {0:b},oct:{0:o},hex:{0:x}".format(9))

print("{:6d}".format(9))####it is used for padding purpose
print("{:<04d}".format(12))
print("{:^9.3f}".format(12.23))##padding the value
print("{:*^5}".format("act"))##padding the value
"""
>for right alignment
<for left alignment
^for central alignment
= for left most alignment of (+)(-) values

"""

#INPUT
"""for user input we use 
input() method """
print(input("enter the number"))

