''' This code example creates a variable called total, 
 iterates over all the values in arg, and adds them to total. 
 It then returns the result once the iterable has been exhausted.
'''

def sum(arg):
    total = 0
    for val in arg:
        total += val
    return total