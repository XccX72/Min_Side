import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("fodselstall.csv", encoding="latin1", sep="\t")

df.info()

df.dtypes

df.columns

df.plot()

df.head(8)

df = df.drop_duplicates()

df = df.dropna(how="all")

df = df[df["Levendefødte i alt"] >= 0]

df["navn"] = df["navn"].fillna("ukjent")
