'''
Chad Meadowcroft
Credit to Sentdex (https://pythonprogramming.net/)
'''

def add_wrapping(item):
    def wrapped_item():
        return 'a wrapped up box of {}'.format(str(item()))
    return wrapped_item

@add_wrapping
def new_bicycle():
    return 'a new bicycle'