# Inheritance ------------------------------------------------------------

# We have two classes which has similarities, they both has name and color.

class Cars:
    def __init__(self, name: str, color: str):
        self.name = name
        self.color = color

    def present(self):
        return print(f"This is {self.name} and color is {self.color}")


class Sedan:
    def __init__(self, name: str, color: str, wheel_size: int):
        self.name = name
        self.color = color
        self.wheel_size = wheel_size

    def present(self):
        return print(f"This is {self.name} color is {self.color} and wheel size is {self.wheel_size} ")


car1 = Cars("mercedes", "blue")
sedan1 = Sedan("mercedes", "blue", 18)
print("----------------------------------1-----------------------------------")

# As we can notice class Sedan takes name and color arguments as class Cars, and we have to initialize
# them in __init__ method.Here is Idea of INHERITANCE, if the second class takes same arguments as the
# first class we can just inherit second(Sedan) from first(Cars).So the first class becomes parent class,
# second becomes child class.|
#                            |
# -------------------------------------------------------------------------------------------------


class Cars:
    def __init__(self, name: str, color: str):
        self.name = name
        self.color = color

    def present(self):
        return print(f"This is {self.name} and color is {self.color}")


class Sedan(Cars):  # (Cars) means that Sedan takes all arguments from Cars
    def __init__(self, name: str, color: str, wheel_size: int):
        self.wheel_size = wheel_size
        super().__init__(name, color)

    def present(self):
        return print(f"This is {self.name} color is {self.color} and wheel size is {self.wheel_size} ")


sedan2 = Sedan("mercedes", "blue", 18)
sedan2.present()
# So we made Sedan class to inherit from Cars(Sedan(Cars)).We said that Sedan's __init__ takes name,
# color, wheel_size arguments and instead of initializing them "self.name = name", "self.color = color"
# like that, we use "super().__init__(name, color)" this. Super() calls __init__ constructor of parent
# class and gives it "name" and "color" attributes.

# Instead of using super() method we also can do this.


class Sedan(Cars):
    def __init__(self, wheel_size: int, name: str, color: str, ):
        self.wheel_size = wheel_size
        Cars.__init__(self, name, color)

    def present(self):
        pass


sedan3 = Sedan(18, "mercedes", "blue")

# So what is the difference.By using super() we say bring parent classes __init__ function, by using
# Cars.__init__ we say bring Cars classes __init__ function
#
#
#
# ------------------------------------------ TYPES OF INHERITANCE ------------------------------------------------------
#
# 1.Single inheritance - when a class inherits from another class(Sedan(Cars)).

# 2.Multilevel inheritance - when a class inherits from another which inherits another(Bike(Sedan), Sedan(Cars)).

# 3.Hierarchical inheritance - when 2 classes inherit a class(Bike(Cars), Sedan(Cars)).

# 4.Multiple inheritance - when a class inherits from 2 classes(Bike(Sedan, Cars)).
#
#
#
#
# ------------------------------------------ MULTIPLE INHERITANCE ------------------------------------------------------

# Multiple Inheritance has its (__mro__)Model Resolution Order which says how its arrangement(դասավորվածություն)
# would be.


class Cars:
    pass


class Sedan(Cars):
    pass


class Bike(Sedan):
    pass


# print(Bike.__mro__) --> (<class '__main__.Bike'>, <class '__main__.Sedan'>, <class '__main__.Cars'>, <class 'object'>)

# So here we can see how inheritance organized here due to __mro__ method.
#
#
# Here we have example of multiple inheritance--------------------------------------------------------------------------

class Work:
    def __init__(self, company: str, salary: int):
        self.company = company
        self.salary = salary


class Study:
    def __init__(self, uni: str, course: int):
        self.uni = uni
        self.course = course


class Person(Study, Work):
    def __init__(self, phone: str, uni: str, course: int, company: str, salary: int):
        self.phone = phone
        Study.__init__(self, uni, course)
        Work.__init__(self, company, salary)


person1 = Person("098222429", "YSU", 4, "Google", 1500)
# print(person1.uni)

# ----------------So what we have.

# We created 2 classes Work, Study and a class Person, which inherits from Work and Study.Pay attention that first
# positional argument is Study(Person(Study, Work):), this means that Study has high priority than Work, so if we
# want to find argument or method, at first will be checked Study than Work.

# ----------------About __init__ constructor

# (131)def __init__(self, phone: str, uni: str, course: int, company: str, salary: int):

# __init__ function we gave first Persons arguments(phone) than Studies(uni, course) than Works(company, salary).
# So arguments must be sequential(հաջորդական)․


#         self.phone = phone
#         Study.__init__(self, uni, course)
#         Work.__init__(self, company, salary)

