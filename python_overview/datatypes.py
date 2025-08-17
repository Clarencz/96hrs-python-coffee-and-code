# datatype.py

# -----------------------------
# Python Data Types (Built-in)
# -----------------------------

# Python has dynamic typing: you do not need to declare the data type of a variable.
# The interpreter determines the type at runtime.

# ---------------------
# 1. Numeric Data Types
# ---------------------

# int - Integer numbers (positive, negative, or zero)
age = 25
year = -2025
zero = 0

# float - Floating point (decimal) numbers
price = 99.99
temperature = -10.5
pi = 3.14159

# complex - Complex numbers (used in advanced mathematics)
complex_num = 2 + 3j  # real part = 2, imaginary part = 3j

# ---------------------
# 2. Boolean Data Type
# ---------------------

# bool - Only two possible values: True or False (capitalized)
is_active = True
is_logged_in = False

# Booleans are often the result of comparison operations:
is_adult = age >= 18  # True

# ---------------------
# 3. String Data Type
# ---------------------

# str - A sequence of Unicode characters (text)
name = "Alice"
greeting = 'Hello, world!'
multiline = """This is
a multi-line
string."""

# Strings are immutable (cannot be changed after creation)

# ------------------------
# 4. Sequence Data Types
# ------------------------

# list - Ordered, mutable collection of items
fruits = ["apple", "banana", "cherry"]
mixed_list = [1, "hello", True, 3.14]

# tuple - Ordered, immutable collection of items
coordinates = (10.0, 20.5)
singleton = (42,)  # Note the comma — required for a single-item tuple

# range - Represents an immutable sequence of numbers
numbers = range(5)  # Equivalent to [0, 1, 2, 3, 4] when converted to a list

# ------------------------
# 5. Set Data Types
# ------------------------

# set - Unordered, mutable collection of unique items
unique_numbers = {1, 2, 3, 3, 4}  # Duplicates are removed: {1, 2, 3, 4}

# frozenset - Unordered, **immutable** collection of unique items
immutable_set = frozenset([1, 2, 3, 3])  # {1, 2, 3}

# ---------------------------
# 6. Mapping Data Type
# ---------------------------

# dict - Unordered, mutable collection of key-value pairs
person = {
    "name": "Alice",
    "age": 30,
    "is_employed": True
}

# Keys must be unique and immutable (e.g., strings, numbers, or tuples)

# ---------------------------
# 7. NoneType
# ---------------------------

# None - Special type to indicate absence of a value or null
nothing = None

# Often used to initialize variables or represent 'no result'

# ---------------------------
# Type Checking and Conversion
# ---------------------------

# Use type() to check the type of a variable
print(type(name))         # <class 'str'>
print(type(price))        # <class 'float'>
print(type(unique_numbers))  # <class 'set'>

# Type casting (conversion)
int_value = int("10")       # 10
float_value = float("3.14") # 3.14
str_value = str(100)        # "100"
list_from_tuple = list((1, 2, 3))  # [1, 2, 3]

# ---------------------------
# Summary Table of Data Types
# ---------------------------

# Category       | Type Name     | Example
# -------------- | ------------- | ------------------------
# Numeric        | int           | 10
#                | float         | 3.14
#                | complex       | 2 + 3j
# Boolean        | bool          | True / False
# Text           | str           | "hello"
# Sequence       | list          | [1, 2, 3]
#                | tuple         | (1, 2, 3)
#                | range         | range(0, 5)
# Set            | set           | {1, 2, 3}
#                | frozenset     | frozenset([1, 2])
# Mapping        | dict          | {"key": "value"}
# None Type      | NoneType      | None

