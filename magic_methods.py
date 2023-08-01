import math


class Triangle:
    NUMBER_OF_TRIANGLE = 0
    NUMBER_OF_SHAPES = 0

    def __new__(cls, *args, **kwargs):
        cls.NUMBER_OF_TRIANGLE += 1
        cls.NUMBER_OF_SHAPES += 1
        return super().__new__(cls)

    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def square_counter(self):
        half_perimeter = (self.side1 + self.side2 + self.side3) / 2
        result = half_perimeter * (half_perimeter - self.side1)*(half_perimeter - self.side2) *\
            (half_perimeter - self.side3)
        result = math.sqrt(int(result))
        result = int(result)
        return "The square of", self.present(), f"is {result}"

    def perimeter_counter(self):
        result = self.side1 + self.side2 + self.side3
        return "The perimetr of", self.present(), f"is {result}"

    def type_of_triangle(self):
        triangle_sides = [self.side1, self.side2, self.side3]
        longest_side = 0
        for side in triangle_sides:
            if side > longest_side:
                longest_side = side
        triangle_sides.remove(longest_side)

        if self.side1 == self.side2 == self.side3:
            return self.present(), "is Equilateral triangle"
        if self.side1 == self.side2 or self.side1 == self.side3 or self.side2 == self.side3:
            return self.present(), "is  Isosceles triangle"
        if longest_side**2 == triangle_sides[0]**2 + triangle_sides[1]**2:
            return self.present(), "is Right triangle"

    def present(self):
        return f"Triangle {self.side1} {self.side2} {self.side3}"

    def __str__(self):
        return self.present()

    def __repr__(self):
        return self.present()

# -------------------------------------------------------------------------------------------
# Here we have some function methods which takes an argument of "other".
# It's used when we have comparisons('>','<','=') or arithmetic operation('+','-','*','/') for example'
# __eq__(equal),
# __ne__(not equal),
# __gt__(greater than),
# __lt__(lower than),
# __add__(adding),
# __sub__(subtraction)
# __mul__(multiply)
#  etc.

# When we want to use + - * / > < etc. operators for our objects due to dunder methods we can say what
# in that case because we cant do arithmetic operation between objects.

    def __eq__(self, other):

        if not isinstance(other, Triangle):               # Here we are checking is the other triangle that we what
            raise ValueError("comparison cant be done")   # to compare to our triangle instance to our class

        eq1 = self.side1 == other.side1     # Here we compare first triangles sides to second triangles sides
        eq2 = self.side2 == other.side2     # triangle1 == triangle2
        eq3 = self.side3 == other.side3

        if eq1 == eq2 == eq3:
            if eq1 is True:
                return True
        else:
            return False

    def __gt__(self, other):
        if not isinstance(other, Triangle):
            raise ValueError("comparison cant be done")
        gt = self.side1 + self.side2 + self.side3 > other.side1 + other.side2 + other.side3
        if gt is True:
            return True
        else:
            return False

    def __lt__(self, other):
        if not isinstance(other, Triangle):
            raise ValueError("comparison cant be done")
        lt = self.side1 + self.side2 + self.side3 < other.side1 + other.side2 + other.side3
        if lt is True:
            return True
        else:
            return False

    def __add__(self, other):
        if not isinstance(other, Triangle):
            raise ValueError("comparison cant be done")
        count1 = self.side1 + other.side1
        count2 = self.side2 + other.side2
        count3 = self.side3 + other.side3
        return count1, count2, count3

# Here __call__ method which gives us opportunity to call our object as a function meanwhile we can give it
# arguments by using *args and **kwargs.
# *args and **kwargs meaning is that we can give to function unlimited key value arguments("hellow", 1, name="Joe")
    def __call__(self, *args, **kwargs):
        print(args, kwargs)
        return self.square_counter(), self.perimeter_counter(), self.type_of_triangle()


trg1 = Triangle(4, 5, 3)
trg2 = Triangle(3, 2, 4)

