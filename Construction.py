#Problem #4
#Create a class called construction.  Launch a new process of chrome.exe that will 
#automatically open this youtube video when the constructor 
#is called-> https://www.youtube.com/watch?v=hl_9_q_uLF8
#open this youtube video when the destructor is called ->
#https://youtu.be/JwXohnAYyuc?t=22s

import webbrowser

class Construction:
	def __init__(self):
		webbrowser.open("https://www.youtube.com/watch?v=hl_9_q_uLF8")
		
	def __del__(self):
		webbrowser.open("https://youtu.be/JwXohnAYyuc?t=22s")
		
new1 = Construction()
del new1