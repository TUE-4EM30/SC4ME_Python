import pandas as pd
df = pd.read_csv('data_renewables_Netherlands')

# Plot the data with a line style and marker for clarity
plt.plot(df['year'], df['Wind'], marker='o', 
         linestyle='-', color='b', label='Wind Power')

# Add title and labels
plt.title('Wind Power Generation Over the Years', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Wind Power Output', fontsize=12)

# Add grid for better readability
plt.grid(True, linestyle='--', alpha=0.6)

# Add a legend
plt.legend()

plt.show()
