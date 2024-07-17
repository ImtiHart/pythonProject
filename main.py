character_name = "Imtiyaaz"
character_age = "18"
print("My name is " + character_name + ",")
print("I am " + character_age + " years old. ")
sister_name = "Ilhaam"
sister_age = "15"
print("My sister is " + sister_name + ",")
print("she is " + sister_age + ".")
print(sister_name + " drew a castle:")
print("|_|_|_|")
print("|0   0|")
print("|     |")
print("|  H  |")


phrase = "Giraffe Academy"
print(phrase.replace("Giraffe","Elephant"))
print(phrase.lower())
print(phrase.upper())
print(phrase.isupper())
print(phrase.lower().islower())
print(len(phrase))

print(phrase.index("G"))
print(phrase.index("ir"))

coordinates = (4,5)
print(coordinates[1])

print(3*(4+5))
print(10%2)

my_number = 5
print(str(my_number)+" my favourite number")

print(pow(4,6))
print(min(4,6))
print(max(4,6))
print(round(3.2))
print(round(3.7))

from math import *
print(floor(3.7))
print(ceil(3.7))
print(sqrt(36))

name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + "! You are " + age + ".")

num1 = input("Enter a number: ")
num2 = input("Enter a number: ")
result = int(num1) + int(num2)
print(result)

num3 = input("Enter a number: ")
num4 = input("Enter a number: ")
result = float(num3) + float(num4)
print(result)

colour1 = input("Enter a colour: ")
colour2 = input("Enter a colour: ")
verb = input("Enter a verb: ")
print("Roses are " + colour1)
print("Violets are " + colour2)
print("I " + verb + " you!")

friends = ["Imti", "Levi", "Nicky", "John"]
print(friends)
print(friends[0])
print(friends[2])
print(friends[1:3])
print(friends[1:])
numbers_random = [4, 5, 6, 7, 8, 9]
friends.extend(numbers_random)
print(friends)
friends.append("kong")
print(friends)
friends.insert(1, "Kelly")
print(friends)
friends.remove("Imti")
print(friends)
friends.pop()
print(friends)
friends.clear()
print(friends)
Friends = ["jojo", "jeff", "jeff", "abe"]
Friends.sort()
print(Friends)
Friends.reverse()
print(Friends)
Friends2 = Friends.copy()
print(Friends2)
print(Friends.count("jeff"))

coordinates = (4,5)
print(coordinates[0])
print(coordinates[1])

def say_hi(name, age):
    print("hello " + name + "you are " + str(age))
say_hi("John ", 34)

def cube(nums):
    return nums*nums*nums
print(cube(3))

is_male = True
is_tall = False
if is_male or is_tall:
    print("You are a male or not tall")
else:
    print("You are not male nor tall")

is_female = True
is_short = True
if is_short and is_female:
    print("You are tall female")
elif is_female and not( is_short):
    print("You are a short female")
else:
    print("You are either not male or not tall or both")

def max_num(number1, number2, number3,):
    if number1>=number2 and number1>=number3:
        return number1
    elif number2>=number1 and number2>=number3:
        return number2
    else:
        return number3
print(max_num(300, 40, 5))

numb1 = float(input("Enter number: "))
symbol = input("Enter operator: ")
numb2 = float(input("Enter number: "))
if symbol == "+":
    print(numb1+numb2)
elif symbol == "-":
    print(numb1-numb2)
elif symbol == "*":
    print(numb1*numb2)
elif symbol == "/":
    print(numb1/numb2)
else:
    print("Not valid operation")

monthlyConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "Ma": "May",
    "Ju": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}
print(monthlyConversions.get("Sep", "Not valid"))

i = 1
while i <= 10:
    print(i)
    i += 1
print("Loop done")

secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False
while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("Out of guesses, YOU LOSE!!!")
else:
    print("You Win!!!")

for letter in "Imtiyaaz world"
    print(letter)

people = ("Joe, Elon, Sophy")
for person in people:
    print(person)

def raise_to_power(base_num,pow_num):
    answer = 1
    for index in range(pow_num):
        answer = answer * base_num
        return result
print(raise_to_power(2, 3))

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
print(number_grid[1][2])

numgrid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
for row in numgrid:
    for col in row:
        print(col)

def transalte(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou" :
            if letter.isupper():
            translation = translation + Y
            else:
            translation = translation + y
        else:
            translation = translation + letter
        return translation
print(transalte(input("Enter Phrase: ")))

