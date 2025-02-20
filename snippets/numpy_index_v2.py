# renewable energy consumption in the Netherlands (TWh)
df = pd.read_csv('data_renewables_Netherlands.csv') 

# Manually calculate yearly increase
wind_increase = [None]  # First year
for i in range(1, len(df)):
    difference = df.loc[i, "Wind"] - df.loc[i - 1, "Wind"]
    wind_increase.append(difference)

# Add the calculated increase to the DataFrame
df["Yearly_Increase"] = wind_increase
