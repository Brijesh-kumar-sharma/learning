import sys
sys.path.append('/pythonproject/')
import pythonproject
from pythonproject.mathtech import *
print(responses[0])
print(responses[1])
while True:
    print()
    text=input("Enter some text")
    for word in text.split(' '):
        if word.upper() in operation.keys():
            try:
                l=extractnumber(text)
                r=operations[word.upper()](l[0],l[1])
                print(r)
            except:
                print("Something is wrong Please retry")
            finally:
                break
        elif word.upper() in commands.keys():
            commands[word.upper()]()
            break
    else:
        sorry()

        
