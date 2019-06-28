import tkinter as tk
import requests
from _ast import Lambda

#a44acbd7889045255234e0556f8834ca
#api.openweathermap.org/data/2.5/forecast?q={city name},{country code}


def test_fun(entry):
    print("this is the entry:", entry)


def formet_response(weather) :
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']

        final = 'City: %s \nConditions: %s \nTemperature: %s ' % (name, desc, temp)
    except:
        final = 'Wrong input'

    return final

def get_weather(city):

    weather_key = 'a44acbd7889045255234e0556f8834ca'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city}
    response = requests.get(url, params = params)
    weather= response.json()

    labal['text']= formet_response(weather)

root = tk.Tk()

canvas = tk.Canvas(root,height=400, width=600)
canvas.pack()

background_image = tk.PhotoImage(file='good.png')
background_label = tk.Label(root, image= background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

frame = tk.Frame(root, bg ='#66b3ff', bd=5)
frame.place(relx=0.5, rely=0.2, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, bg= '#cce6ff', font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Search", font= 40, command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg ='#66b3ff', bd=10)
lower_frame.place(relx=0.5, rely=0.4, relwidth=0.75, relheight=0.6, anchor='n')


labal = tk.Label(lower_frame,font= 50, anchor='nw', justify='left', bd=4)
labal.place(relwidth=1, relheight=1)


root.mainloop()