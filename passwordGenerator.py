#Random Password Generator

#import random module
import random

#generate random number and print it out
myNumber = random.randint(100000000000000, 999999999999999)
print(myNumber)

#convert number into an integer array and print it out
numberArray = map(int, str(myNumber))
print(numberArray)

#establish all the possible characters in your password
specialChar = "!@#$%^&*()-=+_"
numbers = "01234567890"
upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowerCase = "abcdefghijklmnopqrstuvwxyz"
myPassword = []

#test
for x in numberArray:
    if x in range(1,2):
        myPassword.append(random.choice(specialChar))

    elif x in range(3,5):
        myPassword.append(random.choice(upperCase))

    elif x in range(6,8):
        myPassword.append(random.choice(lowerCase))

    else:
        myPassword.append(random.choice(numbers))

#convert list into string by joining all the elements of the string together
finalPassword = ''.join(myPassword)

#then print out myPassword
print(finalPassword)
