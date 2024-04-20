import tkinter as tk
import csv

class SensorApp:
    def __init__(self, master):
        self.master = master
        master.title("Sensor Data Display")

        self.temperature_label = tk.Label(master, text="Temperature: ")
        self.temperature_label.grid(row=0, column=0)

        self.humidity_label = tk.Label(master, text="Humidity: ")
        self.humidity_label.grid(row=1, column=0)

        self.sensor_value_label = tk.Label(master, text="Sensor Value: ")
        self.sensor_value_label.grid(row=2, column=0)

        self.temperature_value = tk.Label(master, text="")
        self.temperature_value.grid(row=0, column=1)

        self.humidity_value = tk.Label(master, text="")
        self.humidity_value.grid(row=1, column=1)

        self.sensor_value = tk.Label(master, text="")
        self.sensor_value.grid(row=2, column=1)

        self.data_generator = self.read_sensor_data()
        self.update_values()

    def read_sensor_data(self):
        # Read data from CSV file
        with open('file.csv', 'r') as file:
            reader = csv.DictReader(file)
            # Clean up column names by removing leading/trailing whitespace and empty strings
            fieldnames = [name.strip() for name in reader.fieldnames if name.strip()]
            print("Column Names:", fieldnames)
            # Assuming columns: 'Temperature', 'Humidity', and 'Sensor Value'
            for row in reader:
                # Trim column names in row dictionary
                row = {key.strip(): value for key, value in row.items()}
                print("Row:", row)  # Debug print
                temperature = float(row['Temperature'])
                # Remove '%' from humidity value before converting to float
                humidity = float(row['Humidity'].rstrip('%'))
                sensor_value = row['Sensor Value']
                yield temperature, humidity, sensor_value

    def update_values(self):
        try:
            temperature, humidity, sensor_value = next(self.data_generator)

            # Check temperature thresholds
            temperature_status = ""
            if temperature > 90:
                temperature_status = "Temperature too high!"
            elif temperature < 10:
                temperature_status = "Temperature too low!"

            # Update GUI labels with new values and status
            self.temperature_value.config(text=str(temperature) + " °C\n" + temperature_status)
            self.humidity_value.config(text=str(humidity) + " %")
            self.sensor_value.config(text=sensor_value)

        except StopIteration:
            print("End of data reached, restarting...")
            self.data_generator = self.read_sensor_data()

        except Exception as e:
            print("Error:", e)

        # Schedule next update after 3 seconds
        self.master.after(3000, self.update_values)

root = tk.Tk()
app = SensorApp(root)
root.mainloop()
