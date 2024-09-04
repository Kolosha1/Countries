#місце для твого коду
import pandas as pd

df = pd.read_csv("countries of the world.csv")
df.info()

def strip_string(string):
    return string.strip()

df["Region"] = df["Region"].apply(strip_string)

def replace_comma(data):
    if data != '':
        if isinstance(data,str):
            return float(data.replace(",",'.'))
        else:
            return data
    return -1

df["Pop. Density (per sq. mi.)"] = df["Pop. Density (per sq. mi.)"].apply(replace_comma)
df["Coastline (coast/area ratio)"] = df["Coastline (coast/area ratio)"].apply(replace_comma)
df["Net migration"] = df["Net migration"].apply(replace_comma)
df["Infant mortality (per 1000 births)"] = df["Infant mortality (per 1000 births)"].apply(replace_comma)
df["Literacy (%)"] = df["Literacy (%)"].apply(replace_comma)
df["Phones (per 1000)"] = df["Phones (per 1000)"].apply(replace_comma)
df["Arable (%)"] = df["Arable (%)"].apply(replace_comma)
df["Crops (%)"] = df["Crops (%)"].apply(replace_comma)
df["Other (%)"] = df["Other (%)"].apply(replace_comma)
df["Climate"] = df["Climate"].apply(replace_comma)
df["Birthrate"] = df["Birthrate"].apply(replace_comma)
df["Deathrate"] = df["Deathrate"].apply(replace_comma)
df["Agriculture"] = df["Agriculture"].apply(replace_comma)
df["Industry"] = df["Industry"].apply(replace_comma)
df["Service"] = df["Service"].apply(replace_comma)
df.to_csv("cleaned.csv", index=False)
df.info()

literacy = df[df["GDP ($ per capita)"]> 2000]["Literacy (%)"].mean()
literacy2 = df[df["GDP ($ per capita)"]< 2000]["Literacy (%)"].mean()
print(literacy)
print(literacy2)
Phones = df[df["GDP ($ per capita)"]> 1000]["Phones (per 1000)"].mean()
Phones2 = df[df["GDP ($ per capita)"]< 1000]["Phones (per 1000)"].mean()
print(Phones)
print(Phones2)
