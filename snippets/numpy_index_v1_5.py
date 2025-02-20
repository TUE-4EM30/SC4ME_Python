# renewable energy consumption in the Netherlands (TWh)
df = pd.read_csv('data_renewables_Netherlands.csv') 

# filter out just the year and wind columns
df = df[["year","Wind"]]
