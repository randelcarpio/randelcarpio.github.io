
# Open-Meteo Weather Analysis

## Introduction
Open-Meteo Weather Analysis is a Python script for fetching and analyzing historical weather data using the Open-Meteo API. It visualizes the maximum, minimum, and average daily temperatures over a specified period.

## Prerequisites
- Python 3.x
- openmeteo_requests (`pip install openmeteo_requests`)
- requests_cache (`pip install requests_cache`)
- pandas (`pip install pandas`)
- matplotlib (`pip install matplotlib`)
- retry_requests (`pip install retry_requests`)

## Usage
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the script:
   ```bash
   python weatherdata.py
   ```

## Configuration
- Adjust the parameters in the `params` dictionary in the `weatherdata.py` script to customize the location, time range, and weather variables for the analysis.

## Features
- Fetches historical weather data using the Open-Meteo API.
- Visualizes the maximum, minimum, and average daily temperatures over time.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- [Open-Meteo API](https://open-meteo.com/)
- [openmeteo_requests](https://github.com/MaxLascombe/openmeteo_requests)
- [retry_requests](https://github.com/maximn/retry_requests)

## Author
John Randel Carpio
Contact: carpio.johnrandel@gmail.com
