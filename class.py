# Here I have sample class example.

# class CV:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def present(self):
#         return print(self.name, self.surname, self.age)
#
#
# person1 = CV("Surenchik", "Tonoyan")
# person1.age = 22                                    # Here I'm creating new attribute out of class
# person1.present()
# print(person1.age)
#

# ------------------------------------------------------------------------------------------------
# __slots__ attribute

# __slots__ is an attribute which meaning is that we cant create new attribute out of our class here is example.

# class CV:
#     __slots__ = ['name', 'surname']     # Here we say but name, surname no more attributes
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#
# person1 = CV("Surenchik", "Tonoyan")
# person1.age = 30   # Here is an error


# ---------------------------------------------------------------------------------------------------------
# Class Object Attribute
#
# class CV:
#     Number = 10  # Here is a Class Object Attribute
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def present(self):
#         return f"this is Class Object Attribute {CV.Number}"
#
# person1 = CV("Surenchik", "Tonoyan")
# person2 = CV("Suren", "Toneyan")
#
# print(person1.Number)   # For person1 Number is 10
# person2.Number = 20     # Here we change Number for person2
# print(person2.Number)
# print(person1.present())

# ---------------------------------------------------------------------------------------------------
# Change variable

# class CV:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def change_name(self, new_name):  # Here we create new function which takes new argument(new_name)
#         self.name = new_name
#
#
# person1 = CV("Surenchik", "Tonoyan")
# person1.change_name("Vazgenchik")   # Here we call our new function and give it argument("Vazgenchik")
# print(person1.name)                 # which will be new name
#



class CV:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __int__(self):
        return print("sahdfjaerjvbliae")


person1 = CV("Surenchik", "Tonoyan")
