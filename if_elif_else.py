#if statements

if True:
    print("Hello this is True") #Hello this is True

if False:
    print("Hello this is False") #skips over because nothing is False

#new True statement
print('Start Code') #Start Code

if True:
    print('Hello') #Hello
    print('How are you?') #How are you?

print('End Code') #End Code

#new False statement
print('Start Code') #Start Code

if False:
    print('Hello')
    print('How are you?')

print('End Code') #End Code

#Operators
#Available operators: Greater(>), Less(<), Equal(==)
#Greater or Equal(>=), Less or Equal (<=), Not Equal (!=)

num1 = 10
num2 = 5
num3 = 2

print(num1 > num2) #True
print(num1 == num2 * num3) #True
print(num1 != num3) #True
print(num1 >= num2 * num3) #True

if num1 > num2:
    print('num1 is greater than num2') #num1 is greater than num2

if num1 == num2 * num3:
    print('num1 is equal to num2 multiplied by num3') #num1 is equal to num2 multiplied by num3

if num1 >= num2 * num3 * 2:
    print('num1 is greater than or equal to num2 multiplied by num3 multiplied by 2') #this statement was false so there wasn't an output

#and/or statements
#Truth Tree:
#T and T = T
#T and F = F
#F and T = F
#F and F = F

#T or T = T
#T or F = T
#F or T = T
#F or F = F

#and/if statement
potential_candidate_gpa = 3.2
potential_candidate_act = 24

if potential_candidate_gpa > 2.5 and potential_candidate_act > 25:
    print('Student has met minimum requirements. Move them along...')
else:
    print('Reject student.')
#Reject student.

#or/if statement
potential_candidate_gpa = 3.2
potential_candidate_act = 24

if potential_candidate_gpa > 2.5 or potential_candidate_act > 25:
    print('Student has met minimum requirements. Move them along...')
else:
    print('Reject student.')
#Student has met minimum requirements. Move them along...

#else statements
age = 15
if age >= 18:
    print('person can vote')
else:
    print('Person cannot vote')
#Person cannot vote

#elif statements
required_age = 18
with_a_parent = 15

movie_goer_age = 16

if movie_goer_age >= required_age:
    print('Thanks, enjoy the film!')
elif movie_goer_age >= with_a_parent:
    print('You must be accompanied by an adult to see this film.')
else:
    print('You cannot see this movie')
#You must be accompanied by an adult to see this film.
