def my_decorator(some_function):

    def wrapper():
        print("Something is happening before some_function() is called.")

        some_function()

        print("Something is happening after some_function() is called.")
    return wrapper


def this_function():
    print("Wheee!")


# now the same name points to a replacement function
this_function = my_decorator(this_function)

# calling the replacement function
this_function()

