class Fibonacci(object):	
	def __init__(self, start, max):
		self.start = start
		self.max = max
		
	def fibonacci(self, num):
		if num == 0 or num == 1:
			return num
		else:
			return self.fibonacci(num - 1) + self.fibonacci(num - 2)
			
	def printfib(self, start, max):
		for i in range(start, max):
			print("Fibonacci of %d %d: " % (i, self.fibonacci(i)))
			
start = int(input("enter start: "))
max = int(input("Enter maximum: "))
myfib = Fibonacci(start, max)
myfib.printfib(start, max)

#http://stackoverflow.com/questions/625083/python-init-and-self-what-do-they-do