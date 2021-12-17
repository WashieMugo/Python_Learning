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
# sets are unordered. thus they do not have indices


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
        print(f"option: {code}")

    print("Remove using  .remove('set_value') ")
    print(postcodes)
    postcodes.remove("Mrnga")
    print(postcodes)

    print("Avoid Errors by first using in to check if element exists before removing:")
    if "Nbi" in postcodes:
        postcodes.remove("Nbi")
    print(postcodes)

    print("get length usin: len(set_name)")
    print(len(postcodes))

    print("Check if set is a subset of another set using: # set_name.issubset(subset_name)")
    postcodes2 = {"Ksmu", "Mbsa"}
    postcodes3 = {"Nbi", "Nkuru", 'Mbsa'}
    print(f"P1:{postcodes} \nP2:{postcodes2} \nP3:{postcodes3}")
    p2sub = postcodes2.issubset(postcodes)
    p3sub = postcodes3.issubset(postcodes)
    print(f"P2 sub P1: {p2sub} \nP3 sub P1: {p3sub} ")

    print("Check if a set is Superset to a subset using: # .issuperset(subset_name)")
    p1sup2 = postcodes.issuperset(postcodes2)
    p1sup3 = postcodes.issuperset(postcodes3)
    print(f"P1 super P2: {p2sub} \nP1 super P3: {p3sub} ")

    print("Join sets using:egs # postcodes2.union(postcodes3)")
    print(postcodes2.union(postcodes3))

    print("Check elements present in both sets using : # intersection() ")
    print(postcodes3.intersection(postcodes2))

    print("Check elements different in sets using : # difference()")
    print(postcodes3.difference(postcodes2))

# Lists


def lists_func():
    grocery_list = ["Brocolli", "Cereal", "milk", "Brocolli"]
    print(grocery_list)

    print("transform to set using set(list_name)")
    print(set(grocery_list))
    grocery_set = set(grocery_list)


# --------- Function calls -----------

# dict_func()
sets_func()
# lists_func()
