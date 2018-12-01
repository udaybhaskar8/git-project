def getSumOfLastDigits(numList):
  return sum(x % 10 for x in numList)
print(getSumOfLastDigits([1,2,3,4,5]))