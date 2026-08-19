# program to use the mathematical operators on multiple arrays 
import numpy as np
arr1= np.array([11,22,33,44],int)
arr2=np.array([40,50,60],int)
arr3=np.array([7,8,9],int)

#performing addition and substraction on all the element of an array 
arr4= arr3+arr2-arr1
print("addition and substraction of the arrrys element to create the new element :\n",arr4)

#performing the multiplication and division on all the element of an array 
arr5 = (arr4*arr3)/arr2
print("the multiplication and the divison is :\n",arr5)

#using modulus and  operator % on all element of the array 
arr6 = arr3 % arr2
print("the modulus of all element :\n",arr6)

## Relational operator for 1 d array 
arr7= np.array([214,315,142,157,567,875,980],int)
arr8 = np.array([311,453,711,362,230,453,672,891],int)

print("are element of first array >= coressponding element of second array ?\n",arr7>=arr8)

#using less than or equal to (>=) relational operator 
print("are the eelement of first array <= corresponding element of second array ?\n",arr7<arr8)

#using equals == relational operator 
print("are elements of first array = corresponding element of second array ?\n",arr7==arr8)
 
#usinng not equal to != 
print("are the element of first array != corresponding element of second array?\n",arr3!=arr2)
