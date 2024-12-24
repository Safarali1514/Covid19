import pandas as pd

df = pd.read_csv('covid_data.csv')

df['Date_reported'] = pd.to_datetime(df['Date_reported'], errors='coerce')

print(df[['New_cases', 'Cumulative_cases', 'New_deaths', 'Cumulative_deaths']].describe())

print(df[['New_cases', 'Cumulative_cases', 'New_deaths', 'Cumulative_deaths']].agg(['min', 'max']))

top_new_cases = df[['Country', 'New_cases']].sort_values(by='New_cases', ascending=False).head(10)
print(top_new_cases)

top_new_deaths = df[['Country', 'New_deaths']].sort_values(by='New_deaths', ascending=False).head(10)
print(top_new_deaths)

average_new_cases_by_country = df.groupby('Country')['New_cases'].mean().sort_values(ascending=False).head(10)
print(average_new_cases_by_country)
