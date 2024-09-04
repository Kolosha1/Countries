# %%
import pandas as pd
import matplotlib.pyplot as plt

# %%
df = pd.read_csv("cleaned.csv")
df.info()


# %%
df['Phones (per 1000)'].plot(kind="hist",bins = 25)

# %%
df['Pop. Density (per sq. mi.)'].plot(kind="box")
plt.show()


