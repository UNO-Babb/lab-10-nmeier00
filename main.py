#MapPlot.py
#Name: nick meier
#Date: april 17, 2025
#Assignment: lab 10

import aids
import pandas
import matplotlib.pyplot as plt
report = aids.get_report()

yearsAngola = []
prevalencesAngola = []
prevalencesZimbabwe =[]
prevalencesBotswana = []

for r in report:
    country = r["Country"]
    year = r["Year"]
    prevalence = r["Data"]["HIV Prevalence"]["Adults"]
    if country == 'Angola':
        yearsAngola.append(year)
        prevalencesAngola.append(prevalence)
    #print(years, country, prevalence)


for r in report:
    country = r["Country"]
    year = r["Year"]
    prevalence = r["Data"]["HIV Prevalence"]["Adults"]
    if country == 'Zimbabwe':
        prevalencesZimbabwe.append(prevalence)

for r in report:
    country = r["Country"]
    year = r["Year"]
    prevalence = r["Data"]["HIV Prevalence"]["Adults"]
    if country == 'Botswana':
        prevalencesBotswana.append(prevalence)
    
df = pandas.DataFrame({"Year Angola": yearsAngola, "Adult HIV Prevalence Angola": prevalencesAngola,
                        "Adult HIV Prevalence Zimbabwe": prevalencesZimbabwe,
                        "Adult HIV Prevalence Botswana": prevalencesBotswana})


df.plot(kind = 'line', x = 'Year Angola', y = ['Adult HIV Prevalence Angola', 'Adult HIV Prevalence Zimbabwe', 'Adult HIV Prevalence Botswana'])

plt.savefig("output")

