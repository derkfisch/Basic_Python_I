#Increase the year by 1 and then print out the following statement using type conversion and a formatted string
#OUTPUT:  I drive a blue 2023 Ford Focus.
color = 'blue'
make = 'Ford'
year = '2022'
model = 'Focus'

new_year = int(year) + 1

print(f'I drive a {color} {new_year} {make} {model}.') #I drive a blue 2023 Ford Focus.


#Write a program that will check a person's age and adjust the ticket price. Regular ticket price is $10. Seniors (65+) get 25 percent off and children (under 0-9) are half off. Print out the ticket price at the end

ticket = 10
# person_age = 72 # Output: Your ticket is $7.50
# person_age = 47 # Output: Your ticket is $10
person_age = 8 # Output: Your ticket is $5.00

if person_age >= 65:
    ticket *= .75
elif person_age < 10:
    ticket *= .50

print(f"Your ticket is ${ticket:.2f}")
#your ticket is $5.00

#Print out all cubed numbers up to the total value 1000
num = 0
while num <= 10:
    print(num ** 3)
    num += 1
#0
#1
#8
#27
#64
#125
#216
#343
#512
#729
#1000

#Get first prime numbers up to 100
for i in range(2, 101):
    for j in range(2, i//2):
        if i % j == 0:
            break
    else:
        print(i)

#Take in a user's input for their age, if they're younger than 18 print kids
#If they're 18-65 print adults, else print seniors

age = input('What is your age? ')

print(age, type(age))

if int(age) < 18:
    print('Kids')
elif int(age) >= 18 and int(age) <= 65:
    print('Adults')
else:
    print('Seniors')