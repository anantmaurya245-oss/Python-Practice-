# numpy has one very frequent use feature called multidimensional array it's much like matrix you can perform all operation use used in one dimensional array 

import numpy as np 

#promgram to show creation of mutidimensional array 
arr1 = np.array([[100,200,300,400],[600,700,800,900]])
print("multidimensional array using array function is:\n",arr1)

#creating multidimensional array using reshape() function 
arr_new= np.array([10,20,30,40,50,60])
arr2 = np.reshape(arr_new , (3,2))
print("multidimensional arrray using reshape is :\n ",arr2)

#creating the matrix using a matrix function 
arr3 = np.matrix('11 22; 33 44; 55 66')
print("multidimensional array using matrix function is :\n",arr3)


## accessing Element in multidimensional array
# in multidimensional array  the concept of indexing and slicing 
#program to show indexing and slicing 
arr4 = np.reshape(range(100,400,5), (10,6))
print("the array is :\n",arr4)

print("to print the first row and second columns is :",arr4[0][1])
print("element of second row and first columns:",arr4[1][0])
print("element os second row and second columns :",arr4[1][1])
print("element of third row and first columns :",arr4[2][1])

#slicing by specifying only the row 
print("first two row are :\n",arr4[0:2,])
print("third row is:\n",arr4[2,1])

#slicing by specifying both the row and columns indexes 
print("element in first and second row and columns are :\n",arr4[0:2,0:2])
print("element in second row and second to fourth columns :\n",arr4[1,1:4])


