import pandas as pd

df = pd.read_csv("monks_train.csv")
df.columns = ["class", "a1", "a2", "a3", "a4", "a5", "a6", "id"]
print(df["class"] == 1)

