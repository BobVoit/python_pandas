import pandas as pd

date_to_year = lambda x: x[-4:]

url = "table.csv"

dataframe = pd.read_csv(url)

count_default, _ = dataframe.shape
print(count_default)

# print(date_to_year("01/01/1966"))

dataframe = dataframe[["Date"]]
dataframe["Value"] = [1 for elem in range(count_default)]


result4 = 0
for i, r in enumerate(dataframe['Date']):  
    r1 = date_to_year(r)
    value = int(r1)
    dataframe.at[i, 'Date'] = value  
    if value > 2000:
        result4 += 1

dataframe = dataframe.groupby("Date").count()

print(dataframe)

count_elements, _ = dataframe.shape

# result3 = 0
# max_crash = 0
# for index in dataframe.index:
#     current_value = dataframe['Value'][index]
#     if current_value > max_crash:
#         max_crash = current_value
#         result3 += dataframe['Date'][index]

# print(dataframe.loc[dataframe["Value"] == dataframe["Value"].max()])
# frame = dataframe.loc[dataframe["Value"] == dataframe["Value"].max()]


print(dataframe.loc[dataframe["Value"] == dataframe["Value"].max()])
print("Общее количество после 2000 года: " + str(result4))