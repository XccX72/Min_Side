import pandas as pd

import matplotlib.pyplot as plt


#Du kan combine det fra pandas og matplotlib

df = pd.read_csv("air_quality_no2.csv", index_col=0, parse_dates=True)
#Sep="/t" er for å dobbelsikre at data kan loade
#index:col=0 gjør at man ikke viser index
#parse_dates=true gjør at idfk


df.plot()
#Grafisk kontuinitet av de forskjellige kollone/funksjoner

df["station_paris"].plot()
#Det samme bare kolonnene Station_paris

df.plot.scatter(x="station_london", y="station_paris", alpha=0.5)
#Viser både london og paris data som prikker skjema altså scatter skjema
#alpha =0.5 viser hvor gjennomsiktig prikkene skal være

df.plot.box()
#Viser data som bokser

axs = df.plot.area(figsize=(12, 5), subplots=False)
#Viser ver av kolloner i egen graf boks vis sublpots = True
#Subplots = False gir alle i en boks
#Figsize = x,y størrelse


fig, axs = plt.subplots(figsize=(12, 4))
#Lager en graf som er tom
df.plot.area(ax=axs)
#Hvilken data som skal inn i den tomme grafen
axs.set_ylabel("NO$_2$ concentration")
#$_ gjør at det ligner på 2 tallet fra
#Co2 i kjemi
#Hva skal y akse hete
axs.set_xlabel("Date")
fig.savefig("no2_concentrations.png")
#Save fil som png

df["paris_mg_per_cubic"] = df["station_paris"]*1.882
#Venstre er ny kolonne, andre er den som eksisterer
#Bak tar du hva enn du vil i matte den skal gjøre
#Dette tar bare en kolonne som allere eksisterer
df.head()


df["ratio_paris_antwerp"] = (df["station_paris"] / df["station_antwerp"])
#Venstre kolonne er ny
#Tar to forksjellige allerede eksiterende kolonner 
#Hvilket som helst mattesymbol fungere
df.head()

df_renamed = df.rename(columns={"station_antwerp":"Antwerp", "station_paris":"Paris", "station_london":"London"})
df_renamed.plot.box()
#Lager ny variabel med endret navn for kolloner
#index er for rekker & columns for kolonner

df_renamed.rename(columns=str.upper)
#Endrer alt til store bokstaver

tdf = pd.read_csv("titanic.csv", index_col=0)

tdf[["Age", "Fare"]].mean()
#Viser gjennomsnitt av kollone du valgte
#Fungere bare med float og int

tdf["Age"].median()
#Viser median tallet av kollone fungere ikke med
#str

tdf[["Age", "Fare"]].median()
#Viser median for to kolloner
#Men de er ikke combined

tdf[["Age", "Fare"]].describe()
#For opp median, gjennomsnitt osv 
#For bare de to kollonene

tdf.agg({"Age":["median", "min", "max", "skew"], "Fare":["skew", "mean"]})
#Velger bare noen av tingene fra .describe

tdf[["Sex", "Age",]].groupby("Sex").mean()
#Velger to kolloner og en av de som ikke skal bli
#funnet gjennomsnitt

tdf.groupby("Sex").mean(numeric_only=True)
#numeric:only=True viser bare de kolloner
#med tall

