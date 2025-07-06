## pandas as pd
pd.read_csv(filepath, parse_dates=None) – loads CSV file into a pandas DataFrame where filepath is the path to the CSV file and parse_dates is a list of columns to automatically parse as datetime  
df[column].isin(values) – checks if values in the column exist in the given list, used for filtering  
df[column].value_counts(normalize=False, sort=True) – counts unique values in a column; if normalize is True it returns percentages  
df.groupby(by)[column].mean() – groups data by one or more columns and calculates the mean of the selected column within groups  
Series.sort_index(ascending=True) – sorts values by index in ascending or descending order  
Series.astype(dtype) – converts elements of a Series to the specified data type  
df["col1"] - df["col2"] – subtracts two datetime columns returning a timedelta object  
tdelta.dt.total_seconds() – converts timedelta to total number of seconds  
/ 60 – divides seconds by 60 to get duration in minutes  
df["col"].mean() – calculates the mean of numeric values in a column  
df["col"].apply(func) – applies function func to each element in a column  
pd.isna(value) – checks if a value is missing (NaN)  
df["col1"] == df["col2"] – compares elements of two columns returning a boolean Series  
~boolean_series – negates boolean Series converting True to False and vice versa  
boolean_series.sum() – sums True values counting how many times a condition is met  
len(df) – returns the number of rows in a DataFrame  
print() – prints text or variables to the console  

## TextBlob
TextBlob(text).sentiment.polarity – calculates the sentiment polarity score of text ranging from -1 to 1 where values greater than 0 indicate positive sentiment, less than 0 indicate negative sentiment, and close to 0 indicate neutral sentiment  

## matplotlib.pyplot as plt
plt.figure(figsize=None) – creates a new figure for plotting with an optional size (width, height)  
plt.bar(x, height, color=None) – draws a bar chart with specified x labels, bar heights, and optional colors  
plt.title(label) – sets the title of the plot  
plt.xlabel(label) – sets the x-axis label  
plt.ylabel(label) – sets the y-axis label  
plt.tight_layout() – automatically adjusts the plot layout to avoid overlapping elements  
plt.savefig(fname) – saves the current plot to a file named fname  
plt.show() – displays the plot window  
