
#🟥🟥🟥🟥 Useful funtions (generelle funksjoner) 🟥🟥🟥🟥🟥🟥

help() #hjelper deg
help(print)

#\n gjør at man printer på neste linje
print("jeg elser apekatt \neller gjør jeg det???")

#.any finner ut om i ting (liste, str osv) eksistere 
#og returnere False/True


a = ("jeg heter sigma")
b = a.islower()
print(b)
#.islower/.isupper finner om noe er i store eller 
#små bokstavr

a.isdigit() #sjekker for tall
a.alpha() #Sjekker for bokstaver
a.isspace() # Sjekker for mellomrom
a.isalnum() #sjekker for spesialtegn f eks @
#returnere True hvis den ikke har spesialtegn

#round(x, n)  avrunder til antall n desimaler
tall1 = 4.7
resultat1 = round(tall1, 5)
print(resultat1)
print(round(3.1459, 2)) #--> 3.14
#Hvis x er str f eks variabel navn for liste bruk
#print(format(listenavn, ".nf"))  #hvor n står for antall desimaler

#🟥🟥🟥🟥🟥 Løkker 🟥🟥🟥🟥🟥🟥

#continue fortsetter en løkke
#if i == 2: 
#   continue
#break avslutter koden i en løkke

#🟥🟥🟥🟥🟥 Funksjoner 🟥🟥🟥🟥🟥🟥

def a():
    #et eller anntet
    return 

#Fungere som en f(x) funksjon i matte


#🟥🟥🟥🟥🟥 Liste 🟥🟥🟥🟥🟥🟥
a = ['banan', 'eple', 'appelsin', 'plomme']

f = [rnd.randint(-100, 100) for _ in range (25)]
#Lager 25 random tall mellom verdi -100 og 100

#read er for å lese en verdi via en index
print(a[0]) #skriver banan

#update oppdatere en verdi i en liste
a[0] = 'kiwi' #endrer index 0 banan til kiwi

#insert er å putte noe nytt i en liste
a.append('kiwi')     #putter kiwi bakerst i listen
a.insert(5, 'kiwi') #putter kiwi der n index er 



len(a) #returnere lengde på en liste, str, osv
print(len(a)) #---> viser hvor mange verdier det er i en liste
len("python") #returnere 6

#loop skriver ting under hverandre
for b in a:
    print (b) 

#Byttet str tall med mellomrom til int liste
b = '5 3 3 5 2 6'
ab = [int(s) for s in b.split()]
print(ab)
#output = [5, 3, 3, 5, 2, 6]

#remove er å fjerne noe fra en liste
a.pop(0) #fjerner da index 0 i listen
a.pop() #fjerner og returnere element ved indeks
a.pop(2) #2 er indeks
a.count("banan") #teller hvor mye det er i en liste

a.sort() #sortere listen etter stigende rekkefølge
a.sort(reverse=True) #sortere listen etter synkende rekkefølge

#in/not in sjekker om noe er med i en liste []
# if ape in x:

b.split() #gjør at man lager en liste hviss det er mellomrom
#y = '5 2 4' --> y.split() ---> ['5', '2', '4']
x = [int(s)for s in b.split()]
print(x)
#Gjør det om til int liste

#🟥🟥🟥🟥🟥 Random 🟥🟥🟥🟥🟥🟥🟥
c = [1, 3, 5, 6]

import random as rnd

rnd.randint(1, 100) #tilfedlig tall mellom a og b
rnd.choice(c) #rnd fra en liste
rnd.choice([1, 2, 3, 4]) #Velger et tall fra listen i linjen
rnd.shuffle(c) #stokker om liste

#🟥🟥🟥🟥🟥🟥 Pandas 🟥🟥🟥🟥🟥🟥🟥🟥
import pandas as pd

# ◽◽◽ Lese Fil ◽◽◽◽
df = pd.read_csv("stortingsrepresentanter.csv", sep=";", index_col=False)
# sep=";" gjør at hvis en fil har ; istedenfor , så endrer
# den sånn at filen kan leses i python
# index_col=False gjør at index ikke vises

