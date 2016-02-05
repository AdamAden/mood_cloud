import math
print "hello"
def ex(x,y):
	ans = math.pow(x,y)
	return ans
a = float(raw_input("Input a number..."))
b = float(raw_input("Input a second number..."))
print(ex(a,b))