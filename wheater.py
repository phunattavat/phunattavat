# -*- coding: utf-8 -*-
"""wheater.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-mdX4XFKDqCLP4AfMrLNyAuCN_2dqEpI

## Bangkok
"""

import requests
import pandas as pd
import json
from datetime import datetime
import pytz

# API Key และ URL ของ OpenWeatherMap
API_key = "b340092c31b595f81946a3d8e3d63a01"
city_name = "Bangkok"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
complete_url = base_url + "appid=" + API_key + "&q=" + city_name + "&units=metric"

# ดึงข้อมูลจาก API
response = requests.get(complete_url)
data = response.json()

# เลือก timezone ที่ต้องการ (Asia/Bangkok)
tz = pytz.timezone('Asia/Bangkok')

# ดึงเวลาปัจจุบันตาม timezone ที่กำหนด
current_time = datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')

# สร้าง DataFrame จากข้อมูล JSON พร้อม Timestamp
weather_data = {
    "Timestamp": [current_time],
    "City": [data["name"]],
    "Temperature (C)": [data["main"]["temp"]],
    "Feels Like (C)": [data["main"]["feels_like"]],
    "Min Temperature (C)": [data["main"]["temp_min"]],
    "Max Temperature (C)": [data["main"]["temp_max"]],
    "Humidity (%)": [data["main"]["humidity"]],
    "Weather Description": [data["weather"][0]["description"]],
    "Wind Speed (m/s)": [data["wind"]["speed"]],
    "Wind Direction (deg)": [data["wind"]["deg"]],
    "Visibility (m)": [data["visibility"]]
}

# แปลงข้อมูลเป็น DataFrame
df = pd.DataFrame(weather_data)

# แสดงข้อมูลเป็นตาราง
print(df)

"""## All Province in Thailand"""

import requests
import pandas as pd
import json
from datetime import datetime
import pytz

# API Key และ URL ของ OpenWeatherMap
API_key = "b340092c31b595f81946a3d8e3d63a01"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# รายชื่อจังหวัดในประเทศไทย (List of Provinces in Thailand)
provinces = [
    {"name_en": "Bangkok", "name_th": "กรุงเทพมหานคร"},
    {"name_en": "Chiang Mai", "name_th": "เชียงใหม่"},
    {"name_en": "Phuket", "name_th": "ภูเก็ต"},
    {"name_en": "Khon Kaen", "name_th": "ขอนแก่น"},
    {"name_en": "Chon Buri", "name_th": "ชลบุรี"},
    {"name_en": "Nakhon Ratchasima", "name_th": "นครราชสีมา"},
    {"name_en": "Mae Hong Son", "name_th": "แม่ฮ่องสอน"},
    {"name_en": "Chiang Rai", "name_th": "เชียงราย"},
    {"name_en": "Phayao", "name_th": "พะเยา"},
    {"name_en": "Nan", "name_th": "น่าน"},
    {"name_en": "Lamphun", "name_th": "ลำพูน"},
    {"name_en": "Lampang", "name_th": "ลำปาง"},
    {"name_en": "Phrae", "name_th": "แพร่"},
    {"name_en": "Uttaradit", "name_th": "อุตรดิตถ์"},
    {"name_en": "Tak", "name_th": "ตาก"},
    {"name_en": "Sukhothai", "name_th": "สุโขทัย"},
    {"name_en": "Phitsanulok", "name_th": "พิษณุโลก"},
    {"name_en": "Kamphaeng Phet", "name_th": "กำแพงเพชร"},
    {"name_en": "Phichit", "name_th": "พิจิตร"},
    {"name_en": "Uthai Thani", "name_th": "อุทัยธานี"},
    {"name_en": "Nakhon Sawan", "name_th": "นครสวรรค์"},
    {"name_en": "Phetchabun", "name_th": "เพชรบูรณ์"},
    {"name_en": "Loei", "name_th": "เลย"},
    {"name_en": "Udon Thani", "name_th": "อุดรธานี"},
    {"name_en": "Nong Bua Lam Phu", "name_th": "หนองบัวลำภู"},
    {"name_en": "Nong Khai", "name_th": "หนองคาย"},
    {"name_en": "Sakon Nakhon", "name_th": "สกลนคร"},
    {"name_en": "Nakhon Phanom", "name_th": "นครพนม"},
    {"name_en": "Mukdahan", "name_th": "มุกดาหาร"},
    {"name_en": "Kalasin", "name_th": "กาฬสินธุ์"},
    {"name_en": "Maha Sarakham", "name_th": "มหาสารคาม"},
    {"name_en": "Chaiyaphum", "name_th": "ชัยภูมิ"},
    {"name_en": "Roi Et", "name_th": "ร้อยเอ็ด"},
    {"name_en": "Buri Ram", "name_th": "บุรีรัมย์"},
    {"name_en": "Surin", "name_th": "สุรินทร์"},
    {"name_en": "Si Sa Ket", "name_th": "ศรีสะเกษ"},
    {"name_en": "Ubon Ratchathani", "name_th": "อุบลราชธานี"},
    {"name_en": "Amnat Charoen", "name_th": "อำนาจเจริญ"},
    {"name_en": "Yasothon", "name_th": "ยโสธร"},
    {"name_en": "Kanchanaburi", "name_th": "กาญจนบุรี"},
    {"name_en": "Suphan Buri", "name_th": "สุพรรณบุรี"},
    {"name_en": "Ratchaburi", "name_th": "ราชบุรี"},
    {"name_en": "Phetchaburi", "name_th": "เพชรบุรี"},
    {"name_en": "Prachuap Khiri Khan", "name_th": "ประจวบคีรีขันธ์"},
    {"name_en": "Chai Nat", "name_th": "ชัยนาท"},
    {"name_en": "Sing Buri", "name_th": "สิงห์บุรี"},
    {"name_en": "Lop Buri", "name_th": "ลพบุรี"},
    {"name_en": "Ang Thong", "name_th": "อ่างทอง"},
    {"name_en": "Phra Nakhon Si Ayutthaya", "name_th": "พระนครศรีอยุธยา"},
    {"name_en": "Saraburi", "name_th": "สระบุรี"},
    {"name_en": "Pathum Thani", "name_th": "ปทุมธานี"},
    {"name_en": "Nonthaburi", "name_th": "นนทบุรี"},
    {"name_en": "Samut Prakan", "name_th": "สมุทรปราการ"},
    {"name_en": "Samut Songkhram", "name_th": "สมุทรสงคราม"},
    {"name_en": "Samut Sakhon", "name_th": "สมุทรสาคร"},
    {"name_en": "Nakhon Pathom", "name_th": "นครปฐม"},
    {"name_en": "Nakhon Nayok", "name_th": "นครนายก"},
    {"name_en": "Prachin Buri", "name_th": "ปราจีนบุรี"},
    {"name_en": "Sa Kaeo", "name_th": "สระแก้ว"},
    {"name_en": "Chachoengsao", "name_th": "ฉะเชิงเทรา"},
    {"name_en": "Rayong", "name_th": "ระยอง"},
    {"name_en": "Chanthaburi", "name_th": "จันทบุรี"},
    {"name_en": "Trat", "name_th": "ตราด"},
    {"name_en": "Chumphon", "name_th": "ชุมพร"},
    {"name_en": "Ranong", "name_th": "ระนอง"},
    {"name_en": "Surat Thani", "name_th": "สุราษฎร์ธานี"},
    {"name_en": "Phang Nga", "name_th": "พังงา"},
    {"name_en": "Krabi", "name_th": "กระบี่"},
    {"name_en": "Nakhon Si Thammarat", "name_th": "นครศรีธรรมราช"},
    {"name_en": "Phatthalung", "name_th": "พัทลุง"},
    {"name_en": "Trang", "name_th": "ตรัง"},
    {"name_en": "Satun", "name_th": "สตูล"},
    {"name_en": "Songkhla", "name_th": "สงขลา"},
    {"name_en": "Pattani", "name_th": "ปัตตานี"},
    {"name_en": "Yala", "name_th": "ยะลา"},
    {"name_en": "Narathiwat", "name_th": "นราธิวาส"}
]

