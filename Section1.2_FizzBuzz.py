'''FizzBuzz
	if divisable by 3 sub with Fizz
	if divisable by 5 sub with Buzz
	if divisable by 3 & 5 sub with FizzBuzz
'''
# Create an array with numbers 1-5

number = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

#iterate through the array and check which numbers are fizz and which are Buzz

for num in number :
	if num % 3 == 0 and num % 5 == 0:
		print(num) , ("FizzBuzz")
	elif num % 5  == 0:
		print (num) , ("Buzz")
	elif num % 3 == 0:
		print (num) , ("Fizz") 
	else:
		print (num)
	
