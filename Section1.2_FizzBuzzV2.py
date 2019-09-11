''' Optimizing the orginal FizzBuzz:
		if divisable by 3 sub with Fizz
		if divisable by 5 sub with Buzz
		if divisable by 15 sub with FizzBuzz
'''
# Create an array with numbers 1-5

number = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

#iterate through the array and check which numbers are fizz and which are Buzz

for num in number :
	if num % 15 == 0:
		print(num) , ("FizzBuzz")
	elif num % 5  == 0:
		print (num) , ("Buzz")
	elif num % 3 == 0:
		print (num) , ("Fizz") 
	else:
		print (num)

'''The runtime for the orginal algorithm has been improved by dividing by 15:
we do not have to check for both 3 and 5 again instead we check one time
Check for numbers divisable by 3 (Fizz)
Check for numbers divisable by 5 (Buzz)
and Check for numbers divisable by 15 (FizzBuzz)
'''
