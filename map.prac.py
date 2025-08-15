age = {}
# add key/valye
age["Johan"] = 23
age["Simon"] = 22

if "Aron" not in age:
    print("No age")

print(age["Johan"])

# Removing a key safely
age.pop("Johan", None)

# Accesing a value safely
print(age.get("Simon", "Unknown"))