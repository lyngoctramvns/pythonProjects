# !, -, and number at the beginning of a variable is not valid
name = "Dave"
print("This variable is " + name)

# operators

# 1. Assignment Operator: =
# 2. Arithmatic Operator: +, -, *, /, //(floor division), round(24/5), %, **, +=, -=, /= (divide to decimal numbers)
# 3. Comparison Operators: ==, ===, !=, >, <, >=, <=, not, and, or

# Data types

# String data type
stringData = "Tram"
print(type(stringData))
print(isinstance(stringData, str))

# Constructor function
pizza = str("Pepperoni")
print(pizza)
print(type(pizza))
print(isinstance(pizza, str))

#Concatenate
stringFirst = "Ngoc"
stringSecond = "Tram"
fullname = stringFirst + " " + stringSecond
print(fullname)