# creating 1 D array 
#  program to create artray from the numpy library 
import numpy as np

# creating an array
myarray1 =np.array([121,22,33,44,55,66],int)
print("The array of inmtegers is :\n",myarray1)

#creating an array of characters
myarray2 = np.array(['a','b','c','d','e'])
print("The array ofn character is :\n",myarray2)

#creating a float number 
myarray3 = np.array([6.2,4.6,7.5,8.4],float)
print("the array of the float :\n",myarray3)


#2 program for creating array using function
myarray4 = np.arange(14)
print("the array of integer using arange function:\n",myarray4)

myarray5 =np.arange(14,19,dtype= float)
print("the array of decimal numbers using arange function :\n",myarray5)

myarray6 = np.linspace(12,24,5)
print("the array of integer using linspace function is :\n",myarray6)

myarray7 = np.linspace(1.,4.,5)
print("the array of decimal number using linspace function :\n",myarray7)

myarray8 = np.zeros((4))
print("an array of zeros :",myarray8)

myarray9 = np.ones((5))
print("an array of using ones :",myarray9)

# this program creates arrays using diffrent functions 
#the arange function is either accepts one or two arguments this decide the range from which number you want and where you want to end the array element or number 
# the linspace() functions has three argument also for creating number at eqaul interval 
#the zeros used to make a array of zeros number 
# the ones functioons is used to create a array of 1 and how many it depend on the what you enter inside the function 


## Accessing the elements of 1 D array

# program for using functions on numpy array 
myarray10 = np.array([13,14,15,16,17,18,19,34,56],int)
print("original array is :\n",myarray10)

#modifing the element 
myarray10[4] = 69
print("modified array :\n",myarray10)

#charactersitics of array 

print("size of the array10 is :\n",myarray10.size)

#retun datatype of array 
print("the data type of array :\n",myarray10.dtype)

# for returning the mean of the array 10 
print("the mean of the array 10 is :\n",np.mean(myarray10))

# print the median of an array 
print("the median of the array is :\n",np.median(myarray10))

# the min , max ,sum for the array 
print("the min value in the array is :\n",np.min(myarray10))

print("the maximun value of the array is :\n",np.max(myarray10))

print("the sum of the array of the element is :\n",np.sum(myarray10))

# the product of all the array using function 
print("product of the array is :\n",np.prod(myarray10))

# the cov() functions returnd the covariance of all array function 
print("the covariance of the array is :\n",np.cov(myarray10))

# the var() function returned the variance of the array
print("the variance of the array is :\n",np.var(myarray10))
# the std function retuns the standard deviation the array element 
print("the standard deviation of the element is :\n",np.std(myarray10))




