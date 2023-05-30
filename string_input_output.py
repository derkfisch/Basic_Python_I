#string assignment

name1 = "derek"
print(name1) #derek
print(type(name1)) #<class 'str'>

name2 = "fischer"
print(name2) #fischer
print(type(name2)) #<class 'str'>

contracted1 = "you can't do that"
print(contracted1) #you can't do that

contracted2 = 'you can\'t do that'
print(contracted2) #you can't do that

quote1 = 'He said, "Hello, how are you?"'
print(quote1) #He said, "Hello, how are you?"

quote2 = "He said, \"Hello, how are you?\""
print(quote2) #He said, "Hello, how are you?"

#escape characters

print("Hello my \
name is Derek") #Hello my name is Derek

#\n new line character
print("Hello\nmy name is Derek") #Hello
                                 #my name is Derek

#\t tab character
print("Hello\tmy name is Derek") #Hello    my name is Derek

print("Hello\n\tmy name is Derek") #Hello
                                   #    my name is Derek

#raw string
print(r"Hello\n\tmy name is Derek") #Hello\n\tmy name is Derek

#string concatenation
first_name = 'Derek'
last_name = 'Fischer'

full_name = first_name + ' ' + last_name
print(full_name) #Derek Fischer

full_name += ", Jr."
print(full_name) #Derek Fischer, Jr.

num_a = 10
num_b = '10'
#num_c = num_a + num_b will throw an error because num_a is an int and num_b is a str

#type conversion

print(type(num_b)) #<class 'str'>

#str to int
num_b_int = int(num_b)
print(num_b_int) #10
print(type(num_b_int)) #<class 'int'>

num_c = num_a + num_b_int
print(num_c) #20

#int to str
num_as_a_str = str(num_a)
print(num_as_a_str) #10
print(type(num_as_a_str)) #<class 'str'>

num_c = num_as_a_str + num_b
print(num_c) #1010

#.format() and f-strings

name = 'Derek'
home = 'Las Vegas'
age = 27

print('Hello my name is {}, I am from {}!'.format(name,home)) #Hello my name is Derek, I am from Las Vegas!
print(f'Hello my name is {name}, I am {age} years old and from {home}!') #Hello my name is Derek, I am 27 years old and from Las Vegas!

#boolean

bool_true = True

print(bool_true) #True
print(type(bool_true)) #<class 'bool'>

bool_false = False

print(bool_false) #False
print(type(bool_false)) #<class 'bool'>
