import pandas as pd
import os
import matplotlib.pyplot as mlp

aaaaaa = os.path.dirname(__file__)
filsti = os.path.join(aaaaaa, "imdb_top250.csv")
df = pd.read_csv(filsti)

df.info()


#Oppgave 1 gjort ................................-------- 
af = df.drop(["regissør", "aldersgrense"], axis=1)
af.info()

#oppgave 2 gjort ------------------------------------

b = df.groupby("rangering")["tittel"].value_counts()

(b.head(10))

#oppgave 3 -------------------------------------------

d = df.loc[(df.rangering > 8.5 ) & (df.rangering < 8.7)]
d

e = df.loc[(df.rangering > 8.5 )]

f = e["tittel"]
f


#oppgave 4 Gjort  ---------------------------------------------
a = df[df["varighet_min"] > 120]

aaa = (len(a))
len(df)

b = 250*0.01

cc = aaa / b

print(f"Prosent - {cc}")

#Oppgave 5 Gjort --------------------------------------------

nitti_tall = df[df["år"] >= 1990 ]
nitti_tall1 = nitti_tall[df["år"] < 2000]

aaaaaaaaa = len(nitti_tall1)

b = 250*0.01

ccc = aaaaaaaaa / b

print(f"Prosent - {ccc}")

#Oppgave 6 ----------------------------------







