####################################################
#   Calculates sum of divisors
###################################################

def sum_divisors(n):
  sum = 0
  i = 1
  if n == 0 :
    return 0
  if n == 1:
    return 1
  while (i < n):
    if (n % i == 0):
      sum += i
    i += 1
  return sum
