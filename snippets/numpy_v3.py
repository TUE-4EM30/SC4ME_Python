df = df[df['year']>1995]

df["year_index"] = df["year"] - 1995

plt.semilogy(df['year'], df['Wind'])