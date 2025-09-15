import sys
import pandas as pd
import numpy as np

print(f"python environment is working, version: {sys.version}")

# Create a small dataframe to test pandas and numpy
df = pd.DataFrame({
    "speed_kmph" : [20, 30, 40, 50, 60, 65],
    "engine_rpm" : [1000, 1500, 2000, 2500, 3000, 3500]
})

print(f"\nSample DataFrame:\n", df)
print(f"\nSummanry statistics:\n", df.describe())

