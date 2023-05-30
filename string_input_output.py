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

