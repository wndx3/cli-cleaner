import os

if os.name == 'nt': # NT == WINDOWS
    os.system('cls')
else: # ALL OTHER OS NAME
    os.system('clear')

# MAC/LINUX
os.system('clear')

# WINDOWS
os.system('cls')

# FUNCTION EXAMPLE
def clean()
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

clean() # RUNNING THIS WOULD CLEAN TERMINAL
