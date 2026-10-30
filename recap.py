# x = "I am a: {y}, she is a: {x}".format(x="dog", y="cat")
# print(x)

# my_list =[1,2,['x','y','z']]
# print(my_list[2][1])

# my_stuff = {"key1": 123, "key2": "value2", "key3": {'123': [1,2,'grabMe']}}
#
# print(my_stuff["key3"]["123"][2])

# Problem 1
s = 'django'

print(s[0])
print(s[-1])
print(s[:4])
print(s[1:4])
print(s[4:])

print(s[::-1])

# problem 2
l = [3,7, [1,4, 'hello']]
# reassign "hello" to be "goodbye"

l[2][2]= "goodbye"
print(l)

# Problem 3
d1 = {'simple_key': 'hello'}
d2 = {'k1': {'k2':'hello'}}
d3 = {'k1':[{'nest_key' : ['this is deep' ,['hello']]}]}

print(d1['simple_key'])
print(d2['k1']['k2'])
print(d3['k1'][0]['nest_key'][1][0])

# Use a set to find the unique values of the list below:
my_list = [1,1,1,1,1,2,2,2,2,3,3,3,3]
unique_list = set(my_list)
print(unique_list)

# Problem 5
#Use print formatting to print the following string:
age = 4
name = "Sammy"

print("Hello my dog's name is {} and he is {} years old".format(name, age))