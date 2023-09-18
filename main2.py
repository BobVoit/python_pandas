# Загрузить наборы данных scikit-learn 
from sklearn import datasets

# Загрузить набор изображений рукописных цифр 
digits = datasets.load_digits()

# Создать матрицу признаков 
features = digits.data

# Создать вектор целей 
target = digits.target

# print(features)
print(target)