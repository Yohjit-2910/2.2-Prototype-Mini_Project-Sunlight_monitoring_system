import serial
import csv
import time

# Set the serial port and baud rate to match the Arduino configuration
# Replace 'COMx' with the correct serial port name
ser = serial.Serial('COM3', 9600)

# Create and open a CSV file to store the data
csv_file = open('sunlight_intensity_data.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)

try:
    while True:
        # Read the data from the Arduino's serial monitor
        data = ser.readline().decode('utf-8').strip()

        # Check if the data is valid (you may need to adjust this based on your Arduino code)
        if data.isdigit():
            # Convert the data to an integer (if needed)
            sunlight_intensity = int(data)

            # Get the current time in seconds since the epoch
            current_time = time.time()

            # Save the data (time and sunlight intensity) to the CSV file
            csv_writer.writerow([current_time, sunlight_intensity])

            # Print the data for real-time monitoring (optional)
            print(
                f"Time: {current_time}, Sunlight Intensity: {sunlight_intensity} units")
except KeyboardInterrupt:
    # Close the serial connection and the CSV file upon exiting the loop
    ser.close()
    csv_file.close()
