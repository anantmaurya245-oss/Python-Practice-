# the pandas library is speccially used for handeling data of diffrent dimensions

#program for creating series using series() functions of pandas 

import pandas as pd 

price_list = [100,200,300,400]
df = pd.DataFrame(price_list)
print(df)

# program for creating and determine the characterstics of the data frame
#####syntax Dataframe(data,columns= list of element in columns )

productdf= pd.DataFrame([[100,200,300,400],[4,2,5,6]],columns=('pen','shirt','book','mouse'))

# displaying the data frame
print("the dataframe is :\n",productdf)

#displaying the dimensions of  data frame using shape function
print("the dimensions of the data frame is :",productdf.shape)

#displaying the size of the data frame 

print("the size of the data frame is :\n",productdf.size)
#displaying the name of the columsns using the key() functions
print("the name of the columns of the data frame is :\n",productdf.keys())


# program for the  adding rows amd colummns in data frame 

productdf2= pd.DataFrame([[15,16,17,18],[5,6,7,8]],columns=('pen','shirt','book','mouse'))
print("displaying the 2nd data frame :\n",productdf2)
print("the dimension of the data framme is :",productdf2.shape)

# adding the row to data frame by another data frame 
productdf3 = pd.concat([productdf, productdf2], ignore_index=True)
print("dispaying the new data frame is :\n",productdf3)

# adding new columns of mobile
productdf3["mobile"] =[15000,2,30,40]

# adding the new columns of laptop 
productdf3["laptop"] = [35000,3,10,15]

# displaying the new data 
print("dispaying the new data frame after adding the columns is:\n",productdf3)

