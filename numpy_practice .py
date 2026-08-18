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


