
import random

letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
         'p','q','r','s','t','u','v','w','x','y','z','A','B','C','D',
         'E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S',
         'T','U','V','W','X','Y','Z']

numbers=['0','1','2','3','4','5','6','7','8','9']

symbols=['@','#','$','&','*']

password_list=[]

n_letters=int(input("Enter how many letters do you want : "))
n_numbers=int(input("Enter how many numbers do you want : "))
n_symbols=int(input("Enter how many symbols do you want : "))

for i in range(n_letters):
    password_list.append(random.choice(letters))

for i in range(n_numbers):
    password_list.append(random.choice(numbers))

for i in range(n_symbols):
    password_list.append(random.choice(symbols))

print(password_list)

password=""

random.shuffle(password_list)

for i in password_list:
    password+=i

print(password)



