import os

# CLEANER FOR BOTH WINDOWS AND MAC
os.system('CLS' if os.name == 'nt' else 'CLEAR')

# CLEANER FOR MAC/LINUX:
os.system('CLEAR')

# CLEANER FOR WINDOWS:
os.system('CLS')


# EASIER IF YOU PUT IT INSIDE A BLOCK:
def clean()
    os.system('CLS' if os.name == 'nt' else 'CLEAR')
    # os.system('CLEAR')
    # os.system('CLS')

clean() # <- WILL ERASE CLI
