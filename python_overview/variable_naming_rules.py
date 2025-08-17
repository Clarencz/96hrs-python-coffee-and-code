# variable_naming.py

# -------------------------------
# Variable Naming Rules in Python
# -------------------------------

# 1. A variable name must start with a letter (A–Z or a–z) or an underscore (_)
valid_name = "This is valid"
_valid_name = "This is also valid"

# 2. A variable name cannot start with a number
# 2invalid = "This will raise a SyntaxError"  # ❌ Invalid

# 3. A variable name can contain letters, numbers, and underscores (A–Z, a–z, 0–9, _)
name_1 = "Valid"
user_name_2025 = "Also valid"

# 4. Variable names are case-sensitive
value = 10
Value = 20
# 'value' and 'Value' are two different variables

# 5. Reserved keywords cannot be used as variable names
# Examples of keywords: if, else, class, return, for, while, etc.
# class = "Invalid"  # ❌ Invalid
class_name = "Valid alternative"

# 6. There is no limit to the length of the variable name, but readability matters
this_is_a_very_long_variable_name_but_it_is_still_valid = "Yes, but avoid this unless necessary"

# 7. Use meaningful names — not enforced by the interpreter, but strongly recommended
a = 10           # Poor naming
user_age = 25    # Better naming for clarity

# ------------------------------------
# Common Naming Conventions (Optional)
# ------------------------------------

# snake_case is preferred in Python (PEP 8 recommendation)
first_name = "Alice"
total_price = 99.99

# Constants are usually written in ALL_CAPS (by convention, not enforced)
PI = 3.14159
MAX_USERS = 100

# Avoid using single character names except in short loops
for i in range(5):
    print(i)

