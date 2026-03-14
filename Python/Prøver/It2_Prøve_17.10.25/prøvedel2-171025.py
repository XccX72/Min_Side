import pandas as pd
import matplotlib.pyplot as mlt

df = pd.read_csv("stortingsrepresentanter.csv", sep=";", index_col=False)

#-----Øving

df["etternavn"].head(15)
df.loc[5]




# ---- Enkel info -----
df.dtypes
df.describe

# ---- Oppgave 1 -----

df.head(5)

# ----- Oppgave 2 -----

df.tail

# ----- Oppgave 3 ------

a = df[(df["fylke"] == "Sogn og Fjordane")]

a[["etternavn", "fornavn", "komiteer"]]

#----- Oppgave 4 --------

b = df[(df["fylke"] == True)]

df[["fylke"]].groupby("fylke").value_counts()

#----- Oppgave 5 -----

(df[["parti"]].groupby("parti").value_counts()/168*100).plot(kind="bar"
, title="% deling av representanter")

# ------ Oppgave 6 -----

(df[["fodselsaar"]].groupby("fodselsaar").value_counts()*(-1) + 2025).plot(kind="bar", title="alder")

#----- Oppgave 7a -----

b = df[(df["komiteer"] == True)]

df[["komiteer"]].groupby("komiteer").value_counts()





