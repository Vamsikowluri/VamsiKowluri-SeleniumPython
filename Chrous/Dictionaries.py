my_dict = {"name": "Alice", "age": 25, "city": "New York"}

# Accessing a value
print(my_dict["name"])

# Adding or updating a key-value pair
my_dict["email"] = "alice@example.com"

# Removing a key-value pair
del my_dict["age"]

# Iterating through a dictionary
for key, value in my_dict.items():
    print(f"{key}: {value}")
