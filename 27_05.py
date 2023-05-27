#  print(f'Name Error - {type(NameError)} - {issubclass()}')
#
#  #try:
#       print('start code')
#       print(error)
#       print('No errors')
#
#   except:
#       print('We have an error')
#
#   print('Code after capsule')
#
#  try:
#     print(10/0)
#
#  except NameError:
#     print('You have NameError')
#
#  try:
#      print(10/0)
#
#  except ZeroDivisionError:
#      print('ZeroDivisionError')
# try:
#     a = int(input('First number'))
#     b = int(input('Second number'))
#     c = a / b
#     print(c)
# except ValueError:
#     print('Not correct value')
# except ZeroDivisionError:
#     print('You can not divide by zero')
try:
    print ('__Calculator__')
    x = int (input('First Number: '))
    y = int (input('Second Number: '))

    z = int (input('What would you do? \n 1 - to + \n 2 - to - \n 3 - to / \n 4 - to * \n'))

    if z == 1:
        a = x + y
    if z == 2:
        a = x - y
    if z == 3:
        a = float(x / y)
    if z == 4:
        a = x * y
    else:
        print('You can write only 1, 2, 3, 4!')
        print('Try again')
        print ('Результат ',z,' = ',a)
except ValueError:
    print('Not correct value')
    print('Try again :(')
except ZeroDivisionError:
    print('You can not divide by zero')
    print('Try again :(')
