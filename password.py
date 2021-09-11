# import modules
import random
import string

# input from the user
user_name = input("What's Your Nickname?: \n")
print(f"Hi {user_name}, Welcome To My Password Generator!")
print("-----------------------------------------\n")

pass_length = int(input("How long should it be? \n"))
include_puncts = input("Include punctuations ? Yes or No: \n")

# temp variables
nums = string.digits
letters = string.ascii_letters
puncts = string.punctuation

pass_temp = nums + letters
# if statement
if include_puncts.lower() == "yes":
    pass_temp += puncts
    password = "".join(random.sample(pass_temp, pass_length))
    print(f"Your password is {password}")
else:
    password = "".join(random.sample(pass_temp, pass_length))
    print(f"Your password is {password}")
