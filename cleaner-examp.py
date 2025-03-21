import os
import time

def clean()
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

for i in range(100):
    print("spam spam")
    
time.sleep(5)
clean()
