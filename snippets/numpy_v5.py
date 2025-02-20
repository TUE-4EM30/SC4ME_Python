import numpy as np
window_size = 7
filtered_increase = np.convolve(df["Wind_Yearly_Increase"],
            np.ones(window_size)/window_size, mode='valid')

plt.semilogy(df['year'], df['Wind_Yearly_Increase'])
plt.semilogy(df['year'].iloc[3:-3],filtered_increase)
