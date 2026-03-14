import pandas as pd

df = pd.read_csv("jul_barn_2000.csv")

df.head()

len(df)

df.columns

df["snillhet"].agg(["mean", "max", "min", "median"])

snillhet_Skala = df[["fornavn", "etternavn", "snillhet"]]

snillhet_Skala2 = snillhet_Skala.sort_values(["snillhet", "etternavn"], ascending= [False, True])

snillhet_Skala2.head(10)

df.groupby("gave")["snillhet"].mean()

df["nissehjelper"].value_counts(ascending=False)

df.describe()
df.info()

rader_mangler = df[df.isna().any(axis=1)]

len(rader_mangler)



