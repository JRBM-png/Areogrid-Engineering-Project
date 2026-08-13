import pandas as pd
df = pd.read_csv('telemetry_data(in).csv')

# print(df.head())

# Loads file, presents file

avg_temp = df.groupby('turbine_id')['temperature_c'].mean()

# print(df.groupby('turbine_id')['temperature_c'].mean())

# Presents average temperature of each turbine

failing_temp = avg_temp[avg_temp > 85]

# print(failing_temp)

# Outputs turbines with average temperature greater than 85 degrees

max_vibration = df.groupby('turbine_id')['vibration_mm_s'].max()

# print(max_vibration)

# Presents maximum vibration of each turbine

failing_vibration = max_vibration[max_vibration > 15]

# print(failing_vibration)

# Outputs turbines with maximum vibration greater than 15 mm/s

failing_turbines = set(failing_temp.index).union(set(failing_vibration.index))

print(failing_turbines)

# Outputs turbines that are failing either temperature or vibration criteria

# use python3 analyse_turbines.py to run the script and see the output of failing turbines