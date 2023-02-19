import serial

ser = serial.Serial("COM3")


ser.write(str(0).encode())

ser.close()