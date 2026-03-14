import pandas as pd
import matplotlib.pyplot as plt

#Har antall barn, sivilstatus og inntekt noe for å si om du stemmer venstre,midten, høyre politisk skala

df = pd.read_csv("stemmer_10000.csv")


df[["Parti", "Inntekt"]].groupby("Parti").mean()

df[["Parti", "Antall_barn"]].groupby("Parti").mean()

#Ny variabel 
fparti = ["Ap", "MDG", "FrP"]
graf = df[df["Parti"].isin(fparti)]

graf.describe()

#Viser prosent av hvor alle bor i forksjellige steder
(graf[["Parti", "Bostedstype"]].groupby("Parti").value_counts()/5528*100).plot(kind="bar")

#Prosent for alle partier
(graf["Parti"].value_counts()/5528*100).plot(kind="bar")

#Viser oss data som gj.snitt max og min for inntekt og formue-------
frpStem = df[df["Parti"] == "FrP"]
frpStem[["Inntekt", "Formue"]].describe().plot(kind="bar")
plt.title("FrP")
plt.ylabel("Penger")
plt.xlabel("Forskjellige ting og tang")

apStem = df[df["Parti"] == "Ap"]
apStem[["Inntekt", "Formue"]].describe().plot(kind="bar")
plt.title("Ap")
plt.ylabel("Penger")
plt.xlabel("Forskjellige ting og tang")

mdgStem = df[df["Parti"] == "MDG"]
mdgStem[["Inntekt", "Formue"]].describe().plot(kind="bar")
plt.title("MDG")
plt.ylabel("Penger")
plt.xlabel("Forskjellige ting og tang")
#_-------------------------------

#Viser oss data for barn
(graf[["Parti", "Antall_barn"]].groupby("Parti").value_counts()/5528*100).plot(kind="bar", color=["red", "blue", "green"])
plt.title("Antall Barn")
plt.xlabel("Antall barn per Parti")
plt.ylabel("% / Prosent")

#Hvilken kolonne er viktigst

Ap = graf[graf["Parti"]=="Ap"]
Ap.describe()

Frp = graf[graf["Parti"]=="FrP"]
Frp.describe()

Mdg = graf[graf["Parti"]=="MDG"]
Mdg.describe()




