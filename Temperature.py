import tkinter as tk
from tkinter import ttk

def convert():
    try:
        temperature = float(Entry.get())
        unit = drop_down.get()
        convert_to = selected_unit.get()

        converted_output = tk.StringVar()

        if unit == 'c':
            converted = convert_to_celcius(temperature, convert_to)
            converted_output.set(f"Temperature in {convert_to}: {converted}") 
        elif unit == 'k':
            converted = convert_to_kelvin(temperature, convert_to)
            converted_output.set(f"Temperature in {convert_to}: {converted}") 
        elif unit == 'f':
            converted = convert_to_fahrenheit(temperature, convert_to)
            converted_output.set(f"Temperature in {convert_to}: {converted}") 
                
        new_window = tk.Toplevel()
        new_window.title('Converted Temperature')
        new_window.geometry('200x50')

        resulting = ttk.Label(new_window, textvariable = converted_output)
        resulting.pack(padx= 10, pady = 10)

        new_window.pack()

    except ValueError as e:
        converted_output.set(f"ValueError: {e}")

def convert_to_celcius(temperature, convert_to):
    if convert_to == 'k':
        return temperature + 273.15
    elif convert_to == 'f':
        return (temperature - 32) * 5/9
    else:
        return temperature

def convert_to_kelvin(temperature, convert_to):
    if convert_to == 'c':
        return temperature - 273.15
    elif convert_to == 'f':
        return (temperature - 32) * 9/5 + 32
    else:
        return temperature
    
def convert_to_fahrenheit(temperature, convert_to):
    if convert_to == 'k':
        return (temperature - 32) * 5/9 + 273.15
    elif convert_to == 'c':
        return (9/5 * temperature) + 32
    else:
        return temperature


window = tk.Tk()
window.title('Temperature Convert')
window.geometry('350x200')


temperature_label = ttk.Label(window, text = 'Enter Temperature To Convert')
temperature_label.pack(pady = 20)

frame = ttk.Frame(window) 
Entry = ttk.Entry(frame)
units = ["c", "k", "f"]
drop_down = ttk.Combobox(frame, values = units, state = 'readonly')
drop_down.set("c")
Entry.grid( padx = 5, row = 0, column = 1)
drop_down.grid( padx = 2, row = 0, column = 2)
frame.pack()

frame2 = ttk.Frame(window)
selected_unit = tk.StringVar()
celcius = ttk.Radiobutton(frame2, text = 'Celcius(c)', value = 'c', variable = selected_unit)
kelvin = ttk.Radiobutton(frame2, text = 'Kelvin(k)', value = 'k', variable = selected_unit)
fahrenheit = ttk.Radiobutton(frame2, text = 'Fahrenheit(f)', value = 'f', variable = selected_unit)
celcius.grid(row = 0, column = 1, padx = 2)
kelvin.grid(row = 0, column = 2, padx = 2)
fahrenheit.grid(row = 0, column = 3, padx = 2)
frame2.pack()

button = ttk.Button(window, text = 'convert', command = convert)
button.pack(pady = 20)


window.mainloop()