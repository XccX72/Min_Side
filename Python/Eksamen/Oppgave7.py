import pandas as pd

df = pd.read_csv("Eksamen/Elever-fag.csv")

df.info()

df.head()

len(df)

#------ 7a ------------------

assd = df.dropna(subset=["2022-23"])

assd.groupby("Fagomraadenavn")["2022-23"].count()

asssd = df.dropna(subset=["2023-24"])

asssd.groupby("Fagomraadenavn")["2023-24"].count()

assssd = df.dropna(subset=["2024-25"])

assssd.groupby("Fagomraadenavn")["2024-25"].count()

#------ 7b -----------------------

input_velger = input("Hvilket fagkområde vil du velge? ")

def velg_område(x):
    print(df.loc[df["Fagomraadenavn"] == x, ["Opplaeringsfagnavn", "2022-23", "2023-24", "2024-25"]])

velg_område(input_velger)