# ◽◽◽◽◽ Utforske dataframe ◽◽◽◽◽◽◽
df.dtypes         # viser forskjellige series og int/str osv
df.head()         # Første 5 rader
df.tail()         # Siste 5 rader
df.shape          # (rader, kolonner)
df.info()         # Kolonneinfo og datatyper
df.describe()     # Statistikk for numeriske kolonner
df.columns        # Liste over kolonnenavn
df.index          # Radeindeks
len(df)           # Viser antall rader 


#◽◽◽◽◽◽ Velge data ◽◽◽◽◽◽
df["etternavn"]          #Velger kolonner
df[["kjoenn", "parti"]]   # Hvis du vil ha flere kolonner

df.loc[0]
#Viser alt til tingen som har rad 0 i df
df.loc[0:5]
# Viser informasjon fra index 0 til 5
df.loc[(df.fylke=="Hordaland")]
#Viser alle som oppfyller kolonne fylke og er row hordaland
df.loc[(df.komiteer=="Næringskomiteen") & (df.fylke=="Hordaland")]
#Begge kriterier må bli oppfylt
df.loc[(df.komiteer=="Næringskomiteen") | (df.fylke=="Hordaland")]
#En av de må bli oppfylt
df.loc[(df.fodselsaar >= 1980)]
#Kan bruke for bare int kolonner, sjekk ved df.dtypes f eks
df.loc[(df.kjoenn == "mann"), ['epost']] = "@gmail.com"
#Endrer alle som er mann til å ha ny gmail


df.iloc[0]   # Viser bare index 0
df.iloc[[0, 1, 2, 3, 4, 167]] 
#Viser index til de som er i "liste" []
df.iloc[1:5]
# Viser index [1, 5> altså tar ikke med 5, men 4 max
df.iloc[1:5, 2:4]
#Viser kolonner [2,4> altså tar ikke med 4, men 3 max
df.iloc[[1, 3, 5, 7, 0], 2:5]
#Viser bare de index som er i listen


# ◽◽◽◽◽Filtere og Sortere ◽◽◽◽◽◽
df[df['alder'] > 25]              # Filter
df.sort_values('alder')           # Sorter stigende
df.sort_values('alder', ascending=False)  # Sorter synkende
df.groupby() #velger en av flere kolonner for å se data på om

#◽◽◽◽◽◽◽ Endre og legge til ◽◽◽◽◽◽
df['by'] = ['Oslo', 'Bergen']     # Ny kolonne
df.rename(columns={'navn': 'Navn'})  # Endre kolonnenavn
df.drop('by', axis=1)             # Fjern kolonne
df.drop(0, axis=0)                # Fjern rad

#◽◽◽◽◽ Manlende verdier ◽◽◽◽◽◽◽
df.isnull()           # Sjekk NaN
df.dropna(axis = 0)           # Fjern rader med NaN
df.fillna(0)          # Fyll NaN med 0



#🟥🟥🟥🟥🟥🟥 Plot 🟥🟥🟥🟥🟥🟥🟥🟥🟥
import matplotlib.pyplot as mlt

#df.plot()
#Grafisk kontuinitet av de forskjellige kollone/funksjoner

#df["station_paris"].plot()
#Det samme bare kolonnene Station_paris

#df.plot.scatter(x="station_london", y="station_paris", alpha=0.5)
#Viser både london og paris data som prikker skjema altså scatter skjema
#alpha =0.5 viser hvor gjennomsiktig prikkene skal være

#df.plot.box()
#Viser data som bokser

#axs = df.plot.area(figsize=(12, 5), subplots=False)
#Viser ver av kolloner i egen graf boks vis sublpots = True
#Subplots = False gir alle i en boks
#Figsize = x,y størrelse


#fig, axs = plt.subplots(figsize=(12, 4))
#Lager en graf som er tom
#df.plot.area(ax=axs)
#Hvilken data som skal inn i den tomme grafen
#axs.set_ylabel("NO$_2$ concentration")
#$_ gjør at det ligner på 2 tallet fra
#Co2 i kjemi
#Hva skal y akse hete
#axs.set_xlabel("Date")
#fig.savefig("no2_concentrations.png")
#Save fil som png

