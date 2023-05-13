# try:
#   код який виконується
# except:
#   обробка вийнятку

# приклад
# try:
#     print("start code")
#     print(error)
#     print("No errors")
# except:
#     print("we have an error")
#
# print("code after capsule")

# def checker(text):
#     if type(text) != str:
#         raise TypeError(f"Sorry,we cant work with {type(text)}, we need class STR!")
#
#
# try:
#     print("started code")
#     print(checker(5))
#     print("No Errors")
# except(TypeError, NameError):
#     print(f"Sorry we cant work with {TypeError}, we need class STR!")

# def calculate(n1, n2, op):
#     if op == '+':
#         result = n1 + n2
#     elif op == '-':
#         result = n1 - n2
#     elif op == '*':
#         result = n1 * n2
#     elif op == '/':
#         result = n1 / n2
#     elif op == '^':
#         result = n1 ** n2
#
#     else:
#         raise ValueError(f"Sorry,we cant work with {ValueError}.")
#     try:
#         print("counted if all ok")
#         print(calculate())
#
#
#     except(ZeroDivisionError, ValueError):
#         print(f"error {ZeroDivisionError} or {ValueError}")
#
#
#     return result
#
#
#
# number1 = float(input('Enter first number: '))
# op = input('Enter operator (+,-,*,/,**): ')
# number2 = float(input('Enter second number: '))
#
#
#
# result = calculate(number1, number2, op)

# import logging
# logging.basicConfig(level=logging.DEBUG, filename="logs.log",format = "[%(asctime)s] %(message)s (%(levelname)s)")
# logging.debug("TEXT")
# logging.info("User 123 succesful logget to account 'loginfr34' (IP: 192.33.33.2)")
# logging.warning("TEXT")
# logging.error("TEXT")
# logging.critical("TEXT")
import logging
abc = 12345678
user = input(print("enter user: "))
name = input(print("enter name: "))
password = input("enter password: ")


if name == abc and password == abc:
    logging.info(f"User: {user} succesful logget to account: {name} with correct password: {password}")





