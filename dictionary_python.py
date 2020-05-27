dictionary ={}


dictionary[0] = 'hello'

dictionary[2] = 'world'

dictionary[3] = 1

dictionary['Things'] =2,3,4,5
dictionary[2] ='Geek'

# five = 5

five = 'five'

dictionary[five]= {'Nested': {'1': 'Goodbye','2': 'Saturn'}}
#print(dictionary)

#print(dictionary['Things'])

# for key in dictionary:
#     print(dictionary[key])

colors = ['red','blue','ruby','magenta','red','red']    

uni_colors = {'green','yellow','blue'}

unique_colors = set(colors)
# print("Unique colors",unique_colors)

uni_color_set = {'red','blue','ruby','green','emrald','emrald'}

uni_color_s1 = {'red','blue','ruby','green','emrald','emrald'}



# print("Unique colors",uni_color_set)

# print("Unique colors s1",uni_color_s1)

colorssss = ['red','blue','ruby','magenta','red','red']   
colorssss.append('chartreuse')
print("colorssss",colorssss)

colorssss_set = set(colorssss)
colorssss_set.add('green')
colorssss_set.add('blue')

print("colorssss_set",colorssss_set)

colorssss_set.remove('chartreuse')
print("colorssss_set remove",colorssss_set)

colors_tuple = ('red1','blue1','green1','blue1')
#  tuples cannot be changed so you cannot pop anything from it
print("tuple",colors_tuple)

print("type",type(colors_tuple))

print("set type",type(colorssss_set))


