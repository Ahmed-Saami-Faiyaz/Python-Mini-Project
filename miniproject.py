import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Sample population data (Years 2000-2025)
years = np.arange(2000, 2026)
population = [1000, 1023, 1048, 1072, 1100, 1130, 1163, 1198, 1235, 1270, 
              1305, 1338, 1370, 1395, 1415, 1430, 1442, 1450, 1456, 1460, 
              1465, 1470, 1475, 1480, 1484, 1487]  # In millions (hypothetical data)

# Create a DataFrame
df = pd.DataFrame({'Year': years, 'Population (millions)': population})

# Calculate growth rate
df['Growth Rate (%)'] = df['Population (millions)'].pct_change() * 100

# Plot population trends
plt.figure(figsize=(10, 5))
plt.plot(df['Year'], df['Population (millions)'], marker='o', linestyle='-', color='b', label='Population')
plt.xlabel('Year')
plt.ylabel('Population (millions)')
plt.title('Population Growth in India (2000-2025)')
plt.legend()
plt.grid()
plt.show()

# Plot growth rate
plt.figure(figsize=(10, 5))
plt.bar(df['Year'][1:], df['Growth Rate (%)'][1:], color='g', label='Growth Rate (%)')
plt.xlabel('Year')
plt.ylabel('Growth Rate (%)')
plt.title('Population Growth Rate in India (2000-2025)')
plt.legend()
plt.grid()
plt.show()

# Display DataFrame
print(df)