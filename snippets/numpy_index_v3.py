# renewable energy consumption in the Netherlands (TWh)
df = pd.read_csv('data_renewables_Netherlands.csv') 

# Calculate yearly increase in wind energy
df["Yearly_Increase"] = df["Wind"].diff()
