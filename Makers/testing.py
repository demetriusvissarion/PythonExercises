# name = "Ahmed"

# if name == "Ahmed":
#     print("Hi, Ahmed")
# else:
#     print("Oh, a new friend!")


# num = 63
# if num > 50:
#     if num % 2 == 0:
#        print(f"This number, {num}, is even and larger than 50!")
#     elif num % 3 == 0:
#       print(f"This number, {num}, is divisible by 3 and larger than 50!")
#     else:
#         print(f"This number {num} is odd, and not divisible by 3!")
# else:
#      print(f"This number, {num}, is too small!")

# for i in range(5):
#    print('Hello World')


# num = 10
# for i in range(5):
#     num = num + 5
#     print(num)

# for i in range(1, 32, 2):
#     print(i)


# name = "Eric"
# for char in name:
#    print("Give me a " + char + " !") 


# from random import randint
# fav_number = 77
# guess_correct = False
# while not guess_correct:
#     guess = randint(0, 100)
#     if guess == fav_number:
#         print("You guessed right: 77!")
#         guess_correct = True
#     else:
#         print(f"{guess} is wrong! Try again.")


# while True:
#    print("This will run foreverrrrrr!")

# # Add two numbers together
# def add_two(a, b):
#     print(a + b)
# add_two(2,3)

# # Add three numbers together
# def add_three(a, b, c):
#     print(sum([a,b,c]))
# add_three(1,2,3)

# # Concatenate the names of a few of your closest friends
# def concatenate_names(firstname, lastname):
#     print(firstname + " " + lastname)
# concatenate_names("Mircea", "Matei")
# concatenate_names("Simion", "Ion")

# # Calculate the number of seconds in X weeks, where X is a number (like 3)
# def seconds_calculator(weeks):
#     print(weeks * 7 * 24 * 60 * 60)
# seconds_calculator(3)
# seconds_calculator(6)


# # File: add_five.py
# def add_five(num):
#     print(f"I have received {num}")
#     num_after_adding = num + 5
#     print(f"I have calculated {num} + 5 = {num_after_adding}")
#     return num_after_adding

# result = add_five(23)
# print(result)


# def superify(name):
#     return "super" + name

# # Don't edit below this line.

# dog_result = superify("dog")
# print(f"Look, it's {dog_result}!")
# # Should print "Look, it's superdog!"

# cat_result = superify(superify(superify("cat")))
# print(f"Look, it's {cat_result}!")
# # Should print "Look, it's supersupersupercat!"

# practice_list = [1, 17, 10, 1, 20, 22]
# practice_list.clear()
# result = practice_list
# practice_list.reverse()
# result = practice_list
# result = practice_list.pop()
# result = practice_list.index(20)
# practice_list.sort()
# result = practice_list
# print(result)


# Dictionaries

# person = {
#     "name": "Demetrius Vissarion",
#     "age": "40",
#     "nationality": ["British", "Romanian"]
# }

# capitals = {
#     "France": "Paris",
#     "USA": "Washignton",
#     "Russia": "Moscow"
# }

# practice_dict = { 
#     "London": "England", 
#     "Edinburgh": "Scotland", 
#     "Cardiff": "Wales", 
#     "Belfast": "Northern Ireland" 
# }

# result = practice_dict.keys()
# result = practice_dict.values()
# result = practice_dict.get("London")
# result = practice_dict.items()
# result = practice_dict.pop("London")
# practice_dict.clear()
# result = practice_dict
# result = practice_dict.setdefault("London", "UK")

# print(result)


## Classes

# class Greeter():
#     def hello():
#         return "Hello"
# greeter = Greeter()

# greeter.hello()
## outputs an error

# print(greeter)


# class Greeter():
#     def __init__(self):
#         print("Hello!")

# new = Greeter()


# class Person():
#     def __init__(self, name, birthday, favourite_language):
#         self.name = name
#         self.birthday = birthday
#         self.favourite_language = favourite_language

# person1 = Person("Alan Turing", "June 23, 1912", "Standard Description")

# print(person1.name)


# class Greeter():
#     def __init__(self, name):
#         self.name = name

#     def hello(self):
#         return f"Hello, {self.name}"

# greeter = Greeter("Alan")
# print(greeter.hello())



# class Person():
#     def __init__(self, first_name, surname):
#         # note that we're not using instance variables here
#         first_name = first_name
#         surname = surname

