import pandas as pd
df = pd.read_csv('data_renewables_Netherlands')

import matplotlib.pyplot as plt
plt.plot(df['year'], df['Wind'])
plt.show()

