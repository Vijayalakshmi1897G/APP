import numpy as np

# 1. Create a NumPy array containing temperatures for 10 days
temperatures = np.array([22.5, 24.0, 21.8, 23.2, 25.1, 26.4, 24.8, 23.0, 22.1, 25.5])
print("Original 10-day temperatures:")
print(temperatures)

# 2. Display the temperatures for the first 3 days (Indices 0, 1, 2)
print("\nTemperatures for the first 3 days:")
print(temperatures[:3])

# 3. Display temperatures from day 5 to day 8 (Indices 4, 5, 6, 7)
print("\nTemperatures from day 5 to day 8:")
print(temperatures[4:8])

# 4. Calculate the average, maximum, minimum, and total temperature
avg_temp = np.mean(temperatures)
max_temp = np.max(temperatures)
min_temp = np.min(temperatures)
total_temp = np.sum(temperatures)

print("\nTemperature Statistics:")
print(f"Average Temperature: {avg_temp:.2f}°C")
print(f"Maximum Temperature: {max_temp:.2f}°C")
print(f"Minimum Temperature: {min_temp:.2f}°C")
print(f"Total Temperature: {total_temp:.2f}°C")

# 5. Increase every temperature by 2°C using broadcasting
modified_temperatures = temperatures + 2

# 6. Display the modified array
print("\nModified temperatures (increased by 2°C):")
print(modified_temperatures)
