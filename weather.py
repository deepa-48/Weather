from tkinter import *
from tkinter import ttk
# import requests
import http.client
import json

def get_data():
    try:
        city = city_name.get()
        api_key = "c9d8cefbc682e80b2f8076256f5e30aa"
        conn = http.client.HTTPSConnection("api.openweathermap.org")
        endpoint = f"/data/2.5/weather?q={city}&appid={api_key}"
        conn.request("GET", endpoint)
        response = conn.getresponse()
        data = response.read().decode("utf-8")
        conn.close()
        json_data = json.loads(data)
        
        w_label1.config(text=json_data["weather"][0]["main"])
        wb_label1.config(text=json_data["weather"][0]["description"])
        temp_label1.config(text=str(int(json_data["main"]["temp"] - 273.15)))
        pre_label1.config(text=json_data["main"]["pressure"])
        hum_label1.config(text=json_data["main"]["humidity"])
    except Exception as e:
        print("An error occurred:", e)


# def get_data():
#     city = city_name.get()
#     data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=c9d8cefbc682e80b2f8076256f5e30aa").json()
#     w_label1.config(text=data["weather"][0]["main"])
#     wb_label1.config(text=data["weather"][0]["description"])
#     temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))
#     pre_label1.config(text=data["main"]["pressure"])


win = Tk()
win.title("Weather App Made by - Deepika")
win.config(bg="blue")
win.geometry("500x620")
name_label = Label(win,text="Weather App",font=("Time New Roman",40,"bold"))
name_label.place(x=25,y=50,height=50,width=450)

city_name = StringVar()
list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com = ttk.Combobox(win,text="Weather App",values=list_name,font=("Time New Roman",20,"bold"),textvariable=city_name)
com.place(x=25,y=120,height=50,width=450)

done_button = Button(win,text="Done",font=("Time New Roman",20,"bold"),command=get_data)
done_button.place(y=190,height=50,width=100,x=200)

w_label = Label(win,text="Weather Climate",font=("Time New Roman",15))
w_label.place(x=25,y=260,height=50,width=210)
w_label1 = Label(win,text="",font=("Time New Roman",15))
w_label1.place(x=250,y=260,height=50,width=210)

wb_label = Label(win,text="Weather Description",font=("Time New Roman",15))
wb_label.place(x=25,y=330,height=50,width=210)
wb_label1 = Label(win,text="",font=("Time New Roman",15))
wb_label1.place(x=250,y=330,height=50,width=210)

temp_label = Label(win,text="Temperaturen",font=("Time New Roman",15))
temp_label.place(x=25,y=400,height=50,width=210)
temp_label1 = Label(win,text="",font=("Time New Roman",15))
temp_label1.place(x=250,y=400,height=50,width=210)

pre_label = Label(win,text="Pressure",font=("Time New Roman",15))
pre_label.place(x=25,y=470,height=50,width=210)
pre_label1 = Label(win,text="",font=("Time New Roman",15))
pre_label1.place(x=250,y=470,height=50,width=210)

hum_label = Label(win,text="Humidity",font=("Time New Roman",15))
hum_label.place(x=25,y=540,height=50,width=210)
hum_label1 = Label(win,text="",font=("Time New Roman",15))
hum_label1.place(x=250,y=540,height=50,width=210)

win.mainloop()