#     def full_name(self):
#         # will this work without using instance variables above?
#         return f"{first_name} {surname}"

# alan_turing = Person("Alan", "Turing")
# alan_turing.full_name()


# def i_joined_the_beatles(me):
#     beatles = ['john', 'paul', 'george', 'ringo']
#     beatles.append(me)
#     return beatles

# print(i_joined_the_beatles('yoko'))


# service_passwords = {'gmail': '12ab5!678'}

# def get_for_service(service_name):
#     return service_passwords[service_name]

# print(get_for_service('gmail'))


# def add(num1, num2):
#     return num1 + num2

# adder = add
# print(adder(1,2))



# def calculate_tax_for_the_shire(grossPay):
#     # The friendly Shire has a 20% tax rate
#     return grossPay * 0.2


# def calculate_tax_for_mirkwood(grossPay):
#     # Dodgy Mirkwood has a 90% tax rate
#     return grossPay * 0.9


# def calculate_tax_for_mordor(grossPay):
#     # Terrible Mordor has a 90% tax rate plus a fixed tax of £500.
#     return grossPay * 0.9 + 500


# def calculate_tax_for_texas(grossPay):
#     # Texas has a 5% tax rate
#     return grossPay * 0.05


# def report_pay(gross_pay, calculate_tax):
#     # The `calculate_tax` argument is a function
#     tax = calculate_tax(gross_pay)
#     net_pay = gross_pay - tax
#     return f"Your gross pay was {gross_pay}, minus {tax} makes your net pay {net_pay}"


# print("Frodo's Pay:")
# print(report_pay(5000.0, calculate_tax_for_the_shire))
# # Your gross pay was 5000.0, minus 1000.0 makes your net pay 4000.0

# print("Bombadil's Pay:")
# print(report_pay(4320.0, calculate_tax_for_mirkwood))
# # Your gross pay was 4320.0, minus 3888.0 makes your net pay 432.0

# print("Mount Doom's Pay:")
# print(report_pay(5000.0, calculate_tax_for_mordor))
# # Your gross pay was 5000.0, minus 5000.0 makes your net pay 0.0

# print("Billy the Kid's Pay:")
# print(report_pay(7000.0, calculate_tax_for_texas))
# # Your gross pay was 7000.0, minus 350.0 makes your net pay 6650.0


# python_foundations/chapter3/04_functions_as_arguments.md
# Part Four: Exercise II

# def as_sun_lover(temperature):
#     if temperature >= 25:
#         return 'great'
#     else:
#         return 'not great'


# def as_snow_lover(temperature):
#     if temperature <= 0:
#         return 'great'
#     else:
#         return 'not great'


# def report_weather(temperature, function):
#     return function(temperature)

# print(report_weather(24, as_sun_lover))
# print(report_weather(25, as_sun_lover))
# print(report_weather(1, as_snow_lover))
# print(report_weather(0, as_snow_lover))


# passwords = [
#     {'service': 'takeaway', 'password': 'asdf', 'added_on': '21/03/22'},
#     {'service': 'acebook', 'password': 'password123', 'added_on': '22/03/22'},
#     {'service': 'makersbnb', 'password': 'qwerty789', 'added_on': '22/03/22'}
# ]

# print(next(filter(lambda func: func['service'] == 'acebook', passwords)))
# print([password for password in passwords if password['service'] == 'acebook'])

# def are_all_passwords_long_enough(passwords):
#     return len([ password for password in passwords if len(password['password']) < 8]) == 0

# print(are_all_passwords_long_enough(passwords))

# # challenge: Write a function that checks whether any passwords were added on 21/03/22
# print(next(filter(lambda func: func['added_on'] == '21/03/22', passwords)))

# # challenge: Write a function that returns a list of all passwords added on 22/03/22
# def finder(date):
#     result = []
#     for password in passwords:
#         if password['added_on'] == date:
#             result.append(password)
#     return result

# print(finder('22/03/22'))
# # OR:
# print([password for password in passwords if password['added_on'] == '22/03/22'])



## Map
# result = map(lambda number: number * 2, [1, 2, 3, 4])
# print(list(result))
# or:
# print([number * 2 for number in [1, 2, 3, 4]])

# result = []
# for number in [1, 2, 3, 4]:
#     result.append(number * 2)
# print(result)