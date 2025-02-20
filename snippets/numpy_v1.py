df = df[df['year']>1995]

plt.semilogy(df['year'], df['Wind'])