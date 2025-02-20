# renewable energy consumption in the Netherlands (TWh)
df = pd.read_csv('data_renewables_Netherlands.csv') 

# Calculate yearly increase in wind energy
df["Yearly_Increase"] = df["Wind"].diff()

# Remove the first NaN entry from diff() to avoid fitting problems
df = df.dropna()

# Prepare data for linear regression
X = df["year"].values.reshape(-1, 1)  # Years as independent variable
y = df["Wind_Yearly_Increase"].values  # Yearly increase as dependent variable

from sklearn.linear_model import LinearRegression

# Create a linear regression model
model = LinearRegression()

# Fit the model
model.fit(X, y)

# Get the fitted line
df["Fitted_Line"] = model.predict(X)