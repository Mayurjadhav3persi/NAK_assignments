print("Python program to demonstrate finally")
try:
	k = 5//0 
	print(k)
except ZeroDivisionError:
	print("Can't divide by zero")
finally:
	print('Finally block - This is always executed')