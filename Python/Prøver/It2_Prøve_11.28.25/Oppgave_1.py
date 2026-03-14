import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("elever.csv")

df.head() #Første 5 linjer

len(df)
df.info()

ad = df.groupby("klasse")["karaktersnitt"].mean()

print(ad.head(20)) #1kda har høyest snitt
#head(20) sånn at jeg er sikker på at jeg har alle klasser
#Kunne ha skrevet:
print(ad)

ad = df.groupby("klasse")["karaktersnitt"].mean()

helse = df.loc[(df.klasse == "1HOA") | (df.klasse == "1HOB") | (df.klasse == "1HOC") | (df.klasse == "1HOD")]

Studie = df.loc[(df.klasse == "1STA") | (df.klasse == "1STB") | (df.klasse == "1STC")]

kda = df.loc[(df.klasse == "1KDA")]

#Siden KDA har kun en linje er gjennomsnitt i kda bare det 4.4 som vises i 
#linje 13 og 16

studie_gj = sum(Studie.groupby("klasse")["karaktersnitt"].mean()) / 3

studie_gj

helse_gj = sum(helse.groupby("klasse")["karaktersnitt"].mean()) / 3

helse_gj

kda_gj = sum(kda["karaktersnitt"])/ len(kda)

kda_gj

print(f"Helse Gjennonsnitt {studie_gj} \nStudie Gjennomsnitt{helse_gj} \nKDA Gjennomsnitt {kda_gj}")

#-------

top_10 = df[["fornavn", "etternavn", "karaktersnitt", "klasse"]]

top_10.groupby("klasse").mean(ascending=[True])

top_10.groupby("fornavn")["karaktersnitt"].mean(ascending=[True])

asfdf = top_10.sort_values(["karaktersnitt"], ascending=[True])

asfdf.tail(10)

#..........................
Studie.plot()

studie_graf = Studie.query("dato > '06-01'")

studie_sf = studie_graf.loc[(studie_graf.karaktersnitt >= 4)]
studie_sf.drop(columns=["elevid"])
studie_sf.drop(columns=['fodselsaar'])

studie_sf.plot()
plt.title("Elever i studie som har over 4 i karaktersnitt")
plt.show()
#Finner alle elever som har over 4 i karaketsnitt og går studie




