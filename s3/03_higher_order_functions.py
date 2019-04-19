# higher-order functions


def doubleit(arg):
    return arg * 2

def is_positive(arg):
    if arg > 0:
        return True
    else:
        return False

proclist = [-3, -2, -1, 0, 1, 2, 3]

transformed_list = map(doubleit, proclist)
##map function takes a function and object and applies the function to each item

filtered_list = filter(is_positive, proclist)
##filter function takes a function and object and returns the item that of which returns TRUE by the function

print('* mapped list *')
print(transformed_list)

print()

print('* filtered list *')
print(filtered_list)

doubleit = def do(arg)


