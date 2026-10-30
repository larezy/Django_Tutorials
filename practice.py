from operator import indexOf

user_profile= [{"name": "lael", "age": 27, "occupation": "student"},
               {"name": "laish", "age": 25, "occupation": "student"},
               {"name": "lami", "age": 19, "occupation": "student"}]
print(type(user_profile))

for i in range(len(user_profile)):
    print(f"My name is {user_profile[i]["name"]}, I am {user_profile[i]["age"]} years old and am a {user_profile[i]["occupation"]}")