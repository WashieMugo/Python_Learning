# Dictionaries are used to to store data values in key:value pairs
def dict_func():
    print("-----------\nDictionaries\n------------")
    users = {
        "names": ("Mr.", "Washington", 29),
        "org": "HCISS",
        "unit": "CSA",
        "married": False
    }
    print(users)

    print("we can pop using: #  users.pop('married') ")
    users.pop("married")
    print(users)

    print("We can add a key value pair eg: #  users['nationality']='Kenyan'")
    users["nationality"] = "Kenyan"
    print(users)

    print("Check if a value exists using: #  ' <key_name> in users ' : eg 'continent' in users '")
    cont = "continent" in users
    print(cont)

    print("we can update key value by using: # users['nationality']='Human'")
    users["nationality"] = "Human"
    print(users)

    print("Ierate with for loop")
    for bio in users:
        print(bio)

# sets are used to store unique values of a collection


def sets_func():
    print("\n--------\nSETS:\n--------")
    postcodes = {"Nbi", "Nyri", "Eld", "Mbsa", "Nkru", "Ksmu"}
    print(postcodes)

    print("\nadd using: #  set_name.add('value')  ")
    postcodes.add("Mrnga")
    print(postcodes)

    print("check if an element exists in set using 'in' keyword eg: #  'Nyri'in postcodes' ")
    print("Nyri" in postcodes)  # gives boolean True / False

    print("Iteration using for loop")
    for code in postcodes:
        print(code)


# --------- Function calls -----------
# dict_func()
sets_func()
