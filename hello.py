import pandas as pd
import matplotlib.pyplot as plt

file_path = "https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv"
df = pd.read_csv(file_path)

x = df["GDP per capita (constant 2010 US$)"]
y = df["Mortality rate, infant (per 1,000 live births)"]

plt.plot(x, y)
plt.xlabel("GDP per Capita")
plt.ylabel("Mortality Rate")
plt.show()
