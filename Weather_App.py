import requests
import tkinter as tk
from tkinter import ttk

api_key = '359ba8e8885e9693cdd234f0ea7bc9c8'

def weather():
    user_city = user_input_city.get()

    user_input = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={user_city}&limit={1}&appid={api_key}")

    try:
        city_name = user_input.json()[0]['name']
        latitude = user_input.json()[0]['lat']
        longitude = user_input.json()[0]['lon']
    except IndexError as e:
        review.config(text = f"{e}")

    try:    
        weather_info = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}")

        if weather_info.json()['cod'] == 200:
            weather_description = weather_info.json()['weather'][0]['main']
            weather_temperature = weather_info.json()['main']['temp']

            city_name_label.config(text = f"{city_name}")

            current_temp.config(text = f"Current Temperature: {weather_temperature}")
            weather_descp.config(text = f"Weather Description: {weather_description}")

            if weather_temperature >= 320:
                weather_img.config(image = sunny_img)
                review.config(text = 'The weather is very Hot.')
            elif weather_description == 'Rain':
                weather_img.config(image = rainy_img)
                review.config(text = 'The weather is Rainy.')
            elif weather_temperature < 320:
                weather_img.config(image = cloudy_img)
                review.config(text = 'The weather is Pleasant.')
                if weather_temperature < 273:
                    weather_img.config(image = snowing_img)
                    review.config(text = 'The weather is very Cold.')
            else:
                weather_img.config(image = cloudy_img)
                review.config(text = 'The weather is Pleasant.')
        else:
            print(f"The Server gave back an {weather_info.json()['cod']} Error")

    except UnboundLocalError as e:
            review.config(text = f"The City with the name {user_city} does not exists.")

root = tk.Tk()
root.title("Weather App")
root.geometry('300x350')


cloudy_img = tk.PhotoImage(file = "./weather_app_assets/cloud.png")
cloudy_img = cloudy_img.subsample(4,4)

sunny_img = tk.PhotoImage(file = "./weather_app_assets/sun.png")
sunny_img = sunny_img.subsample(4,4)

rainy_img = tk.PhotoImage(file = "./weather_app_assets/rain.png")
rainy_img = rainy_img.subsample(4,4)

snowing_img = tk.PhotoImage(file = "./weather_app_assets/snow.png")
snowing_img = snowing_img.subsample(4,4)

input_frame = tk.Frame(root)
city_label = ttk.Label(input_frame, text = "Enter A City Name", font = 'Arial, 14')
city_label.grid(row = 0, columnspan = 4, pady = 10)
user_input_city = tk.StringVar()
user_input_entry = ttk.Entry(input_frame, textvariable = user_input_city)
user_input_entry.grid(row = 1, column = 1, padx = 5)
chck_weather = ttk.Button(input_frame, text = "Check Weather", command = weather)
chck_weather.grid(row = 1, column = 2)
input_frame.pack()

output_frame = tk.Frame(root)
city_name_frame = tk.Frame(output_frame)
font_style = ('Arial', 14, 'bold')
city_name_label = ttk.Label(city_name_frame, text = '', font = font_style)
city_name_label.pack(side = 'left')
city_name_frame.pack(pady = 10)
weather_img_frame = tk.Frame(output_frame)
weather_img = ttk.Label(output_frame)
weather_img.pack()
weather_img_frame.pack()

weather_info_frame = tk.Frame(output_frame)
smaller_font_style = ('Arial', 12,'bold')
current_temp = ttk.Label(weather_info_frame, font = smaller_font_style)
current_temp.grid(row = 0, column = 1)
weather_descp = ttk.Label(weather_info_frame, font = smaller_font_style)
weather_descp.grid(row = 1, column = 1)
review = ttk.Label(weather_img_frame)
review.grid(row = 2, column = 1)
weather_info_frame.pack()
output_frame.pack(pady = 10)

root.mainloop()
