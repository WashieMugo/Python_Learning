import math

# create a list with a dynamic size


def create_list(num):
    num = int(num)
    my_list = []
    for i in range(num):
        inpt = input(f"enter element {i+1}:")
        try:
            if int(float(inpt)):
                my_list.append(int(float(inpt)))
        except:
            my_list.append(inpt)

    print(f"Your List => : {my_list}")


create_list("5")


# print(type(5.751))
# print(int(5.751))
print(bool(int(5.751)))  # > For reference this retuns True
