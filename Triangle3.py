#In this problem, you MUST use a 2 dimensional list, and you MUST use nested loops
#Write three functions, Triangle, BackwardsTriangle, and UpsideDown Triangle
#given the number 4, Triangle will output
#.
#..
#...
#....
#
#BackwardsTriange will output
#   .
#  ..
# ...
#....
#
#UpsideDownTriangle will output
#....
#...
#..
#.

import sys

class Triangle(object):
	def __init__(self,size):
		self.size = size

		self.elements2 = [ ["" for i in range(size) ] for j in range(size) ]

		for i in range(size):
			for j in range(i+1):
				self.elements2[i][j] = "*"	
				
	def UpsideDownTriangle(self):
		for i in reversed(self.elements2):
			str = ""
			for j in i:
				str = str + j
			print(str)
		print("\n")
	
	def PrintTriangle(self):
		for i in self.elements2:
			str = ""
			for j in i:
				str = str + j
			print(str)
		print("\n")
	
	def BackwardsTriangle(self):
		spaces = size
		for i in self.elements2:
			str = " " * (spaces - 1)
			for j in i:
				str = str + j
			print(str)
			spaces -= 1
		print("\n")
		
size = int(input("Enter triangle size: "))
MyTriangle = Triangle(size)
MyTriangle.PrintTriangle()
MyTriangle.UpsideDownTriangle()
MyTriangle.BackwardsTriangle()