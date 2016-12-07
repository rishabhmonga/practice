import pandas as pd
import numpy as np

if __name__ == '__main__':
    df = pd.read_csv(".\mushroom_data.csv")
    # print(df.head())
    df.columns = ["droppable", "cap-shape", "cap-surface", "cap-color", "bruises", "odor", "gill-attachment",
                  "gill-spacing", "gill-size", "gill-color", "stalk-shape", "stalk-root", "stalk-surface-above-ring",
                  "stalk-surface-below-ring", "stalk-color-above-ring", "stalk-color-below-ring", "veil-type",
                  "veil-color", "ring-number", "ring-type", "spore-print-color", "population", "habitat"]

    droppable = df['droppable']
    df.drop('droppable', 1, inplace=True)
    bruises = df['bruises']
    df.drop('bruises', 1, inplace=True)
    df.insert(0, 'bruises', bruises)
    df.insert(len(df.columns), 'droppable', droppable)
    print(df.head())
