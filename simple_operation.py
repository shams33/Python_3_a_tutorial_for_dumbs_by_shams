"""python has the abilty of carrying out calculations.Enter a calculation directly into the Python console,and it will output the answer"""
""">>>2+2
      4
    >>>5+4-3
       6
    ""
Python also carries out multiplication and division, using an asterisk to indicate multiplication and a forward slash to indicate division.

Use parentheses to determine which operations are performed first.>>> 2 * (3 + 4)
14
>>> 10 / 2
5.0"""
"""The minus sign indicates a negative number.
Operations are performed on negative numbers, just as they are on positive ones. >>> -7
-7
>>> (-7 + 2) * (-4)
20"""

"""Dividing by zero in Python produces an error, as no answer can be calculated. >>> 11 / 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero"""
"""Floats are used in Python to represent numbers that aren't integers.
Some examples of numbers that are represented as floats are 0.5 and -7.8237591.
They can be created directly by entering a number with a decimal point, or by using operations such as division on integers. Extra zeros at the number's end are ignored. >>> 3/4
0.75
>>> 9.8765000
9.8765"""
"""
As you saw previously, dividing any two integers produces a float.
A float is also produced by running an operation on two floats, or on a float and an integer.>>> 8 / 2
4.0
>>> 6 * 7.0
42.0
>>> 4 + 1.65
5.65
A float can be added to an integer, because Python silently converts the integer to a float. However, this implicit conversion is the exception rather the rule in Python - usually you have to convert values manually if you want to operate on them."""
"""Besides addition, subtraction, multiplication, and division, Python also supports exponentiation, which is the raising of one number to the power of another. This operation is performed using two asterisks.>>> 2**5
32
>>> 9 ** (1/2)
3.0"""
"""
To determine the quotient and remainder of a division, use the floor division and modulo operators, respectively.
Floor division is done using two forward slashes.
The modulo operator is carried out with a percent symbol (%).
These operators can be used with both floats and integers.

This code shows that 6 goes into 20 three times, and the remainder when 1.25 is divided by 0.5 is 0.25. >>> 20 // 6
3
>>> 1.25 % 0.5
0.25
In the example above, 20 % 6 will return 2, because 3*6+2 is equal to 20."""
a=12
b= .2
print(a+b)#for sum
print(a-b)#for substraction
print(a*b)#for multiplication
print(a**4)#for power
print(a/b) #for division
print(a//b) #floor division for qoutient
print(a % b) #for remainder
