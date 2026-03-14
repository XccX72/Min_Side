import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ansatte.csv", parse_dates= ["Ansettelsesdato"]) 

df.head()

df.describe()

df.info()

len(df)

df_it = df.loc[(df.Avdeling == "IT")]

df_renset_it = df_it.dropna(axis = 0)

df_it.head()

df_renset_it.head()

def beregn_bonus(rad):
    if rad["Poeng"] > 80 and rad["Avdeling"] =="IT":
        return ("Ja")
    elif rad["Poeng"] > 80 and rad["Avdeling"] =="Salg":
        return ("Ja")
    else:
        return ("Nei")

df["Bonus"] = df.apply(beregn_bonus, axis = 1)

print(df["Bonus"])

df_filtrert = df.loc[((df.Avdeling == "Salg") | (df.Poeng >85))]

df_filtrert.head()

df["Ansettelsesdato"]

df_query = df.query("Avdeling != 'HR' and Ansettelsesdato > '2019-12-31'")

df_query.head()

df[["Avdeling", "Poeng"]].groupby("Avdeling").mean()


cf = pd.read_csv("salgsanalyse_Gemini.csv")

cf.head(10)
cf.info()
len(cf)

af = cf.loc[(cf.Product == "A")]
bf = cf.loc[(cf.Product == "B")]
ef = cf.loc[(cf.Product == "C")]

af.head()

cf.plot(kind = "bar")
plt.title("Totalt Salg per produkt")
plt.xlabel("Produkt")
plt.ylabel("Totalt Salg")
plt.show()



cf = pd.read_csv("salgsanalyse_Gemini.csv")

a = cf[["Product", "Sales"]].groupby("Product").mean()

cf.plot(kind = "bar")
plt.title("Totalt Salg per produkt")
plt.xlabel("Produkt")
plt.ylabel("Totalt Salg")
plt.show()

a.plot(kind = "bar")
plt.title("Sales Per Product")
plt.xlabel("Produkt")
plt.ylabel("Total Sale")
plt.show()


df = pd.read_csv("trafikk.csv", parse_dates= ["Dato"])

nettbutikk_df = df.query("Nettsted == 'Nettbutikk'")

#nettbutikk_df.plot(x = "Dato", y = "Besøkende")
#plt.title("Besøkstrend for Nettbutikken")
#plt.ylabel("Antall besøkonde")
#plt.show()

df["Konv_Rate"] = df["Konverteringer"] / df["Besøkende"]*100

gruppert_df = df.groupby(["Dato", "Nettsted"])

af =gruppert_df["Konv_Rate"].mean().unstack()

af.head()

af.plot()
plt.title("Konverteringsrate over tid")
plt.ylabel("Rate (%)")
plt.xlabel("Dat0")
plt.show()

