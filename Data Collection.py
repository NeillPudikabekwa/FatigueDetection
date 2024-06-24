import serial

# Connect to wearable sensor
ser = serial.Serial('/dev/tty.sensor_name', baudrate=9600)

# Continuously read data from sensor
while True:
    data = ser.readline()
    # Process and store sensor data
    process_sensor_data(data)
