class Fibonacci(object):	
	def __init__(self, start, max):
		self.start = start
		self.max = max
		
	def fibonacci(self, max):
		if max == 0 or max == 1:
			return max
		else:
			return self.fibonacci(max - 1) + self.fibonacci(max - 2)
			
	def printfib(self, start, max):
		for i in range(start, max):
			print("Fibonacci of %d %d: " % (i, self.fibonacci(i)))
			

while True:
	start = int(input("enter start : "))
	max = int(input("Enter maximum: "))
	myfib = Fibonacci(start, max)
	myfib.printfib(start, max)
	quit = input("Run again?Y/N: ")
	if quit == "N" or quit == "n":
		break

