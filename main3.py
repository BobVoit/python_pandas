import pandas as pd

url = "https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/titanic.csv"

dataframe = pd.read_csv(url)

# print(dataframe.head(5))
# print(dataframe.iloc[1:4])

# Задать индекс
# dataframe = dataframe.set_index(dataframe["Name"])

# Показать строку
# print(dataframe.loc["Allen, Miss Elisabeth Walton"])
# print(dataframe[dataframe['Sex'] == 'female'].head(2))
# print(dataframe["Sex"].replace("female", "Woman").head(2))
# print(dataframe.replace(1, "One").head(2))
# print(dataframe.replace(r"1st", "First", regex=True).head(2))

# print("Максимум: ", dataframe["Age"].max())
# print("Минимум: ", dataframe["Age"].min())
# print("Среднее: ", dataframe["Age"].mean())
# print("Сумма: ", dataframe["Age"].sum())
# print("Количество: ", dataframe["Age"].count())

# print(dataframe["Sex"].unique())
# print(dataframe["Sex"].value_counts())

# print(dataframe[dataframe['Age'].isnull()].head(2))

# print(dataframe.drop("Age", axis=1).head(2))

# print(dataframe[dataframe['Sex'] != 'male'].head(2))
# print(dataframe.drop_duplicates(subset=["Sex"]).head(2))

dataframe = dataframe.drop(["Name", "PClass"], axis=1)
print(dataframe.groupby("Sex").mean())