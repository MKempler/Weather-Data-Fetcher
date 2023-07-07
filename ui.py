import tkinter as tk
from api import get_weather
from tkinter import messagebox

def display_weather_data(data, weather_frame):
    for widget in weather_frame.winfo_children():
        widget.destroy()

    weather_frame.config(bg="#F0F8FF")

    tk.Label(weather_frame, text="Current weather in " + data['name'], font=("Helvetica", 20), bg="#F0F8FF").pack(pady=10)

    tk.Label(weather_frame, text=f"Temperature: {data['main']['temp']}°F", font=("Helvetica", 16), bg="#F0F8FF").pack()
    tk.Label(weather_frame, text=f"Humidity: {data['main']['humidity']}%", font=("Helvetica", 16), bg="#F0F8FF").pack()
    tk.Label(weather_frame, text=f"Weather: {data['weather'][0]['description'].capitalize()}", font=("Helvetica", 16), bg="#F0F8FF").pack()

def get_weather_data(city_name_var, state_var, country_var, weather_frame):
    city_name = city_name_var.get()
    state = state_var.get()
    country = country_var.get()
    
    location = city_name
    if state:
        location += f",{state}"
    if country:
        location += f",{country}"

    if city_name:
        try:
            data = get_weather(location)
            display_weather_data(data, weather_frame)
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showinfo("Missing Information", "Please enter a city name")

def create_window():
    window = tk.Tk()
    window.title('Weather App')
    window.geometry('400x400')
    window.config(bg="#F0F8FF")

    city_name_var = tk.StringVar()
    state_var = tk.StringVar()
    country_var = tk.StringVar()

    instruction_label = tk.Label(window, text="Enter the name of a city, state, and country to get its current weather:", font=("Helvetica", 14), bg="#F0F8FF")
    instruction_label.pack(pady=10)

    city_name_entry = tk.Entry(window, textvariable=city_name_var, font=("Helvetica", 14))
    city_name_entry.pack()

    state_entry = tk.Entry(window, textvariable=state_var, font=("Helvetica", 14))
    state_entry.pack()

    country_entry = tk.Entry(window, textvariable=country_var, font=("Helvetica", 14))
    country_entry.pack()

    get_weather_button = tk.Button(window, text="Get Weather", command=lambda: get_weather_data(city_name_var, state_var, country_var, weather_frame), font=("Helvetica", 14), bg="#ADD8E6")
    get_weather_button.pack(pady=10)

    weather_frame = tk.Frame(window)
    weather_frame.pack()

    window.mainloop()

def main():
    create_window()

if __name__ == "__main__":
    main()
