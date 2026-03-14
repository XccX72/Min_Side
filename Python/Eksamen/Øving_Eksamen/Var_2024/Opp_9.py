import pandas as pd
import matplotlib.pyplot as plt
import os

mappe = os.path.dirname(__file__)
filsti = os.path.join(mappe, "abc.csv")
df = pd.read_csv(filsti, sep= ";", skiprows= 1)


#a) ---------------------------------------------------------

new_names = df.rename(
    columns={
        "alle aktiviteter": "Aktivitet",
        "kjønn": "Kjonn",
        "Tidsbruk 2000 I alt": "Tidsbruk"
    }
)
#print(new_names.head())


#b) ---------------------------------------------------------
user_input = input("Hvilket kjønn? Skriv: Alle, Menn, Kvinner: ").capitalize()

abc = new_names[new_names["Kjonn"] == user_input]

#print(abc.head(75))

#c) ----------------------------------------------------------

#Skal vise Tidsbruk utifra valgte kjønn

abc[["Tidsbruk", "Aktivitet"]].plot.bar()
plt.title("Tidsbruk Via Valgt Kjønn")
plt.xlabel("Index Nr")
plt.ylabel("Tidsbruk")
plt.show()
