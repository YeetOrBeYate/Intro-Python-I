"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:


if len(sys.argv) > 1:
    for arg in sys.argv:
        print(arg)
else:
    print('please do needful and pass us arguments')


# YOUR CODE HERE

# Print out the OS platform you're using:
if sys.platform.startswith('l'):
    print("The OS platform:", sys.platform)
# YOUR CODE HERE

# Print out the version of Python you're using:

print("the version of python", sys.version_info[0],".",sys.version_info[1],".",sys.version_info[2])
# YOUR CODE HERE


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
print("the process id:", os.getpid())
# YOUR CODE HERE

# Print the current working directory (cwd):
working = os.getcwd()
print("current working directory:", working)
# YOUR CODE HERE

# Print out your machine's login name
login = os.getlogin()
print("User login: ", login)
# YOUR CODE HERE
