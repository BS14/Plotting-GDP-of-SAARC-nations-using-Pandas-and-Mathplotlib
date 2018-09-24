import pandas as pd

import matplotlib.pyplot as plt
#Reading Data from wave
df = pd.read_csv('https://pkgstore.datahub.io/core/gdp/gdp_csv/data/0048bc8f6228d0393d41cac4b663b90f/gdp_csv.csv', index_col = 'Year')

#Filtering Data
df1 = df[(df['Country Name'] == 'Nepal')]
df2 = df[(df['Country Name'] == 'India')]
df3 = df[(df['Country Name'] == 'Afghanistan')]
df4 = df[(df['Country Name'] == 'Bhutan')]
df5 = df[(df['Country Name'] == 'Maldives')]
df6 = df[(df['Country Name'] == 'Pakistan')]
df7 = df[(df['Country Name'] == 'Sri Lanka')]

#Plotting Data
a, = plt.plot(df1['Value'])
b, = plt.plot(df2['Value'])
c, = plt.plot(df3['Value'])
d, = plt.plot(df4['Value'])
e, = plt.plot(df5['Value'])
f, = plt.plot(df6['Value'])
g, = plt.plot(df7['Value'])

#Adding Information to Plots
plt.title('GDP of SAARC Nations')
plt.ylabel('GDP')
plt.xlabel('Years')
plt.legend([a,b,c,d,e,f,g],['Nepal','India','Afganistan','Bhutan','Maldives','Pakistan','Sri Lanka'])
plt.show()
