from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
import pandas as pd

crime_data = pd.read_csv('/content/drive/MyDrive/Crime_Data_from_2020_to_Present.csv')
crime_data.head()

  data_shuffled = data.sample(frac=1)

  train_rows = int(train_size * len(data))
  val_rows = int(val_size * len(data))
  test_rows = len(data) - (train_rows + val_rows)

  train_data = data_shuffled.iloc[:train_rows]
  val_data = data_shuffled.iloc[train_rows:train_rows + val_rows]
  test_data = data_shuffled.iloc[train_rows + val_rows:]

  train_x = train_data[data.columns[:-1]]
  train_y = train_data[data.columns[-1]]
  val_x = val_data[data.columns[:-1]]
  val_y = val_data[data.columns[-1]]
  test_x = test_data[data.columns[:-1]]
  test_y = test_data[data.columns[-1]]

  return train_x, train_y, val_x, val_y, test_x, test_y

train_x, train_y, val_x, val_y, test_x, test_y = split_dataset(data)
