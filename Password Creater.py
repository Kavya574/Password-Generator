# import the needed library
import random
import string

# Welcome message to the user
print("Hello, Welcome to Password Generator")

# Ask the users for the length of the password
length = int(input("Enter the length of the password: "))

#define data using string module
lower = string.ascii_letters
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

# combine the data and store it all new variable
all = lower+upper+num+symbols

#Use random module to generate password
temp = random.sample(all,length)
password = "".join(temp)

#At last print password
print(password)

