modules = a file containing Python definitions and statements, which can be later imported and used when necessary.

dir(module) - able to reveal all the names provided through a particular module.

The first group of the math's functions are connected with trigonometry:

sin(x) → the sine of x;
cos(x) → the cosine of x;
tan(x) → the tangent of x.
All these functions take one argument (an angle measurement expressed in radians) and return the appropriate result (be careful with tan() - not all arguments are accepted).

Of course, there are also their inversed versions:

asin(x) → the arcsine of x;
acos(x) → the arccosine of x;
atan(x) → the arctangent of x.
These functions take one argument (mind the domains) and return a measure of an angle in radians.

To effectively operate on angle measurements, the math module provides you with the following entities:

pi → a constant with a value that is an approximation of π;
radians(x) → a function that converts x from degrees to radians;
degrees(x) → acting in the other direction (from radians to degrees)

Apart from the circular functions (listed above) the math module also contains a set of their hyperbolic analogues:

sinh(x) → the hyperbolic sine;
cosh(x) → the hyperbolic cosine;
tanh(x) → the hyperbolic tangent;
asinh(x) → the hyperbolic arcsine;
acosh(x) → the hyperbolic arccosine;
atanh(x) → the hyperbolic arctangent.

Another group of the math's functions is formed by functions which are connected with exponentiation:

e → a constant with a value that is an approximation of Euler's number (e)
exp(x) → finding the value of ex;
log(x) → the natural logarithm of x
log(x, b) → the logarithm of x to base b
log10(x) → the decimal logarithm of x (more precise than log(x, 10))
log2(x) → the binary logarithm of x (more precise than log(x, 2))
Note: the pow() function:

pow(x, y) → finding the value of xy (mind the domains)

The last group consists of some general-purpose functions like:

ceil(x) → the ceiling of x (the smallest integer greater than or equal to x)
floor(x) → the floor of x (the largest integer less than or equal to x)
trunc(x) → the value of x truncated to an integer (be careful - it's not an equivalent either of ceil or floor)
factorial(x) → returns x! (x has to be an integral and not a negative)
hypot(x, y) → returns the length of the hypotenuse of a right-angle triangle with the leg lengths equal to x and y (the same as sqrt(pow(x, 2) + pow(y, 2)) but more precise)

random() - produces a float number x coming from the range (0.0, 1.0) - in other words: (0.0 <= x < 1.0).

The seed() function is able to directly set the generator's seed.

seed() - sets the seed with the current time;
from random import random, seed

seed(0)
for i in range(5):
print(random())

seed(int_value) - sets the seed with the integer value int_value.
