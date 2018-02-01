# import unittest
# import testcase
#
# class TestRunner():
#     def run_test(self):
#         suite = unittest.TestSuite
#         suite.addTest(testcase.TestCase('test_login'))
#         runner = unittest.TextTestResult()
#         runner.run(suite)
#
#
# if __name__=="__main__":
#     pinpin_test_runner= TestRunner()
#     pinpin_test_runner.run_test()
#

# import turtle
# from math import sin, cos, pi
#
# r = 200
# inc = 2 * pi / 100
# t = 0;
# n = 1.5
#
# for i in range(100):
#     x1 = r * sin(t)
#     y1 = r * cos(t)
#     x2 = r * sin(t + n)
#     y2 = r * cos(t + n)
#     turtle.penup()
#     turtle.goto(x1, y1)
#     turtle.pendown()
#     turtle.goto(x2, y2)
#     t += inc
# turtle.getscreen()._root.mainloop

# import string
# import random
#
# def randompassword():
#     chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
#     size = 4
#     return "".join(random.choice(chars) for x in range(size,25))
#
# print (randompassword())
