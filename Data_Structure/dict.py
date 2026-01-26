user = {
    "name": "Khushal",
    "role": "Dev",
    "is_active": True
}

# print(user["name"])

# print(user.get("rob")) # .get() is imp, if key is not there then it return None it prevent to crash 

print(user.keys()) 
print(user.values()) 

name = user.pop("name",None) # This pop the key and assign none as mention. Useful when you have to return a value or want to hide some things while returning data.
print(name)
print(user)