
"""In Python, it's impossible to complete certain operations due to the types involved. For instance, you can't add two strings containing the numbers 2 and 3 together to produce the integer 5, as the operation will be performed on strings, making the result '23'.
The solution to this is type conversion.
In that example, you would use the int function."""
x="2"
y="3"
print(x+y)
print(int('2')+int('3'))