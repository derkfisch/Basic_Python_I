#for loops

for x in [5, 10, 15, 20, 25, 30]:
    print(x)
#5
#10
#15
#20
#25
#30

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

for color in colors:
    print(color)
#red
#orange
#yellow
#green
#blue
#indigo
#violet

name = 'Derek'
for letter in name:
    print(letter)
#D
#e
#r
#e
#k

#continue statements
list_to_use = [10, 20, 30, 40, 50, 60, 70, 80, 90]

for element in list_to_use:
    if element == 50:
        continue
    print(element)
    print('Hello')
#10
#Hello
#20
#Hello
#30
#Hello
#40
#Hello
#60
#Hello
#70
#Hello
#80
#Hello
#90
#Hello

#break statements
for element in list_to_use:
    if element == 50:
        break
    print(element)
    print('Hello')
#10
#Hello
#20
#Hello
#30
#Hello
#40
#Hello

#pass statement
for num in list_to_use:
    pass

print('Hello World') #Hello World

#while loop

while num < 10:
    print(num)
    num += 1
#0
#1
#2
#3
#4
#5
#6
#7
#8
#9

