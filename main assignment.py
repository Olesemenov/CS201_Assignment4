import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("random_walk.csv")
def distance(x,y):
    return (x**2+y**2)**0.5
df['distance'] = distance(df['x'],df['y'])
max_distance = round(np.max(df['distance']), 2)
mean_distance = round(np.mean(df['distance']), 2)
print(f'the longest walk is {max_distance}, the mean distance is {mean_distance}')
critical_deviation = df[df['distance'] > mean_distance]
critical_deviation.to_json('filtered_walk.json', orient='records', indent=4)
plt.figure(figsize=(8,4))
plt.plot(df['x'], df['y'], color='green', label='walk')
plt.scatter(0, 0, color='blue', label="start point", alpha=0.5)
plt.scatter(df['x'].iloc[-1], df['y'].iloc[-1], color='red', label="end point", alpha=0.5)
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.8)
plt.legend()
plt.title("A random walk path")
plt.show()