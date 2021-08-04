"""
this file will be executed in 2 ways.
1. python file1.py
2. import this file1 in another file, for example main.py: run python main.py
"""
x=1000
name="jay"
def fun1():
	print("this is fun1 in file1")
	
if __name__ == "__main__":# this will gets true in first scenario.
	print("this is file1")
	print("started")
	fun1()
	print("ended")