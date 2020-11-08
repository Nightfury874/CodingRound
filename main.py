#numpy library will also give imaginery numbers
import numpy as np
arr = [] 
  
# number of elements as input 
n = int(input("Enter number of elements : ")) 
  
# iterating till the range 
for i in range(0, n): 
    ele = int(input()) 
  
    arr.append(ele) # adding the element 
      
print(arr)


prr = np.sqrt(arr)
#print(prr)
nrr = (prr*-1)
#print (nrr)
#for concatenatuing the two numpy arrays
out = [y for x in [prr, nrr] for y in x] 
  
# Printing numpy list 
#print (str(out)) 
out.sort()
print (out)
