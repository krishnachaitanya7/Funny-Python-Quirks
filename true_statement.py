print(True == 1)   # True
print(True is 1)   # False
# Why: bool is a subclass of int; equality compares value, `is` checks identity.