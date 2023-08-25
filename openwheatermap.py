from dotenv import load_dotenv
from datetime import datetime
import requests, os

# Load env variable
load_dotenv()
api_key = os.getenv("API_KEY")

# API Request
url = f'https://api.openweathermap.org/data/2.5/forecast?q=Jakarta&appid={api_key}&units=metric&cnt=35'
response = requests.get(url)


cuaca_harian_jakarta = {}
if(response.status_code == 200):
    data = response.json()

    for forecast in data['list']:
        date = forecast['dt_txt'].split()[0]
        if date not in cuaca_harian_jakarta:
            # Format tanggal
            tanggal_obj = datetime.strptime(date, '%Y-%m-%d')
            cuaca_harian_jakarta[date] = {
                "date": f"{tanggal_obj.strftime('%a')}, {tanggal_obj.strftime('%d')} {tanggal_obj.strftime('%b')} {tanggal_obj.strftime('%Y')}",
                "suhu": forecast['main']['temp']
            }
    # Print data cuaca
    print("Weather Forecast:")
    for _, data_cuaca in cuaca_harian_jakarta.items():
        print("{}: {}°C".format(data_cuaca['date'],data_cuaca['suhu']))
else:
    print("Gagal mendapatkan data cuaca")