# name = 'Mac'
""" name = input('What is your name? ')

if name == '':
    print('Not fair')
    print('type in something')
elif name.lower() == 'mac':
    print('Not you again')    
else:
    print('Hello',name)
    print('Hello '+name) # Comment with hash
    print(f'Hello {name}') """

classes = ['calculus', 'Math', 'Geography','Reading']

""" print('classes first', classes[0])
print('classes last',classes[-1]) """

""" for c in classes:
    print(c) """

""" for i in range(0,len(classes)):
    print(i+1,classes[i])    
 """

""" for i in range(len(classes)):
    print(i+1,classes[i]) 

# range(start,stop,step)
for i in range(0, len(classes), 2):
    print(i+1,classes[i])  

# range(start,stop,step)
for i in range(0, len(classes)-1):
    print(i+1,classes[i])    """   

# # range(start,stop(exclusive),step)
# for i in range( len(classes)-1, -1,-1):
#     print(i+1,classes[i])      

if 3 == '3':
    print('loosey goose')
else:
    print('STRICT!')

# # Simple - can drop start if 0, step if 1
# for i in range(len(classes)):
#     print(i + 1, classes[i])
# # Skip every other elem
# for i in range(0, len(classes), 2):
#     print(i + 1, classes[i])
# # Backward through list: range(start (inclusive), stop (exclusive), step)
# for i in range(len(classes) - 1, -1, -1):
#     print(i + 1, classes[i])

# tired = True
# while tired:
#     print('sleep')
#     tired = False


def say_hi():
    print('hello')

say_hi()


def say_hi_personally(name):
    print('hello',name)

say_hi_personally('MAc')

def triple(name):
    return name+name+name

tripled_name = triple("Maci")
print('tripled name',tripled_name)