import pandas as pd
import numpy as np

# Generate synthetic sensor data
timestamps = pd.date_range(start="2025-01-01", periods=100, freq="H")
data = {
    "timestamp": timestamps,
    "temperature": np.random.normal(30, 2, size=100),
    "humidity": np.random.normal(60, 5, size=100),
    "air_quality": np.random.uniform(50, 150, size=100),
    "noise": np.random.uniform(30, 80, size=100),
}

df = pd.DataFrame(data)
df.to_csv("backend/data/sensor_data.csv", index=False)
print("Synthetic sensor data generated!")