#df["paris_mg_per_cubic"] = df["station_paris"]*1.882
#Venstre er ny kolonne, andre er den som eksisterer
#Bak tar du hva enn du vil i matte den skal gjøre
#Dette tar bare en kolonne som allere eksisterer
#df.head()


#df["ratio_paris_antwerp"] = (df["station_paris"] / df["station_antwerp"])
#Venstre kolonne er ny
#Tar to forksjellige allerede eksiterende kolonner 
#Hvilket som helst mattesymbol fungere
#df.head()

#df_renamed = df.rename(columns={"station_antwerp":"Antwerp", "station_paris":"Paris", "station_london":"London"})
#df_renamed.plot.box()
#Lager ny variabel med endret navn for kolloner
#index er for rekker & columns for kolonner

#df_renamed.rename(columns=str.upper)
#Endrer alt til store bokstaver

#tdf = pd.read_csv("titanic.csv", index_col=0)

#tdf[["Age", "Fare"]].mean()
#Viser gjennomsnitt av kollone du valgte
#Fungere bare med float og int

#tdf["Age"].median()
#Viser median tallet av kollone fungere ikke med
#str

#tdf[["Age", "Fare"]].median()
#Viser median for to kolloner
#Men de er ikke combined

#tdf[["Age", "Fare"]].describe()
#For opp median, gjennomsnitt osv 
#For bare de to kollonene

#tdf.agg({"Age":["median", "min", "max", "skew"], "Fare":["skew", "mean"]})
#Velger bare noen av tingene fra .describe

#tdf[["Sex", "Age",]].groupby("Sex").mean()
#Velger to kolloner og en av de som ikke skal bli
#funnet gjennomsnitt

#tdf.groupby("Sex").mean(numeric_only=True)
#numeric:only=True viser bare de kolloner
#med tall

#🟥🟥🟥🟥🟥🟥 Object-oriented programming (OPP) 🟥🟥🟥🟥🟥🟥🟥🟥🟥

#class skaper en variabel som er en klasse
class Myclass:
    x=5

print(Myclass)

#Skaper et objekt i class
ob1 = Myclass()

print(ob1.x)

#Sletter object i klasse
del ob1
#sletter parameter i object
del ob1.x

#For tom klasse bruk pass
class Person:
    pass

#The _init_() method
class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

#Lager objekt som har name og age
k = Person2("Danni", 17)

#Printer ut navnet siden det står i __init__()
print(k.name)

#Hvis objekt ikke har age, men vi vil ha age
class Person3:
  def __init__(self, name, age=18):
    self.name = name
    self.age = age

#P2 har bare navn, da får den automatisk alder 18
p2 = Person3("Emil")
print(p2.name, p2.age)
#P1 har alder da blir det alderen til objektet
p1 = Person3("Jonathan", 25)
print(p1.name, p1.age)

#Se 1 parameter skrevet ut med engang
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
#Utføre denne funksjonen til Terminal
#Du kan putte alle parametere der hvis du vil
  def greet(self):
    print(self.name, self.age) 

p1 = Person("Emil", 25)
p1.greet()

#Hvis hver parameter skal gjøre noe spesialt
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
    return "Hello, " + self.name
  
  def greet2(self):
     return "oogabooga" + self.age

  def welcome(self):
    message = self.greet() + self.greet2()
    print(message + "! Welcome to our website.")

p1 = Person("Tobias")
p1.welcome()

#Endre parameter sin verdi
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Tobias", 25)
print(p1.age)
#Her endrer vi verdien på parameter age
p1.age = 26
print(p1.age)

#Funksjoner som forandrer verdier
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def celebrate_birthday(self):
    self.age += 1
    print(f"Happy birthday, {self.name}! You are now {self.age}")

p1 = Person("Linus", 25)
p1.celebrate_birthday()


#def __str__() gjør at den printer det ut automatisk
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

