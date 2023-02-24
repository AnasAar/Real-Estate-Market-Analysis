#pricing/rate/amountFormatted location/lat","location/lng","name"
import numpy as np
import pandas as pd

df = pd.read_csv("/home/anasaar/airflow/dataLake/airbnb_scraping.csv")
addresses = []
latitudes = []
longitudes = []
noms = []
numberOfGuests = []
prix = []
roomTypes = []
stars = []
i=0
id = []
d = pd.DataFrame(data=df)
for adr in d.loc[:, 'address']:
    addresses.append(adr)
    i+=1
    id.append(i)
for lat in d.loc[:, 'location/lat']:
    latitudes.append(lat)
for lon in d.loc[:, 'location/lng']:
    longitudes.append(lon)
for nom in d.loc[:, 'name']:
    noms.append(nom)
for num in d.loc[:, 'numberOfGuests']:
    numberOfGuests.append(num)
for pr in d.loc[:, 'pricing/rate/amountFormatted']:
    prix.append(pr)
for rt in d.loc[:, 'roomType']:
    roomTypes.append(rt)
for st in d.loc[:, 'stars']:
    stars.append(st)
data = {'id': id, 'adresse': addresses, 'latitude': latitudes, 'longitude': longitudes, 'noms': noms, 'numberOfGuests':numberOfGuests, 'prices': prix, 'roomTypes': roomTypes, 'rating': stars}
comb = pd.DataFrame(data= data)
comb.to_csv("/home/anasaar/airflow/airbnb/airbnb_clean.csv", index=False)



