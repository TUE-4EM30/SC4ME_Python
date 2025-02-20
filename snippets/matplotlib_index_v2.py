import pandas as pd
df = pd.read_csv('data_renewables_Netherlands')

plt.plot(df['year'], df['Wind'])

# Add title and labels
plt.title('Wind Power Generation Over the Years', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Wind Power Output', fontsize=12)

plt.show()
