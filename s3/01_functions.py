# functions:  positional and keyword arguments


def greet(greeting):
    print('{}!'.format(greeting))


def return_greeting(greeting):
    var = '{}!'.format(greeting)
    return var


def return_greeting_place(greeting, place='world'):
    var = '{}, {}!'.format(greeting, place)
    return var



greet('hi')
x = return_greeting('hi'); print(x)
y = return_greeting_place('hi'); print(y)
z = return_greeting_place('hi', 'mars'); print(z)

