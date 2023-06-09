# Session 2 Exercises

## Section A
# 1. Create two variables that hold the width and height of a rectangle, work out and store the area in a third variable. 
# Print out the string: `Rectangle of width <x> and height <y> has an area of <area>`.
x = 2; y = 3; a = x*y
print(a)


# 2. Write code that prints the length of the string, 'python'.
print(len('python'))

# 3. Print out the first and third letter of the word 'python'. 
n = 'python'
print(n[0])
print(n[2])

# 4. Ask the user to enter their name, and print out `Hello, <name>`.
name = input('Enter your name: ')
print("hello", name)

# 5. Ask the user to enter their age, tell them how old they will be in 15 years time.
age = input('Enter your age: ')
print("you will be", age*15, "in fifteen years")



# 6. Combine the two input statements above and print out the message `Hello, <name>, you are currently <age> years old. 
#   In 15 years time you will be <age_in_15_years_time>`.
print("Hello", name, "you are currently", age, "years old. In 15 years time you will be", age*15)


# 7. Ask the user to enter their hometown, print it out in uppercase letters.
hometown = input("Please Enter your hometown")
print(hometown.upper())


# 8. Ask the user to enter their favourite colour and find out the length of the colour they input.

color = input("Please Enter your color")
print(len(color))

# 9. Ask the user to enter the weather and the month. Print out the string, `It is <month> and it is <weather> today`.

weather = input("Please Enter weather: ")
month =  input("Please Enter month: ")
print("It is", month, "and it is", weather, "today")

# 10. Ask the user to enter 5 different temperatures and the month. Work out the average temperature and print out the string: 
#   `It is <month> and the average temperature is <average_temperature> degrees celsius`.
user = 0
for i in range(5):
  user += input("please enter temperature")
avg = user/5
print("It is", month, "and the average temperature is", avg, "degrees celsius")


# 11. Print out the above sentence but make the month upper case.

print("It is", month.upper(), "and the average temperature is", avg, "degrees celsius")

# 12. Create a variable that holds your favourite animals and print it out. 
#    Make sure the animals are all on different lines and tabbed.
favAnimal = "Parrot"
print("Favourite Animal: ", favAnimal)


# 13. Ask the user to enter their name as well as a number. 
#    Print out the uppercase character at that position in the string.
name = input("Enter name and number: ")
print(name[0].upper())


# 14. Slice the string with steps of 2, excluding the first and last characters of the string "WelcometoPython".
s = "WelcometoPython"
print(s[1:14])