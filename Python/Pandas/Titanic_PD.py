import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("DataFiles/titanic.csv")
#pd.read_csv gjør at den kan faktisk lese filen

print(df.head(20))

print(df.dtypes) #Viser om data er int, float
#eller object(str)

print (df["Age"]) #Print series(kolonnen) age
print(df.head(20))

df["Age"].max() #.max() viser maximum alder

df.info() #Forklar data som True/False

df.describe()# forklarer enkelt og greit data
#Som median, gjennomsnitt, minimum
#Maximum osv

df= pd.to_excel("titanic.xlsx", sheet_name ="passengers", index=False)
#to_excel() er excel fil og shett_name er hva papairet innenfor excel skal hete
#Index=False/True sier om den skal vise numerisk av kolonnene anbefales False
#Installer i TERMINAL pip install openpyxl


df= pd.read_excel("titanic.xlsx", sheet_name ="passengers", index=False)

print(df["Age"].shape)
#Denne viser hvor mange kolonner*rader det er

print(df[["Age", "Sex"]])
#Viser de kolonner du vil
#1 antall = [], 2 eller flere =[[]]

type(df["Age"])#sjekker om noe er en series eller ikke

print(df[df["Age"]<35])
#Viser alt data om de som er under 35 altså True

alfa = (df["Age"]<35)
#Viser alle rader og om det er True/False

class_23 = df[df["Age"].isin([1, 2])]
#Sjekker for alle som har de verdiene i kolonne som du velger
#.isin er for rad

class_23.head()

class_24 = df[(df["Pclass"] == 2) & (df["Age"] <25)] 
# & for begge skal være True eller | for at minumum 1 skal være True
# Du kan adde til så mange series som du vil

age_no_na = df[df["Age"].notna()]
#Sjekker for alle rekker som har en verdi for age
print(age_no_na.head(5))

adult_names = df.loc[df["Age"] > 35, "Pclass"]
#Tar å velge verdi for rekke og 1 kolonne
#Før komma er rekke, etter komma er kolonne
#loc er for str

df.iloc[1:5, 1:5]
#1:5 betyr hvis meg rad 1 til 4 og 1:5 er for kolonner
#Basically det du skrev -1

df.iloc[0:6, 3] = "ord du velger"
#kan navngi ting inni dataframe som du vil
#0:6 endre de første 6 og 3 etter komma er for kolonne
#Bakerste må du tenke kolonne du vil ha -1

df.head(8)


#--------------------------------------------------------------------------
#Bruk av plt 




