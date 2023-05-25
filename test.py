#define a function that prints 'hello_DEREKF!"

def hello_name(user_name):
    print(f"hello_{user_name.upper()}!")

hello_name('derekf')

#define a function that prints the all of the odd numbers from 0-100

def first_odds():
    for num in range(0, 100):
        if num % 2 != 0:
            print(num)
            
first_odds()

#define a function that returns the max from a given list

def max_num_in_list(x):
    return max(x)

print(max_num_in_list([71, 2, 83, 93, 3233, 345]))

#define a function that returns a boolean statement whether a year is a leap year or not

def leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    return False
    
print(leap_year(2023))
print(leap_year(2024))
print(leap_year(2000))
print(leap_year(2100))

#define a function that returns a boolean statement checking if a given list contains consecutive numbers or not

def is_consecutive(a_list):
    for i in range(len(a_list) - 1):
        value = a_list[i]
        value_to_right = a_list[i + 1]
        if value + 1 != value_to_right:
            return False
    return True

print(is_consecutive([2, 3, 4, 5, 6, 7]))
print(is_consecutive([1, 2, 3, 5, 6, 7]))