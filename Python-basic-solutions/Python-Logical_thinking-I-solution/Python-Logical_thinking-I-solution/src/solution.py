# Tasks

# Task 1

# username = input("What is your username? ")
# password = input(f"Type the password for username {username}: ")
# valid = {"username": "admin", "password": "admin"}
# if username == valid["username"] and password == valid["password"]:
#     print(f"Welcome, {username}!")
# else:
#     print("Credentials are invalid")


# Task 2

# import datetime
#
#
# def isweekend(date=datetime.datetime.now()):
#     """Return True if the date is either Saturday or Sunday."""
#     weekday = date.weekday()
#     return weekday == 5 or weekday == 6
#
#
# # Test cases
# print(isweekend(datetime.date(2021, 8, 6)))
# print(isweekend(datetime.date(2021, 8, 7)))
# print(isweekend(datetime.date(2021, 8, 8)))
# print(isweekend(datetime.date(2021, 8, 9)))


# Task 3

# username = input("What is your username? ")
# password = input(f"Type the password for username {username}: ")
# valid = {"username": "admin", "password": "admin"}
# today = datetime.date(2021, 8, 6)
# if username == valid["username"] and password == valid["password"] or isweekend(today):
#     print(f"Welcome, {username}!")
# else:
#     print("Credentials are invalid")



# Task 4

# users = [
#     {
#         "name": "Holly",
#         "password": "hunter"
#     },
#     {
#         "name": "Peter",
#         "password": "pan"
#     },
#     {
#         "name": "Janis",
#         "password": "joplin"
#     }
# ]
#
# def get_user(username, password):
#     """Return the first user matching username and password."""

#     u = None

#     for i in users:
#         if i["name"] == username and i["password"] == password:
#             u = i   
#     return u


# username = input("What is your username? ")
# password = input(f"Type the password for username {username}: ")
# user = get_user(username, password)
# if not user:
#     print("An error occurred. You are not authorized.")


# Task 5

# users = [
#     {
#         "name": "Holly",
#         "type": "Student",
#         "password": "hunter"
#     },
#     {
#         "name": "Peter",
#         "type": "Student",
#         "password": "pan"
#     },
#     {
#         "name": "Janis",
#         "type": "Teacher",
#         "password": "joplin"
#     }
# ]
#
# def is_student(user):
#     """Return True if the user is a student."""
#     return user["type"] == "Student"
#
# def show_offers(username, password):
#     """Show offers if the user is anonymous or a student."""
#     user = get_user(username, password)
#     if not user or is_student(user):
#         print("We have great courses to offer you!")
#
# # Test cases
# username = input("What is your username? ")
# password = input(f"Type the password for username {username}: ")
# show_offers(username, password)
