'''
Write a Python class named Circle constructed by a radius
and two methods which will compute the area and
the perimeter of a circle
'''

class Circle:

    def area(r):
        a = 3.14 * r * r
        print(a)

    def perimeter(r):
        p = 2 * 3.14 * r
        print(p)

Circle.area(3)
Circle.perimeter(3)
