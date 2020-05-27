'''
Write a Python class named Circle constructed by a radius
and two methods which will compute the area and
the perimeter of a circle
'''

class Circle:


    def area(self, r):
        a = 3.14 * r * r
        print(a)

    def perimeter(self, r):
        p = 2 * 3.14 * r
        print(p)

object1 = Circle()
object1.area(3)
object1.perimeter(3)
