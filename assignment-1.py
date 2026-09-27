# Week 1 Assignment

# Section 1: Variable and types
# Declare one variable of each of the four basic types below, then print each variable along with its type using type():

name = "Mike"
age = 49
height = 5.6
is_student = True

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))


# Section 2: User Input and Math
"""
Add to your script: use input() to ask for the user's name and the year they were born. Compute their approximate age and print a sentence. The example below shows the format — your greeting will use the name and birth year the user types:

Hi, Jordan! You are approximately 24 years old.

    Hint: input() always returns a string. Convert the birth year to int before doing math.
"""

name = input("Enter your name: ")
birth_year = int(input("Enter the year you were born: "))
age = 2026 - birth_year
print(f"Hi, {name}! You are approximately {age} years old.")

# Section 3: Type Conversion and f-strings
"""
Add to your script: ask the user to enter two numbers (as separate inputs). Convert both to float, multiply them, and print the result using an f-string. The example below shows the format — your two numbers and their product will differ:

12.5 × 4.0 = 50.0
"""
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
product = num1 * num2
print(f"{num1} × {num2} = {product}")

# Section 4: Formatted Receipt
"""
Add to your script: using only variables and print() — no input() — print a formatted receipt. Store the item name, price, and quantity in variables, and compute the total from those variables:

===========================
        RECEIPT
===========================
Item:      Python textbook
Price:     $29.99
Quantity:  2
---------------------------
Total:     $59.98
===========================

Use your own item, price, and quantity. The border style and spacing above are an example — any clean, labeled layout is fine, as long as the total is computed from your variables.
"""
item_name = "Python/Java textbook"
price = 29.99
quantity = 3
total = price * quantity

print("===========================")
print("        RECEIPT")
print("===========================")
print(f"Item:      {item_name}")
print(f"Price:     ${price:.2f}")
print(f"Quantity:  {quantity}")
print("---------------------------")
print(f"Total:     ${total:.2f}")
print("===========================")

# Section 5: Mini-Project — Profile Card
"""
Finally, tie it all together. Use input() to ask the user for:

    Their name
    Their hometown
    Their favorite hobby
    One fun fact about themselves
    The year they were born

Then print a formatted profile card using f-strings. Compute their age from the birth year — don't ask for it directly.

╔══════════════════════════════╗
      PROFILE: Alex Rivera
╚══════════════════════════════╝
Hometown:   Chicago, IL
Hobby:      Rock climbing
Fun fact:   I've visited 12 countries.
Age:        27

Align the labels so the output looks clean. The border style above is an example — any clean, aligned layout is fine.
"""
name = input("Enter your name: ")
hometown = input("Enter your hometown: City, State ")
hobby = input("Enter your favorite hobby: ")
fun_fact = input("Enter one fun fact about yourself: ")
birth_year = int(input("Enter the year you were born: "))
age = 2026 - birth_year

print("╔══════════════════════════════╗")
print(f"      PROFILE: {name}")
print("╚══════════════════════════════╝")
print(f"Hometown:   {hometown}")
print(f"Hobby:      {hobby}")
print(f"Fun fact:   {fun_fact}")
print(f"Age:        {age}")