#Skal ha return og ikke print
  def __str__(self):
    return f"{self.name} ({self.age})"

p1 = Person("Tobias", 36)
print(p1)

#Slette method(funksjon) i klasse
class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    print("Hello!")

p1 = Person("Emil")
#Dette sletter selve method
del Person.greet

#Skape child class av Parent Class
#Inni () er den eksisterende Parent Class du
#Vil bruke
class student(Person):
  pass

#init funksjon i child class overskriver parent sin init
#Har ikke egenskapene til Parent Class
class student(Person):
  def __init__(self, fname, lname):
    self.fname = fname
    self.lname = lname

#Gjør at den beholder egenskapene til Parent CLass
class atudent(Person):
  def __init__(self, name):
    Person.__init__(self, name)

#Kan bruke istedenfor super() for å beholde egenskaper
class student(Person):
  def __init__(self, name):
    super().__init__(name)

#Adde parameter til Child class
class student(Person):
  def __init__(self, name):
    super().__init__(name)
    self.variabel = 2019
#Hvis parameteren er en variabel som er forkjellig
#Fra objekt til objekt
class student(Person):
  def __init__(self, name, variabel):
    super().__init__(name)
    self.variabel = variabel

#Adde methods til child class
#I method så må du bruke Parent variablene
class student(Person):
  def __init__(self, name, variabel):
    super().__init__(name)
    self.variabel = variabel
#Husk å bruke Parent Class variablene!!!!
  def welcome(self):
    print(f"Welfome {self.name} {self.variabel}")

#Lage privat parameter
#Gjør at objekt har data, men viser ikke det til andre
class abc:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

#Hvordan se privat parameter
class abc:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

  def get_age(self):
    return self.__age
  
#Fortsatt lyst å se privat parameter??
#Bruk objekt.ClassName.parameter

class Person:
  def __init__(self, name, salary):
    self.name = name
    self.__salary = salary # Protected property

p1 = Person("Linus", 50000)
print(p1.name)
#Gjør at du kan se privat parameter
print(p1._Person__salary)

#Privat Method
#Bare methods i Klassen kan kalle på 
#Den private method
class Person:
  def __init__(self, name, salary):
    self.name = name
    self.__salary = salary # Protected property
  
  def __Validate(self, num):
    print("Hei")

#Hvordan lage Inner Class
class Outer:
  def __init__(self):
    self.name = "Outer Class"
#Bare putt en class i en annen class
  class Inner:
    def __init__(self):
      self.name = "Inner Class"

#Hvordan bruke Inner Class
class Outer:
  def __init__(self):
    self.name = "Outer"

  class Inner:
    def __init__(self):
      self.name = "Inner"

    def display(self):
      print("Hello from inner class")

outer = Outer()
inner = outer.Inner()
inner.display()

"""Accessing Outer Class from Inner Class
Inner classes in Python do not automatically have access to the outer class instance.

If you want the inner class to access the outer class, you need to pass the outer class instance as a parameter:"""



#Practical example
class Outer:
  def __init__(self):
    self.name = "Emil"

  class Inner:
    def __init__(self, outer):
      self.outer = outer

    def display(self):
      print(f"Outer class name: {self.outer.name}")

outer = Outer()
inner = outer.Inner(outer)
inner.display()

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
    self.engine = self.Engine()

  class Engine:
    def __init__(self):
      self.status = "Off"

    def start(self):
      self.status = "Running"
      print("Engine started")

    def stop(self):
      self.status = "Off"
      print("Engine stopped")

  def drive(self):
    if self.engine.status == "Running":
      print(f"Driving the {self.brand} {self.model}")
    else:
      print("Start the engine first!")

car = Car("Toyota", "Corolla")
car.drive()
car.engine.start()
car.drive()



#Practical example
class Computer:
  def __init__(self):
    self.cpu = self.CPU()
    self.ram = self.RAM()

  class CPU:
    def process(self):
      print("Processing data...")

  class RAM:
    def store(self):
      print("Storing data...")

computer = Computer()
computer.cpu.process()
computer.ram.store()
