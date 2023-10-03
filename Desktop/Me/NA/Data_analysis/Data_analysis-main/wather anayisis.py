import pandas as pd




data=pd.read_csv("WeatherDataset.csv")

# print(data.head())
# print(data.shape)
# print(data.index)
# print(data.columns)
# print(data.dtypes)
# print(data.values)
# print(data['Weather'].unique())
# print(data.nunique())
# print(data.count())
# print(data['Weather'].value_counts())
# print(data.info)
# print(data.head(2))
# print(data.nunique())
# print(data['Wind Speed_km/h'].nunique())
# print(data['Wind Speed_km/h'].unique())
# print(data.Weather.value_counts())
# print(data[data.Weather=='Clear'])
# print(data.groupby('Weather').get_group('Clear'))
# print(data[data['Wind Speed_km/h']==4])
# print(data.isnull().sum)
# print(data.notnull().sum)


# print(data.rename(columns={"Weather": "Weather Condition "}))
#ToDo mean
# print(data.Visibility_km.mean())

#ToDo standaed deviation
 # print(data.Press_kPa.std())

#ToDo Variance
# print(data['Rel Hum_%'].var())
# print(data[data.Weather=='Snow'])
# print(data[data["Weather"].str.contains('Snow')].tail(10))
# print(data[(data['Wind Speed_km/h']>24) & (data['Visibility_km']==25 )])

#get all mean value of each column against each 'weather condition'
# print(data.groupby('Weather').head().mean())-> not working
# print(data.groupby('Weather').min())
# print(data.groupby('Weather').max())
# print(data[(data["Weather"]=='Clear') | (data['Visibility_km']>40)].tail(20))
print(data[(data["Weather"]=="Clear") & (data["Rel Hum_%"]> 50 ) | (data["Visibility_km"]> 40 )])