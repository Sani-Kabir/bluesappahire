# def sing_happy_birthday():
    
#     print('Happy Birthday To You')
#     print('Happy Birthday To You')
#     print('Happy Birthday Dear You')
#     print('Happy Birthday To You')


#     sing_happy_birthday()
#     sing_happy_birthday()
#     sing_happy_birthday()



# def addition(num1, num2):
#     return num1 + num2

# print(addition(10,100))
# print(addition(600,500))


# def divide(num1, num2):
#     return num1 / num2
# print(divide(10, 100))
# print(divide(400, 200))


# def single_param(name, school):
#     return name + " "+ school

# print(single_param('Edris', 'Mustapha'))


# def passwordlenght(password):
#     password = str(password)
#     lenght = len(password)

#     return lenght
# password ='123456789120'
# print(passwordlenght(password))


def passwordcheck(password):
    if len(password) <7:
        print('password has to be consisted with more than or equal to 7 digits')
    else:
        print('the account has been created')
password = '1234567'

print(passwordcheck(password))




