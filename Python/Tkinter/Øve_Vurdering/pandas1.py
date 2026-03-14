import pandas as pd
#Tkinter/Øve_vurdering/
df = pd.read_csv("ps5_top100.csv")

print(df.head(20))

df.info()

#Fjerne kolonner snapschot og source
af = df.drop(["snapshot_date", "source"], axis= 1)

af.info()


af.groupby("game")["players"].value_counts()

#Finne spill som har mest spilletid ved å bruke sum() som summere alle 
#spillerne sine tid så kan sort_values ranksjere de
af.groupby("game")["hours_played"].sum().sort_values(ascending= False)

#Lager ny kolonne, min_session og den tar kolonneen hours_played og sessions
#og ganger det med 60 for å få minutter
af["min_session"] = af["hours_played"] / af["sessions"] *60

#Finner for min_session
af.groupby("game")["min_session"].sum().sort_values(ascending= False)

#Lager ny dataframe med bare top 20 spill via kolonne
#rank
#Finner antall spillere for spillene
bf = df[df["rank"] <= 20]
bf.groupby("game")["players"].mean()

#Finner antall timer altså sum for hours_played
#Returnere np.int64(885802)
#np = numpy, int64 er typen og (885802) er svaret
df["hours_played"].sum()
#Hvis du vil ha bare tallet
a = df["hours_played"].sum()
print(a)
#For svaret i dager
b = a / 24
print(round(b, 0))
