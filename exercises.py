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

print(f"your ticket is ${ticket:.2f}")
#your ticket is $5.00