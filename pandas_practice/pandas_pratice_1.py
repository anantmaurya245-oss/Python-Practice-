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
