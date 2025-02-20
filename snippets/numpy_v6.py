import numpy as np
plt.semilogy(df['year_index'], df['Wind'])

#Fit a line to the data
c = 10*(df.loc[df["year_index"] == 4, "Wind"].values[0])

a_values = [0.5,1,1.3]
for a in a_values:
    p = np.exp(np.log(c) + a * np.log(filtered_increase))
    plt.semilogy(df['year_index'].iloc[3:-3], p, label=f"a = {a}")

plt.legend()
plt.show()