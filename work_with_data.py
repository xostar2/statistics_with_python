import requests
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# Get the data from the API
today=datetime.now()
print(today)

week_ago=today-timedelta(days=7)
print(week_ago)


# Format dates for API (YYYY-MM-DD)
start_date=week_ago.strftime('%Y-%m-%d')
print(start_date)

end_date=today.strftime('%Y-%m-%d')
print(end_date)

url=f"https://api.open-meteo.com/v1/forecast?latitude=48.85&longitude=2.35&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"

response=requests.get(url)
print(response.status_code)
print(response.text)
data=response.json()

print(data)

daily_data=data['daily']
print(daily_data)

df=pd.DataFrame({
    'date':daily_data['time'],
    'max_temp':daily_data['temperature_2m_max'],
    'min_temp':daily_data['temperature_2m_min']
})

df['date']=pd.to_datetime(df['date'])
#````````````````````````````````````````````````````````````````````````

#````````````````````````````````````````````````````````````````````````
# Plot the data
#create plot
plt.figure(figsize=(10,6))
plt.plot(df['date'],df['max_temp'],marker='o')
plt.plot(df['date'],df['min_temp'],marker='o')


plt.xlable('Date')
plt.ylable('Temperature (°C)')
plt.title('paris weather-past 7 days')
plt.legend()

#rotate x-axis labels for readabilit
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('paris_weather.png')
plt.show()
