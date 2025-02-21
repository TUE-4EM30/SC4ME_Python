import pandas as pd
# Read in the data from a .csv file
df = pd.read_csv('renewables.csv') 
df # Renewable energy consumption (TWh)

# Add a row with the global renewable energy consumption
global_row = pd.DataFrame({
    "Country": ["World"],
    "Hydro": [df["Hydro"].sum()],
    "Nuclear": [df["Nuclear"].sum()],
    "Solar": [df["Solar"].sum()],
    "Wind": [df["Wind"].sum()]
})
df = pd.concat([df, global_row], ignore_index=True)

# Add a row of total renewable energy consumption
energy_sources = ["Hydro", "Nuclear", "Solar", "Wind"]
df = df[energy_sources].sum(axis=1)

# Reindex for wind energy consumption
df = df.sort_values(by="Wind", ascending=False)
df = df.reset_index(drop=True)