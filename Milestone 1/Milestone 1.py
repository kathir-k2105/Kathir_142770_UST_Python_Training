
#Import the library
import re
import pandas as pd

#Read the input file and concat all the columns
getbook=pd.read_csv(r'C:\\Users\\142770\Documents\\Python_training\\Books.csv')
getbook['Final Text']=getbook['The Project Gutenberg eBook of A knight of the air'].fillna('')  + getbook['Unnamed: 1'].fillna('') +getbook['Unnamed: 2'].fillna('') +getbook['Unnamed: 3'].fillna('') +getbook['Unnamed: 4'].fillna('') +getbook['Unnamed: 5'].fillna('') 
dfbook=pd.DataFrame(getbook['Final Text'])

# Function to split and convert the list from sentance of text
def getandsplit(text):
    cleaned_text = re.sub(r'[^\w\s]', '', text.lower())
    return cleaned_text.split()
    

Df_list=pd.DataFrame(dfbook['Final Text'].apply(getandsplit))
#Convert list into column value
bookwords = Df_list.explode('Final Text').reset_index(drop=True)
DfFinal=bookwords['Final Text'].value_counts().reset_index()
DfFinal.columns=['word','count']

Bookscount=pd.DataFrame(DfFinal)

Bookscount.sort_values(by='count', ascending=False)

Bookscount.to_csv('Wordfrequencies.csv')



