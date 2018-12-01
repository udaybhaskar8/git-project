def getSumOfLastDigits(numList): 
     x = sum(int(num[-1:]) for num in numList)
     return x
print(getSumOfLastDigits([1,2,3,4]))