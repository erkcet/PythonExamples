####################################################
#   Prints all the prime numbers
###################################################

def print_prime_factors(number):
  factor = 2
  while factor <= number:
    if number % factor == 0:
      print(factor)
      number = number / factor
    else:
      factor = factor + 1
  return "Done"

print_prime_factors(100)
# Should print 2,2,5,5
