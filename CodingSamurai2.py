import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = "f6e1b9b3f29becfeab6982d324ab0702"

def get_weather(city, unit="metric"):
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units={unit}"
    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def display_weather_on_same_page():
    city = city_entry.get()
    unit = unit_var.get()
    if unit not in ['metric', 'imperial']:
        messagebox.showerror("Error", "Invalid unit entered. Please enter either 'metric' or 'imperial'.")
        return
    
    data = get_weather(city, unit)
    if data is not None:
        for widget in root.winfo_children():
            widget.destroy()
        
        heading_label = tk.Label(root, text=f"The weather of {city}", font=("Helvetica", 16, "bold"))
        heading_label.pack(pady=10)

        current_temperature = data["main"]["temp"]
        current_pressure = data["main"]["pressure"]
        current_humidity = data["main"]["humidity"]
        weather_description = data["weather"][0]["description"]
        
        weather_label = tk.Label(root, text=f"Temperature: {current_temperature} °{'C' if unit == 'metric' else 'F'}\n"
                                            f"Atmospheric pressure: {current_pressure} hPa\n"
                                            f"Humidity: {current_humidity}%\n"
                                            f"Description: {weather_description}")
        weather_label.pack(pady=10)
        back_button = tk.Button(root, text="Back", command=main)
        back_button.pack(pady=10)
    else:
        messagebox.showerror("Error", "City Not Found")

def main():
    for widget in root.winfo_children():
        widget.destroy()
    
    root.title("Weather App")
    
    tk.Label(root, text="Enter city name:").pack()
    global city_entry
    city_entry = tk.Entry(root)
    city_entry.pack()
    
    tk.Label(root, text="Select unit:").pack()
    global unit_var
    unit_var = tk.StringVar(root)
    unit_var.set("metric")  
    unit_options = ["metric", "imperial"]
    unit_menu = tk.OptionMenu(root, unit_var, *unit_options)
    unit_menu.pack()
    
    submit_button = tk.Button(root, text="Get Weather", command=display_weather_on_same_page)
    submit_button.pack()

root = tk.Tk()
main()  
root.mainloop()
