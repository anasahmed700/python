# Question 6:
# Write a function to compute 5/0 and use try/except to catch the
# exceptions.
# Hints:
# Use try/except to catch exceptions.

import traceback
def check():
    try:
        x = 0
        y = 5
        print(y/x)
    except ZeroDivisionError:
        print('Error dividing %d/%d' % (y,x))
        traceback.print_exc()
    except:
        print('a non-ZeroDivisionError occurred')
print(check())