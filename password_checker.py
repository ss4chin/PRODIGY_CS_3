import string

#Taking input from the user
password = input("Enter your passsword: ")

#Checking the types of characters in the password
upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])
lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password])
special = any([1 if c in string.punctuation else 0 for c in password])
digits = any([1 if c in string.digits else 0 for c in password])

#Defining the types of characters in the password
characters = [upper_case, lower_case, special, digits]

#Extracting the length of the password 
length = len(password)

#Setting the score as a measure of password strength
score = 0

#Checking if the password is a commonly used one
with open('common_passwords.txt', 'r') as f:
    common = f.read().splitlines()

if password in common:
    print('Password weak. Please try an alternate password')
    exit()

#Evaluating password based on length
if length > 8:
    score += 1
if length > 14:
    score += 1
if length > 17:
    score += 1
if length >= 20:
    score += 1

print(f'Password length is {str(length)} characters, adding {str(score)} security points')

#Evaluating password based on number of special characters
if sum(characters) > 1:
    score += 1
if sum(characters) > 3:
    score += 1
if sum(characters) > 5:
    score += 1

print(f"Password has {str(sum(characters))} different characters, adding {str(sum(characters) -1)} points")

#Evaluating the final strength of the password
if score < 3:
    print("Password weak. Please try a stronger password")
elif score == 3:
    print("Password is moderately secure")
elif score > 3:
    print("Password is strong")