# Inside __init__ function we are saying to bring Studies and Works __init__ functions.


#
# Here is another way for handling multiple inheritance-----------------------------------------------------------------
#
# In this case we are turning multiple inheritance to multilevel inheritance
class Work:
    def __init__(self, company: str, salary: int):
        self.company = company
        self.salary = salary


class Study:
    def __init__(self, uni: str, course: int, company: str, salary: int):
        self.uni = uni
        self.course = course
        super().__init__(company, salary)


class Person(Study, Work):
    def __init__(self, phone: str, uni: str, course: int, company: str, salary: int):
        self.phone = phone
        super().__init__(uni, course, company, salary)


person2 = Person("098222429", "YSU", 4, "Google", 1500)
# Here we are saying that Person inherits from Study, Study inherits from Work
# ----------------------------------------------------------------------------------------------------------------------
#
#
#
#
# ----------------------------------------------- OPTIMIZING CODE ------------------------------------------------------

# __________________________________________________________________________________
# At first lets understand how *args, **kwargs work                                 |
#                                                                                   |
#                                                                                   |
# def foo(*args, **kwargs):                                                         |
#     print(*args)              ----> 1, 2, 3, 4                                    |
#     print(args, kwargs)       ----> (1, 2, 3, 4) {'a': 'hello', 'b': 'world'}     |
#                                                                                   |
#                                                                                   |
# foo(1, 2, 3, 4, a='hello', b='world')                                             |
#                                                                                   |
# Here we have function which takes *args and **kwargs which means that it takes    |
# unlimited arguments which can be also key value arguments.The arguments are stored|
# for *args in tuple and for **kwargs in dictionary.                                |
#                                                                                   |
# print(*args) the output of this is 1, 2, 3, 4 because '*' is unpacking tuple so   |
# the output of print(args) will be (1, 2, 3, 4)                                    |
#                                                                                   |
# print(kwargs) the output of this is dictionary {'a': 'hello', 'b': 'world'}, but  |
# here print(**kwargs) we would have an error, because we cant unpack dictionary,   |
# because unpacking dictionary would mean this print(a="hello", b="world"), as      |
# we can see print() function has given wrong attributes.                           |
#                                                                                   |
# -----------------------------------------------------------------------------------
#
#
# ______________________________________________________________________________________________________________________
# --------------------------------------------- MULTIPLE INHERITANCE ---------------------------------------------------


class Work:
    def __init__(self, company: str, salary: int):
        self.company = company
        self.salary = salary


class Study:
    def __init__(self, uni: str, course: int, *args, **kwargs):
        self.uni = uni
        self.course = course
        super().__init__(*args, **kwargs)


class Person(Study, Work):
    def __init__(self, phone: str, *args, **kwargs):
        self.phone = phone
        super().__init__(*args, **kwargs)


person3 = Person("098222429", "YSU", 4, "Google", 1500)

# As we can see our code became shorter and optimized due to *args and **kwargs.Now we can give to each class their own
# arguments and rest arguments by using *args and **kwargs, so don't pay attention what arguments parent class takes.


# ______________________________________________________________________________________________________________________
# -------------------------------------------- HIERARCHICAL INHERITANCE ------------------------------------------------


class Person:
    def __init__(self, phone: str):
        self.phone = phone


class Work(Person):
    def __init__(self, company: str, salary: int, *args, **kwargs):
        self.company = company
        self.salary = salary
        super().__init__(*args, **kwargs)


class Study(Person):
    def __init__(self, uni: str, course: int, *args, **kwargs):
        self.uni = uni
        self.course = course
        super().__init__(*args, **kwargs)


person4 = Work("Google", 1500, "098222429")
person5 = Study("YSU", 4, "098222429")

#
# ______________________________________________________________________________________________________________________
# ---------------------------------------------- MULTILEVEL INHERITANCE ------------------------------------------------


class Person:
    def __init__(self, phone: str):
        self.phone = phone


class Work(Person):
    def __init__(self, company: str, salary: int, *args, **kwargs):
        self.company = company
        self.salary = salary
        super().__init__(*args, **kwargs)


class Study(Work):
    def __init__(self, uni: str, course: int, *args, **kwargs):
        self.uni = uni
        self.course = course
        super().__init__(*args, **kwargs)


person6 = Study("YSU", 4, "Google", 1500, "098222429")


# ______________________________________________________________________________________________________________________
# ----------------------------------------------- SINGLE INHERITANCE ---------------------------------------------------


class Person:
    def __init__(self, phone: str):
        self.phone = phone


class Work(Person):
    def __init__(self, company: str, salary: int, *args, **kwargs):
        self.company = company
        self.salary = salary
        super().__init__(*args, **kwargs)


person7 = Work("Google", 1500, "098222429")
