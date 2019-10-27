
def main():
  print "-----------------------"
  print "Hacktobercub calculator"
  print "-----------------------"
  print ""	

  print(addition(3,5))
  print(subtraction(4,2))
  print(multi(3,3))
  print("Finished")
  
def addition(a,b):
	sum = a + b
	return sum
def subtraction(a,b):
	min = a - b
	return min
	
def multi(a,b):
   return a * b
if __name__ == '__main__':
	main()

