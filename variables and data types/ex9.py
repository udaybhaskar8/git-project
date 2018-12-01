str1  = 'abcefghxyzThis,is,the,target,string  xyzlkdjf'
idx1 = str1.find( 'xyz'  )                    
idx2 = str1.find('xyz', idx1+1)            
str1 = str1[idx1+3:idx2].replace(',' ,'|')   
str1 = str1.   strip()                          
print(str1)
