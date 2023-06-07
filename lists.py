#Lists

#Declaring lists
list_1 = []
print(list_1) #[]
print(type(list_1)) #<class 'list'>

names = ['Mike', 'Carol', 'Angelica', 'Jeff', 'Jim', 'Penelope']
print(names) #['Mike', 'Carol', 'Angelica', 'Jeff', 'Jim', 'Penelope']
print(type(names)) #<class 'list'>

#indexing a list
print(names[2]) #Angelica
print(names[-1]) #Penelope
print(names[-5]) #Carol
print(names[1:]) #['Carol', 'Angelica', 'Jeff', 'Jim', 'Penelope']
print(names[1:5]) #['Carol', 'Angelica', 'Jeff', 'Jim']
print(names[:4]) #['Mike', 'Carol', 'Angelica', 'Jeff']
print(names[:]) #['Mike', 'Carol', 'Angelica', 'Jeff', 'Jim', 'Penelope']
print(names[::2]) #['Mike', 'Angelica', 'Jim"]
print(names[::-1]) #['Penelope', 'Jim', 'Jeff', 'Angelica', 'Carol', 'Mike']
print(names[1:5:2]) #['Carol', 'Jeff']

#item assignment
print(names) #['Mike', 'Carol', 'Angelica', 'Jeff', 'Jim', 'Penelope']
names[4] = 'James'
print(names) #['Mike', 'Carol', 'Angelica', 'Jeff', 'James', 'Penelope']

