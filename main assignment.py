import pandas as pd
import numpy as np
df = pd.read_csv("random_walk.csv")
def distance(x,y):
    return (x**2+y**2)**0.5
df['distance'] = distance(df['x'],df['y'])
max_distance = round(np.max(df['distance']), 2)
mean_distance = round(np.mean(df['distance']), 2)
print(f'the longest walk is {max_distance}, the mean distance is {mean_distance}')

