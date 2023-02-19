import serial

ser = serial.Serial("COM3")

while True:
    color = input("color")
    ser.write(color.encode())

ser.close()