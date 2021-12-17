# classes help us group data and fucntionality.
# classes help us make similar but distinct things

class virtual_pet:
    color = "brown"
    legs = 4
    lives = "9"
    wagging_tail = False

skippy = virtual_pet() #creaing an instance of the class
print(skippy.wagging_tail) # accessing a vaiable
print(skippy.color)  # accessing a variable using class_name.variable_name
