#Data Types
#string, integer, float, boolean

#subscript:
#in strings we can pull out each charater individually by using the index "[]" and it always start counting with "0"
print("Hello"[0])
print("Hello"[4])

#integer: are whole numbers without any decimals, can be positive or negative
print(45)
print(-38)
#large integers can have an underscore to be more visual friendly
print(5_000_000)
#float (floating point number)
print(3.14159)
#boolean: it only has 2 values "True" or "False" always with a capital letter
True
False
is_single = True
print(is_single)
print(not is_single)
is_single = not is_single
print(is_single)
#"TypeError:object of type'xxx'has no len()" this error happens when functions don't support certain data types

#type () function is used to type checking
#gives the data type of the item between parenthesis
print(type(123))
name=len(input("¿cuál es tu nombre?"))
print(type(name))

#type conversion or casting with functions
#str()  int()  float()
name_letra=str(name)
print("tu nombre tiene "+name_letra+" letras")
print("tu nombre tiene "+str(name)+" letras")
#float () function converts to float
print(70+float("30.67"))
#str() function converts to string
print(str(90)+str(40))
#int () function converts to integer
print(int("987")+int("1"))

#mathematical operators
# addition "+"
print(4+3)
#subtraction "-"
print(48-8)
# multiplication "*"
print(2*3)
#division "/" always output a float number
print(12/4)
#exponent "**" raise a number to a power
print(3**3)
#floor division "//" converts the result directly to an integer
print(8//3)

# PEMDAS always from left to right
# Parenthesis
# Exponent
# Multiplication
# Division
# Adding
# Subtraction
print(3*3+3/3-3)
print(3*(3+3)/3-3)
print(2**3+3-7/1//4)

#round () function you can specify the number of decimal digits with a coma
print(round(8/3))
print(round(8/3,4))

#modify variables with +=,-=,*=,/= when you have to manipulate a value based on its previous value
#"+="
score=0
score=score+1
score+=1
print(score)
#"/="
result=4/2
result/=2
print(result)

# String interpolation: is a process substituting values of variables into placeholders in a string

#f-string mix strings and diferent data types by writing an "f" before the quotes of a string and using curly braces "{}". Python 3.6 added new string interpolation method called literal string interpolation and introduced a new literal prefix "f". This new way of formatting strings is powerful and easy to use. It provides access to embedded Python expressions inside string constants.
score=2
height=1.8
iswinning=True
print(f"your score is {score}, your height is {height} and you are winning is {iswinning}")
print("\n")
#This new string interpolation is powerful as we can embed arbitrary python expressions we can even do inline arithmetic with it, which is only possible with this method
print(f"we can do inline arithmetic {score*height} like this")

# If the number is too large it wil be represented as scientific notation
number1 = 450000000000000000000.1
number2 = 0.000000000000000000002
print(number1)
print(number2)

# abs() function returns the absolute value of a number
print(abs(-45))
print(abs(87))
print(-25 == 25)
print(abs(-25) == abs(25))

# Comparing floats with different decimal precision
x = 3.3
y = 1.1 + 2.2
print(x,"\n",y)
print(x == y)

y_string = format(y, ".2g")
print("this is a string:", y_string)
print(str(x) == y_string)

tolerance = .0001
print(format(x-y,".51f"))
print(abs(x - y) <= tolerance)


#format () method: formats the specified value and insert them inside the string's placeholder. The placeholder is defined using curly brackets {}, it returns the formatted string. The values are either a list of values separated by commas, a key=value list, or a combination of both. The values can be of any data type.
print("For only {price:.2f}".format(price = 49))
print("For only {:.2f} you can buy {}".format(49, "apples"))
print("For only {price:.2f} you can buy {fruits}".format(fruits="apples", price=49))
print("For only {price} you can buy {}".format("apples", price=49))

# The placeholders can be identified using named indexes
print("My name is {fname}, I'm {age}".format(fname = "John", age = 36))

# numbered indexes
print("My name is {0}, I'm {1}".format("John",36))
print("My name is {1}, I'm {0}".format("John",36))

# or even empty placeholders
print("My name is {}, I'm {}".format("John",36))

# Inside the placeholders you can add a formatting type to format the result
#The operators "< ^ > =" are used for alignment when assigned a certain width to the numbers.If no alignment option is specified, it is aligned to the right of the remaining spaces. (For strings, it is aligned to the left.)
# Left aligned to the remaining space
print("We have{:<8}chickens.".format(49))
print("We have{:<08d}chickens".format(49))
print("We have{:k<8d}chickens".format(49))
print("We have{:<08}chickens".format(49))
print("We have{:k<8}chickens".format(49))
# Right aligned to the remaining space
print("We have{:>8}chickens.".format(50))
print("We have{:8d}chickens.".format(50))
print("We have{:8}chickens.".format(50))
print("We have{:>08}chickens.".format(50))
print("We have{:08d}chickens.".format(50))
print("We have{:k>8d}chickens.".format(50))
print("We have{:k>8}chickens.".format(50))
# Center aligned to the remaining space
print("We have{:k^8}chickens.".format(51))
print("We have{:^8}chickens.".format(51))
print("We have{:^08}chickens.".format(51))
print("We have{:^10.3f}chickens".format(12.2346))
# place the plus/minus sign at the left most position
print("The temperature is{:=8}degrees celsius."
.format(-5))
print("The temperature is{:=08}degrees celsius."
.format(-5))
print("The temperature is{:k=8}degrees celsius."
.format(-5))
print("The temperature is{:=8.3f}degrees celsius".format(-12.2346))
# always indicate if the number is positive or negative
print("The temperature is between {:+} and {:+} degrees celsius.".format(-3, 7))
print("{:+f} {:+f}".format(12.23, -12.23))
# indicate if the number is negative (positive numbers are displayed without any sign)
print("The temperature is between {:-} and {:-} degrees celsius.".format(-3, 7))
print("{:-f} {:-f}".format(12.23, -12.23))
# insert a space before positive numbers and a minus sign before negative numbers
print("The temperature is between {: } and {: } degrees celsius.".format(-3, 7))
print("{: f} {: f}".format(12.23, -12.23))
# add a comma as a thousand separator
print("The universe is {:,} years old.".format(13800000000))
# add a underscore character as a thousand separator
print("The universe is {:_} years old.".format(13800000000))
# convert the number into binary format:
print("The binary version of {0} is {0:b}".format(5))
# Converts the value into the corresponding unicode character
print("The unicode version of {0} is {0:c}".format(88))
# convert a number, in this case a binary number, into decimal number format
print("We have {:d} chickens.".format(0b101))
# Same as 'd'. Except it uses current locale setting for number separator
print("We have {:n} chickens.".format(0b101))
# convert a number into scientific number format (with a lower-case e)
print("We have {:e} chickens.".format(5))
# convert a number into scientific number format (with an upper-case E)
print("We have {:E} chickens.".format(5))
# convert a number into a fixed point number, default with 6 decimals, but use a period followed by a number to specify the number of decimals,"f" specifies the format is dealing with a float number.
print("The price is {:.2f} dollars.".format(49))
print("The price is {:f} dollars.".format(49))
print("The price is {:.4f} dollars.".format(1.23456789))
print("The price is {:f} dollars.".format(1.23456789))
# The part before the "." specifies the minimum width/padding the number can take including the "."
print("hello your balance is{:7.3f}".format(230.2346))
print("hello your balance is{:8.3f}".format(230.2346))
print("hello your balance is{:9.3f}".format(230.2346))
print("{:5d}".format(12))
print("{:05d}".format(12))
print("{:08.3f}".format(12.2346))
print("{:5}For strings, it is aligned to the left by default".format("12"))

# General format
print("The price is {:.4g} dollars.".format(1.23456789))
print("The price is {:g} dollars.".format(1.23456789))
print("The price is {:.4g} dollars.".format(1234567890000000000000))
print("The price is {:g} dollars.".format(1234567890000000000000))
# General format (using a upper case E for scientific notations)
print("The price is {:.4G} dollars.".format(1234567890000000000000))
print("The price is {:G} dollars.".format(1234567890000000000000))
# convert a number into a fixed point number, but display inf and nan as INF and NAN
strange = float('inf')
strange2 = float('nan')
print("The price is {:F} dollars.".format(strange))
print("The price is {:f} dollars.".format(strange))
print("The price is {:F} dollars.".format(strange2))
print("The price is {:f} dollars.".format(strange2))
print("The price is {:F} dollars.".format(50))
print("The price is {:f} dollars.".format(50))
# convert the number into octal format
print("The octal version of {0} is {0:o}".format(10))
# convert the number into Hex format
print("The Hexadecimal version of {0} is {0:x}"
.format(255))
# convert the number into upper-case Hex format
print("The Hexadecimal version of {0} is {0:X}".format(255))
# convert the number into a percentage format
print("You scored {:%}".format(0.25))
print("You scored {:.0%}".format(0.25))
# As numbers, string can be formatted in a similar way
print("hear the{:6}meows".format("cat"))
print("hear the{:<6}meows".format("cat"))
print("hear the{:>6}meows".format("cat"))
print("hear the{:^6}meows".format("cat"))
print("hear the{:9^6}meows".format("cat"))
print("the{:.3}becomes a butterfly".format("caterpillar"))
print("the{:6.3}becomes a butterfly".format("caterpillar"))
print("the{:<6.3}becomes a butterfly".format("caterpillar"))
print("the{:^6.3}becomes a butterfly".format("caterpillar"))

# python internally uses getattr() for class members, inside the template string,
# IceCream's flavor and weight are accessed using .flavor and .weight respectively
class IceCream:
    flavor = "pineapple"
    weight = 1

print("i like my {yumi.flavor} ice cream of {yumi.weight}kg".format(yumi = IceCream()))

# python uses __getitem__() lookup for dictionary members,
# Inside the string, ice_cream's flavor and weight are accessed using [flavor] and [weight] respectively.
ice_cream = {"flavor": "pineapple", "weight": 1}
print("i like my {ice[flavor]} ice cream of {ice[weight]}kg".format(ice=ice_cream))
# There's an easier way to format dictionaries in python using str.format(**mapping)
# "**" is a format parameter (minimum field width).
print("i like my {flavor} ice cream of {weight}kg".format(**ice_cream))

# You can pass format codes like precision, alignment, fill character as positional or keyword arguments dynamically
print("hear the{:{fill}{align}{width}}meows".format('cat', fill='*', align='^', width=6))
print("i have{:{align}{width}.{precision}f}in my bank account".format(123.236, align='<', width=12, precision=6))
print("i spent{:{align}{width}.{precision}f}in my{:{fill}{align}{width}}food".format(123.236, 'cat', align='<', width=12, precision=6, fill='*'))

# format() also supports type-specific formatting options like datetime's and complex number formatting

# format() internally calls __format__() for datetime, Current datetime is passed as a positional argument to the format() method.
# And, internally using __format__() method, format() accesses the year, month, day, hour, minutes and seconds
import datetime
today_date = datetime.datetime.now()
print("It's now: {:%Y/%m/%d %H:%M:%S}".format(today_date))

# format() accesses the attributes of the complex number, 1+2j is internally converted to a ComplexNumber object.
# Then accessing its attributes "real" and "imag", the number is formatted.
my_complex_number = 1+2j
print("Real part: {0.real} and Imaginary part: {0.imag}".format(my_complex_number))

# You can easily override the __format__() method of any object for custom formatting. Like datetime, you can override
# your own __format__() method for custom formatting which returns "goku_age" when accessed as {:goku_age}
class DragonBallZ:
    def __format__(self, my_format):
        if my_format == 'goku_age':
            return '23'
        return 'None'

print("goku's age is{:goku_age}".format(DragonBallZ()))
print("goku's age is{:ramen}".format(DragonBallZ()))

# You can also use object's __str__() and __repr__() functionality with shorthand notations using format()
# __str__() and __repr__() shorthand !r and !s
print("this is the representation with quotes {0!r}, and this is the string {0!s}".format("cat"))
print("we can use {!r}, and {!s} however {!s} we want {!r}".format("cat", "dog", "fish", "bum"))

# Like __format__(), you can easily override object's __str__() and __repr_() methods.
class DragonBallSuper:
    def __str__(self):
        return "freezer"
    def __repr__(self):
        return "mayimbu"

print("this {dragon!s} fears {dragon!r}".format(dragon=DragonBallSuper()))

# format() function: works similar to the .format() method, it returns a formatted value based on the specified formatter
value = 7
binary_value = format(value, 'b')
print(binary_value)

print(format(7, "f"))
print(format(123, 'd'))
print(format(123, 'b'))
print("Without specified width:", format(123, 'd'))
print("Right-aligned with width 10:", format(123, '>10d'), "more text")
print("Left-aligned with width 10:", format(123, '<10d'), "more text")
print("Center-aligned with width 10:", format(123, '^10d'), "more text")
print("Positive with '+':", format(123, '+'))
print("Positive with '+':", format(-123, '+'))
print("Positive with '-':", format(123, '-'))
print("Positive with '-':", format(-123, '-'))
print("Positive with ' ':", format(123, ' '))
print("Positive with ' ':", format(-123, ' '))
print(format(123.4567, '.2f'))

# Strings in Python have a unique built-in operation that can be accessed with the "%" operator.
# "%s" string format specifier tells python where to substitute the value. the "%" operator only takes one argument,
# so we need to wrap the right-hand side in a tuple. This format method is very old and is not recommended
# to use as it decrease the code readability
print("just a %s string" % "simple")
print("i like to drink %s %s" % ('maracuyá', 'water'))
cool_name = 'world'
cool_program = 'python'
print('Hello %s! This is %s.' % (cool_name, cool_program))

# It’s also possible to refer to variable substitutions by name in our format string, if we pass a mapping to the "%"
# operator, this makes our format strings easier to maintain and easier to modify in the future. We don’t have to worry
# about the order of the values that we’re passing with the order of the values that are referenced in the format string
print('Hello %(shrimp)s! This is %(dolphin)s.' % {"shrimp": cool_name, "dolphin": cool_program})

gpl = "%(identifier)s : %(attribute)s"
objects = [{'id': 1, 'content': [{'atr': 'big', 'no': 2}]},  {'id': 2, 'content': [{'atr': 'small', 'no': 3}]}]
for obj in objects:
    for con in obj['content']:
        print(gpl % {"identifier": obj["id"], "attribute": con["atr"]})

# Template Strings is simpler and less powerful mechanism of string interpolation.
# We need to import Template classfrom Python’s built-in string module to use it.
from  string import Template
new_template_object = Template('Hello $the_name! This is $the_program.')
print(new_template_object.substitute(the_name= cool_name, the_program=cool_program))

# limits the string representation of a float to a given number of decimals for display without changing the actual value.
number=3.141592653589793
print(number)
print(format(number,".3f"))
print("{:.4f}".format(number))

name = "Pedro"
last_name = "Corrales"

print("You have to pay {:.5f} everyday".format(number))
print("Hi my name is {} and my last name is {}".format(name, last_name))
#format function converts the float to string so you can concatenate to other strings
print("this is the new number "+format(number,".6f"))
print("\n")

#format with f-string and .xf
print(f"{number:.7f}")
print(f"you have to pay {number:.2f} everyday")
print("\n")

#format with %.xf (search string interpolation for more info in the bibliography at the end of this file)
print("%.3f"%number)
print("give me %.4f right now"%number)
print("\n")

#format with round function
print(round(number,5))
print(f"you have to pay {round(number,6)}")
print("\n")

#formating can be mixed with the round function
print("you have to pay {:.7f} everyday".format(round(number,3)))
print("You have to pay %.8f everyday"%round(number,4))
print("you have to pay "+format(round(number,5),".9f"))
print(f"you have to pay {round(number,6):.10f}")

#examples of formating
number_formated1="{:.2f}".format(number)
number_formated2=format(number,".3f")
number_formated3=f"{number:.4f}"
number_formated4="%.5f"%number
number_formated5=round(number,6)

#the "g" give x significant digits
number_formated6="{:.2g}".format(number)
number_formated7=format(number,".3g")
number_formated8=f"{number:.4g}"
number_formated9="%.5g"%number

print(number_formated1)
print(number_formated2)
print(number_formated3)
print(number_formated4)
print(number_formated5)
print(number_formated6)
print(number_formated7)
print(number_formated8)
print(number_formated9)

print("this is a concatenated string with "+number_formated4)
print(type(number_formated2))

# https://www.programiz.com/python-programming/string-interpolation
# https://www.programiz.com/python-programming/methods/built-in/format

# https://www.w3schools.com/python/ref_string_format.asp

# for more info https://docs.python.org/3/tutorial/floatingpoint.html

#https://www.google.com/search?q=format+string+to+2+decimal+places+python&oq=format+string+to+2+decimal+places+Python&aqs=chrome.0.0i457j0i22i30.6232j0j1&sourceid=chrome&ie=UTF-8

#https://www.adamsmith.haus/python/answers/how-to-print-a-float-with-two-decimal-places-in-python

# https://docs.python.org/3/library/functions.html#abs

# https://www.w3schools.com/python/python_datatypes.asp