# Loop through each province to get weather data
weather_list = []

for province in provinces:
    complete_url = base_url + "appid=" + API_key + "&q=" + province["name_en"] + "&units=metric"

    # ดึงข้อมูลจาก API
    response = requests.get(complete_url)
    data = response.json()

    # เลือก timezone ที่ต้องการ (Asia/Bangkok)
    tz = pytz.timezone('Asia/Bangkok')


        # Extract data
    timezone = pytz.timezone('Asia/Bangkok')
    current_time = datetime.now(timezone).strftime('%Y-%m-%d %H:%M:%S')

    # Convert Unix UTC timestamps to local time
    sunrise = datetime.fromtimestamp(data["sys"]["sunrise"], timezone).strftime('%Y-%m-%d %H:%M:%S')
    sunset = datetime.fromtimestamp(data["sys"]["sunset"], timezone).strftime('%Y-%m-%d %H:%M:%S')

    # Create weather data dictionary
    weather_data = {
        "Timestamp": current_time,
        "Province (TH)": province["name_th"],
        "Province (EN)": province["name_en"],
        "Temperature (C)": data["main"]["temp"],
        "Feels Like (C)": data["main"]["feels_like"],
        "Pressure (hPa)": data["main"]["pressure"],
        "Humidity (%)": data["main"]["humidity"],
        "Weather Description": data["weather"][0]["description"],
        "Wind Speed (m/s)": data["wind"]["speed"],
        "Wind Direction (deg)": data["wind"]["deg"],
        "Visibility (m)": data.get("visibility", "N/A"),
        "Sunrise": sunrise,
        "Sunset": sunset
    }

    weather_list.append(weather_data)

# แปลงข้อมูลเป็น DataFrame
df = pd.DataFrame(weather_list)

# แสดงข้อมูลเป็นตาราง
print(df)

"""Select top/Bottom and sorting"""

import pandas

data = weather_list

df = pd.DataFrame(data)
selected_columns = df[['Province (TH)', 'Temperature (C)']]
top_10 = selected_columns.nlargest(10, 'Temperature (C)')
sort_top = top_10.sort_values(by='Temperature (C)', ascending=False)
print("Top 10 in Thailand:")
print(sort_top)

bottom_10 = selected_columns.nsmallest(10, 'Temperature (C)')
sort_bottom = bottom_10.sort_values(by='Temperature (C)', ascending=False)
print("Bottom 10 in Thailand:")
print(sort_bottom)

import numpy as np
import pandas as pd

# ... (your existing code)

# Convert the selected columns to a NumPy array
temperature_array = selected_columns['Temperature (C)'].values

# Calculate the average temperature using NumPy
average_temperature = np.mean(temperature_array)
round_up = np.round(average_temperature, decimals=2)

print("Average Temperature in Thailand:")
print(round_up)

import matplotlib.pyplot as plt

# ... (your existing code)

# Plot a horizontal line to represent the average temperature
plt.axhline(y=average_temperature, color='r', linestyle='-', label=f'Average Temperature: {round_up}')

# Add labels and title
plt.xlabel('Province')
plt.ylabel('Temperature (C)')
plt.title('Average Temperature in Thailand')

# Show the plot
plt.legend()
plt.show()