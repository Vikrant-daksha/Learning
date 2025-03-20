import tkinter as tk
from tkinter import ttk


def convert_temperature():
    try:
        
        temperature = float(temperature_entry.get())
        input_unit = input_unit_combobox.get()
        output_unit = output_unit_var.get()

       
        if input_unit == 'Celsius':
            if output_unit == 'Fahrenheit':
                converted = (temperature * 9/5) + 32
            elif output_unit == 'Kelvin':
                converted = temperature + 273.15
            else:
                converted = temperature
        elif input_unit == 'Fahrenheit':
            if output_unit == 'Celsius':
                converted = (temperature - 32) * 5/9
            elif output_unit == 'Kelvin':
                converted = (temperature - 32) * 5/9 + 273.15
            else:
                converted = temperature
        elif input_unit == 'Kelvin':
            if output_unit == 'Celsius':
                converted = temperature - 273.15
            elif output_unit == 'Fahrenheit':
                converted = (temperature - 273.15) * 9/5 + 32
            else:
                converted = temperature
        
     
        result_label.config(text=f"Converted Temperature: {converted:.2f} {output_unit}")
    
    except ValueError:
  
        result_label.config(text="Please enter a valid number!")


root = tk.Tk()
root.title("Temperature Converter")
root.geometry("400x250")

instructions_label = ttk.Label(root, text="Enter the temperature and select units")
instructions_label.pack(pady=10)


input_frame = ttk.Frame(root)
temperature_entry = ttk.Entry(input_frame)
temperature_entry.grid(row=0, column=0, padx=5)
input_unit_combobox = ttk.Combobox(input_frame, values=['Celsius', 'Fahrenheit', 'Kelvin'], state='readonly')
input_unit_combobox.set('Celsius') 
input_unit_combobox.grid(row=0, column=1, padx=5)
input_frame.pack(pady=10)


output_frame = ttk.Frame(root)
output_unit_var = tk.StringVar(value='Celsius') 
celsius_radio = ttk.Radiobutton(output_frame, text="Celsius", value="Celsius", variable=output_unit_var)
fahrenheit_radio = ttk.Radiobutton(output_frame, text="Fahrenheit", value="Fahrenheit", variable=output_unit_var)
kelvin_radio = ttk.Radiobutton(output_frame, text="Kelvin", value="Kelvin", variable=output_unit_var)
celsius_radio.grid(row=0, column=0, padx=5)
fahrenheit_radio.grid(row=0, column=1, padx=5)
kelvin_radio.grid(row=0, column=2, padx=5)
output_frame.pack(pady=10)


convert_button = ttk.Button(root, text="Convert", command=convert_temperature)
convert_button.pack(pady=10)


result_label = ttk.Label(root, text="Converted Temperature: ", font=('Arial', 14))
result_label.pack(pady=10)

root.mainloop()
