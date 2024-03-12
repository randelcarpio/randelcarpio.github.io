import openmeteo_requests
import requests_cache
import pandas as pd
import matplotlib.pyplot as plt
from retry_requests import retry

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after=-1)
retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
openmeteo = openmeteo_requests.Client(session=retry_session)

# Make sure all required weather variables are listed here
# The order of variables in hourly or daily is important to assign them correctly below
url = "https://archive-api.open-meteo.com/v1/archive"
params = {
    "latitude": 14.5995,  # Latitude for Manila
    "longitude": 120.9842,  # Longitude for Manila
    "start_date": "1990-01-01",  # Start date for the past decade
    "end_date": "2023-12-31",  # End date for the past decade
    "daily": "temperature_2m_max,temperature_2m_min"
}
responses = openmeteo.weather_api(url, params=params)

# Process first location. Add a for-loop for multiple locations or weather models
response = responses[0]
print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")
print(f"Elevation {response.Elevation()} m asl")
print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

# Process daily data. The order of variables needs to be the same as requested.
daily = response.Daily()
daily_temperature_2m_max = daily.Variables(0).ValuesAsNumpy()
daily_temperature_2m_min = daily.Variables(1).ValuesAsNumpy()

daily_data = {"date": pd.date_range(
    start=pd.to_datetime(daily.Time(), unit="s", utc=True),
    end=pd.to_datetime(daily.TimeEnd(), unit="s", utc=True),
    freq=pd.Timedelta(days=1),
    inclusive="left"
)}
daily_data["temperature_2m_max"] = daily_temperature_2m_max
daily_data["temperature_2m_min"] = daily_temperature_2m_min

daily_dataframe = pd.DataFrame(data=daily_data)

# Calculate the average temperature for each day
daily_dataframe['temperature_2m_avg'] = daily_dataframe[['temperature_2m_max', 'temperature_2m_min']].mean(axis=1)

# Resample the data to get the maximum, minimum, and average temperature for each year
yearly_max_temperatures = daily_dataframe.resample('Y', on='date')['temperature_2m_max'].max()
yearly_min_temperatures = daily_dataframe.resample('Y', on='date')['temperature_2m_min'].min()
yearly_avg_temperatures = daily_dataframe.resample('Y', on='date')['temperature_2m_avg'].mean()

# Plot the maximum, minimum, and average temperature over time
plt.figure(figsize=(10, 6))
plt.plot(yearly_max_temperatures.index.year, yearly_max_temperatures, label='Max Temperature')
plt.plot(yearly_min_temperatures.index.year, yearly_min_temperatures, label='Min Temperature')
plt.plot(yearly_avg_temperatures.index.year, yearly_avg_temperatures, label='Avg Temperature')
plt.title('Max, Min, and Avg Yearly Temperature over Time')
plt.xlabel('Year')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.show()
