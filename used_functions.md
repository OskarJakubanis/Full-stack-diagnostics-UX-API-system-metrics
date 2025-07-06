## pandas as pd

pd.read_csv() – loads CSV file into a pandas DataFrame  
df_logs[...] – filters rows in the DataFrame based on condition  
df_feedback[...] – accesses or filters rows/columns in the DataFrame  
isin() – checks if values exist in a given list  
value_counts() – counts unique values in a column  
groupby() – groups data by one or more columns  
mean() – calculates the average of grouped values or column values  
sort_index() – sorts values by index  
astype(str) – converts values to string (for axis labels)  
pd.isna() – checks if a value is missing (NaN)  
df["col"].apply(func) – applies a function to each element in a column  
df["col1"] == df["col2"] – compares values across two columns (returns boolean Series)  
~df["col"] – inverts a boolean Series (True → False, False → True)  
df["col"].sum() – sums boolean values (counts how many times condition is True)  
len(df) – counts the number of rows in the DataFrame  

## matplotlib.pyplot as plt

plt.figure() – creates a new plot figure  
plt.bar() – draws a bar chart  
plt.title() – sets the chart title  
plt.xlabel() – sets the label for the x-axis  
plt.ylabel() – sets the label for the y-axis  
plt.tight_layout() – adjusts layout to avoid overlap  
plt.savefig() – saves the plot to a file  
plt.show() – displays the plot window  
plt.imshow() – displays image data (used to show the word cloud)  
plt.axis(off) – hides axis lines and labels  
plt.close() – closes the current figure to free up memory  

## wordcloud.WordCloud

WordCloud() – creates a WordCloud object for generating word clouds  
.generate(text) – generates a word cloud image from a single string of text  

## textblob.TextBlob

TextBlob(text).sentiment.polarity – calculates sentiment polarity (from -1 to 1) from a text string  

## general python functions

print() – prints text or variables to the console  
\n – inserts a line break in the printed output  
[... for ... in ... if ... else ...] – list comprehension with condition (used for coloring bars)  
round(val, 2) – rounds a number to 2 decimal places
