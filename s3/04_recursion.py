# recursion

import os


def print_val(num):
    if num <= 0:
        return
    print(num)
    num = num - 1
    print_val(num)

print_val(3)


def list_dir(this_dir):
    print('* entering list_dir {} *'.format(this_dir))
    for name in os.listdir(this_dir):
        pathname = os.path.join(this_dir, name)
        if os.path.isdir(pathname):
            list_dir(pathname)
        else:
            print('  ' + name)
    print('* leaving list_dir *')   # base condition:  looping is complete
list_dir('/Users/david/test')